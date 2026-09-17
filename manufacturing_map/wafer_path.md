# Raw materials to accepted wafer

[Map home](README.md) · [Schema](SCHEMA.md) · [Full entity register](process_nodes.md)

<!-- BEGIN GENERATED MAP -->
**Generated from the canonical CSV graph.** Planned scope is not technical evidence.

```mermaid
flowchart LR
  MAT_0001["Quartz-bearing feedstock"]
  MAT_0002["Qualified quartz and carbon charge"]
  MAT_0003["Metallurgical-grade silicon"]
  MAT_0004["Crude chlorosilane mixture"]
  MAT_0005["Purified chlorosilane feed"]
  MAT_0006["Electronic-grade polysilicon"]
  MAT_0007["Single-crystal silicon ingot"]
  MAT_0008["Sliced silicon wafer"]
  MAT_0009["Finished polished wafer"]
  MAT_0010["Accepted starting wafer"]
  MAT_0011["Carbon reductants"]
  PROC_0001["Mine, beneficiate and qualify feedstock"]
  PROC_0002["Carbothermic silicon smelting"]
  PROC_0003["Chlorosilane synthesis"]
  PROC_0004["Chemical purification by distillation"]
  PROC_0005["Polysilicon deposition"]
  PROC_0006["Czochralski single-crystal growth"]
  PROC_0007["Ingot shaping and wafer slicing"]
  PROC_0008["Wafer surface finishing"]
  PROC_0009["Wafer cleaning and acceptance inspection"]
  MAT_0001 -->|"consumes"| PROC_0001
  PROC_0001 -->|"produces"| MAT_0002
  MAT_0002 -->|"consumes"| PROC_0002
  PROC_0002 -->|"produces"| MAT_0003
  MAT_0003 -->|"consumes"| PROC_0003
  PROC_0003 -->|"produces"| MAT_0004
  MAT_0004 -->|"consumes"| PROC_0004
  PROC_0004 -->|"produces"| MAT_0005
  MAT_0005 -->|"consumes"| PROC_0005
  PROC_0005 -->|"produces"| MAT_0006
  MAT_0006 -->|"consumes"| PROC_0006
  PROC_0006 -->|"produces"| MAT_0007
  MAT_0007 -->|"consumes"| PROC_0007
  PROC_0007 -->|"produces"| MAT_0008
  MAT_0008 -->|"consumes"| PROC_0008
  PROC_0008 -->|"produces"| MAT_0009
  MAT_0009 -->|"consumes"| PROC_0009
  PROC_0009 -->|"produces"| MAT_0010
  MAT_0011 -->|"consumes"| PROC_0002
```

*MAP-WAFER-PATH — Representative chlorosilane/Siemens/CZ path at aggregate operation level; qualified output boundaries, not a complete recipe. FZ is documented separately in the crystal-growth chapter and entity register. Original schematic; CC BY 4.0. Source: graph records and their evidence links; no physical scale.*

