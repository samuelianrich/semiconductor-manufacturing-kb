# Phase 2 author review record

Review date: 2026-09-17. Scope: fab fundamentals, modules 08–16. Status: delivered following the checks recorded below; independent specialist review remains pending. This is a bounded author technical/source review, not peer review or process qualification.

## Delivered coverage

| Module | Core coverage and exit evidence |
|---|---|
| 08 Fab | FEOL/MOL/BEOL boundaries, repeated loops, lots/carriers, recipe/mask distinction, contamination interfaces, throughput/cycle-time example |
| 09 Lithography | Resist sequence and tone, DUV/EUV optics, tin-plasma source, multilayer reflection, masks/pellicles, CAR/PEB, stochastic limits, CD/CDU/overlay, OPC, multiple-patterning concept, resolution and DOF examples |
| 10 Deposition | CVD/LPCVD/PECVD, ALD, sputter PVD and epitaxy; materials/tool functions, nucleation, coverage, stress, growth-cycle example |
| 11 Etch | Wet/RIE/DRIE/Bosch/ALE, profile/selectivity/loading, damage, aspect ratio and mask budget |
| 12 Doping | Implant/diffusion, beam functions, mask/energy/dose/channeling, activation/RTP, thermal budget, dose charge balance |
| 13 Oxidation | Silicon consumption versus deposition, dry/wet, moving interface, kinetics/model limits and planar mass balance |
| 14 Clean | Contaminant classes, material history, solvent/RCA/plasma functions, rinse/water quality, termination, damage and scoped removal metric |
| 15 CMP | Pad/slurry/conditioning/contact/endpoint, planarity, dishing/erosion/scratches, local pressure–velocity approximation |
| 16 Metrology | Optical/electron/thickness/height/composition methods, sampling, uncertainty, SPC/control limits versus specifications, process windows and excursion response |

Nine original SVG schematics have accessible titles/descriptions, conceptual/not-to-scale labels, source bases and manifest records. The generator preserves editable geometry. A generated Mermaid route adds a separate physical-navigation view. Glossary, method comparisons, engineering cost-driver notes and reading path accompany the chapters.

## Source and scientific review

Primary sources include university teaching material, author-hosted lectures, NIST, imec and equipment developers' descriptions of their own technology. The [source index](42_references/phase2_source_index.json) records 33 new sources; HU-FAB-001 has expanded reviewed scope. Vendor descriptions support mechanisms, not market share, exclusivity, customer wins or Rubin use. No new supplier edge or product-specific claim is inferred.

The reviewer checked dimensions and assumptions for resolution/focus scaling, ALD cycle arithmetic, selectivity/mask loss, dose/current conversion, oxide mass balance, CMP rate conversion, count-based removal, binomial sampling and the control-limit example. All numerical process inputs are explicitly hypothetical. Conservation/unit checks are automated; model applicability remains an author judgment.

Source limitations retained: the NIST thin-film report was reviewed at metadata/abstract level only; historical teaching sources do not establish current production recipes; the German ZEISS optics explanation was used for optics only; overly broad vendor claims about perfect films, universal layer-per-cycle growth or flatness were not adopted. No external drawings or operating procedures were copied. Existing bibliography rights remain unchanged.

## Graph review

The teaching route is accepted wafer → thermal oxide → developed resist → etched oxide with resist → stripped patterned oxide. It is explicitly an author-composed educational route. Process-family membership and equipment functions are distinct from physical flow. Deposition, implant/activation, CMP and measurement are not falsely forced into one serial route. Aggregate logic, DRAM, test, packaging and system paths remain planned.

Every new reviewed entity description and edge has a source locator; recipe conditions and detection limitations remain explicit. No fabricated supplier adoption, market concentration or performance figures were added.

## Corrections and remaining boundaries

M39 history was incorrectly marked reviewed during Phase 1 despite having only an index. Its status is now architecture-only. A regression check requires a reviewed module to own at least one reviewed canonical article; that structural rule does not replace a coverage review. The research-strategy introduction now distinguishes the historical candidate-source plan from actual retrieved evidence.

This phase establishes fundamentals, not complete transistor/interconnect recipes. Advanced resist formulations, detailed ALE windows, full measurement-system analysis, exact process limits and current supplier capability comparisons need specialist/deeper review. Phase 3 owns device and wiring integration. Yield/test qualification, economics and product-specific case studies remain assigned to later phases.

## Validation evidence

- Repository validator passed: 43 modules, 125 Markdown documents, 2,422 local links and 35 registered diagrams; map contains 96 entities and 119 edges.
- All 22 unit checks passed: existing graph/foundation regressions plus Phase 2 arithmetic/model invariants and reviewed-module status regression.
- Visual review: rasterized contact sheet of all nine new SVGs, inspected for readability, clipping and process-direction consistency.
- Git diff whitespace check and GitHub validation workflow after publication.

Automated checks establish structural consistency and arithmetic, not independent scientific accuracy. CI run status is reported with the release rather than assumed by this record.
