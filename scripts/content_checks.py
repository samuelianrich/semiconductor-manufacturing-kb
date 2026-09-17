"""Reference, review, math-delimiter and asset checks for registered articles."""
import csv,json,re
import xml.etree.ElementTree as ET
from pathlib import Path

def reviewed_module_errors(modules, articles):
    """An index alone must never satisfy a technical module's review state."""
    owners = {Path(a['path']).parts[0] for a in articles if a['status'] == 'reviewed'}
    return [f'Reviewed module has no reviewed article: {m["id"]}'
            for m in modules if m['status'] == 'reviewed' and m['path'] not in owners]

def validate(root):
    errors=[]
    def need(ok,msg):
        if not ok:errors.append(msg)
    articles=json.loads((root/'catalog/articles.json').read_text())
    errors.extend(reviewed_module_errors(json.loads((root/'catalog/modules.json').read_text()), articles))
    ids=set(re.findall(r'<a id="([^"]+)"', (root/'42_references/bibliography.md').read_text()))
    with (root/'42_references/claims.csv').open() as f:claims=list(csv.DictReader(f))
    with (root/'assets/manifest.csv').open() as f:assets=list(csv.DictReader(f))
    with (root/'manufacturing_map/data/entities.csv').open() as f:nodes={x['entity_id'] for x in csv.DictReader(f)}
    need(len({x['claim_id'] for x in claims})==len(claims),'Duplicate company claim ID')
    need(len({x['path'] for x in articles})==len(articles),'Duplicate article path')
    claim_ids={x['claim_id'] for x in claims}
    for c in claims:
        need(c['confidence'] in ['CONFIRMED','INDUSTRY-STANDARD INFERENCE','ANALYST ESTIMATE','UNKNOWN / PROPRIETARY'],f'Invalid confidence {c["claim_id"]}')
        for key in ['claim_text','conditions','locator','source_date','as_of_date','last_review','uncertainty']:
            need(bool(c[key]),f'Empty claim {key}: {c["claim_id"]}')
        for source in c['source_ids'].split(';'):need(source.lower() in ids,f'Unknown claim source {source}')
        for path in c['article_paths'].split(';'):need((root/path).is_file(),f'Missing claim article {path}')
    for a in articles:
        path=root/a['path'];need(path.is_file(),f'Missing article {a["path"]}')
        if not path.exists():continue
        s=path.read_text()
        need(a['status'] in ['drafted','reviewed'],f'Invalid article status {path.name}')
        if a['status']=='reviewed':
            need(bool(a['last_reviewed']) and 'Status: **Reviewed' in s,f'Review metadata mismatch {path.name}')
        for key in ['Prerequisites','Position in the manufacturing map','Sources and review']:
            need('## '+key in s,f'Missing article section {key}: {path.name}')
        for source in a['sources']:
            need(source.lower() in ids,f'Unknown article source {source}')
            need('bibliography.md#'+source.lower() in s,f'Registered source absent from article {source}')
        for node in a['node_ids']:need(node in nodes,f'Unknown article node {node}')
        for claim in re.findall(r'CLM-\d{6}',s):need(claim in claim_ids,f'Unregistered article claim {claim}')
        need(not any(ord(c)<32 and c not in '\n\t' for c in s),f'Control character in {path.name}')
        need(r'\[' not in s and r'\]' not in s and r'\)' not in s,f'Unsupported/damaged math delimiter in {path.name}')
        need(s.count('$$')%2==0,f'Unbalanced display math in {path.name}')
        prose=re.sub(r'\$\$.*?\$\$','',s,flags=re.S)
        for line in prose.splitlines():need(line.count('$')%2==0,f'Unbalanced inline math in {path.name}')
        for image in re.findall(r'!\[[^\]]*\]\(([^)]+)\)',s):
            target=(path.parent/image).resolve()
            need(any((root/x['path']).resolve()==target for x in assets),f'Unregistered illustration {image}')
    registered={x['path'] for x in assets}
    for p in (root/'assets').rglob('*.svg'):
        need(str(p.relative_to(root)) in registered,f'Unregistered SVG {p.name}')
        try:
            svg=ET.parse(p).getroot();ns={'s':'http://www.w3.org/2000/svg'}
            need(svg.find('s:title',ns) is not None and svg.find('s:desc',ns) is not None,f'Inaccessible SVG {p.name}')
        except ET.ParseError:errors.append(f'Malformed SVG {p.name}')
    return errors
