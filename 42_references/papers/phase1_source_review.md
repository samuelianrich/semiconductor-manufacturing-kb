# Phase 1 source review notes

Reviewed 2026-09-16. This is author source review, not independent peer review. The bibliography records the exact access scope and locators. Sources were selected to explain mechanisms and validate important boundary distinctions.

| Question | Evidence selected | Review decision |
|---|---|---|
| Is abundant silica the same as qualified feedstock? | USGS-SILICON-001, NTNU-QUARTZ-001, CHEGINI-QUARTZ-001 | Separate mineral identity, chemistry, physical behavior and qualification. Laboratory beneficiation is an example, not a production certification. |
| Is quartz for crucibles the same supply path as reduced silicon? | SIBELCO-QUARTZ-001, ELKEM-QUARTZ-001 | Separate enabling consumable from mass feedstock. Do not infer a mine-to-Rubin lineage. |
| Does the net reduction equation describe one furnace reaction? | NTNU-SMELTING-001 | No. Explain SiO/SiC intermediates, gradients and transport; reserve the equation for mass bookkeeping. |
| Does “polysilicon” establish electronic-grade qualification? | WACKER-POLY-001, HSC-POLY-001, REC-FBR-001 | No. Distinguish crystal form from impurity/customer specification. FBR example is historical and PV-focused. |
| Can one growth method or finish represent all wafers? | SUMCO-WAFER-001, PVA-CZ-001, SILTRONIC-FZ-001 | No. Show CZ and FZ and the boundary between polished, epitaxial and SOI starting materials. |
| Can public SEMI catalog text establish all acceptance limits? | SEMI-WAFER-001, SEMI-TERMS-001 | No. Define quantities; explicitly leave normative/customer numeric limits unspecified. |
| Are textbook MOSFET equations valid for a modern GPU? | HU-MOSFET-001, HU-SCALING-001, MIT-MOSFET-001 | Use only as teaching models with assumptions. No extraction of Rubin parameters. |
| Do ideal CMOS diagrams mean zero real leakage? | MIT-CMOS-001, MIT-POWER-001, HU-SCALING-001 | Explain ideal static path separately from real leakage and switching loss. |

## Sources not promoted into evidence

Search results from general blogs, unsourced market-size pages and social discussions were not used. The Elkem Iceland page describes ferrosilicon and was not used as a pure-silicon process source. Vendor superlatives, current market shares and customer-specific input allocations were omitted. IBM research descriptions explain architecture without proving a commercial product's implementation.

## Differences preserved

Vendor pages give differently scoped approximate process temperatures. This release does not manufacture a single universal temperature setpoint. The wafer standard's public scope and terminology compilation are accessible, but the full normative M1 limits were not accessed. The Chegini paper is an early accepted version and only its abstract was read; quantitative experimental recipes/results are not imported.
