#!/usr/bin/env python3
"""Validate the typed graph and deterministically render its navigation views."""
import argparse
import csv
import json
import re
from collections import defaultdict, deque
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
START, END = '<!-- BEGIN GENERATED MAP -->', '<!-- END GENERATED MAP -->'

def read_data(root=ROOT):
    data = root / 'manufacturing_map/data'
    out = {}
    for p in data.glob('*.csv'):
        with p.open(newline='') as handle: out[p.stem] = list(csv.DictReader(handle))
    out['schema'] = json.loads((data/'schema.json').read_text())
    out['views'] = json.loads((data/'views.json').read_text())
    return out

def material_graph(edges):
    adj = defaultdict(set)
    for e in edges:
        s, t, rel = e['source_id'], e['target_id'], e['relationship']
        if rel == 'CONSUMES': adj[t].add(s)
        elif rel in ('PRODUCES', 'INTEGRATED_INTO'): adj[s].add(t)
    return adj

def reachable(adj, start, stops=None):
    seen, queue = set(), deque(adj[start])
    while queue:
        item = queue.popleft()
        if item in seen: continue
        seen.add(item)
        if stops is None or item not in stops: queue.extend(adj[item])
    return seen

def has_cycle(pairs):
    adj = defaultdict(list)
    for s, t in pairs: adj[s].append(t)
    active, done = set(), set()
    def visit(n):
        if n in active: return True
        if n in done: return False
        active.add(n)
        if any(visit(t) for t in adj[n]): return True
        active.remove(n); done.add(n)
        return False
    return any(visit(n) for n in list(adj))

def validate(data, root=ROOT):
    errors=[]
    def need(ok, msg):
        if not ok: errors.append(msg)
    schema=data['schema']; entities={e['entity_id']: e for e in data['entities']}
    edges={e['edge_id']:e for e in data['process_edges']}; routes={r['route_id']:r for r in data['routes']}
    for table, field in [('entities','entity_id'),('process_edges','edge_id'),('routes','route_id')]:
        vals=[x[field] for x in data[table]]
        need(len(vals)==len(set(vals)), f'Duplicate IDs in {table}')
    modules={x['id'] for x in json.loads((root/'catalog/modules.json').read_text())}
    with (root/'42_references/claims.csv').open() as handle:
        claims={x['claim_id']:x for x in csv.DictReader(handle)}
    bibliography=(root/'42_references/bibliography.md').read_text()
    sources=set(re.findall(r'<a\s+id="([^"]+)"',bibliography))
    evidenced=set(); supported_claims=defaultdict(set)
    for ev in data['evidence_links']:
        key=(ev['record_type'],ev['record_id'],ev['field'])
        target=entities.get(ev['record_id']) if ev['record_type']=='entity' else edges.get(ev['record_id']) if ev['record_type']=='edge' else None
        need(target is not None,f'Invalid evidence target: {key}')
        need(ev['field']=='relationship' if ev['record_type']=='edge' else target is not None and ev['field'] in target, f'Invalid evidence field: {key}')
        need(ev['source_id'].lower() in sources,f'Missing bibliography source: {ev["source_id"]}')
        need(bool(ev['locator']), f'Missing evidence locator: {key}')
        if ev['claim_id']:
            need(ev['claim_id'] in claims,f'Missing claim: {ev["claim_id"]}')
            if ev['claim_id'] in claims:
                need(ev['source_id'] in claims[ev['claim_id']]['source_ids'].split(';'),f'Claim/source mismatch: {key}')
                need(claims[ev['claim_id']]['confidence'] in ['CONFIRMED','INDUSTRY-STANDARD INFERENCE','ANALYST ESTIMATE','UNKNOWN / PROPRIETARY'],f'Invalid confidence: {key}')
            supported_claims[(ev['record_type'],ev['record_id'])].add(ev['claim_id'])
        evidenced.add(key)
    for e in entities.values():
        need(e['entity_type'] in schema['entity_types'],f'Invalid entity type: {e["entity_id"]}')
        need(e['status'] in schema['statuses'],f'Invalid status: {e["entity_id"]}')
        need(e['module_id'] in modules,f'Invalid module: {e["entity_id"]}')
        need((root/e['primary_article']).is_file(),f'Missing article: {e["primary_article"]}')
        if e['status']=='reviewed':
            need(('entity',e['entity_id'],'description') in evidenced,f'No description evidence: {e["entity_id"]}')
            need(bool(e['last_reviewed']),f'No review date: {e["entity_id"]}')
    related=set(); signatures=set()
    for e in edges.values():
        s,t,r=e['source_id'],e['target_id'],e['relationship']; related.update([s,t])
        need(s in entities and t in entities, f'Dangling edge: {e["edge_id"]}')
        rule=schema['relationships'].get(r)
        need(rule is not None,f'Unknown relationship: {r}')
        if rule and s in entities and t in entities:
            need(entities[s]['entity_type'] in rule['source_types'] and entities[t]['entity_type'] in rule['target_types'],f'Wrong endpoint types: {e["edge_id"]}')
            if rule['route_required']: need(bool(e['route_id']),f'Missing route: {e["edge_id"]}')
            if rule['conditions_required']: need(bool(e['conditions']),f'Missing conditions: {e["edge_id"]}')
        if e['route_id']: need(e['route_id'] in routes,f'Unknown route: {e["edge_id"]}')
        signature=(s,r,t,e['route_id'],e['conditions'])
        if r=='ALTERNATIVE_TO':
            need(s<t,f'Noncanonical symmetric edge: {e["edge_id"]}')
            signature=(*sorted([s,t]),r,e['route_id'],e['conditions'])
        need(signature not in signatures,f'Duplicate edge: {e["edge_id"]}');signatures.add(signature)
        need(e['status'] in schema['statuses'],f'Invalid edge status: {e["edge_id"]}')
        if e['status']=='reviewed':
            need(('edge',e['edge_id'],'relationship') in evidenced,f'No edge evidence: {e["edge_id"]}')
            need(bool(e['last_reviewed']),f'Missing edge review date: {e["edge_id"]}')
            if r=='SUPPLIED_BY': need(bool(supported_claims[('edge',e['edge_id'])]),f'Supplier relationship lacks claim ID: {e["edge_id"]}')
    for e in entities.values():
        if e['entity_id'] not in related:
            reason=schema['disconnected_exceptions'].get(e['entity_id'])
            need(bool(reason),f'Unexplained isolated entity: {e["entity_id"]}')
    for table,allowed in [('process_nodes',['operation','process_family']),('materials',['material']),('equipment',['equipment']),('suppliers',['supplier'])]:
        vals=[x['entity_id'] for x in data[table]]
        need(len(vals)==len(set(vals)),f'Duplicate extension records: {table}')
        need(set(vals)=={i for i,e in entities.items() if e['entity_type'] in allowed},f'Incomplete or invalid typed extension: {table}')
    need(not has_cycle([(e['source_id'],e['target_id']) for e in edges.values() if e['relationship']=='PART_OF']),'Containment cycle')
    need(not has_cycle([(r['route_id'],r['parent_route']) for r in routes.values() if r['parent_route']]),'Route hierarchy cycle')
    for r in routes.values():
        need(not r['parent_route'] or r['parent_route'] in routes,f'Unknown parent route: {r["route_id"]}')
        need((root/r['primary_article']).is_file(),f'Missing route article: {r["route_id"]}')
        need(not has_cycle([(e['source_id'],e['target_id']) for e in edges.values() if e['relationship']=='PRECEDES' and e['route_id']==r['route_id']]),f'Sequence cycle: {r["route_id"]}')
    adj=material_graph(edges.values()); scope=schema['reachability']
    for t in scope['targets']:need(t in reachable(adj,scope['source']),f'Material chain cannot reach {t}')
    return errors

