# Raw materials to accepted wafer

[Map home](README.md) · [Schema](SCHEMA.md) · [Full entity register](process_nodes.md)

<!-- BEGIN GENERATED MAP -->
**Generated from the canonical CSV graph.** Planned scope is not technical evidence.

```mermaid
flowchart LR
  MAT_0001["Quartz-bearing feedstock [planned]"]
  MAT_0002["Qualified quartz and carbon charge [planned]"]
  MAT_0003["Metallurgical-grade silicon [planned]"]
  MAT_0004["Crude chlorosilane mixture [planned]"]
  MAT_0005["Purified chlorosilane feed [planned]"]
  MAT_0006["Electronic-grade polysilicon [planned]"]
  MAT_0007["Single-crystal silicon ingot [planned]"]
  MAT_0008["Sliced silicon wafer [planned]"]
  MAT_0009["Finished polished wafer [planned]"]
  MAT_0010["Accepted starting wafer [planned]"]
  PROC_0001["Mine, beneficiate and qualify feedstock [planned]"]
  PROC_0002["Carbothermic silicon smelting [planned]"]
  PROC_0003["Chlorosilane synthesis [planned]"]
  PROC_0004["Chemical purification by distillation [planned]"]
  PROC_0005["Polysilicon deposition [planned]"]
  PROC_0006["Single-crystal growth [planned]"]
  PROC_0007["Ingot shaping and wafer slicing [planned]"]
  PROC_0008["Wafer surface finishing [planned]"]
  PROC_0009["Wafer cleaning and acceptance inspection [planned]"]
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
```

*MAP-WAFER-PATH — Representative learning route; arrow labels distinguish operation inputs and outputs from operation ordering. Detailed route variants are introduced with research. Original schematic; CC BY 4.0. Source: graph records and their evidence links; no physical scale.*

| ID | Entity | Status | Canonical article |
|---|---|---|---|
| MAT-0001 | Quartz-bearing feedstock | planned | [Quartz-bearing feedstock](../01_raw_materials/README.md) |
| MAT-0002 | Qualified quartz and carbon charge | planned | [Qualified quartz and carbon charge](../01_raw_materials/README.md) |
| MAT-0003 | Metallurgical-grade silicon | planned | [Metallurgical-grade silicon](../02_silicon_refining/README.md) |
| MAT-0004 | Crude chlorosilane mixture | planned | [Crude chlorosilane mixture](../02_silicon_refining/README.md) |
| MAT-0005 | Purified chlorosilane feed | planned | [Purified chlorosilane feed](../02_silicon_refining/README.md) |
| MAT-0006 | Electronic-grade polysilicon | planned | [Electronic-grade polysilicon](../02_silicon_refining/README.md) |
| MAT-0007 | Single-crystal silicon ingot | planned | [Single-crystal silicon ingot](../03_crystal_growth/README.md) |
| MAT-0008 | Sliced silicon wafer | planned | [Sliced silicon wafer](../04_wafer_manufacturing/README.md) |
| MAT-0009 | Finished polished wafer | planned | [Finished polished wafer](../04_wafer_manufacturing/README.md) |
| MAT-0010 | Accepted starting wafer | planned | [Accepted starting wafer](../04_wafer_manufacturing/README.md) |
| PROC-0001 | Mine, beneficiate and qualify feedstock | planned | [Mine, beneficiate and qualify feedstock](../01_raw_materials/README.md) |
| PROC-0002 | Carbothermic silicon smelting | planned | [Carbothermic silicon smelting](../02_silicon_refining/README.md) |
| PROC-0003 | Chlorosilane synthesis | planned | [Chlorosilane synthesis](../02_silicon_refining/README.md) |
| PROC-0004 | Chemical purification by distillation | planned | [Chemical purification by distillation](../02_silicon_refining/README.md) |
| PROC-0005 | Polysilicon deposition | planned | [Polysilicon deposition](../02_silicon_refining/README.md) |
| PROC-0006 | Single-crystal growth | planned | [Single-crystal growth](../03_crystal_growth/README.md) |
| PROC-0007 | Ingot shaping and wafer slicing | planned | [Ingot shaping and wafer slicing](../04_wafer_manufacturing/README.md) |
| PROC-0008 | Wafer surface finishing | planned | [Wafer surface finishing](../04_wafer_manufacturing/README.md) |
| PROC-0009 | Wafer cleaning and acceptance inspection | planned | [Wafer cleaning and acceptance inspection](../04_wafer_manufacturing/README.md) |

| Edge | Relationship | Conditions | Evidence |
|---|---|---|---|
| EDGE-0001 | PROC-0001 → CONSUMES → MAT-0001 |  | Planned; not evidence-backed |
| EDGE-0002 | PROC-0001 → PRODUCES → MAT-0002 |  | Planned; not evidence-backed |
| EDGE-0003 | PROC-0002 → CONSUMES → MAT-0002 |  | Planned; not evidence-backed |
| EDGE-0004 | PROC-0002 → PRODUCES → MAT-0003 |  | Planned; not evidence-backed |
| EDGE-0006 | PROC-0003 → CONSUMES → MAT-0003 |  | Planned; not evidence-backed |
| EDGE-0007 | PROC-0003 → PRODUCES → MAT-0004 |  | Planned; not evidence-backed |
| EDGE-0009 | PROC-0004 → CONSUMES → MAT-0004 |  | Planned; not evidence-backed |
| EDGE-0010 | PROC-0004 → PRODUCES → MAT-0005 |  | Planned; not evidence-backed |
| EDGE-0012 | PROC-0005 → CONSUMES → MAT-0005 |  | Planned; not evidence-backed |
| EDGE-0013 | PROC-0005 → PRODUCES → MAT-0006 |  | Planned; not evidence-backed |
| EDGE-0015 | PROC-0006 → CONSUMES → MAT-0006 |  | Planned; not evidence-backed |
| EDGE-0016 | PROC-0006 → PRODUCES → MAT-0007 |  | Planned; not evidence-backed |
| EDGE-0018 | PROC-0007 → CONSUMES → MAT-0007 |  | Planned; not evidence-backed |
| EDGE-0019 | PROC-0007 → PRODUCES → MAT-0008 |  | Planned; not evidence-backed |
| EDGE-0021 | PROC-0008 → CONSUMES → MAT-0008 |  | Planned; not evidence-backed |
| EDGE-0022 | PROC-0008 → PRODUCES → MAT-0009 |  | Planned; not evidence-backed |
| EDGE-0024 | PROC-0009 → CONSUMES → MAT-0009 |  | Planned; not evidence-backed |
| EDGE-0025 | PROC-0009 → PRODUCES → MAT-0010 |  | Planned; not evidence-backed |
<!-- END GENERATED MAP -->
