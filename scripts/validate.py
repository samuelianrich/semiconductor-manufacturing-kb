#!/usr/bin/env python3
"""Validate architecture structure, without claiming technical/source accuracy."""
from pathlib import Path
from urllib.parse import unquote
import csv, json, re, sys
ROOT = Path(__file__).resolve().parents[1]
errors = []
def check(ok, message):
    if not ok: errors.append(message)
for name in ['README.md','ROADMAP.md','ARCHITECTURE.md','CONTRIBUTING.md','SOURCE_POLICY.md','CONFIDENCE_LEVELS.md','ARTICLE_TEMPLATE.md','DEPENDENCIES.md','LEARNING_PATHS.md','RESEARCH_STRATEGY.md','TAXONOMY.md','MAINTENANCE.md','AUDIT_PHASE0.md']:
    check((ROOT/name).is_file(), f'Missing document: {name}')
modules = json.loads((ROOT/'catalog/modules.json').read_text())
by_id = {m['id']:m for m in modules}
check(len(modules) == len(by_id) == 43, 'Expected 43 unique module IDs')
check(len({m['path'] for m in modules}) == len(modules), 'Duplicate paths')
for m in modules:
    check((ROOT/m['path']/'README.md').is_file(), f'Missing module: {m["id"]}')
    check(bool(m['topics']), f'Missing scope: {m["id"]}')
    for p in m['prerequisites']:
        check(p in by_id, f'Unknown prerequisite: {p}')
        if p in by_id: check(by_id[p]['phase'] <= m['phase'], f'Phase conflict: {p} -> {m["id"]}')
visited, active = set(), set()
def visit(node):
    if node in active:
        errors.append(f'Prerequisite cycle: {node}')
        return
    if node in visited or node not in by_id: return
    active.add(node)
    for p in by_id[node]['prerequisites']: visit(p)
    active.remove(node)
    visited.add(node)
for node in by_id: visit(node)
expected = 'flowchart TD\n'+''.join(f'  {m["id"]}["{m["id"]}: {m["title"]}"]\n' for m in modules)+''.join(f'  {p} --> {m["id"]}\n' for m in modules for p in m['prerequisites'])
graph = (ROOT/'assets/diagrams/prerequisites.mmd').read_text().strip()
check(graph == expected.strip(), 'Registry/graph mismatch')
for name in ['assets/diagrams/prerequisites.mmd','assets/process_flows/physical_chain.mmd','assets/supply_chain_maps/enabling_inputs.mmd']:
    check((ROOT/name).read_text().strip() in (ROOT/'DEPENDENCIES.md').read_text(), f'Displayed graph mismatch: {name}')
link_count = 0
md_files = [p for p in ROOT.rglob('*.md') if '.git' not in p.parts and 'project' not in p.relative_to(ROOT).parts]
for path in md_files:
    body = re.sub(r'```.*?```', '', path.read_text(), flags=re.S)
    body = re.sub(r'`[^`]*`', '', body)
    for target in re.findall(r'\[[^\]\n]*\]\(([^)\n]+)\)', body):
        target = target.strip().strip('<>')
        if re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*:', target): continue
        link_count += 1
        file_part, _, anchor = unquote(target).partition('#')
        resolved = (path.parent/file_part).resolve() if file_part else path
        check(resolved.is_relative_to(ROOT), f'Escaping link: {target}')
        check(resolved.exists(), f'Broken link: {path.relative_to(ROOT)} -> {target}')
        if anchor and resolved.is_file():
            content = resolved.read_text()
            explicit = set(re.findall(r'<a\s+(?:id|name)=["\']([^"\']+)["\']', content))
            headings = {re.sub(r'[^\w\- ]','',h.lower()).replace(' ','-') for h in re.findall(r'^#{1,6}\s+(.+)$',content,flags=re.M)}
            check(anchor in explicit|headings, f'Unresolved anchor: {target}')
ids = re.findall(r'<a\s+(?:id|name)=["\']([a-z0-9]+-[a-z0-9]+-\d+)["\']',(ROOT/'42_references/bibliography.md').read_text())
check(len(ids) == len(set(ids)), 'Duplicate bibliography IDs')
asset_ids = set()
for asset in csv.DictReader((ROOT/'assets/manifest.csv').open()):
    check(asset['asset_id'] not in asset_ids, 'Duplicate asset ID')
    asset_ids.add(asset['asset_id'])
    check((ROOT/asset['path']).is_file(), f'Missing asset: {asset["path"]}')
    check(bool(asset['title'] and asset['source'] and asset['license']), 'Incomplete asset metadata')
if errors:
    print('\n'.join('FAIL: '+e for e in errors)); sys.exit(1)
print(f'PASS: {len(modules)} modules; {sum(len(m["prerequisites"]) for m in modules)} prerequisite edges; {len(md_files)} Markdown documents; {link_count} local links; {len(asset_ids)} registered diagrams.')
print('No prerequisite cycles, phase conflicts, missing paths, or graph synchronization errors.')
print('Structural checks only; technical/source review remains deferred until content exists.')
