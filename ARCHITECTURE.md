# Repository architecture

## Design decisions

Preserve the requested 00–42 topic numbering as stable addresses. Build order is intentionally different from directory order: physics can be learned alongside raw materials, detailed tapeout follows fab fundamentals, and economics waits until engineering exists. A module index is an explicit scope placeholder; a reviewed article is a different artifact.

Use **42_references** as the only canonical reference root, replacing the earlier illustrative `/references` location. Never duplicate bibliography entries in both. Canonical ownership prevents the interconnect/BEOL and deposition/oxidation branches from repeating each other.

The repository contains three connected but distinct graphs: prerequisite knowledge (acyclic), physical material/assembly flow (branching and sometimes repetitive), and related-concept links (may have cycles). Equipment and EDA are enabling inputs, not material stages inserted between wafers and foundries.

## Canonical ownership and boundary rules

| Potential overlap | Canonical owner | Other pages do |
|---|---|---|
| Transistor operation versus manufacture | 06 owns operation; 17 owns fabrication | Link physical mechanism to process implementation |
| Oxidation versus deposition | 13 owns oxide growth; 10 owns deposition methods | Compare growth and deposition, link instead of duplicate |
| Interconnect versus BEOL | 18 owns structures/materials/RC; 19 owns integration sequence | 17 introduces contact/MOL handoff; 18 explains contact physics |
| DRAM versus HBM | 23 owns memory cells and DRAM fabrication; 24 owns memory stacks | 25 integrates stacks with logic |
| TSV and bonding | 25 owns general integration primitives | 24 owns DRAM/HBM-specific application and sequencing |
| Substrate versus PCB | 26 owns package substrate; 30 owns board laminate and assembly | Explicitly identify which routing level is discussed |
| Wafer polishing versus fab CMP | 04 owns starting-wafer finishing; 15 owns device-layer CMP | Link common removal principles |
| Known-good-die versus compound yield | 20 owns test evidence; 21 owns yield definitions; 25 owns assembly flow | 36 owns cost calculations |
| Power and heat | 28 and 27 own cross-scale principles | 29–32 apply them at package, board, server and rack |
| Suppliers versus industrial economics | 33–35 own source-labeled factual mappings | 37 interprets economic implications |
| Rubin evidence | 38 case study and central claim register | General chapters link claim IDs rather than copy specifications |
| Historical context | 39 owns transition narratives | Brief context elsewhere links back; no speculative roadmap |

## Full directory tree

The module contents are planned in the [topic inventory](catalog/topic_inventory.md); only indexes are created at Phase 0.

```text
semiconductor-manufacturing-kb/
  README.md
  ARCHITECTURE.md
  DEPENDENCIES.md
  LEARNING_PATHS.md
  ROADMAP.md
  RESEARCH_STRATEGY.md
  SOURCE_POLICY.md
  CONFIDENCE_LEVELS.md
  CONTRIBUTING.md
  ARTICLE_TEMPLATE.md
  TAXONOMY.md
  MAINTENANCE.md
  AUDIT_PHASE0.md
  LICENSE.md
  .gitignore
  .github/workflows/validate.yml
  catalog/{modules.json,topic_inventory.md}
  scripts/validate.py
  templates/{economics.md,investment.md,company.md,source_record.md,diagram_record.md}
  00_overview/README.md
  01_raw_materials/README.md
  02_silicon_refining/README.md
  03_crystal_growth/README.md
  04_wafer_manufacturing/README.md
  05_semiconductor_physics/README.md
  06_transistor_fundamentals/README.md
  07_ic_design_and_tapeout/README.md
  08_fab_overview/README.md
  09_photolithography/README.md
  10_deposition/README.md
  11_etching/README.md
  12_doping/README.md
  13_oxidation/README.md
  14_cleaning/README.md
  15_cmp/README.md
  16_metrology_and_inspection/README.md
  17_transistor_fabrication/README.md
  18_interconnects/README.md
  19_back_end_of_line/README.md
  20_wafer_test/README.md
  21_yield_engineering/README.md
  22_dicing_and_die_prep/README.md
  23_dram_fundamentals/README.md
  24_hbm_manufacturing/README.md
  25_advanced_packaging/README.md
  26_substrates/README.md
  27_thermal_management/README.md
  28_power_delivery/README.md
  29_gpu_package/README.md
  30_pcb_and_module/README.md
  31_system_integration/README.md
  32_rack_scale_system/README.md
  33_equipment_ecosystem/README.md
  34_materials_ecosystem/README.md
  35_supply_chain/README.md
  36_economics/README.md
  37_investment_analysis/README.md
  38_case_studies/README.md
  39_history/README.md
  40_glossary/README.md
  41_reference_tables/README.md
  42_references/README.md
  38_case_studies/nvidia_rubin/{README.md,coverage_matrix.md}
  40_glossary/SCHEMA.md
  42_references/{bibliography.md,claims.csv,research_queue.md}
  42_references/{papers,patents,standards,company_sources}/README.md
  assets/{diagrams,process_flows,cross_sections,supply_chain_maps,equipment,tables}/README.md
  assets/manifest.csv
  assets/process_flows/physical_chain.mmd
  assets/diagrams/prerequisites.mmd
  assets/supply_chain_maps/enabling_inputs.mmd
  project/USER_SPECIFICATION.md
```

## Article lifecycle

`planned → scoped → researched → outlined → drafted → reviewed → maintained`

A document carries status, scope, owner (unassigned until assigned), last review date and prerequisite links. Only reviewed content may be counted as complete. A stale claim remains visible with a warning and review task; never silently refresh its access date.

## Explicit boundary bridges

The scope includes CMOS logic as the transistor-to-circuit bridge, passivation and terminal metallization as the wafer-to-package interface, temporary bonding/debonding for thin-die handling, package reliability qualification beyond functional test, and PCB fabrication and assembly beyond merely naming the board. At system level it includes networking and facility power/cooling interfaces, without expanding into a datacenter operations textbook.

Device makers use different process sequences. General diagrams must show conditional paths where TSV formation, thinning or bonding order differs. A logical prerequisite never asserts a proprietary production sequence.

## Persistent manufacturing map

The accepted [Phase 0A extension](project/PHASE_0A_REVISED_PROPOSAL.md) is implemented under [manufacturing_map](manufacturing_map/README.md). Its typed CSV registry owns manufacturing entities and edges; the module catalog continues to own learning prerequisites. Repeated physical and enabling-input diagrams are generated by `scripts/manufacturing_map.py`, including the compatibility asset paths already used by this repository.

Additional files: `manufacturing_map/data/{entities,process_nodes,process_edges,materials,equipment,suppliers,evidence_links,routes}.csv`, `schema.json`, `views.json`, human-readable map views and `tests/test_manufacturing_map.py`.
