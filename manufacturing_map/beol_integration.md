# Representative Cu wiring integration

[Map home](README.md) · [Schema](SCHEMA.md) · [Full entity register](process_nodes.md)

<!-- BEGIN GENERATED MAP -->
**Generated from the canonical CSV graph.** Planned scope is not technical evidence.

```mermaid
flowchart LR
  ART_0201["Device wafer with MOL contacts"]
  ART_0210["Trench/via cavity wafer"]
  ART_0211["Prepared cavity wafer"]
  ART_0212["Filled wafer with overburden"]
  ART_0213["One added wiring level"]
  ART_0214["Fabricated wired wafer - test pending"]
  PROC_0210["Wiring-level dielectric and cavity"]
  PROC_0211["Barrier liner and seed"]
  PROC_0212["Copper cavity fill"]
  PROC_0213["Wiring-level CMP and clean"]
  PROC_0214["Additional levels and terminal finish"]
  ART_0201 -->|"consumes"| PROC_0210
  PROC_0210 -->|"produces"| ART_0210
  ART_0210 -->|"consumes"| PROC_0211
  PROC_0211 -->|"produces"| ART_0211
  ART_0211 -->|"consumes"| PROC_0212
  PROC_0212 -->|"produces"| ART_0212
  ART_0212 -->|"consumes"| PROC_0213
  PROC_0213 -->|"produces"| ART_0213
  ART_0213 -->|"consumes"| PROC_0214
  PROC_0214 -->|"produces"| ART_0214
```

*MAP-BEOL-INTEGRATION — Illustrative Cu dual-damascene module; via/trench mask order aggregated. Additional levels are explicitly aggregated in the finishing node. Not a qualified full logic flow. Original schematic; CC BY 4.0. Source: graph records and their evidence links; no physical scale.*

| ID | Entity | Status | Canonical article |
|---|---|---|---|
| ART-0201 | Device wafer with MOL contacts | reviewed | [Device wafer with MOL contacts](../17_transistor_fabrication/contacts_and_mol.md) |
| ART-0210 | Trench/via cavity wafer | reviewed | [Trench/via cavity wafer](../19_back_end_of_line/beol_integration.md) |
| ART-0211 | Prepared cavity wafer | reviewed | [Prepared cavity wafer](../19_back_end_of_line/beol_integration.md) |
| ART-0212 | Filled wafer with overburden | reviewed | [Filled wafer with overburden](../19_back_end_of_line/beol_integration.md) |
| ART-0213 | One added wiring level | reviewed | [One added wiring level](../19_back_end_of_line/beol_integration.md) |
| ART-0214 | Fabricated wired wafer - test pending | reviewed | [Fabricated wired wafer - test pending](../19_back_end_of_line/beol_integration.md) |
| PROC-0210 | Wiring-level dielectric and cavity | reviewed | [Wiring-level dielectric and cavity](../19_back_end_of_line/beol_integration.md) |
| PROC-0211 | Barrier liner and seed | reviewed | [Barrier liner and seed](../19_back_end_of_line/beol_integration.md) |
| PROC-0212 | Copper cavity fill | reviewed | [Copper cavity fill](../19_back_end_of_line/beol_integration.md) |
| PROC-0213 | Wiring-level CMP and clean | reviewed | [Wiring-level CMP and clean](../19_back_end_of_line/beol_integration.md) |
| PROC-0214 | Additional levels and terminal finish | reviewed | [Additional levels and terminal finish](../19_back_end_of_line/beol_integration.md) |

| Edge | Relationship | Conditions | Evidence |
|---|---|---|---|
| EDGE-0147 | PROC-0210 → CONSUMES → ART-0201 | Illustrative Cu dual-damascene module; via/trench mask order aggregated. Additional levels are explicitly aggregated in the finishing node. Not a qualified full logic flow. | [IBM-BEOL-001](../42_references/bibliography.md#ibm-beol-001) (Opening damascene discussion and barrier/liner tradeoffs) |
| EDGE-0148 | PROC-0210 → PRODUCES → ART-0210 | Illustrative Cu dual-damascene module; via/trench mask order aggregated. Additional levels are explicitly aggregated in the finishing node. Not a qualified full logic flow. | [IBM-BEOL-001](../42_references/bibliography.md#ibm-beol-001) (Opening damascene discussion and barrier/liner tradeoffs) |
| EDGE-0149 | PROC-0211 → CONSUMES → ART-0210 | Illustrative Cu dual-damascene module; via/trench mask order aggregated. Additional levels are explicitly aggregated in the finishing node. Not a qualified full logic flow. | [IBM-LINER-001](../42_references/bibliography.md#ibm-liner-001) (Abstract only: TaN/Ta, Cu seed and plated fill) |
| EDGE-0150 | PROC-0211 → PRODUCES → ART-0211 | Illustrative Cu dual-damascene module; via/trench mask order aggregated. Additional levels are explicitly aggregated in the finishing node. Not a qualified full logic flow. | [IBM-LINER-001](../42_references/bibliography.md#ibm-liner-001) (Abstract only: TaN/Ta, Cu seed and plated fill) |
| EDGE-0151 | PROC-0212 → CONSUMES → ART-0211 | Illustrative Cu dual-damascene module; via/trench mask order aggregated. Additional levels are explicitly aggregated in the finishing node. Not a qualified full logic flow. | [IBM-FILL-001](../42_references/bibliography.md#ibm-fill-001) (Abstract only: voids, seams and superconformal fill) |
| EDGE-0152 | PROC-0212 → PRODUCES → ART-0212 | Illustrative Cu dual-damascene module; via/trench mask order aggregated. Additional levels are explicitly aggregated in the finishing node. Not a qualified full logic flow. | [IBM-FILL-001](../42_references/bibliography.md#ibm-fill-001) (Abstract only: voids, seams and superconformal fill) |
| EDGE-0153 | PROC-0213 → CONSUMES → ART-0212 | Illustrative Cu dual-damascene module; via/trench mask order aggregated. Additional levels are explicitly aggregated in the finishing node. Not a qualified full logic flow. | [MACK-CMP-001](../42_references/bibliography.md#mack-cmp-001) (CMP roles and overpolishing defects) |
| EDGE-0154 | PROC-0213 → PRODUCES → ART-0213 | Illustrative Cu dual-damascene module; via/trench mask order aggregated. Additional levels are explicitly aggregated in the finishing node. Not a qualified full logic flow. | [MACK-CMP-001](../42_references/bibliography.md#mack-cmp-001) (CMP roles and overpolishing defects) |
| EDGE-0155 | PROC-0214 → CONSUMES → ART-0213 | Illustrative Cu dual-damascene module; via/trench mask order aggregated. Additional levels are explicitly aggregated in the finishing node. Not a qualified full logic flow. | [HU-FAB-001](../42_references/bibliography.md#hu-fab-001) (Chapter 3 §3.8: multilevel interconnect and terminal boundaries) |
| EDGE-0156 | PROC-0214 → PRODUCES → ART-0214 | Illustrative Cu dual-damascene module; via/trench mask order aggregated. Additional levels are explicitly aggregated in the finishing node. Not a qualified full logic flow. | [HU-FAB-001](../42_references/bibliography.md#hu-fab-001) (Chapter 3 §3.8: multilevel interconnect and terminal boundaries) |
<!-- END GENERATED MAP -->
