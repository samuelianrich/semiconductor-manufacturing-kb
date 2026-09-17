# Semiconductor Manufacturing Knowledge Base

**From quartz to a powered, cooled, rack-scale AI system.**

A GitHub-ready knowledge repository for a second-year electrical engineering student. General semiconductor manufacturing is the foundation; NVIDIA Vera Rubin will be a source-labeled case study. Engineering, manufacturing economics and investment research have separate homes. No buy/sell recommendations.

**Current release: Phase 0 architecture.** Directories and indexes describe planned coverage, not completed semiconductor chapters. No Rubin product specifications or supplier assignments have been asserted. Architecture is ready for Phase 1 after the checks in the [audit](AUDIT_PHASE0.md); later phases remain unbuilt.

## Start here

1. Read the [learning sequence](LEARNING_PATHS.md).
2. Inspect the [architecture and full directory tree](ARCHITECTURE.md) and [topic inventory](catalog/topic_inventory.md).
3. Follow the [dependency graph](DEPENDENCIES.md), which distinguishes learning order from physical flow.
4. Use the [roadmap](ROADMAP.md) for staged research, authoring and review.

```mermaid
flowchart TD
  earth[Quartz and carbon feedstocks] --> refine[Silicon refining]
  refine --> crystal[Single-crystal growth]
  crystal --> wafer[Wafer manufacture]
  physics[Semiconductor physics] --> devices[Transistor fundamentals]
  devices --> design[Design and tapeout]
  wafer --> logic[Logic wafer fabrication: FEOL and BEOL]
  design -. masks and design constraints .-> logic
  wafer --> dram[DRAM wafer fabrication]
  logic --> test[Wafer test and die preparation]
  dram --> memorytest[Memory test, TSV, thinning and stacking]
  memorytest --> hbm[HBM stack]
  test --> pkg[Advanced package assembly and test]
  hbm --> pkg
  substrate[Substrate and interposer manufacture] --> pkg
  pkg --> board[PCB and accelerator module]
  board --> server[Server]
  server --> rack[Rack-scale system]
  power[Power delivery] -. constrains .-> board
  cooling[Thermal management] -. constrains .-> rack
```

*Figure P0-01 — Learning overview with physical assembly branches. Original schematic, not to scale; arrows simplify process variations. Source: this project's scope specification; CC BY 4.0. Technical process details await research. See the separate physical-flow and prerequisite graphs for precise edge meanings.*

## Navigate the repository

- [All 43 module indexes](catalog/topic_inventory.md)
- [Research strategy](RESEARCH_STRATEGY.md), [source policy](SOURCE_POLICY.md), [confidence labels](CONFIDENCE_LEVELS.md)
- [Article and diagram taxonomy](TAXONOMY.md), [article template](ARTICLE_TEMPLATE.md), [contributing](CONTRIBUTING.md)
- [Equipment](33_equipment_ecosystem/README.md), [materials](34_materials_ecosystem/README.md), [supply chain](35_supply_chain/README.md)
- [Economics](36_economics/README.md), [investment research](37_investment_analysis/README.md)
- [Rubin case-study plan](38_case_studies/nvidia_rubin/README.md)
- [Glossary conventions](40_glossary/SCHEMA.md), [bibliography](42_references/bibliography.md), [claim register](42_references/claims.csv)

## Reproduce the architecture checks

Run `python3 scripts/validate.py` from the repository root. The same structural checks run on GitHub pushes and pull requests. Human source and technical review remains necessary.

GitHub home: [samuelianrich/semiconductor-manufacturing-kb](https://github.com/samuelianrich/semiconductor-manufacturing-kb) (private). The repository includes no scheduled external actions; use the [maintenance protocol](MAINTENANCE.md) as content is developed.