def md(s): return s.replace('|','\\|').replace('\n',' ')
def diagram_id(s): return s.replace('-','_')
def render_view(data, name, config):
    ents={e['entity_id']:e for e in data['entities']}; edges=data['process_edges']
    lines=['flowchart LR']; selected=[]; pairs=[]
    if 'keep' in config:
        chosen=set(config['keep']); adj=material_graph(edges)
        selected=[ents[i] for i in config['keep']]
        for s in sorted(chosen):
            for t in sorted(reachable(adj,s,chosen)&chosen): pairs.append((s,t,'collapsed path'))
        evidence_edges=[]
    else:
        if 'routes' in config: evidence_edges=[e for e in edges if e['route_id'] in config['routes'] and e['relationship']!='PRECEDES']
        elif 'relationships' in config: evidence_edges=[e for e in edges if e['relationship'] in config['relationships']]
        else:
            chosen={i for i,e in ents.items() if e['entity_type'] in config.get('types',[])}
            evidence_edges=[e for e in edges if e['source_id'] in chosen or e['target_id'] in chosen]
        ids={e[k] for e in evidence_edges for k in ['source_id','target_id']}
        selected=[ents[i] for i in sorted(ids)]
        for e in evidence_edges:
            s,t=e['source_id'],e['target_id']
            if e['relationship']=='CONSUMES': s,t=t,s
            pairs.append((s,t,e['relationship'].lower().replace('_',' ')))
    for e in selected:
        label=e['name'].replace('"',"'")
        if e['status']=='planned':label+=' [planned]'
        lines.append(f'  {diagram_id(e["entity_id"])}["{label}"]')
    for s,t,l in pairs:lines.append(f'  {diagram_id(s)} -->|"{l}"| {diagram_id(t)}')
    body='\n'.join(lines)+'\n' if selected else ''
    result=['**Generated from the canonical CSV graph.** Planned scope is not technical evidence.\n']
    if body:result+=['```mermaid\n'+body+'```\n']
    else:result+=['No researched relationships have been entered for this view yet.\n']
    result += [f'*MAP-{name.upper().replace("_","-")} — {config["caption"]} Original schematic; CC BY 4.0. Source: graph records and their evidence links; no physical scale.*\n']
    result += ['| ID | Entity | Status | Canonical article |','|---|---|---|---|']
    for e in selected:result.append(f'| {e["entity_id"]} | {md(e["name"])} | {e["status"]} | [{md(e["name"])}](../{e["primary_article"]}) |')
    if evidence_edges:
        result+=['\n| Edge | Relationship | Conditions | Evidence |','|---|---|---|---|']
        for e in evidence_edges:
            evs=[v for v in data['evidence_links'] if v['record_type']=='edge' and v['record_id']==e['edge_id']]
            refs='; '.join(f'[{v["source_id"]}](../42_references/bibliography.md#{v["source_id"].lower()}) ({md(v["locator"])})'+(f' · {v["claim_id"]}' if v['claim_id'] else '') for v in evs) or 'Planned; not evidence-backed'
            result.append(f'| {e["edge_id"]} | {e["source_id"]} → {e["relationship"]} → {e["target_id"]} | {md(e["conditions"])} | {refs} |')
    return '\n'.join(result)+'\n',body

