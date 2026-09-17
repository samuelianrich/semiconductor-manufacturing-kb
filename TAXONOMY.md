# Article and diagram taxonomy

## Article classes

| Class | Reader outcome | Required distinctive structure | Canonical home |
|---|---|---|---|
| Concept explainer | Understand what a term means and why it exists | Intuition, mechanism, definitions, limits, concept diagram | Topic module |
| Unit-process article | Explain one material-changing operation | Inputs/outputs, numbered steps, chamber/tool, materials, control variables, defects, alternatives | 09–16 and relevant upstream modules |
| Integration article | Explain how processes jointly create a structure | Ordered/conditional flow, interfaces, cross sections, thermal budget, controls and test | 17, 19, 23–32 |
| Architecture comparison | Distinguish competing implementations | Common comparison dimensions, assumptions, advantages and costs; avoid false mutually exclusive categories | Owning module |
| Equipment category | Connect machine action to process challenge | What it physically does, process location, controls, supplier evidence; link economics | 33; separate file per category |
| Materials category | Connect material properties to use and qualification | Function, specifications, contamination/handling, alternatives, supplier evidence | 34; separate file per category |
| Company profile | Identify a firm's documented role | Entity/segment/date, sourced roles and dependencies; product claims labeled | 35; template provided |
| Economics model | Explain cost/throughput/yield sensitivity | Cost boundary, inputs with units, equations, assumptions, worked example and sensitivities | 36 |
| Investment research note | Explain industry structure and value capture | Evidence-backed segment analysis; risks and substitution; no recommendations | 37 |
| Product case study | Reconstruct a disclosed real implementation | Claim IDs, exact product variant, date, fact/inference/estimate/unknown, generic links | 38 |
| Historical narrative | Explain what problem motivated a transition | Contemporary evidence, dates, continuing alternatives | 39 |
| Glossary/reference table | Help readers navigate or compare | Definition/dimensions, purpose, canonical links and citations | 40–41 |

Packaging taxonomy first distinguishes flip chip, 2.5D, 3D and fan-out, then explains interposers, bridges, TSVs and bonding as implementation choices. Chiplets describe partitioning and can coexist with multiple package categories; these terms must not be presented as mutually exclusive bins.

## Diagram classes

| Class and directory | Initial priority subjects | Required annotations |
|---|---|---|
| Process flows — assets/process_flows | Earth-to-wafer; lithography; design-to-mask; logic/memory convergence; die prep | Inputs, outputs, arrow meanings, optional/repeated paths and process boundaries |
| Cross sections — assets/cross_sections | MOS capacitor/MOSFET; FinFET; GAA; multilayer IC; TSV; HBM; interposer/package | Material names, orientation, contacts, scale disclaimer and conceptual versus documented status |
| Equipment — assets/equipment | CZ puller; scanner; deposition chamber; plasma etcher; implanter; CMP tool | Material/energy flow, key components and controls; schematic, not construction instructions |
| Knowledge diagrams — assets/diagrams | Prerequisites; concept links; wafer maps; yield illustrations; package exploded views | Legend, graph edge type, test/bin meaning or layer order |
| Supply maps — assets/supply_chain_maps | Materials, tools, design, foundry, memory, packaging and system roles | Material versus enabling-service edges; geography dates; supplier confidence where populated |
| Comparison tables/plots — assets/tables | Lithography, deposition, etch, packaging, equipment, materials, yield/cost curves | Units, source IDs, assumptions, comparable basis and accessible text equivalent |

Prefer original SVG for simple reusable cross sections and equipment schematics; Mermaid for small flow/knowledge diagrams; standard plotting tools for quantitative figures with reproducible input data. Avoid generated photorealism for technical cross sections. Large graphs should also have an accessible text/table representation, as the Phase 0 inventory does.

Every visual requires an asset ID, title, caption, source/derivation, creator, license/permission, editable source, figure type, article uses, and accessible description. Track these in [assets/manifest.csv](assets/manifest.csv). A diagram's caption must say whether it is conceptual or depicts a documented implementation. Never imply an original conceptual drawing reveals proprietary Rubin geometry.