| ID | Entity | Status | Canonical article |
|---|---|---|---|
| MAT-0001 | Quartz-bearing feedstock | reviewed | [Quartz-bearing feedstock](../01_raw_materials/quartz_and_feedstocks.md) |
| MAT-0002 | Qualified quartz and carbon charge | reviewed | [Qualified quartz and carbon charge](../01_raw_materials/quartz_and_feedstocks.md) |
| MAT-0003 | Metallurgical-grade silicon | reviewed | [Metallurgical-grade silicon](../02_silicon_refining/metallurgical_silicon.md) |
| MAT-0004 | Crude chlorosilane mixture | reviewed | [Crude chlorosilane mixture](../02_silicon_refining/electronic_grade_polysilicon.md) |
| MAT-0005 | Purified chlorosilane feed | reviewed | [Purified chlorosilane feed](../02_silicon_refining/electronic_grade_polysilicon.md) |
| MAT-0006 | Electronic-grade polysilicon | reviewed | [Electronic-grade polysilicon](../02_silicon_refining/electronic_grade_polysilicon.md) |
| MAT-0007 | Single-crystal silicon ingot | reviewed | [Single-crystal silicon ingot](../03_crystal_growth/crystal_growth.md) |
| MAT-0008 | Sliced silicon wafer | reviewed | [Sliced silicon wafer](../04_wafer_manufacturing/wafer_finishing_and_acceptance.md) |
| MAT-0009 | Finished polished wafer | reviewed | [Finished polished wafer](../04_wafer_manufacturing/wafer_finishing_and_acceptance.md) |
| MAT-0010 | Accepted starting wafer | reviewed | [Accepted starting wafer](../04_wafer_manufacturing/wafer_finishing_and_acceptance.md) |
| MAT-0011 | Carbon reductants | reviewed | [Carbon reductants](../02_silicon_refining/metallurgical_silicon.md) |
| PROC-0001 | Mine, beneficiate and qualify feedstock | reviewed | [Mine, beneficiate and qualify feedstock](../01_raw_materials/quartz_and_feedstocks.md) |
| PROC-0002 | Carbothermic silicon smelting | reviewed | [Carbothermic silicon smelting](../02_silicon_refining/metallurgical_silicon.md) |
| PROC-0003 | Chlorosilane synthesis | reviewed | [Chlorosilane synthesis](../02_silicon_refining/electronic_grade_polysilicon.md) |
| PROC-0004 | Chemical purification by distillation | reviewed | [Chemical purification by distillation](../02_silicon_refining/electronic_grade_polysilicon.md) |
| PROC-0005 | Polysilicon deposition | reviewed | [Polysilicon deposition](../02_silicon_refining/electronic_grade_polysilicon.md) |
| PROC-0006 | Czochralski single-crystal growth | reviewed | [Czochralski single-crystal growth](../03_crystal_growth/crystal_growth.md) |
| PROC-0007 | Ingot shaping and wafer slicing | reviewed | [Ingot shaping and wafer slicing](../04_wafer_manufacturing/wafer_finishing_and_acceptance.md) |
| PROC-0008 | Wafer surface finishing | reviewed | [Wafer surface finishing](../04_wafer_manufacturing/wafer_finishing_and_acceptance.md) |
| PROC-0009 | Wafer cleaning and acceptance inspection | reviewed | [Wafer cleaning and acceptance inspection](../04_wafer_manufacturing/wafer_finishing_and_acceptance.md) |

