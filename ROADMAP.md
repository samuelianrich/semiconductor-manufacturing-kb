# Staged research and build roadmap

**Phases 0, 0A and 1 are delivered; Phase 2 is next.** Do not bulk-generate chapter placeholders that appear to be completed articles. A phase can be coherent before every possible extension is written, but all stated core coverage must pass its exit gate.

| Phase | Scope | Prerequisites | Exit evidence |
|---|---|---|---|
| 0 — Architecture | Navigation, scope, dependencies, templates, policies, source plan, validation | User specification | Coherent graphs, no broken local links, coverage audit, logical Git commits |
| 0A — Persistent process map | Typed CSV graph, generated views, evidence links and validation | 0 | Seven dimensions representable; route and reference checks pass; later scope clearly planned |
| 1 — Foundation (1A materials-to-wafer; 1B physics/MOSFET) | 01–06; relevant glossary; historical context as needed | 0 | Cited Earth-to-wafer path and device fundamentals; crystal and MOS diagrams; impurity and carrier vocabulary |
| 2 — Fab fundamentals | 08–16 | 1 | Cited unit-process articles, tool schematics and process variables/failure modes; no unexplained fab vocabulary |
| 3 — Devices and wiring | 17–19 | 2 | Planar/FinFET/GAA and BEOL cross sections; FEOL/MOL/BEOL boundaries; interconnect alternatives |
| 4 — Design/manufacturing interface | 07 | 3 | Concise design-to-mask flow; PDK, DRC/LVS, node terminology and reticle context |
| 5 — Yield and test | 21 → 20 → 22 | 3; coordinate 4 | Worked unit-aware yield example; wafer map; KGD caveats; thinning/dicing flow |
| 6 — Memory | 23–24 | 2 and 5 | DRAM cell and HBM stack visuals; bandwidth example; TSV and stack-test evidence |
| 7 — Packaging | 25–26 | 3, 5 and 6 | Taxonomy by primary architecture; package cross sections; assembly/test/yield interactions; alternative comparison |
| 8 — Final system | 27–32 | 7 | Package → PCB/module → server → rack trace; power and thermal worked examples; final test and reliability boundaries |
| 9 — Ecosystem | 33–35; equipment/material category files | Relevant process chapters and 8 | Dated sourced supplier/role/country/dependency tables and enabling-input map; no unsupported concentration figures |
| 10 — Economics and investment | 36–37 | 5, 7, 8 and 9 | Auditable hypothetical models; separate dated industry profiles; sensitivity and assumptions; no recommendations |
| 11 — Rubin case study | 38 | General chain and 10 | Every important product claim registered, source-labeled and dated; product variants separated; unknowns explicit |
| 12 — Repository audit | Entire repository | 1–11 | Human technical/source review plus structural audit; missing terms/graphics, contradictions and stale claims tracked |

## Module-sized work loop

1. Scope one reader outcome and article boundary; register prerequisites and canonical ownership.
2. Search the designated source families; record exact supporting sections and uncertainty.
3. Outline before prose. Resolve contradictory sources or show both positions.
4. Draft intuition → mechanism → implementation → manufacturing difficulty → optional deeper detail.
5. Add original labeled diagrams, a glossary delta, cross-links and unit-aware examples.
6. Capture process cost drivers as evidence notes. Before Phase 10, defer full economics and investment essays; link their planned module indexes instead. This preserves the engineering-first gate.
7. Validate sources, equations, rights, graph links and vocabulary. Record status and unresolved issues.
8. Make a small descriptive Git commit for the completed module or coherent submodule.

## Phase 1 delivery

Both work packages are delivered: ten chapters, nine original figures, a glossary, comparisons, process evidence and scoped company claims. [Review record](AUDIT_PHASE1.md) · [Reading path](LEARNING_PATHS.md#phase-1-reading-path). The next engineering work is Phase 2, modules 08–16.

## Progress accounting

Track module state in `catalog/modules.json`; an index is not a chapter. Record article status in its metadata; require source and technical review before `reviewed`. A build phase is complete only when its exit evidence exists. Do not count empty reference folders, templates or scope inventories as researched content.

## Deferred by design

Later-phase technical chapters, comprehensive supplier tables, quantitative market research, Rubin specifications and the full-repository Phase 12 audit remain pending. Phase 1 supplier examples document narrow roles only.
