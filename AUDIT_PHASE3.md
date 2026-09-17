# Phase 3 author review record

Review date: 2026-09-17. Scope: modules 17–19, device integration and wiring. Review is bounded author technical/source review; independent specialist review remains pending. The chapters explain mechanisms and integration boundaries, not qualified foundry recipes.

## Coverage and ownership

| Module / article | Exit evidence |
|---|---|
| 17 — Planar and FinFET | Wells/STI, gate/spacer/source-drain functions, replacement gate, thermal constraints, original longitudinal/transverse sections and series-capacitance EOT example |
| 17 — Nanosheets | Alternating Si/SiGe, inner spacers, attached source/drain, release, surrounding gate and bottom-isolation concerns; two complementary sections; perimeter/clearance examples |
| 17 — Contacts/MOL | Semiconductor versus gate contact, interface/plug resistance, contact module, W/Co process functions, contact-area/liner-area calculations and labeled contact section |
| 18 — Wire RC | Contact/via/local/global definitions, resistance/capacitance, distributed first moment, coupling, IR loss, original RC schematic and unit-aware examples |
| 18 — Materials/reliability | Cu/W/Co/Ru roles, barrier/liner/seed, low-k damage, electromigration, thermomechanical fatigue and dielectric breakdown; material ranking limits and current-density example |
| 19 — BEOL | Dielectric/cavity/liner/fill/CMP loop, single/dual damascene and subtractive alternative, four-level cross-section, passivation/terminal boundary, enclosure example and defect table |

The [reading path](LEARNING_PATHS.md#phase-3-reading-path), [glossary](40_glossary/phase3_glossary.md), [comparisons](41_reference_tables/phase3_comparisons.md) and [cost-driver notes](36_economics/phase3_cost_drivers.md) link these boundaries. Engineering costs are data requirements only; quantitative economics and investment remain later phases.

## Source fitness and limitations

Fifteen new primary research, university or developer source records are indexed in [Phase 3 source metadata](42_references/phase3_source_index.json). Existing MOS, epitaxy, CMP and fabrication references are reused within their scope. HU-FAB-001 review was extended to §3.8 for metallization. The exact locators and access limits live in the canonical bibliography.

Historical planar and 2012 FinFET teaching sources support functions, not current production setpoints or node forecasts. The 2017 nanosheet paper was read for fabrication, isolation and gate/contact discussion; its numerical research performance is not attributed to a product. The two IBM liner/fill papers were reviewed through their primary abstracts only. The AVS low-k source is a primary conference abstract. A blocked PMC review page was not used as evidence. Vendor claims about perfect fill, record results, universal resistance ranking and customer adoption were excluded.

The historical RC lecture includes an inconsistent resistance-per-length unit statement. The chapter derives and uses Ω per length, not Ω times length. Elmore first moment is explicitly distinguished from exact 50% delay. New numerical examples are hypothetical and do not inherit production values from the sources.

## Diagram and physical review

Eight original SVGs label orientation, materials/functions and conceptual scale. No external illustrations were copied. Visual inspection uses rasterized outputs: planar source/channel/drain continuity, dielectric separation around the fin/sheets, MOL terminal isolation, RC connectivity, selected multilevel vias, liner/fill geometry and inner spacers are checked against the prose. Transverse sheet sections explicitly place anchors outside the section; the longitudinal view shows the missing end geometry. Both omit layers where stated.

## Map semantics

Two new generated views separate device alternatives/MOL and Cu BEOL. Planar, FinFET and nanosheet operations converge at an abstract compatible terminal boundary; they are alternatives, not three required inputs. The copper route uses separate cavity, preparation, fill and CMP states. Additional levels and terminal finishing are explicitly aggregated; an actual layer-specific flow would create new instances.

All new reviewed descriptions and relationships have evidence locators. No supplier assignment was inferred. The endpoint is a fabricated wafer with test pending. The larger aggregate logic/test/die-preparation node and tested die remain planned; graph regression checks preserve this boundary. The map contains 118 entities and 164 relationships.

## Verification

Repository validation checks local references, catalog/source/node IDs, accessible asset registration, math delimiters, typed graph constraints and generated-view synchronization. Unit tests cover EOT/capacitance equivalence, geometry and area conversion, contact shrink scaling, RC dimensional consistency and distributed-ladder convergence, voltage/power/current density, enclosure and the fabricated-versus-tested boundary. Existing Phase 1/2 regressions remain required.

Local checks passed: 43 modules, 138 Markdown documents, 2,946 local links, 45 registered diagrams and all 30 unit tests. GitHub workflow outcome is checked after publication. A passing structural or arithmetic check is not independent technical approval. Specialist review remains open for advanced process variants, current-crowding/nanoscale transport models, reliability extrapolation and foundry-specific limits.