def generated_files(data, root=ROOT):
    result={}
    for name,cfg in data['views'].items():
        block,diagram=render_view(data,name,cfg)
        path=root/'manufacturing_map'/f'{name}.md'
        current=path.read_text() if path.exists() else f'# {cfg["title"]}\n\n[Map home](README.md) · [Schema](SCHEMA.md) · [Full entity register](process_nodes.md)\n\n{START}\n{END}\n'
        assert current.count(START)==current.count(END)==1,f'Invalid markers: {path}'
        prefix, rest=current.split(START);_,suffix=rest.split(END)
        result[path]=prefix+START+'\n'+block+END+suffix
        if diagram:result[root/'assets/process_flows'/f'map_{name}.mmd']=diagram
    nodes=['# Manufacturing entity and process register','', 'Generated from the canonical entity and process tables; edit CSVs, then regenerate.','', '[Map home](README.md) · [Schema](SCHEMA.md)','']
    for e in data['entities']:
        nodes.extend([f'<a id="{e["entity_id"].lower()}"></a>',f'## {e["entity_id"]} — {e["name"]}','',f'Type: `{e["entity_type"]}` · Status: **{e["status"]}** · [Article](../{e["primary_article"]})','',e['description'],''])
        p=next((p for p in data['process_nodes'] if p['entity_id']==e['entity_id']),None)
        if p:nodes.extend([f'Purpose: {p["purpose"]}',f'\nScope: {p["scope"]}',f'\nMechanism: {p["mechanism_summary"] or "Not yet researched."}',f'\nNotes: {p["notes"]}',''])
    result[root/'manufacturing_map/process_nodes.md']='\n'.join(nodes)+'\n'
    # Compatibility paths now generated from the graph, not manually authored parallel truths.
    result[root/'assets/process_flows/physical_chain.mmd']=render_view(data,'master_process_map',data['views']['master_process_map'])[1]
    result[root/'assets/supply_chain_maps/enabling_inputs.mmd']=render_view(data,'enabling_inputs',data['views']['enabling_inputs'])[1]
    for name in ['README.md','DEPENDENCIES.md']:
        path=root/name
        text=path.read_text()
        for key,asset in [('OVERVIEW','assets/process_flows/physical_chain.mmd'),('ENABLING','assets/supply_chain_maps/enabling_inputs.mmd')]:
            start,end=f'<!-- BEGIN {key} -->',f'<!-- END {key} -->'
            if start in text:
                before,rest=text.split(start);_,after=rest.split(end)
                text=before+start+'\n```mermaid\n'+result[root/asset]+'```\n'+end+after
        result[path]=text
    return result

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--check',action='store_true');args=parser.parse_args()
    data=read_data();errors=validate(data)
    if errors: raise SystemExit('\n'.join('FAIL: '+e for e in errors))
    outputs=generated_files(data)
    if args.check:
        stale=[str(p.relative_to(ROOT)) for p,s in outputs.items() if not p.exists() or p.read_text()!=s]
        if stale:raise SystemExit('Stale generated views: '+', '.join(stale))
    else:
        for p,s in outputs.items():p.parent.mkdir(parents=True,exist_ok=True);p.write_text(s)
    print(f'MAP PASS: {len(data["entities"])} entities, {len(data["process_edges"])} edges; evidence references, route constraints and generated views checked.')
if __name__=='__main__':main()