| Edge | Relationship | Conditions | Evidence |
|---|---|---|---|
| EDGE-0001 | PROC-0001 → CONSUMES → MAT-0001 | Representative chlorosilane/Siemens/CZ route; aggregate operation boundaries and qualified output only. | [ELKEM-QUARTZ-001](../42_references/bibliography.md#elkem-quartz-001) (Tana extraction description; general feedstock input) · CLM-000001 |
| EDGE-0002 | PROC-0001 → PRODUCES → MAT-0002 | Representative chlorosilane/Siemens/CZ route; aggregate operation boundaries and qualified output only. | [NTNU-SMELTING-001](../42_references/bibliography.md#ntnu-smelting-001) (Quartz and carbon inputs to silicon furnace; aggregate preparation boundary) |
| EDGE-0003 | PROC-0002 → CONSUMES → MAT-0002 | Representative chlorosilane/Siemens/CZ route; aggregate operation boundaries and qualified output only. | [NTNU-SMELTING-001](../42_references/bibliography.md#ntnu-smelting-001) (SiC role and furnace observations) |
| EDGE-0004 | PROC-0002 → PRODUCES → MAT-0003 | Representative chlorosilane/Siemens/CZ route; aggregate operation boundaries and qualified output only. | [NTNU-SMELTING-001](../42_references/bibliography.md#ntnu-smelting-001) (SiC role and furnace observations) |
| EDGE-0006 | PROC-0003 → CONSUMES → MAT-0003 | Representative chlorosilane/Siemens/CZ route; aggregate operation boundaries and qualified output only. | [WACKER-POLY-001](../42_references/bibliography.md#wacker-poly-001) (Chlorosilane synthesis description) |
| EDGE-0007 | PROC-0003 → PRODUCES → MAT-0004 | Representative chlorosilane/Siemens/CZ route; aggregate operation boundaries and qualified output only. | [WACKER-POLY-001](../42_references/bibliography.md#wacker-poly-001) (Chlorosilane synthesis description) |
| EDGE-0009 | PROC-0004 → CONSUMES → MAT-0004 | Representative chlorosilane/Siemens/CZ route; aggregate operation boundaries and qualified output only. | [WACKER-POLY-001](../42_references/bibliography.md#wacker-poly-001) (Distillation section) |
| EDGE-0010 | PROC-0004 → PRODUCES → MAT-0005 | Representative chlorosilane/Siemens/CZ route; aggregate operation boundaries and qualified output only. | [WACKER-POLY-001](../42_references/bibliography.md#wacker-poly-001) (Distillation section) |
| EDGE-0012 | PROC-0005 → CONSUMES → MAT-0005 | Representative chlorosilane/Siemens/CZ route; aggregate operation boundaries and qualified output only. | [HSC-POLY-001](../42_references/bibliography.md#hsc-poly-001) (TCS CVD and product finishing) |
| EDGE-0013 | PROC-0005 → PRODUCES → MAT-0006 | Representative chlorosilane/Siemens/CZ route; aggregate operation boundaries and qualified output only. | [HSC-POLY-001](../42_references/bibliography.md#hsc-poly-001) (TCS CVD and product finishing) |
| EDGE-0015 | PROC-0006 → CONSUMES → MAT-0006 | Representative chlorosilane/Siemens/CZ route; aggregate operation boundaries and qualified output only. | [PVA-CZ-001](../42_references/bibliography.md#pva-cz-001) (The Process) |
| EDGE-0016 | PROC-0006 → PRODUCES → MAT-0007 | Representative chlorosilane/Siemens/CZ route; aggregate operation boundaries and qualified output only. | [PVA-CZ-001](../42_references/bibliography.md#pva-cz-001) (The Process) |
| EDGE-0018 | PROC-0007 → CONSUMES → MAT-0007 | Representative chlorosilane/Siemens/CZ route; aggregate operation boundaries and qualified output only. | [SUMCO-WAFER-001](../42_references/bibliography.md#sumco-wafer-001) (Wafer forming) |
| EDGE-0019 | PROC-0007 → PRODUCES → MAT-0008 | Representative chlorosilane/Siemens/CZ route; aggregate operation boundaries and qualified output only. | [SUMCO-WAFER-001](../42_references/bibliography.md#sumco-wafer-001) (Wafer forming) |
| EDGE-0021 | PROC-0008 → CONSUMES → MAT-0008 | Representative chlorosilane/Siemens/CZ route; aggregate operation boundaries and qualified output only. | [SUMCO-WAFER-001](../42_references/bibliography.md#sumco-wafer-001) (Lapping; etching; polishing) |
| EDGE-0022 | PROC-0008 → PRODUCES → MAT-0009 | Representative chlorosilane/Siemens/CZ route; aggregate operation boundaries and qualified output only. | [SUMCO-WAFER-001](../42_references/bibliography.md#sumco-wafer-001) (Lapping; etching; polishing) |
| EDGE-0024 | PROC-0009 → CONSUMES → MAT-0009 | Representative chlorosilane/Siemens/CZ route; aggregate operation boundaries and qualified output only. | [SUMCO-WAFER-001](../42_references/bibliography.md#sumco-wafer-001) (Cleaning and inspection) |
| EDGE-0025 | PROC-0009 → PRODUCES → MAT-0010 | Representative chlorosilane/Siemens/CZ route; aggregate operation boundaries and qualified output only. | [SUMCO-WAFER-001](../42_references/bibliography.md#sumco-wafer-001) (Cleaning and inspection) |
| EDGE-0061 | PROC-0002 → CONSUMES → MAT-0011 |  | [NTNU-SMELTING-001](../42_references/bibliography.md#ntnu-smelting-001) (Carbon sources) |
<!-- END GENERATED MAP -->
