# Failure, detection and yield relationships

[Map home](README.md) · [Schema](SCHEMA.md) · [Full entity register](process_nodes.md)

<!-- BEGIN GENERATED MAP -->
**Generated from the canonical CSV graph.** Planned scope is not technical evidence.

```mermaid
flowchart LR
  CHAR_0001["Carrier concentration"]
  CHAR_0002["Electrical resistivity"]
  CHAR_0003["Wafer geometry"]
  FAIL_0001["Surface contamination outside specification"]
  FAIL_0002["Geometry outside specification"]
  FAIL_0003["Electrical resistivity outside specification"]
  METRIC_0001["Accepted wafer fraction"]
  PROC_0009["Wafer cleaning and acceptance inspection"]
  CHAR_0001 -->|"affects"| CHAR_0002
  PROC_0009 -->|"measures"| CHAR_0003
  FAIL_0001 -->|"detected by"| PROC_0009
  FAIL_0002 -->|"detected by"| PROC_0009
  FAIL_0001 -->|"affects"| METRIC_0001
  FAIL_0002 -->|"affects"| METRIC_0001
  CHAR_0001 -->|"can cause"| FAIL_0003
  FAIL_0003 -->|"detected by"| PROC_0009
  FAIL_0003 -->|"affects"| METRIC_0001
```

*MAP-YIELD-MAP — Failure modes, detection operations and measured characteristics; arrows do not represent an inevitable cascade. Original schematic; CC BY 4.0. Source: graph records and their evidence links; no physical scale.*

| ID | Entity | Status | Canonical article |
|---|---|---|---|
| CHAR-0001 | Carrier concentration | reviewed | [Carrier concentration](../05_semiconductor_physics/doping_and_transport.md) |
| CHAR-0002 | Electrical resistivity | reviewed | [Electrical resistivity](../05_semiconductor_physics/doping_and_transport.md) |
| CHAR-0003 | Wafer geometry | reviewed | [Wafer geometry](../04_wafer_manufacturing/wafer_finishing_and_acceptance.md) |
| FAIL-0001 | Surface contamination outside specification | reviewed | [Surface contamination outside specification](../04_wafer_manufacturing/wafer_finishing_and_acceptance.md) |
| FAIL-0002 | Geometry outside specification | reviewed | [Geometry outside specification](../04_wafer_manufacturing/wafer_finishing_and_acceptance.md) |
| FAIL-0003 | Electrical resistivity outside specification | reviewed | [Electrical resistivity outside specification](../05_semiconductor_physics/doping_and_transport.md) |
| METRIC-0001 | Accepted wafer fraction | reviewed | [Accepted wafer fraction](../04_wafer_manufacturing/wafer_finishing_and_acceptance.md) |
| PROC-0009 | Wafer cleaning and acceptance inspection | reviewed | [Wafer cleaning and acceptance inspection](../04_wafer_manufacturing/wafer_finishing_and_acceptance.md) |

| Edge | Relationship | Conditions | Evidence |
|---|---|---|---|
| EDGE-0076 | CHAR-0001 → AFFECTS → CHAR-0002 | At stated mobility and low-field conditions; changing impurity scattering can also change mobility. | [HU-TRANSPORT-001](../42_references/bibliography.md#hu-transport-001) (Conductivity relation) |
| EDGE-0077 | PROC-0009 → MEASURES → CHAR-0003 | Acceptance operation aggregates multiple metrology methods; laser scattering alone does not measure all geometry. | [SEMI-WAFER-001](../42_references/bibliography.md#semi-wafer-001) (Public scope of wafer measurements) |
| EDGE-0078 | FAIL-0001 → DETECTED_BY → PROC-0009 | Only detectable events within method sensitivity and inspection coverage. | [UCSB-INSPECT-001](../42_references/bibliography.md#ucsb-inspect-001) (Surface scattering detection) |
| EDGE-0079 | FAIL-0002 → DETECTED_BY → PROC-0009 | Appropriate geometry metrology and agreed specification required. | [SEMI-WAFER-001](../42_references/bibliography.md#semi-wafer-001) (Geometry measurement categories) |
| EDGE-0080 | FAIL-0001 → AFFECTS → METRIC-0001 | A detected out-of-spec event excludes a wafer from accepted count under the chosen disposition policy. | [SUMCO-WAFER-001](../42_references/bibliography.md#sumco-wafer-001) (Cleaning and inspection; acceptance boundary) |
| EDGE-0081 | FAIL-0002 → AFFECTS → METRIC-0001 | Only failures of the applicable specification reduce this boundary-specific accepted count. | [SEMI-WAFER-001](../42_references/bibliography.md#semi-wafer-001) (Specification scope; accounting implication) |
| EDGE-0084 | CHAR-0001 → CAN_CAUSE → FAIL-0003 | Only if the resulting resistivity crosses the specified bound; mobility and temperature must be accounted for. | [HU-TRANSPORT-001](../42_references/bibliography.md#hu-transport-001) (Conductivity dependence on carriers) |
| EDGE-0085 | FAIL-0003 → DETECTED_BY → PROC-0009 | Appropriate electrical metrology under specified conditions; not detection by surface laser scattering. | [SEMI-WAFER-001](../42_references/bibliography.md#semi-wafer-001) (Public scope; resistivity measurement categories) |
| EDGE-0086 | FAIL-0003 → AFFECTS → METRIC-0001 | A detected failure of the applicable electrical specification changes accepted-wafer count under the chosen policy. | [SEMI-WAFER-001](../42_references/bibliography.md#semi-wafer-001) (Specified wafer characteristics; author accounting implication) |
<!-- END GENERATED MAP -->
