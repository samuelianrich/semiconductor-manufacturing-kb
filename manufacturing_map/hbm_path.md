# HBM manufacturing path

[Map home](README.md) · [Schema](SCHEMA.md) · [Full entity register](process_nodes.md)

<!-- BEGIN GENERATED MAP -->
**Generated from the canonical CSV graph.** Planned scope is not technical evidence.

```mermaid
flowchart LR
  ART_0031["DRAM wafer [planned]"]
  ART_0032["Prepared DRAM dies [planned]"]
  ART_0033["Tested HBM stack [planned]"]
  MAT_0010["Accepted starting wafer [planned]"]
  PROC_0031["DRAM wafer fabrication [planned]"]
  PROC_0032["DRAM test, TSV and die preparation [planned]"]
  PROC_0033["HBM stack assembly and test [planned]"]
  MAT_0010 -->|"consumes"| PROC_0031
  PROC_0031 -->|"produces"| ART_0031
  ART_0031 -->|"consumes"| PROC_0032
  PROC_0032 -->|"produces"| ART_0032
  ART_0032 -->|"consumes"| PROC_0033
  PROC_0033 -->|"produces"| ART_0033
```

*MAP-HBM-PATH — Later-phase scope only. Test/TSV/thinning are aggregated here; no universal sequence or proprietary recipe is asserted. Original schematic; CC BY 4.0. Source: graph records and their evidence links; no physical scale.*

| ID | Entity | Status | Canonical article |
|---|---|---|---|
| ART-0031 | DRAM wafer | planned | [DRAM wafer](../23_dram_fundamentals/README.md) |
| ART-0032 | Prepared DRAM dies | planned | [Prepared DRAM dies](../24_hbm_manufacturing/README.md) |
| ART-0033 | Tested HBM stack | planned | [Tested HBM stack](../24_hbm_manufacturing/README.md) |
| MAT-0010 | Accepted starting wafer | planned | [Accepted starting wafer](../04_wafer_manufacturing/README.md) |
| PROC-0031 | DRAM wafer fabrication | planned | [DRAM wafer fabrication](../23_dram_fundamentals/README.md) |
| PROC-0032 | DRAM test, TSV and die preparation | planned | [DRAM test, TSV and die preparation](../24_hbm_manufacturing/README.md) |
| PROC-0033 | HBM stack assembly and test | planned | [HBM stack assembly and test](../24_hbm_manufacturing/README.md) |

| Edge | Relationship | Conditions | Evidence |
|---|---|---|---|
| EDGE-0030 | PROC-0031 → CONSUMES → MAT-0010 |  | Planned; not evidence-backed |
| EDGE-0031 | PROC-0031 → PRODUCES → ART-0031 |  | Planned; not evidence-backed |
| EDGE-0032 | PROC-0032 → CONSUMES → ART-0031 |  | Planned; not evidence-backed |
| EDGE-0033 | PROC-0032 → PRODUCES → ART-0032 |  | Planned; not evidence-backed |
| EDGE-0034 | PROC-0033 → CONSUMES → ART-0032 |  | Planned; not evidence-backed |
| EDGE-0035 | PROC-0033 → PRODUCES → ART-0033 |  | Planned; not evidence-backed |
<!-- END GENERATED MAP -->
