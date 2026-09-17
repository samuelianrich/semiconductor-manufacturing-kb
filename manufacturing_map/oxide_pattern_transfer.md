# Teaching oxide pattern transfer

[Map home](README.md) · [Schema](SCHEMA.md) · [Full entity register](process_nodes.md)

<!-- BEGIN GENERATED MAP -->
**Generated from the canonical CSV graph.** Planned scope is not technical evidence.

```mermaid
flowchart LR
  MAT_0010["Accepted starting wafer"]
  MAT_0101["Thermal oxide on silicon"]
  MAT_0102["Resist-patterned oxide wafer"]
  MAT_0103["Etched oxide with remaining resist"]
  MAT_0104["Patterned oxide after strip"]
  PROC_0101["Resist patterning"]
  PROC_0103["Pattern transfer etch"]
  PROC_0105["Thermal oxidation"]
  PROC_0106["Resist strip and surface clean"]
  MAT_0010 -->|"consumes"| PROC_0105
  PROC_0105 -->|"produces"| MAT_0101
  MAT_0101 -->|"consumes"| PROC_0101
  PROC_0101 -->|"produces"| MAT_0102
  MAT_0102 -->|"consumes"| PROC_0103
  PROC_0103 -->|"produces"| MAT_0103
  MAT_0103 -->|"consumes"| PROC_0106
  PROC_0106 -->|"produces"| MAT_0104
```

*MAP-OXIDE-PATTERN-TRANSFER — Illustrative positive-tone oxide pattern transfer only; no actual dimensions, qualified chemistry or universal device sequence implied. Original schematic; CC BY 4.0. Source: graph records and their evidence links; no physical scale.*

| ID | Entity | Status | Canonical article |
|---|---|---|---|
| MAT-0010 | Accepted starting wafer | reviewed | [Accepted starting wafer](../04_wafer_manufacturing/wafer_finishing_and_acceptance.md) |
| MAT-0101 | Thermal oxide on silicon | reviewed | [Thermal oxide on silicon](../13_oxidation/oxidation.md) |
| MAT-0102 | Resist-patterned oxide wafer | reviewed | [Resist-patterned oxide wafer](../09_photolithography/lithography.md) |
| MAT-0103 | Etched oxide with remaining resist | reviewed | [Etched oxide with remaining resist](../11_etching/etching.md) |
| MAT-0104 | Patterned oxide after strip | reviewed | [Patterned oxide after strip](../14_cleaning/cleaning.md) |
| PROC-0101 | Resist patterning | reviewed | [Resist patterning](../09_photolithography/lithography.md) |
| PROC-0103 | Pattern transfer etch | reviewed | [Pattern transfer etch](../11_etching/etching.md) |
| PROC-0105 | Thermal oxidation | reviewed | [Thermal oxidation](../13_oxidation/oxidation.md) |
| PROC-0106 | Resist strip and surface clean | reviewed | [Resist strip and surface clean](../14_cleaning/cleaning.md) |

| Edge | Relationship | Conditions | Evidence |
|---|---|---|---|
| EDGE-0105 | PROC-0105 → CONSUMES → MAT-0010 | Illustrative positive-tone oxide pattern transfer only; no actual dimensions, qualified chemistry or universal device sequence implied. | [UALBERTA-OXIDE-001](../42_references/bibliography.md#ualberta-oxide-001) (Introduction and calculation details) |
| EDGE-0106 | PROC-0105 → PRODUCES → MAT-0101 | Illustrative positive-tone oxide pattern transfer only; no actual dimensions, qualified chemistry or universal device sequence implied. | [UALBERTA-OXIDE-001](../42_references/bibliography.md#ualberta-oxide-001) (Introduction and calculation details) |
| EDGE-0107 | PROC-0101 → CONSUMES → MAT-0101 | Illustrative positive-tone oxide pattern transfer only; no actual dimensions, qualified chemistry or universal device sequence implied. | [MACK-QUALITY-001](../42_references/bibliography.md#mack-quality-001) (Pattern-transfer and resist-property slides) |
| EDGE-0108 | PROC-0101 → PRODUCES → MAT-0102 | Illustrative positive-tone oxide pattern transfer only; no actual dimensions, qualified chemistry or universal device sequence implied. | [MACK-QUALITY-001](../42_references/bibliography.md#mack-quality-001) (Pattern-transfer and resist-property slides) |
| EDGE-0109 | PROC-0103 → CONSUMES → MAT-0102 | Illustrative positive-tone oxide pattern transfer only; no actual dimensions, qualified chemistry or universal device sequence implied. | [LAM-ETCH-001](../42_references/bibliography.md#lam-etch-001) (Etch process overview and process categories) |
| EDGE-0110 | PROC-0103 → PRODUCES → MAT-0103 | Illustrative positive-tone oxide pattern transfer only; no actual dimensions, qualified chemistry or universal device sequence implied. | [LAM-ETCH-001](../42_references/bibliography.md#lam-etch-001) (Etch process overview and process categories) |
| EDGE-0111 | PROC-0106 → CONSUMES → MAT-0103 | Illustrative positive-tone oxide pattern transfer only; no actual dimensions, qualified chemistry or universal device sequence implied. | [UBC-CLEAN-001](../42_references/bibliography.md#ubc-clean-001) (Overview, solvent clean and oxide-removal discussion) |
| EDGE-0112 | PROC-0106 → PRODUCES → MAT-0104 | Illustrative positive-tone oxide pattern transfer only; no actual dimensions, qualified chemistry or universal device sequence implied. | [UBC-CLEAN-001](../42_references/bibliography.md#ubc-clean-001) (Overview, solvent clean and oxide-removal discussion) |
<!-- END GENERATED MAP -->
