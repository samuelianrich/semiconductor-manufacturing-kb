# Manufacturing entity and process register

Generated from the canonical entity and process tables; edit CSVs, then regenerate.

[Map home](README.md) · [Schema](SCHEMA.md)

<a id="mat-0001"></a>
## MAT-0001 — Quartz-bearing feedstock

Type: `material` · Status: **reviewed** · [Article](../01_raw_materials/quartz_and_feedstocks.md)

Quartz or quartzite provides silica-bearing feed; mineral association and impurities require characterization.

Evidence: [USGS-SILICON-001](../42_references/bibliography.md#usgs-silicon-001) — Opening commodity description

- Composition or state: Quartz or quartzite provides silica-bearing feed; mineral association and impurities require characterization.
- Qualification notes: Application-specific specification; impurity, geometry and electrical limits are not interchangeable. See owner article; no proprietary limits researched.

| Edge | Directional relationship | Scope / condition |
|---|---|---|
| EDGE-0001 | [PROC-0001](#proc-0001) → CONSUMES → [MAT-0001](#mat-0001) | Representative chlorosilane/Siemens/CZ route; aggregate operation boundaries and qualified output only. (reviewed) |
| EDGE-0069 | [MAT-0001](#mat-0001) → SUPPLIED_BY → [SUP-0001](#sup-0001) | Elkem describes Tana quartzite extraction and industrial uses. Role example only; see claim boundary. (reviewed) |

<a id="mat-0002"></a>
## MAT-0002 — Qualified quartz and carbon charge

Type: `material` · Status: **reviewed** · [Article](../01_raw_materials/quartz_and_feedstocks.md)

Quartz and selected carbon reductants are prepared for furnace use; qualification is furnace-specific, not electronic-grade acceptance.

Evidence: [NTNU-SMELTING-001](../42_references/bibliography.md#ntnu-smelting-001) — Carbon sources and quartz in silicon production

- Composition or state: Quartz and selected carbon reductants are prepared for furnace use; qualification is furnace-specific, not electronic-grade acceptance.
- Qualification notes: Application-specific specification; impurity, geometry and electrical limits are not interchangeable. See owner article; no proprietary limits researched.

| Edge | Directional relationship | Scope / condition |
|---|---|---|
| EDGE-0002 | [PROC-0001](#proc-0001) → PRODUCES → [MAT-0002](#mat-0002) | Representative chlorosilane/Siemens/CZ route; aggregate operation boundaries and qualified output only. (reviewed) |
| EDGE-0003 | [PROC-0002](#proc-0002) → CONSUMES → [MAT-0002](#mat-0002) | Representative chlorosilane/Siemens/CZ route; aggregate operation boundaries and qualified output only. (reviewed) |

<a id="mat-0003"></a>
## MAT-0003 — Metallurgical-grade silicon

Type: `material` · Status: **reviewed** · [Article](../02_silicon_refining/metallurgical_silicon.md)

Reduced silicon requiring further chemical purification for electronic-material applications.

Evidence: [WACKER-POLY-001](../42_references/bibliography.md#wacker-poly-001) — Starting silicon and chemical purification

- Composition or state: Reduced silicon requiring further chemical purification for electronic-material applications.
- Qualification notes: Application-specific specification; impurity, geometry and electrical limits are not interchangeable. See owner article; no proprietary limits researched.

| Edge | Directional relationship | Scope / condition |
|---|---|---|
| EDGE-0004 | [PROC-0002](#proc-0002) → PRODUCES → [MAT-0003](#mat-0003) | Representative chlorosilane/Siemens/CZ route; aggregate operation boundaries and qualified output only. (reviewed) |
| EDGE-0006 | [PROC-0003](#proc-0003) → CONSUMES → [MAT-0003](#mat-0003) | Representative chlorosilane/Siemens/CZ route; aggregate operation boundaries and qualified output only. (reviewed) |

<a id="mat-0004"></a>
## MAT-0004 — Crude chlorosilane mixture

Type: `material` · Status: **reviewed** · [Article](../02_silicon_refining/electronic_grade_polysilicon.md)

Silicon is converted to a volatile chlorosilane stream for chemical purification.

Evidence: [WACKER-POLY-001](../42_references/bibliography.md#wacker-poly-001) — Chlorosilane and distillation discussion

- Composition or state: Silicon is converted to a volatile chlorosilane stream for chemical purification.
- Qualification notes: Application-specific specification; impurity, geometry and electrical limits are not interchangeable. See owner article; no proprietary limits researched.

| Edge | Directional relationship | Scope / condition |
|---|---|---|
| EDGE-0007 | [PROC-0003](#proc-0003) → PRODUCES → [MAT-0004](#mat-0004) | Representative chlorosilane/Siemens/CZ route; aggregate operation boundaries and qualified output only. (reviewed) |
| EDGE-0009 | [PROC-0004](#proc-0004) → CONSUMES → [MAT-0004](#mat-0004) | Representative chlorosilane/Siemens/CZ route; aggregate operation boundaries and qualified output only. (reviewed) |

<a id="mat-0005"></a>
## MAT-0005 — Purified chlorosilane feed

Type: `material` · Status: **reviewed** · [Article](../02_silicon_refining/electronic_grade_polysilicon.md)

Purified chlorosilane feed precedes deposition in the representative Siemens route.

Evidence: [WACKER-POLY-001](../42_references/bibliography.md#wacker-poly-001) — Chlorosilane/distillation and deposition

- Composition or state: Purified chlorosilane feed precedes deposition in the representative Siemens route.
- Qualification notes: Application-specific specification; impurity, geometry and electrical limits are not interchangeable. See owner article; no proprietary limits researched.

| Edge | Directional relationship | Scope / condition |
|---|---|---|
| EDGE-0010 | [PROC-0004](#proc-0004) → PRODUCES → [MAT-0005](#mat-0005) | Representative chlorosilane/Siemens/CZ route; aggregate operation boundaries and qualified output only. (reviewed) |
| EDGE-0012 | [PROC-0005](#proc-0005) → CONSUMES → [MAT-0005](#mat-0005) | Representative chlorosilane/Siemens/CZ route; aggregate operation boundaries and qualified output only. (reviewed) |

<a id="mat-0006"></a>
## MAT-0006 — Electronic-grade polysilicon

Type: `material` · Status: **reviewed** · [Article](../02_silicon_refining/electronic_grade_polysilicon.md)

Purified deposited silicon is sized, cleaned and packaged to limit recontamination; electronic qualification is specification-dependent.

Evidence: [HSC-POLY-001](../42_references/bibliography.md#hsc-poly-001) — Science of Polysilicon; cleaning and packaging

- Composition or state: Purified deposited silicon is sized, cleaned and packaged to limit recontamination; electronic qualification is specification-dependent.
- Qualification notes: Application-specific specification; impurity, geometry and electrical limits are not interchangeable. See owner article; no proprietary limits researched.

| Edge | Directional relationship | Scope / condition |
|---|---|---|
| EDGE-0013 | [PROC-0005](#proc-0005) → PRODUCES → [MAT-0006](#mat-0006) | Representative chlorosilane/Siemens/CZ route; aggregate operation boundaries and qualified output only. (reviewed) |
| EDGE-0015 | [PROC-0006](#proc-0006) → CONSUMES → [MAT-0006](#mat-0006) | Representative chlorosilane/Siemens/CZ route; aggregate operation boundaries and qualified output only. (reviewed) |
| EDGE-0066 | [PROC-0010](#proc-0010) → CONSUMES → [MAT-0006](#mat-0006) | Requires suitable feed-rod form and purity; not arbitrary deposited chunks. (reviewed) |
| EDGE-0071 | [MAT-0006](#mat-0006) → SUPPLIED_BY → [SUP-0003](#sup-0003) | WACKER describes a chlorosilane/distillation and Siemens deposition route for polysilicon. Role example only; see claim boundary. (reviewed) |
| EDGE-0072 | [MAT-0006](#mat-0006) → SUPPLIED_BY → [SUP-0004](#sup-0004) | Hemlock describes TCS-based CVD and controlled polysilicon sizing, cleaning and packaging. Role example only; see claim boundary. (reviewed) |

<a id="mat-0007"></a>
## MAT-0007 — Single-crystal silicon ingot

Type: `material` · Status: **reviewed** · [Article](../03_crystal_growth/crystal_growth.md)

Seeded growth produces an oriented crystal for subsequent wafer forming.

Evidence: [SUMCO-WAFER-001](../42_references/bibliography.md#sumco-wafer-001) — Monocrystalline pulling

- Composition or state: Seeded growth produces an oriented crystal for subsequent wafer forming.
- Qualification notes: Application-specific specification; impurity, geometry and electrical limits are not interchangeable. See owner article; no proprietary limits researched.

| Edge | Directional relationship | Scope / condition |
|---|---|---|
| EDGE-0016 | [PROC-0006](#proc-0006) → PRODUCES → [MAT-0007](#mat-0007) | Representative chlorosilane/Siemens/CZ route; aggregate operation boundaries and qualified output only. (reviewed) |
| EDGE-0018 | [PROC-0007](#proc-0007) → CONSUMES → [MAT-0007](#mat-0007) | Representative chlorosilane/Siemens/CZ route; aggregate operation boundaries and qualified output only. (reviewed) |
| EDGE-0067 | [PROC-0010](#proc-0010) → PRODUCES → [MAT-0007](#mat-0007) | Generic ingot category; CZ and FZ specifications are not interchangeable. (reviewed) |
| EDGE-0074 | [MAT-0007](#mat-0007) → SUPPLIED_BY → [SUP-0006](#sup-0006) | Siltronic describes float-zone silicon products and their lower-oxygen and high-resistivity application context. Role example only; see claim boundary. (reviewed) |

<a id="mat-0008"></a>
## MAT-0008 — Sliced silicon wafer

Type: `material` · Status: **reviewed** · [Article](../04_wafer_manufacturing/wafer_finishing_and_acceptance.md)

Slicing establishes a wafer blank that still needs surface and geometry finishing.

Evidence: [SUMCO-WAFER-001](../42_references/bibliography.md#sumco-wafer-001) — Wafer forming; slicing and lapping

- Composition or state: Slicing establishes a wafer blank that still needs surface and geometry finishing.
- Qualification notes: Application-specific specification; impurity, geometry and electrical limits are not interchangeable. See owner article; no proprietary limits researched.

| Edge | Directional relationship | Scope / condition |
|---|---|---|
| EDGE-0019 | [PROC-0007](#proc-0007) → PRODUCES → [MAT-0008](#mat-0008) | Representative chlorosilane/Siemens/CZ route; aggregate operation boundaries and qualified output only. (reviewed) |
| EDGE-0021 | [PROC-0008](#proc-0008) → CONSUMES → [MAT-0008](#mat-0008) | Representative chlorosilane/Siemens/CZ route; aggregate operation boundaries and qualified output only. (reviewed) |

<a id="mat-0009"></a>
## MAT-0009 — Finished polished wafer

Type: `material` · Status: **reviewed** · [Article](../04_wafer_manufacturing/wafer_finishing_and_acceptance.md)

Polishing prepares a controlled wafer surface before final cleaning and inspection.

Evidence: [SUMCO-WAFER-001](../42_references/bibliography.md#sumco-wafer-001) — Polishing; cleaning and inspection

- Composition or state: Polishing prepares a controlled wafer surface before final cleaning and inspection.
- Qualification notes: Application-specific specification; impurity, geometry and electrical limits are not interchangeable. See owner article; no proprietary limits researched.

| Edge | Directional relationship | Scope / condition |
|---|---|---|
| EDGE-0022 | [PROC-0008](#proc-0008) → PRODUCES → [MAT-0009](#mat-0009) | Representative chlorosilane/Siemens/CZ route; aggregate operation boundaries and qualified output only. (reviewed) |
| EDGE-0024 | [PROC-0009](#proc-0009) → CONSUMES → [MAT-0009](#mat-0009) | Representative chlorosilane/Siemens/CZ route; aggregate operation boundaries and qualified output only. (reviewed) |

<a id="mat-0010"></a>
## MAT-0010 — Accepted starting wafer

Type: `material` · Status: **reviewed** · [Article](../04_wafer_manufacturing/wafer_finishing_and_acceptance.md)

A cleaned and inspected wafer meets a specified acceptance boundary; no universal numerical limits or downstream defect-free guarantee are implied.

Evidence: [SUMCO-WAFER-001](../42_references/bibliography.md#sumco-wafer-001) — Cleaning and inspection

- Composition or state: A cleaned and inspected wafer meets a specified acceptance boundary; no universal numerical limits or downstream defect-free guarantee are implied.
- Qualification notes: Application-specific specification; impurity, geometry and electrical limits are not interchangeable. See owner article; no proprietary limits researched.

| Edge | Directional relationship | Scope / condition |
|---|---|---|
| EDGE-0025 | [PROC-0009](#proc-0009) → PRODUCES → [MAT-0010](#mat-0010) | Representative chlorosilane/Siemens/CZ route; aggregate operation boundaries and qualified output only. (reviewed) |
| EDGE-0027 | [PROC-0030](#proc-0030) → CONSUMES → [MAT-0010](#mat-0010) |  (planned) |
| EDGE-0030 | [PROC-0031](#proc-0031) → CONSUMES → [MAT-0010](#mat-0010) |  (planned) |
| EDGE-0075 | [MAT-0010](#mat-0010) → SUPPLIED_BY → [SUP-0007](#sup-0007) | SUMCO describes wafer forming through slicing, lapping, etching, polishing, cleaning and inspection. Role example only; see claim boundary. (reviewed) |
| EDGE-0105 | [PROC-0105](#proc-0105) → CONSUMES → [MAT-0010](#mat-0010) | Illustrative positive-tone oxide pattern transfer only; no actual dimensions, qualified chemistry or universal device sequence implied. (reviewed) |

<a id="art-0030"></a>
## ART-0030 — Tested logic die

Type: `artifact` · Status: **planned** · [Article](../20_wafer_test/README.md)

Tested logic die

| Edge | Directional relationship | Scope / condition |
|---|---|---|
| EDGE-0028 | [PROC-0030](#proc-0030) → PRODUCES → [ART-0030](#art-0030) |  (planned) |
| EDGE-0039 | [PROC-0036](#proc-0036) → CONSUMES → [ART-0030](#art-0030) |  (planned) |

<a id="art-0031"></a>
## ART-0031 — DRAM wafer

Type: `artifact` · Status: **planned** · [Article](../23_dram_fundamentals/README.md)

DRAM wafer

| Edge | Directional relationship | Scope / condition |
|---|---|---|
| EDGE-0031 | [PROC-0031](#proc-0031) → PRODUCES → [ART-0031](#art-0031) |  (planned) |
| EDGE-0032 | [PROC-0032](#proc-0032) → CONSUMES → [ART-0031](#art-0031) |  (planned) |

<a id="art-0032"></a>
## ART-0032 — Prepared DRAM dies

Type: `artifact` · Status: **planned** · [Article](../24_hbm_manufacturing/README.md)

Prepared DRAM dies

| Edge | Directional relationship | Scope / condition |
|---|---|---|
| EDGE-0033 | [PROC-0032](#proc-0032) → PRODUCES → [ART-0032](#art-0032) |  (planned) |
| EDGE-0034 | [PROC-0033](#proc-0033) → CONSUMES → [ART-0032](#art-0032) |  (planned) |

<a id="art-0033"></a>
## ART-0033 — Tested HBM stack

Type: `artifact` · Status: **planned** · [Article](../24_hbm_manufacturing/README.md)

Tested HBM stack

| Edge | Directional relationship | Scope / condition |
|---|---|---|
| EDGE-0035 | [PROC-0033](#proc-0033) → PRODUCES → [ART-0033](#art-0033) |  (planned) |
| EDGE-0040 | [PROC-0036](#proc-0036) → CONSUMES → [ART-0033](#art-0033) |  (planned) |

<a id="art-0034"></a>
## ART-0034 — Package substrate

Type: `artifact` · Status: **planned** · [Article](../26_substrates/README.md)

Package substrate

| Edge | Directional relationship | Scope / condition |
|---|---|---|
| EDGE-0036 | [PROC-0034](#proc-0034) → PRODUCES → [ART-0034](#art-0034) |  (planned) |
| EDGE-0041 | [PROC-0036](#proc-0036) → CONSUMES → [ART-0034](#art-0034) |  (planned) |

<a id="art-0035"></a>
## ART-0035 — Interposer or bridge

Type: `artifact` · Status: **planned** · [Article](../25_advanced_packaging/README.md)

Interposer or bridge

| Edge | Directional relationship | Scope / condition |
|---|---|---|
| EDGE-0037 | [PROC-0035](#proc-0035) → PRODUCES → [ART-0035](#art-0035) |  (planned) |
| EDGE-0042 | [PROC-0036](#proc-0036) → CONSUMES → [ART-0035](#art-0035) |  (planned) |

<a id="art-0036"></a>
## ART-0036 — Tested accelerator package

Type: `artifact` · Status: **planned** · [Article](../29_gpu_package/README.md)

Tested accelerator package

| Edge | Directional relationship | Scope / condition |
|---|---|---|
| EDGE-0043 | [PROC-0036](#proc-0036) → PRODUCES → [ART-0036](#art-0036) |  (planned) |
| EDGE-0044 | [PROC-0038](#proc-0038) → CONSUMES → [ART-0036](#art-0036) |  (planned) |

<a id="art-0037"></a>
## ART-0037 — Fabricated PCB

Type: `artifact` · Status: **planned** · [Article](../30_pcb_and_module/README.md)

Fabricated PCB

| Edge | Directional relationship | Scope / condition |
|---|---|---|
| EDGE-0038 | [PROC-0037](#proc-0037) → PRODUCES → [ART-0037](#art-0037) |  (planned) |
| EDGE-0045 | [PROC-0038](#proc-0038) → CONSUMES → [ART-0037](#art-0037) |  (planned) |

<a id="art-0038"></a>
## ART-0038 — Tested accelerator module

Type: `artifact` · Status: **planned** · [Article](../30_pcb_and_module/README.md)

Tested accelerator module

| Edge | Directional relationship | Scope / condition |
|---|---|---|
| EDGE-0046 | [PROC-0038](#proc-0038) → PRODUCES → [ART-0038](#art-0038) |  (planned) |
| EDGE-0047 | [PROC-0039](#proc-0039) → CONSUMES → [ART-0038](#art-0038) |  (planned) |

<a id="art-0039"></a>
## ART-0039 — Integrated server

Type: `artifact` · Status: **planned** · [Article](../31_system_integration/README.md)

Integrated server

| Edge | Directional relationship | Scope / condition |
|---|---|---|
| EDGE-0048 | [PROC-0039](#proc-0039) → PRODUCES → [ART-0039](#art-0039) |  (planned) |
| EDGE-0049 | [PROC-0040](#proc-0040) → CONSUMES → [ART-0039](#art-0039) |  (planned) |

<a id="art-0040"></a>
## ART-0040 — Integrated rack system

Type: `artifact` · Status: **planned** · [Article](../32_rack_scale_system/README.md)

Integrated rack system

| Edge | Directional relationship | Scope / condition |
|---|---|---|
| EDGE-0050 | [PROC-0040](#proc-0040) → PRODUCES → [ART-0040](#art-0040) |  (planned) |

<a id="art-0041"></a>
## ART-0041 — Power and cooling assemblies

Type: `artifact` · Status: **planned** · [Article](../28_power_delivery/README.md)

Power and cooling assemblies

| Edge | Directional relationship | Scope / condition |
|---|---|---|
| EDGE-0051 | [ART-0041](#art-0041) → ENABLES → [PROC-0038](#proc-0038) | Boundary-specific assemblies and interfaces; not a serial conversion of power into hardware. (planned) |
| EDGE-0052 | [ART-0041](#art-0041) → ENABLES → [PROC-0039](#proc-0039) | Boundary-specific assemblies and interfaces; not a serial conversion of power into hardware. (planned) |
| EDGE-0053 | [ART-0041](#art-0041) → ENABLES → [PROC-0040](#proc-0040) | Boundary-specific assemblies and interfaces; not a serial conversion of power into hardware. (planned) |

<a id="art-0042"></a>
## ART-0042 — Design and mask information

Type: `artifact` · Status: **planned** · [Article](../07_ic_design_and_tapeout/README.md)

Design and mask information

| Edge | Directional relationship | Scope / condition |
|---|---|---|
| EDGE-0029 | [ART-0042](#art-0042) → ENABLES → [PROC-0030](#proc-0030) | Information input, not material consumed. (planned) |

<a id="proc-0001"></a>
## PROC-0001 — Mine, beneficiate and qualify feedstock

Type: `operation` · Status: **reviewed** · [Article](../01_raw_materials/quartz_and_feedstocks.md)

Extract and prepare quartz-bearing feed; processing targets depend on the deposit and furnace requirements.

Purpose: Extract and prepare quartz-bearing feed; processing targets depend on the deposit and furnace requirements.

Scope: Phase 1 general engineering, aggregate operation boundary; see article for inputs/outputs and alternative routes.

Mechanism: Extract and prepare quartz-bearing feed; processing targets depend on the deposit and furnace requirements.

Notes: Controls, material/equipment functions, failures and metrology discussed in owner article. Numerical recipes, vendor pricing and customer qualifications unknown/not researched. No Rubin assignment.

Evidence: [NTNU-QUARTZ-001](../42_references/bibliography.md#ntnu-quartz-001) — High Temperature Quartz research description; [ELKEM-QUARTZ-001](../42_references/bibliography.md#elkem-quartz-001) — Extraction and deposit description (CLM-000001); [CHEGINI-QUARTZ-001](../42_references/bibliography.md#chegini-quartz-001) — Abstract: deposit-specific beneficiation only

| Edge | Directional relationship | Scope / condition |
|---|---|---|
| EDGE-0001 | [PROC-0001](#proc-0001) → CONSUMES → [MAT-0001](#mat-0001) | Representative chlorosilane/Siemens/CZ route; aggregate operation boundaries and qualified output only. (reviewed) |
| EDGE-0002 | [PROC-0001](#proc-0001) → PRODUCES → [MAT-0002](#mat-0002) | Representative chlorosilane/Siemens/CZ route; aggregate operation boundaries and qualified output only. (reviewed) |
| EDGE-0005 | [PROC-0001](#proc-0001) → PRECEDES → [PROC-0002](#proc-0002) | Representative chlorosilane/CZ/polished-wafer learning route; variants are separately scoped. (reviewed) |

<a id="proc-0002"></a>
## PROC-0002 — Carbothermic silicon smelting

Type: `operation` · Status: **reviewed** · [Article](../02_silicon_refining/metallurgical_silicon.md)

Electrical furnace heating and carbon reduction remove oxygen from silica through reactions involving SiO and SiC.

Purpose: Electrical furnace heating and carbon reduction remove oxygen from silica through reactions involving SiO and SiC.

Scope: Phase 1 general engineering, aggregate operation boundary; see article for inputs/outputs and alternative routes.

Mechanism: Electrical furnace heating and carbon reduction remove oxygen from silica through reactions involving SiO and SiC.

Notes: Controls, material/equipment functions, failures and metrology discussed in owner article. Numerical recipes, vendor pricing and customer qualifications unknown/not researched. No Rubin assignment.

Evidence: [NTNU-SMELTING-001](../42_references/bibliography.md#ntnu-smelting-001) — SiC role and furnace observations

| Edge | Directional relationship | Scope / condition |
|---|---|---|
| EDGE-0003 | [PROC-0002](#proc-0002) → CONSUMES → [MAT-0002](#mat-0002) | Representative chlorosilane/Siemens/CZ route; aggregate operation boundaries and qualified output only. (reviewed) |
| EDGE-0004 | [PROC-0002](#proc-0002) → PRODUCES → [MAT-0003](#mat-0003) | Representative chlorosilane/Siemens/CZ route; aggregate operation boundaries and qualified output only. (reviewed) |
| EDGE-0005 | [PROC-0001](#proc-0001) → PRECEDES → [PROC-0002](#proc-0002) | Representative chlorosilane/CZ/polished-wafer learning route; variants are separately scoped. (reviewed) |
| EDGE-0008 | [PROC-0002](#proc-0002) → PRECEDES → [PROC-0003](#proc-0003) | Representative chlorosilane/CZ/polished-wafer learning route; variants are separately scoped. (reviewed) |
| EDGE-0054 | [PROC-0002](#proc-0002) → USES_EQUIPMENT → [EQ-0001](#eq-0001) |  (reviewed) |
| EDGE-0061 | [PROC-0002](#proc-0002) → CONSUMES → [MAT-0011](#mat-0011) |  (reviewed) |
| EDGE-0083 | [PROC-0002](#proc-0002) → MEASURES → [METRIC-0002](#metric-0002) | Aggregated energy and accepted-mass accounting at the furnace boundary; original metric definition, no actual operating data supplied. (reviewed) |

<a id="proc-0003"></a>
## PROC-0003 — Chlorosilane synthesis

Type: `operation` · Status: **reviewed** · [Article](../02_silicon_refining/electronic_grade_polysilicon.md)

Convert metallurgical silicon to chlorosilanes suitable for purification.

Purpose: Convert metallurgical silicon to chlorosilanes suitable for purification.

Scope: Phase 1 general engineering, aggregate operation boundary; see article for inputs/outputs and alternative routes.

Mechanism: Convert metallurgical silicon to chlorosilanes suitable for purification.

Notes: Controls, material/equipment functions, failures and metrology discussed in owner article. Numerical recipes, vendor pricing and customer qualifications unknown/not researched. No Rubin assignment.

Evidence: [WACKER-POLY-001](../42_references/bibliography.md#wacker-poly-001) — Chlorosilane synthesis description

| Edge | Directional relationship | Scope / condition |
|---|---|---|
| EDGE-0006 | [PROC-0003](#proc-0003) → CONSUMES → [MAT-0003](#mat-0003) | Representative chlorosilane/Siemens/CZ route; aggregate operation boundaries and qualified output only. (reviewed) |
| EDGE-0007 | [PROC-0003](#proc-0003) → PRODUCES → [MAT-0004](#mat-0004) | Representative chlorosilane/Siemens/CZ route; aggregate operation boundaries and qualified output only. (reviewed) |
| EDGE-0008 | [PROC-0002](#proc-0002) → PRECEDES → [PROC-0003](#proc-0003) | Representative chlorosilane/CZ/polished-wafer learning route; variants are separately scoped. (reviewed) |
| EDGE-0011 | [PROC-0003](#proc-0003) → PRECEDES → [PROC-0004](#proc-0004) | Representative chlorosilane/CZ/polished-wafer learning route; variants are separately scoped. (reviewed) |
| EDGE-0064 | [MAT-0014](#mat-0014) → ENABLES → [PROC-0003](#proc-0003) | Grouped utility chemistry; actual H2/HCl delivery and recovery are distinct streams. (reviewed) |

<a id="proc-0004"></a>
## PROC-0004 — Chemical purification by distillation

Type: `operation` · Status: **reviewed** · [Article](../02_silicon_refining/electronic_grade_polysilicon.md)

Separate chemical species through repeated vapor/liquid separation before deposition.

Purpose: Separate chemical species through repeated vapor/liquid separation before deposition.

Scope: Phase 1 general engineering, aggregate operation boundary; see article for inputs/outputs and alternative routes.

Mechanism: Separate chemical species through repeated vapor/liquid separation before deposition.

Notes: Controls, material/equipment functions, failures and metrology discussed in owner article. Numerical recipes, vendor pricing and customer qualifications unknown/not researched. No Rubin assignment.

Evidence: [WACKER-POLY-001](../42_references/bibliography.md#wacker-poly-001) — Distillation section

| Edge | Directional relationship | Scope / condition |
|---|---|---|
| EDGE-0009 | [PROC-0004](#proc-0004) → CONSUMES → [MAT-0004](#mat-0004) | Representative chlorosilane/Siemens/CZ route; aggregate operation boundaries and qualified output only. (reviewed) |
| EDGE-0010 | [PROC-0004](#proc-0004) → PRODUCES → [MAT-0005](#mat-0005) | Representative chlorosilane/Siemens/CZ route; aggregate operation boundaries and qualified output only. (reviewed) |
| EDGE-0011 | [PROC-0003](#proc-0003) → PRECEDES → [PROC-0004](#proc-0004) | Representative chlorosilane/CZ/polished-wafer learning route; variants are separately scoped. (reviewed) |
| EDGE-0014 | [PROC-0004](#proc-0004) → PRECEDES → [PROC-0005](#proc-0005) | Representative chlorosilane/CZ/polished-wafer learning route; variants are separately scoped. (reviewed) |
| EDGE-0055 | [PROC-0004](#proc-0004) → USES_EQUIPMENT → [EQ-0002](#eq-0002) |  (reviewed) |

<a id="proc-0005"></a>
## PROC-0005 — Polysilicon deposition

Type: `operation` · Status: **reviewed** · [Article](../02_silicon_refining/electronic_grade_polysilicon.md)

Deposit silicon from purified gas on heated silicon surfaces; subsequent clean handling protects the product.

Purpose: Deposit silicon from purified gas on heated silicon surfaces; subsequent clean handling protects the product.

Scope: Phase 1 general engineering, aggregate operation boundary; see article for inputs/outputs and alternative routes.

Mechanism: Deposit silicon from purified gas on heated silicon surfaces; subsequent clean handling protects the product.

Notes: Controls, material/equipment functions, failures and metrology discussed in owner article. Numerical recipes, vendor pricing and customer qualifications unknown/not researched. No Rubin assignment.

Evidence: [HSC-POLY-001](../42_references/bibliography.md#hsc-poly-001) — TCS CVD and product finishing

| Edge | Directional relationship | Scope / condition |
|---|---|---|
| EDGE-0012 | [PROC-0005](#proc-0005) → CONSUMES → [MAT-0005](#mat-0005) | Representative chlorosilane/Siemens/CZ route; aggregate operation boundaries and qualified output only. (reviewed) |
| EDGE-0013 | [PROC-0005](#proc-0005) → PRODUCES → [MAT-0006](#mat-0006) | Representative chlorosilane/Siemens/CZ route; aggregate operation boundaries and qualified output only. (reviewed) |
| EDGE-0014 | [PROC-0004](#proc-0004) → PRECEDES → [PROC-0005](#proc-0005) | Representative chlorosilane/CZ/polished-wafer learning route; variants are separately scoped. (reviewed) |
| EDGE-0017 | [PROC-0005](#proc-0005) → PRECEDES → [PROC-0006](#proc-0006) | Representative chlorosilane/CZ/polished-wafer learning route; variants are separately scoped. (reviewed) |
| EDGE-0056 | [PROC-0005](#proc-0005) → USES_EQUIPMENT → [EQ-0003](#eq-0003) |  (reviewed) |

<a id="proc-0006"></a>
## PROC-0006 — Czochralski single-crystal growth

Type: `operation` · Status: **reviewed** · [Article](../03_crystal_growth/crystal_growth.md)

Grow an oriented silicon crystal from a seeded melt in a quartz crucible with thermal and motion control.

Purpose: Grow an oriented silicon crystal from a seeded melt in a quartz crucible with thermal and motion control.

Scope: Phase 1 general engineering, aggregate operation boundary; see article for inputs/outputs and alternative routes.

Mechanism: Grow an oriented silicon crystal from a seeded melt in a quartz crucible with thermal and motion control.

Notes: Controls, material/equipment functions, failures and metrology discussed in owner article. Numerical recipes, vendor pricing and customer qualifications unknown/not researched. No Rubin assignment.

Evidence: [PVA-CZ-001](../42_references/bibliography.md#pva-cz-001) — The Process

| Edge | Directional relationship | Scope / condition |
|---|---|---|
| EDGE-0015 | [PROC-0006](#proc-0006) → CONSUMES → [MAT-0006](#mat-0006) | Representative chlorosilane/Siemens/CZ route; aggregate operation boundaries and qualified output only. (reviewed) |
| EDGE-0016 | [PROC-0006](#proc-0006) → PRODUCES → [MAT-0007](#mat-0007) | Representative chlorosilane/Siemens/CZ route; aggregate operation boundaries and qualified output only. (reviewed) |
| EDGE-0017 | [PROC-0005](#proc-0005) → PRECEDES → [PROC-0006](#proc-0006) | Representative chlorosilane/CZ/polished-wafer learning route; variants are separately scoped. (reviewed) |
| EDGE-0020 | [PROC-0006](#proc-0006) → PRECEDES → [PROC-0007](#proc-0007) | Representative chlorosilane/CZ/polished-wafer learning route; variants are separately scoped. (reviewed) |
| EDGE-0057 | [PROC-0006](#proc-0006) → USES_EQUIPMENT → [EQ-0004](#eq-0004) |  (reviewed) |
| EDGE-0062 | [MAT-0012](#mat-0012) → ENABLES → [PROC-0006](#proc-0006) | Indirect enabling input: quartz is first made into a crucible; quartz ore is not placed into the CZ silicon melt. (reviewed) |
| EDGE-0063 | [MAT-0013](#mat-0013) → ENABLES → [PROC-0006](#proc-0006) | CZ variant; container contacts the melt. FZ has a different boundary. (reviewed) |
| EDGE-0065 | [MAT-0015](#mat-0015) → ENABLES → [PROC-0006](#proc-0006) | Seeded growth; orientation depends on selected seed. (reviewed) |
| EDGE-0068 | [PROC-0006](#proc-0006) → ALTERNATIVE_TO → [PROC-0010](#proc-0010) | Compare single-crystal growth purpose; diameter, oxygen and electrical acceptance must be selected for application. (reviewed) |

<a id="proc-0007"></a>
## PROC-0007 — Ingot shaping and wafer slicing

Type: `operation` · Status: **reviewed** · [Article](../04_wafer_manufacturing/wafer_finishing_and_acceptance.md)

Shape the ingot and cut wafer blanks; kerf and cutting damage precede finishing.

Purpose: Shape the ingot and cut wafer blanks; kerf and cutting damage precede finishing.

Scope: Phase 1 general engineering, aggregate operation boundary; see article for inputs/outputs and alternative routes.

Mechanism: Shape the ingot and cut wafer blanks; kerf and cutting damage precede finishing.

Notes: Controls, material/equipment functions, failures and metrology discussed in owner article. Numerical recipes, vendor pricing and customer qualifications unknown/not researched. No Rubin assignment.

Evidence: [SUMCO-WAFER-001](../42_references/bibliography.md#sumco-wafer-001) — Wafer forming

| Edge | Directional relationship | Scope / condition |
|---|---|---|
| EDGE-0018 | [PROC-0007](#proc-0007) → CONSUMES → [MAT-0007](#mat-0007) | Representative chlorosilane/Siemens/CZ route; aggregate operation boundaries and qualified output only. (reviewed) |
| EDGE-0019 | [PROC-0007](#proc-0007) → PRODUCES → [MAT-0008](#mat-0008) | Representative chlorosilane/Siemens/CZ route; aggregate operation boundaries and qualified output only. (reviewed) |
| EDGE-0020 | [PROC-0006](#proc-0006) → PRECEDES → [PROC-0007](#proc-0007) | Representative chlorosilane/CZ/polished-wafer learning route; variants are separately scoped. (reviewed) |
| EDGE-0023 | [PROC-0007](#proc-0007) → PRECEDES → [PROC-0008](#proc-0008) | Representative chlorosilane/CZ/polished-wafer learning route; variants are separately scoped. (reviewed) |
| EDGE-0058 | [PROC-0007](#proc-0007) → USES_EQUIPMENT → [EQ-0005](#eq-0005) |  (reviewed) |

<a id="proc-0008"></a>
## PROC-0008 — Wafer surface finishing

Type: `operation` · Status: **reviewed** · [Article](../04_wafer_manufacturing/wafer_finishing_and_acceptance.md)

Group lapping, etching and polishing at overview level; removal of damage and control of geometry prepare the surface.

Purpose: Group lapping, etching and polishing at overview level; removal of damage and control of geometry prepare the surface.

Scope: Phase 1 general engineering, aggregate operation boundary; see article for inputs/outputs and alternative routes.

Mechanism: Group lapping, etching and polishing at overview level; removal of damage and control of geometry prepare the surface.

Notes: Controls, material/equipment functions, failures and metrology discussed in owner article. Numerical recipes, vendor pricing and customer qualifications unknown/not researched. No Rubin assignment.

Evidence: [SUMCO-WAFER-001](../42_references/bibliography.md#sumco-wafer-001) — Lapping; etching; polishing

| Edge | Directional relationship | Scope / condition |
|---|---|---|
| EDGE-0021 | [PROC-0008](#proc-0008) → CONSUMES → [MAT-0008](#mat-0008) | Representative chlorosilane/Siemens/CZ route; aggregate operation boundaries and qualified output only. (reviewed) |
| EDGE-0022 | [PROC-0008](#proc-0008) → PRODUCES → [MAT-0009](#mat-0009) | Representative chlorosilane/Siemens/CZ route; aggregate operation boundaries and qualified output only. (reviewed) |
| EDGE-0023 | [PROC-0007](#proc-0007) → PRECEDES → [PROC-0008](#proc-0008) | Representative chlorosilane/CZ/polished-wafer learning route; variants are separately scoped. (reviewed) |
| EDGE-0026 | [PROC-0008](#proc-0008) → PRECEDES → [PROC-0009](#proc-0009) | Representative chlorosilane/CZ/polished-wafer learning route; variants are separately scoped. (reviewed) |
| EDGE-0059 | [PROC-0008](#proc-0008) → USES_EQUIPMENT → [EQ-0006](#eq-0006) |  (reviewed) |

<a id="proc-0009"></a>
## PROC-0009 — Wafer cleaning and acceptance inspection

Type: `operation` · Status: **reviewed** · [Article](../04_wafer_manufacturing/wafer_finishing_and_acceptance.md)

Remove residual contamination and inspect against specified geometry, surface and electrical requirements.

Purpose: Remove residual contamination and inspect against specified geometry, surface and electrical requirements.

Scope: Phase 1 general engineering, aggregate operation boundary; see article for inputs/outputs and alternative routes.

Mechanism: Remove residual contamination and inspect against specified geometry, surface and electrical requirements.

Notes: Controls, material/equipment functions, failures and metrology discussed in owner article. Numerical recipes, vendor pricing and customer qualifications unknown/not researched. No Rubin assignment.

Evidence: [SUMCO-WAFER-001](../42_references/bibliography.md#sumco-wafer-001) — Cleaning and inspection; [SEMI-WAFER-001](../42_references/bibliography.md#semi-wafer-001) — Public scope §§2.2–2.3; no normative limits accessed

| Edge | Directional relationship | Scope / condition |
|---|---|---|
| EDGE-0024 | [PROC-0009](#proc-0009) → CONSUMES → [MAT-0009](#mat-0009) | Representative chlorosilane/Siemens/CZ route; aggregate operation boundaries and qualified output only. (reviewed) |
| EDGE-0025 | [PROC-0009](#proc-0009) → PRODUCES → [MAT-0010](#mat-0010) | Representative chlorosilane/Siemens/CZ route; aggregate operation boundaries and qualified output only. (reviewed) |
| EDGE-0026 | [PROC-0008](#proc-0008) → PRECEDES → [PROC-0009](#proc-0009) | Representative chlorosilane/CZ/polished-wafer learning route; variants are separately scoped. (reviewed) |
| EDGE-0060 | [PROC-0009](#proc-0009) → USES_EQUIPMENT → [EQ-0007](#eq-0007) |  (reviewed) |
| EDGE-0077 | [PROC-0009](#proc-0009) → MEASURES → [CHAR-0003](#char-0003) | Acceptance operation aggregates multiple metrology methods; laser scattering alone does not measure all geometry. (reviewed) |
| EDGE-0078 | [FAIL-0001](#fail-0001) → DETECTED_BY → [PROC-0009](#proc-0009) | Only detectable events within method sensitivity and inspection coverage. (reviewed) |
| EDGE-0079 | [FAIL-0002](#fail-0002) → DETECTED_BY → [PROC-0009](#proc-0009) | Appropriate geometry metrology and agreed specification required. (reviewed) |
| EDGE-0082 | [PROC-0009](#proc-0009) → MEASURES → [METRIC-0001](#metric-0001) | Aggregate count after stated inspection coverage; no lot data supplied. (reviewed) |
| EDGE-0085 | [FAIL-0003](#fail-0003) → DETECTED_BY → [PROC-0009](#proc-0009) | Appropriate electrical metrology under specified conditions; not detection by surface laser scattering. (reviewed) |

<a id="proc-0030"></a>
## PROC-0030 — Logic fabrication, test and die preparation

Type: `operation` · Status: **planned** · [Article](../17_transistor_fabrication/README.md)

Logic fabrication, test and die preparation

Purpose: Logic fabrication, test and die preparation

Scope: Planned general manufacturing scope; not a qualified production recipe

Mechanism: Not yet researched.

Notes: Detailed evidence is added during the owning phase.

| Edge | Directional relationship | Scope / condition |
|---|---|---|
| EDGE-0027 | [PROC-0030](#proc-0030) → CONSUMES → [MAT-0010](#mat-0010) |  (planned) |
| EDGE-0028 | [PROC-0030](#proc-0030) → PRODUCES → [ART-0030](#art-0030) |  (planned) |
| EDGE-0029 | [ART-0042](#art-0042) → ENABLES → [PROC-0030](#proc-0030) | Information input, not material consumed. (planned) |
| EDGE-0103 | [FAM-0100](#fam-0100) → ENABLES → [PROC-0030](#proc-0030) | Fab unit-process functions enable the fabrication portion of the planned aggregate logic path; test and die preparation remain later scope. (reviewed) |

<a id="proc-0031"></a>
## PROC-0031 — DRAM wafer fabrication

Type: `operation` · Status: **planned** · [Article](../23_dram_fundamentals/README.md)

DRAM wafer fabrication

Purpose: DRAM wafer fabrication

Scope: Planned general manufacturing scope; not a qualified production recipe

Mechanism: Not yet researched.

Notes: Detailed evidence is added during the owning phase.

| Edge | Directional relationship | Scope / condition |
|---|---|---|
| EDGE-0030 | [PROC-0031](#proc-0031) → CONSUMES → [MAT-0010](#mat-0010) |  (planned) |
| EDGE-0031 | [PROC-0031](#proc-0031) → PRODUCES → [ART-0031](#art-0031) |  (planned) |
| EDGE-0104 | [FAM-0100](#fam-0100) → ENABLES → [PROC-0031](#proc-0031) | Fab unit-process functions are applicable to device fabrication; DRAM-specific integration remains planned. (reviewed) |

<a id="proc-0032"></a>
## PROC-0032 — DRAM test, TSV and die preparation

Type: `operation` · Status: **planned** · [Article](../24_hbm_manufacturing/README.md)

DRAM test, TSV and die preparation

Purpose: DRAM test, TSV and die preparation

Scope: Planned general manufacturing scope; not a qualified production recipe

Mechanism: Not yet researched.

Notes: Detailed evidence is added during the owning phase.

| Edge | Directional relationship | Scope / condition |
|---|---|---|
| EDGE-0032 | [PROC-0032](#proc-0032) → CONSUMES → [ART-0031](#art-0031) |  (planned) |
| EDGE-0033 | [PROC-0032](#proc-0032) → PRODUCES → [ART-0032](#art-0032) |  (planned) |

<a id="proc-0033"></a>
## PROC-0033 — HBM stack assembly and test

Type: `operation` · Status: **planned** · [Article](../24_hbm_manufacturing/README.md)

HBM stack assembly and test

Purpose: HBM stack assembly and test

Scope: Planned general manufacturing scope; not a qualified production recipe

Mechanism: Not yet researched.

Notes: Detailed evidence is added during the owning phase.

| Edge | Directional relationship | Scope / condition |
|---|---|---|
| EDGE-0034 | [PROC-0033](#proc-0033) → CONSUMES → [ART-0032](#art-0032) |  (planned) |
| EDGE-0035 | [PROC-0033](#proc-0033) → PRODUCES → [ART-0033](#art-0033) |  (planned) |

<a id="proc-0034"></a>
## PROC-0034 — Substrate fabrication

Type: `operation` · Status: **planned** · [Article](../26_substrates/README.md)

Substrate fabrication

Purpose: Substrate fabrication

Scope: Planned general manufacturing scope; not a qualified production recipe

Mechanism: Not yet researched.

Notes: Detailed evidence is added during the owning phase.

| Edge | Directional relationship | Scope / condition |
|---|---|---|
| EDGE-0036 | [PROC-0034](#proc-0034) → PRODUCES → [ART-0034](#art-0034) |  (planned) |

<a id="proc-0035"></a>
## PROC-0035 — Interposer or bridge fabrication

Type: `operation` · Status: **planned** · [Article](../25_advanced_packaging/README.md)

Interposer or bridge fabrication

Purpose: Interposer or bridge fabrication

Scope: Planned general manufacturing scope; not a qualified production recipe

Mechanism: Not yet researched.

Notes: Detailed evidence is added during the owning phase.

| Edge | Directional relationship | Scope / condition |
|---|---|---|
| EDGE-0037 | [PROC-0035](#proc-0035) → PRODUCES → [ART-0035](#art-0035) |  (planned) |

<a id="proc-0036"></a>
## PROC-0036 — Package assembly and test

Type: `operation` · Status: **planned** · [Article](../29_gpu_package/README.md)

Package assembly and test

Purpose: Package assembly and test

Scope: Planned general manufacturing scope; not a qualified production recipe

Mechanism: Not yet researched.

Notes: Detailed evidence is added during the owning phase.

| Edge | Directional relationship | Scope / condition |
|---|---|---|
| EDGE-0039 | [PROC-0036](#proc-0036) → CONSUMES → [ART-0030](#art-0030) |  (planned) |
| EDGE-0040 | [PROC-0036](#proc-0036) → CONSUMES → [ART-0033](#art-0033) |  (planned) |
| EDGE-0041 | [PROC-0036](#proc-0036) → CONSUMES → [ART-0034](#art-0034) |  (planned) |
| EDGE-0042 | [PROC-0036](#proc-0036) → CONSUMES → [ART-0035](#art-0035) |  (planned) |
| EDGE-0043 | [PROC-0036](#proc-0036) → PRODUCES → [ART-0036](#art-0036) |  (planned) |

<a id="proc-0037"></a>
## PROC-0037 — PCB fabrication

Type: `operation` · Status: **planned** · [Article](../30_pcb_and_module/README.md)

PCB fabrication

Purpose: PCB fabrication

Scope: Planned general manufacturing scope; not a qualified production recipe

Mechanism: Not yet researched.

Notes: Detailed evidence is added during the owning phase.

| Edge | Directional relationship | Scope / condition |
|---|---|---|
| EDGE-0038 | [PROC-0037](#proc-0037) → PRODUCES → [ART-0037](#art-0037) |  (planned) |

<a id="proc-0038"></a>
## PROC-0038 — Module assembly and test

Type: `operation` · Status: **planned** · [Article](../30_pcb_and_module/README.md)

Module assembly and test

Purpose: Module assembly and test

Scope: Planned general manufacturing scope; not a qualified production recipe

Mechanism: Not yet researched.

Notes: Detailed evidence is added during the owning phase.

| Edge | Directional relationship | Scope / condition |
|---|---|---|
| EDGE-0044 | [PROC-0038](#proc-0038) → CONSUMES → [ART-0036](#art-0036) |  (planned) |
| EDGE-0045 | [PROC-0038](#proc-0038) → CONSUMES → [ART-0037](#art-0037) |  (planned) |
| EDGE-0046 | [PROC-0038](#proc-0038) → PRODUCES → [ART-0038](#art-0038) |  (planned) |
| EDGE-0051 | [ART-0041](#art-0041) → ENABLES → [PROC-0038](#proc-0038) | Boundary-specific assemblies and interfaces; not a serial conversion of power into hardware. (planned) |

<a id="proc-0039"></a>
## PROC-0039 — Server integration

Type: `operation` · Status: **planned** · [Article](../31_system_integration/README.md)

Server integration

Purpose: Server integration

Scope: Planned general manufacturing scope; not a qualified production recipe

Mechanism: Not yet researched.

Notes: Detailed evidence is added during the owning phase.

| Edge | Directional relationship | Scope / condition |
|---|---|---|
| EDGE-0047 | [PROC-0039](#proc-0039) → CONSUMES → [ART-0038](#art-0038) |  (planned) |
| EDGE-0048 | [PROC-0039](#proc-0039) → PRODUCES → [ART-0039](#art-0039) |  (planned) |
| EDGE-0052 | [ART-0041](#art-0041) → ENABLES → [PROC-0039](#proc-0039) | Boundary-specific assemblies and interfaces; not a serial conversion of power into hardware. (planned) |

<a id="proc-0040"></a>
## PROC-0040 — Rack integration

Type: `operation` · Status: **planned** · [Article](../32_rack_scale_system/README.md)

Rack integration

Purpose: Rack integration

Scope: Planned general manufacturing scope; not a qualified production recipe

Mechanism: Not yet researched.

Notes: Detailed evidence is added during the owning phase.

| Edge | Directional relationship | Scope / condition |
|---|---|---|
| EDGE-0049 | [PROC-0040](#proc-0040) → CONSUMES → [ART-0039](#art-0039) |  (planned) |
| EDGE-0050 | [PROC-0040](#proc-0040) → PRODUCES → [ART-0040](#art-0040) |  (planned) |
| EDGE-0053 | [ART-0041](#art-0041) → ENABLES → [PROC-0040](#proc-0040) | Boundary-specific assemblies and interfaces; not a serial conversion of power into hardware. (planned) |

<a id="eq-0001"></a>
## EQ-0001 — Submerged-arc furnace

Type: `equipment` · Status: **reviewed** · [Article](../02_silicon_refining/metallurgical_silicon.md)

Electrodes and an electrically heated reacting burden supply conditions for silicon reduction.

Evidence: [NTNU-SMELTING-001](../42_references/bibliography.md#ntnu-smelting-001) — Furnace description

- Physical function: Electrodes and an electrically heated reacting burden supply conditions for silicon reduction.
- Control notes: See owner article for variables and limitations; numerical equipment settings and purchase price not researched.

| Edge | Directional relationship | Scope / condition |
|---|---|---|
| EDGE-0054 | [PROC-0002](#proc-0002) → USES_EQUIPMENT → [EQ-0001](#eq-0001) |  (reviewed) |

<a id="eq-0002"></a>
## EQ-0002 — Distillation equipment

Type: `equipment` · Status: **reviewed** · [Article](../02_silicon_refining/electronic_grade_polysilicon.md)

Vapor/liquid separation purifies chlorosilane feed before silicon deposition.

Evidence: [WACKER-POLY-001](../42_references/bibliography.md#wacker-poly-001) — Distillation discussion

- Physical function: Vapor/liquid separation purifies chlorosilane feed before silicon deposition.
- Control notes: See owner article for variables and limitations; numerical equipment settings and purchase price not researched.

| Edge | Directional relationship | Scope / condition |
|---|---|---|
| EDGE-0055 | [PROC-0004](#proc-0004) → USES_EQUIPMENT → [EQ-0002](#eq-0002) |  (reviewed) |

<a id="eq-0003"></a>
## EQ-0003 — Siemens deposition reactor

Type: `equipment` · Status: **reviewed** · [Article](../02_silicon_refining/electronic_grade_polysilicon.md)

Heated silicon surfaces support gas-phase silicon deposition.

Evidence: [WACKER-POLY-001](../42_references/bibliography.md#wacker-poly-001) — Deposition hall

- Physical function: Heated silicon surfaces support gas-phase silicon deposition.
- Control notes: See owner article for variables and limitations; numerical equipment settings and purchase price not researched.

| Edge | Directional relationship | Scope / condition |
|---|---|---|
| EDGE-0056 | [PROC-0005](#proc-0005) → USES_EQUIPMENT → [EQ-0003](#eq-0003) |  (reviewed) |

<a id="eq-0004"></a>
## EQ-0004 — CZ crystal puller

Type: `equipment` · Status: **reviewed** · [Article](../03_crystal_growth/crystal_growth.md)

Heater, crucible and seed-motion systems control growth of a single crystal.

Evidence: [PVA-CZ-001](../42_references/bibliography.md#pva-cz-001) — The Process and system description

- Physical function: Heater, crucible and seed-motion systems control growth of a single crystal.
- Control notes: See owner article for variables and limitations; numerical equipment settings and purchase price not researched.

| Edge | Directional relationship | Scope / condition |
|---|---|---|
| EDGE-0057 | [PROC-0006](#proc-0006) → USES_EQUIPMENT → [EQ-0004](#eq-0004) |  (reviewed) |
| EDGE-0073 | [EQ-0004](#eq-0004) → SUPPLIED_BY → [SUP-0005](#sup-0005) | PVA TePla describes CZ puller equipment and thermal and motion control functions. Role example only; see claim boundary. (reviewed) |

<a id="eq-0005"></a>
## EQ-0005 — Wafer slicing equipment

Type: `equipment` · Status: **reviewed** · [Article](../04_wafer_manufacturing/wafer_finishing_and_acceptance.md)

Mechanical cutting divides the ingot into wafer blanks.

Evidence: [SUMCO-WAFER-001](../42_references/bibliography.md#sumco-wafer-001) — Slicing

- Physical function: Mechanical cutting divides the ingot into wafer blanks.
- Control notes: See owner article for variables and limitations; numerical equipment settings and purchase price not researched.

| Edge | Directional relationship | Scope / condition |
|---|---|---|
| EDGE-0058 | [PROC-0007](#proc-0007) → USES_EQUIPMENT → [EQ-0005](#eq-0005) |  (reviewed) |

<a id="eq-0006"></a>
## EQ-0006 — Wafer polishing equipment

Type: `equipment` · Status: **reviewed** · [Article](../04_wafer_manufacturing/wafer_finishing_and_acceptance.md)

Mechanical and chemical action produces a smooth prepared wafer surface.

Evidence: [SUMCO-WAFER-001](../42_references/bibliography.md#sumco-wafer-001) — Polishing

- Physical function: Mechanical and chemical action produces a smooth prepared wafer surface.
- Control notes: See owner article for variables and limitations; numerical equipment settings and purchase price not researched.

| Edge | Directional relationship | Scope / condition |
|---|---|---|
| EDGE-0059 | [PROC-0008](#proc-0008) → USES_EQUIPMENT → [EQ-0006](#eq-0006) |  (reviewed) |

<a id="eq-0007"></a>
## EQ-0007 — Laser-scattering surface inspection

Type: `equipment` · Status: **reviewed** · [Article](../04_wafer_manufacturing/wafer_finishing_and_acceptance.md)

Scattered laser light detects surface events under instrument-dependent sensitivity and classification limits.

Evidence: [UCSB-INSPECT-001](../42_references/bibliography.md#ucsb-inspect-001) — Surface analysis operating principle

- Physical function: Scattered laser light detects surface events under instrument-dependent sensitivity and classification limits.
- Control notes: See owner article for variables and limitations; numerical equipment settings and purchase price not researched.

| Edge | Directional relationship | Scope / condition |
|---|---|---|
| EDGE-0060 | [PROC-0009](#proc-0009) → USES_EQUIPMENT → [EQ-0007](#eq-0007) |  (reviewed) |

<a id="mat-0011"></a>
## MAT-0011 — Carbon reductants

Type: `material` · Status: **reviewed** · [Article](../02_silicon_refining/metallurgical_silicon.md)

Selected carbon-bearing feed participates in oxygen removal during silicon smelting.

Evidence: [NTNU-SMELTING-001](../42_references/bibliography.md#ntnu-smelting-001) — Carbon sources and SiC reactions

- Composition or state: Selected carbon-bearing feed participates in oxygen removal during silicon smelting.
- Qualification notes: Application-specific specification; impurity, geometry and electrical limits are not interchangeable. See owner article; no proprietary limits researched.

| Edge | Directional relationship | Scope / condition |
|---|---|---|
| EDGE-0061 | [PROC-0002](#proc-0002) → CONSUMES → [MAT-0011](#mat-0011) |  (reviewed) |

<a id="mat-0012"></a>
## MAT-0012 — High-purity quartz for crucibles

Type: `material` · Status: **reviewed** · [Article](../01_raw_materials/quartz_and_feedstocks.md)

High-purity quartz can supply fused-quartz crucible manufacture; this is a separate use from silicon furnace ore.

Evidence: [SIBELCO-QUARTZ-001](../42_references/bibliography.md#sibelco-quartz-001) — Semiconductor application bullet

- Composition or state: High-purity quartz can supply fused-quartz crucible manufacture; this is a separate use from silicon furnace ore.
- Qualification notes: Application-specific specification; impurity, geometry and electrical limits are not interchangeable. See owner article; no proprietary limits researched.

| Edge | Directional relationship | Scope / condition |
|---|---|---|
| EDGE-0062 | [MAT-0012](#mat-0012) → ENABLES → [PROC-0006](#proc-0006) | Indirect enabling input: quartz is first made into a crucible; quartz ore is not placed into the CZ silicon melt. (reviewed) |
| EDGE-0070 | [MAT-0012](#mat-0012) → SUPPLIED_BY → [SUP-0002](#sup-0002) | Sibelco describes IOTA high-purity quartz for making fused-quartz crucibles and quartzware. Role example only; see claim boundary. (reviewed) |

<a id="mat-0013"></a>
## MAT-0013 — Quartz crucible

Type: `material` · Status: **reviewed** · [Article](../03_crystal_growth/crystal_growth.md)

A fused-quartz crucible contains the CZ melt and can contribute oxygen to it.

Evidence: [KIEL-SEGREGATION-001](../42_references/bibliography.md#kiel-segregation-001) — Oxygen from quartz crucible

- Composition or state: A fused-quartz crucible contains the CZ melt and can contribute oxygen to it.
- Qualification notes: Application-specific specification; impurity, geometry and electrical limits are not interchangeable. See owner article; no proprietary limits researched.

| Edge | Directional relationship | Scope / condition |
|---|---|---|
| EDGE-0063 | [MAT-0013](#mat-0013) → ENABLES → [PROC-0006](#proc-0006) | CZ variant; container contacts the melt. FZ has a different boundary. (reviewed) |

<a id="mat-0014"></a>
## MAT-0014 — Hydrogen and hydrogen chloride process streams

Type: `material` · Status: **reviewed** · [Article](../02_silicon_refining/electronic_grade_polysilicon.md)

Hydrogen/chlorine-bearing chemistry enables the representative TCS production and silicon deposition route; streams are separately conditioned.

Evidence: [WACKER-POLY-001](../42_references/bibliography.md#wacker-poly-001) — Chlorosilane chemistry and deposition

- Composition or state: Hydrogen/chlorine-bearing chemistry enables the representative TCS production and silicon deposition route; streams are separately conditioned.
- Qualification notes: Application-specific specification; impurity, geometry and electrical limits are not interchangeable. See owner article; no proprietary limits researched.

| Edge | Directional relationship | Scope / condition |
|---|---|---|
| EDGE-0064 | [MAT-0014](#mat-0014) → ENABLES → [PROC-0003](#proc-0003) | Grouped utility chemistry; actual H2/HCl delivery and recovery are distinct streams. (reviewed) |

<a id="mat-0015"></a>
## MAT-0015 — Oriented silicon seed

Type: `material` · Status: **reviewed** · [Article](../03_crystal_growth/crystal_growth.md)

The silicon seed establishes orientation for continued single-crystal growth.

Evidence: [SUMCO-WAFER-001](../42_references/bibliography.md#sumco-wafer-001) — Monocrystalline pulling

- Composition or state: The silicon seed establishes orientation for continued single-crystal growth.
- Qualification notes: Application-specific specification; impurity, geometry and electrical limits are not interchangeable. See owner article; no proprietary limits researched.

| Edge | Directional relationship | Scope / condition |
|---|---|---|
| EDGE-0065 | [MAT-0015](#mat-0015) → ENABLES → [PROC-0006](#proc-0006) | Seeded growth; orientation depends on selected seed. (reviewed) |

<a id="proc-0010"></a>
## PROC-0010 — Float-zone single-crystal growth

Type: `operation` · Status: **reviewed** · [Article](../03_crystal_growth/crystal_growth.md)

A traveling molten zone recrystallizes silicon without a contacting melt crucible; feed form and qualified applications differ from CZ.

Purpose: A traveling molten zone recrystallizes silicon without a contacting melt crucible; feed form and qualified applications differ from CZ.

Scope: Phase 1 general engineering, aggregate operation boundary; see article for inputs/outputs and alternative routes.

Mechanism: A traveling molten zone recrystallizes silicon without a contacting melt crucible; feed form and qualified applications differ from CZ.

Notes: Controls, material/equipment functions, failures and metrology discussed in owner article. Numerical recipes, vendor pricing and customer qualifications unknown/not researched. No Rubin assignment.

Evidence: [SILTRONIC-FZ-001](../42_references/bibliography.md#siltronic-fz-001) — Float zone subsection

| Edge | Directional relationship | Scope / condition |
|---|---|---|
| EDGE-0066 | [PROC-0010](#proc-0010) → CONSUMES → [MAT-0006](#mat-0006) | Requires suitable feed-rod form and purity; not arbitrary deposited chunks. (reviewed) |
| EDGE-0067 | [PROC-0010](#proc-0010) → PRODUCES → [MAT-0007](#mat-0007) | Generic ingot category; CZ and FZ specifications are not interchangeable. (reviewed) |
| EDGE-0068 | [PROC-0006](#proc-0006) → ALTERNATIVE_TO → [PROC-0010](#proc-0010) | Compare single-crystal growth purpose; diameter, oxygen and electrical acceptance must be selected for application. (reviewed) |

<a id="sup-0001"></a>
## SUP-0001 — Elkem

Type: `supplier` · Status: **reviewed** · [Article](../01_raw_materials/quartz_and_feedstocks.md)

Elkem describes Tana quartzite extraction and industrial uses.

Evidence: [ELKEM-QUARTZ-001](../42_references/bibliography.md#elkem-quartz-001) — Plant description and industrial uses (CLM-000001)

- Headquarters country: Not researched in Phase 1
- Manufacturing geography: Not mapped; no customer allocation inferred
- Scope notes: Scope is the cited company disclosure; no customer allocation, exclusivity, current operating capacity or Rubin qualification asserted.

| Edge | Directional relationship | Scope / condition |
|---|---|---|
| EDGE-0069 | [MAT-0001](#mat-0001) → SUPPLIED_BY → [SUP-0001](#sup-0001) | Elkem describes Tana quartzite extraction and industrial uses. Role example only; see claim boundary. (reviewed) |

<a id="sup-0002"></a>
## SUP-0002 — Sibelco

Type: `supplier` · Status: **reviewed** · [Article](../01_raw_materials/quartz_and_feedstocks.md)

Sibelco describes IOTA high-purity quartz for making fused-quartz crucibles and quartzware.

Evidence: [SIBELCO-QUARTZ-001](../42_references/bibliography.md#sibelco-quartz-001) — Semiconductor application bullet (CLM-000002)

- Headquarters country: Not researched in Phase 1
- Manufacturing geography: Not mapped; no customer allocation inferred
- Scope notes: Scope is the cited company disclosure; no customer allocation, exclusivity, current operating capacity or Rubin qualification asserted.

| Edge | Directional relationship | Scope / condition |
|---|---|---|
| EDGE-0070 | [MAT-0012](#mat-0012) → SUPPLIED_BY → [SUP-0002](#sup-0002) | Sibelco describes IOTA high-purity quartz for making fused-quartz crucibles and quartzware. Role example only; see claim boundary. (reviewed) |

<a id="sup-0003"></a>
## SUP-0003 — WACKER

Type: `supplier` · Status: **reviewed** · [Article](../02_silicon_refining/electronic_grade_polysilicon.md)

WACKER describes a chlorosilane/distillation and Siemens deposition route for polysilicon.

Evidence: [WACKER-POLY-001](../42_references/bibliography.md#wacker-poly-001) — Chlorosilane/distillation and deposition hall sections (CLM-000003)

- Headquarters country: Not researched in Phase 1
- Manufacturing geography: Not mapped; no customer allocation inferred
- Scope notes: Scope is the cited company disclosure; no customer allocation, exclusivity, current operating capacity or Rubin qualification asserted.

| Edge | Directional relationship | Scope / condition |
|---|---|---|
| EDGE-0071 | [MAT-0006](#mat-0006) → SUPPLIED_BY → [SUP-0003](#sup-0003) | WACKER describes a chlorosilane/distillation and Siemens deposition route for polysilicon. Role example only; see claim boundary. (reviewed) |

<a id="sup-0004"></a>
## SUP-0004 — Hemlock Semiconductor

Type: `supplier` · Status: **reviewed** · [Article](../02_silicon_refining/electronic_grade_polysilicon.md)

Hemlock describes TCS-based CVD and controlled polysilicon sizing, cleaning and packaging.

Evidence: [HSC-POLY-001](../42_references/bibliography.md#hsc-poly-001) — What We Do: The Science of Polysilicon (CLM-000004)

- Headquarters country: Not researched in Phase 1
- Manufacturing geography: Not mapped; no customer allocation inferred
- Scope notes: Scope is the cited company disclosure; no customer allocation, exclusivity, current operating capacity or Rubin qualification asserted.

| Edge | Directional relationship | Scope / condition |
|---|---|---|
| EDGE-0072 | [MAT-0006](#mat-0006) → SUPPLIED_BY → [SUP-0004](#sup-0004) | Hemlock describes TCS-based CVD and controlled polysilicon sizing, cleaning and packaging. Role example only; see claim boundary. (reviewed) |

<a id="sup-0005"></a>
## SUP-0005 — PVA TePla

Type: `supplier` · Status: **reviewed** · [Article](../03_crystal_growth/crystal_growth.md)

PVA TePla describes CZ puller equipment and thermal and motion control functions.

Evidence: [PVA-CZ-001](../42_references/bibliography.md#pva-cz-001) — The Process; Czochralski systems (CLM-000006)

- Headquarters country: Not researched in Phase 1
- Manufacturing geography: Not mapped; no customer allocation inferred
- Scope notes: Scope is the cited company disclosure; no customer allocation, exclusivity, current operating capacity or Rubin qualification asserted.

| Edge | Directional relationship | Scope / condition |
|---|---|---|
| EDGE-0073 | [EQ-0004](#eq-0004) → SUPPLIED_BY → [SUP-0005](#sup-0005) | PVA TePla describes CZ puller equipment and thermal and motion control functions. Role example only; see claim boundary. (reviewed) |

<a id="sup-0006"></a>
## SUP-0006 — Siltronic

Type: `supplier` · Status: **reviewed** · [Article](../03_crystal_growth/crystal_growth.md)

Siltronic describes float-zone silicon products and their lower-oxygen and high-resistivity application context.

Evidence: [SILTRONIC-FZ-001](../42_references/bibliography.md#siltronic-fz-001) — Float zone/FZ subsection (CLM-000007)

- Headquarters country: Not researched in Phase 1
- Manufacturing geography: Not mapped; no customer allocation inferred
- Scope notes: Scope is the cited company disclosure; no customer allocation, exclusivity, current operating capacity or Rubin qualification asserted.

| Edge | Directional relationship | Scope / condition |
|---|---|---|
| EDGE-0074 | [MAT-0007](#mat-0007) → SUPPLIED_BY → [SUP-0006](#sup-0006) | Siltronic describes float-zone silicon products and their lower-oxygen and high-resistivity application context. Role example only; see claim boundary. (reviewed) |

<a id="sup-0007"></a>
## SUP-0007 — SUMCO

Type: `supplier` · Status: **reviewed** · [Article](../04_wafer_manufacturing/wafer_finishing_and_acceptance.md)

SUMCO describes wafer forming through slicing, lapping, etching, polishing, cleaning and inspection.

Evidence: [SUMCO-WAFER-001](../42_references/bibliography.md#sumco-wafer-001) — Wafer forming sequence (CLM-000008)

- Headquarters country: Not researched in Phase 1
- Manufacturing geography: Not mapped; no customer allocation inferred
- Scope notes: Scope is the cited company disclosure; no customer allocation, exclusivity, current operating capacity or Rubin qualification asserted.

| Edge | Directional relationship | Scope / condition |
|---|---|---|
| EDGE-0075 | [MAT-0010](#mat-0010) → SUPPLIED_BY → [SUP-0007](#sup-0007) | SUMCO describes wafer forming through slicing, lapping, etching, polishing, cleaning and inspection. Role example only; see claim boundary. (reviewed) |

<a id="char-0001"></a>
## CHAR-0001 — Carrier concentration

Type: `characteristic` · Status: **reviewed** · [Article](../05_semiconductor_physics/doping_and_transport.md)

Mobile carrier concentration in cm^-3 at stated temperature, doping and equilibrium conditions; distinct from total chemical impurity count.

Evidence: [HU-TRANSPORT-001](../42_references/bibliography.md#hu-transport-001) — Carrier transport and conductivity

| Edge | Directional relationship | Scope / condition |
|---|---|---|
| EDGE-0076 | [CHAR-0001](#char-0001) → AFFECTS → [CHAR-0002](#char-0002) | At stated mobility and low-field conditions; changing impurity scattering can also change mobility. (reviewed) |
| EDGE-0084 | [CHAR-0001](#char-0001) → CAN_CAUSE → [FAIL-0003](#fail-0003) | Only if the resulting resistivity crosses the specified bound; mobility and temperature must be accounted for. (reviewed) |

<a id="char-0002"></a>
## CHAR-0002 — Electrical resistivity

Type: `characteristic` · Status: **reviewed** · [Article](../05_semiconductor_physics/doping_and_transport.md)

Bulk resistivity in ohm cm under specified temperature and field; depends on carrier population and mobility.

Evidence: [HU-TRANSPORT-001](../42_references/bibliography.md#hu-transport-001) — Resistivity and conductivity

| Edge | Directional relationship | Scope / condition |
|---|---|---|
| EDGE-0076 | [CHAR-0001](#char-0001) → AFFECTS → [CHAR-0002](#char-0002) | At stated mobility and low-field conditions; changing impurity scattering can also change mobility. (reviewed) |

<a id="char-0003"></a>
## CHAR-0003 — Wafer geometry

Type: `characteristic` · Status: **reviewed** · [Article](../04_wafer_manufacturing/wafer_finishing_and_acceptance.md)

Thickness variation, bow and warp are distinct measured geometry quantities; length units and measurement support/reference conditions must accompany limits.

Evidence: [SEMI-TERMS-001](../42_references/bibliography.md#semi-terms-001) — Wafer geometry terminology; warp

| Edge | Directional relationship | Scope / condition |
|---|---|---|
| EDGE-0077 | [PROC-0009](#proc-0009) → MEASURES → [CHAR-0003](#char-0003) | Acceptance operation aggregates multiple metrology methods; laser scattering alone does not measure all geometry. (reviewed) |

<a id="fail-0001"></a>
## FAIL-0001 — Surface contamination outside specification

Type: `failure_mode` · Status: **reviewed** · [Article](../04_wafer_manufacturing/wafer_finishing_and_acceptance.md)

A particle or contamination measurement fails the defined wafer acceptance limit; detection sensitivity does not prove complete absence.

Evidence: [UCSB-INSPECT-001](../42_references/bibliography.md#ucsb-inspect-001) — Scattering-based surface inspection and limitations

| Edge | Directional relationship | Scope / condition |
|---|---|---|
| EDGE-0078 | [FAIL-0001](#fail-0001) → DETECTED_BY → [PROC-0009](#proc-0009) | Only detectable events within method sensitivity and inspection coverage. (reviewed) |
| EDGE-0080 | [FAIL-0001](#fail-0001) → AFFECTS → [METRIC-0001](#metric-0001) | A detected out-of-spec event excludes a wafer from accepted count under the chosen disposition policy. (reviewed) |

<a id="fail-0002"></a>
## FAIL-0002 — Geometry outside specification

Type: `failure_mode` · Status: **reviewed** · [Article](../04_wafer_manufacturing/wafer_finishing_and_acceptance.md)

Measured wafer geometry is outside its agreed specification; no universal numeric acceptance threshold is asserted.

Evidence: [SEMI-WAFER-001](../42_references/bibliography.md#semi-wafer-001) — Public scope and measurement categories

| Edge | Directional relationship | Scope / condition |
|---|---|---|
| EDGE-0079 | [FAIL-0002](#fail-0002) → DETECTED_BY → [PROC-0009](#proc-0009) | Appropriate geometry metrology and agreed specification required. (reviewed) |
| EDGE-0081 | [FAIL-0002](#fail-0002) → AFFECTS → [METRIC-0001](#metric-0001) | Only failures of the applicable specification reduce this boundary-specific accepted count. (reviewed) |

<a id="metric-0001"></a>
## METRIC-0001 — Accepted wafer fraction

Type: `metric` · Status: **reviewed** · [Article](../04_wafer_manufacturing/wafer_finishing_and_acceptance.md)

Accepted wafers divided by inspected wafers for a stated lot, specification and inspection boundary; dimensionless. Does not predict finished-die yield.

Evidence: [SUMCO-WAFER-001](../42_references/bibliography.md#sumco-wafer-001) — Cleaning and inspection; original boundary definition

| Edge | Directional relationship | Scope / condition |
|---|---|---|
| EDGE-0080 | [FAIL-0001](#fail-0001) → AFFECTS → [METRIC-0001](#metric-0001) | A detected out-of-spec event excludes a wafer from accepted count under the chosen disposition policy. (reviewed) |
| EDGE-0081 | [FAIL-0002](#fail-0002) → AFFECTS → [METRIC-0001](#metric-0001) | Only failures of the applicable specification reduce this boundary-specific accepted count. (reviewed) |
| EDGE-0082 | [PROC-0009](#proc-0009) → MEASURES → [METRIC-0001](#metric-0001) | Aggregate count after stated inspection coverage; no lot data supplied. (reviewed) |
| EDGE-0086 | [FAIL-0003](#fail-0003) → AFFECTS → [METRIC-0001](#metric-0001) | A detected failure of the applicable electrical specification changes accepted-wafer count under the chosen policy. (reviewed) |

<a id="metric-0002"></a>
## METRIC-0002 — Specific process energy

Type: `metric` · Status: **reviewed** · [Article](../02_silicon_refining/metallurgical_silicon.md)

Energy input in kWh divided by accepted silicon mass in kg for a stated process boundary and period; original accounting definition, no industrial benchmark.

Evidence: [NTNU-SMELTING-001](../42_references/bibliography.md#ntnu-smelting-001) — Electrical furnace input; original accounting definition

| Edge | Directional relationship | Scope / condition |
|---|---|---|
| EDGE-0083 | [PROC-0002](#proc-0002) → MEASURES → [METRIC-0002](#metric-0002) | Aggregated energy and accepted-mass accounting at the furnace boundary; original metric definition, no actual operating data supplied. (reviewed) |

<a id="fail-0003"></a>
## FAIL-0003 — Electrical resistivity outside specification

Type: `failure_mode` · Status: **reviewed** · [Article](../05_semiconductor_physics/doping_and_transport.md)

Bulk resistivity falls outside a selected acceptance range when carrier population or mobility changes under otherwise stated measurement conditions; no numerical limit supplied.

Evidence: [HU-TRANSPORT-001](../42_references/bibliography.md#hu-transport-001) — Conductivity and resistivity equations; original out-of-spec boundary definition

| Edge | Directional relationship | Scope / condition |
|---|---|---|
| EDGE-0084 | [CHAR-0001](#char-0001) → CAN_CAUSE → [FAIL-0003](#fail-0003) | Only if the resulting resistivity crosses the specified bound; mobility and temperature must be accounted for. (reviewed) |
| EDGE-0085 | [FAIL-0003](#fail-0003) → DETECTED_BY → [PROC-0009](#proc-0009) | Appropriate electrical metrology under specified conditions; not detection by surface laser scattering. (reviewed) |
| EDGE-0086 | [FAIL-0003](#fail-0003) → AFFECTS → [METRIC-0001](#metric-0001) | A detected failure of the applicable electrical specification changes accepted-wafer count under the chosen policy. (reviewed) |

<a id="fam-0100"></a>
## FAM-0100 — Fab unit processes

Type: `process_family` · Status: **reviewed** · [Article](../08_fab_overview/fab_flow.md)

Repeated film formation, patterning, removal, property modification and measurement functions; not one serial recipe.

Purpose: Repeated film formation, patterning, removal, property modification and measurement functions; not one serial recipe.

Scope: General unit-process function; input/output states and compatible materials are specified in owner article. No complete logic/DRAM integration asserted.

Mechanism: Repeated film formation, patterning, removal, property modification and measurement functions; not one serial recipe.

Notes: Repeated operations require separately qualified instances in real flows. Numerical examples are hypothetical; no Rubin or supplier adoption asserted.

Evidence: [HU-FAB-001](../42_references/bibliography.md#hu-fab-001) — Chapter 3, sections 3.1–3.7; representative process functions

| Edge | Directional relationship | Scope / condition |
|---|---|---|
| EDGE-0087 | [PROC-0101](#proc-0101) → PART_OF → [FAM-0100](#fam-0100) | General functional relationship; application requires material and integration qualification. (reviewed) |
| EDGE-0089 | [PROC-0102](#proc-0102) → PART_OF → [FAM-0100](#fam-0100) | General functional relationship; application requires material and integration qualification. (reviewed) |
| EDGE-0091 | [PROC-0103](#proc-0103) → PART_OF → [FAM-0100](#fam-0100) | General functional relationship; application requires material and integration qualification. (reviewed) |
| EDGE-0093 | [PROC-0104](#proc-0104) → PART_OF → [FAM-0100](#fam-0100) | General functional relationship; application requires material and integration qualification. (reviewed) |
| EDGE-0095 | [PROC-0105](#proc-0105) → PART_OF → [FAM-0100](#fam-0100) | General functional relationship; application requires material and integration qualification. (reviewed) |
| EDGE-0097 | [PROC-0106](#proc-0106) → PART_OF → [FAM-0100](#fam-0100) | General functional relationship; application requires material and integration qualification. (reviewed) |
| EDGE-0099 | [PROC-0107](#proc-0107) → PART_OF → [FAM-0100](#fam-0100) | General functional relationship; application requires material and integration qualification. (reviewed) |
| EDGE-0101 | [PROC-0108](#proc-0108) → PART_OF → [FAM-0100](#fam-0100) | General functional relationship; application requires material and integration qualification. (reviewed) |
| EDGE-0103 | [FAM-0100](#fam-0100) → ENABLES → [PROC-0030](#proc-0030) | Fab unit-process functions enable the fabrication portion of the planned aggregate logic path; test and die preparation remain later scope. (reviewed) |
| EDGE-0104 | [FAM-0100](#fam-0100) → ENABLES → [PROC-0031](#proc-0031) | Fab unit-process functions are applicable to device fabrication; DRAM-specific integration remains planned. (reviewed) |

<a id="proc-0101"></a>
## PROC-0101 — Resist patterning

Type: `operation` · Status: **reviewed** · [Article](../09_photolithography/lithography.md)

Create a developed resist pattern for a subsequent compatible transfer operation.

Purpose: Create a developed resist pattern for a subsequent compatible transfer operation.

Scope: General unit-process function; input/output states and compatible materials are specified in owner article. No complete logic/DRAM integration asserted.

Mechanism: Create a developed resist pattern for a subsequent compatible transfer operation.

Notes: Repeated operations require separately qualified instances in real flows. Numerical examples are hypothetical; no Rubin or supplier adoption asserted.

Evidence: [MACK-QUALITY-001](../42_references/bibliography.md#mack-quality-001) — Pattern-transfer and resist-property slides

| Edge | Directional relationship | Scope / condition |
|---|---|---|
| EDGE-0087 | [PROC-0101](#proc-0101) → PART_OF → [FAM-0100](#fam-0100) | General functional relationship; application requires material and integration qualification. (reviewed) |
| EDGE-0088 | [PROC-0101](#proc-0101) → USES_EQUIPMENT → [EQ-0101](#eq-0101) | General functional relationship; application requires material and integration qualification. (reviewed) |
| EDGE-0107 | [PROC-0101](#proc-0101) → CONSUMES → [MAT-0101](#mat-0101) | Illustrative positive-tone oxide pattern transfer only; no actual dimensions, qualified chemistry or universal device sequence implied. (reviewed) |
| EDGE-0108 | [PROC-0101](#proc-0101) → PRODUCES → [MAT-0102](#mat-0102) | Illustrative positive-tone oxide pattern transfer only; no actual dimensions, qualified chemistry or universal device sequence implied. (reviewed) |
| EDGE-0113 | [PROC-0105](#proc-0105) → PRECEDES → [PROC-0101](#proc-0101) | Illustrative positive-tone oxide pattern transfer only; no actual dimensions, qualified chemistry or universal device sequence implied. (reviewed) |
| EDGE-0114 | [PROC-0101](#proc-0101) → PRECEDES → [PROC-0103](#proc-0103) | Illustrative positive-tone oxide pattern transfer only; no actual dimensions, qualified chemistry or universal device sequence implied. (reviewed) |

<a id="eq-0101"></a>
## EQ-0101 — Coat/develop track and exposure tool

Type: `equipment` · Status: **reviewed** · [Article](../09_photolithography/lithography.md)

Prepare resist, expose an aligned image and develop a physical resist pattern.

Evidence: [MACK-QUALITY-001](../42_references/bibliography.md#mack-quality-001) — Pattern-transfer and resist-property slides

- Physical function: Prepare resist, expose an aligned image and develop a physical resist pattern.
- Control notes: Tool function only; process targets, models and supplier qualification not asserted.

| Edge | Directional relationship | Scope / condition |
|---|---|---|
| EDGE-0088 | [PROC-0101](#proc-0101) → USES_EQUIPMENT → [EQ-0101](#eq-0101) | General functional relationship; application requires material and integration qualification. (reviewed) |

<a id="proc-0102"></a>
## PROC-0102 — Film deposition

Type: `operation` · Status: **reviewed** · [Article](../10_deposition/deposition.md)

Add a film through a selected physical or chemical deposition mechanism.

Purpose: Add a film through a selected physical or chemical deposition mechanism.

Scope: General unit-process function; input/output states and compatible materials are specified in owner article. No complete logic/DRAM integration asserted.

Mechanism: Add a film through a selected physical or chemical deposition mechanism.

Notes: Repeated operations require separately qualified instances in real flows. Numerical examples are hypothetical; no Rubin or supplier adoption asserted.

Evidence: [ASM-ALD-001](../42_references/bibliography.md#asm-ald-001) — ALD process and thermal/plasma discussion

| Edge | Directional relationship | Scope / condition |
|---|---|---|
| EDGE-0089 | [PROC-0102](#proc-0102) → PART_OF → [FAM-0100](#fam-0100) | General functional relationship; application requires material and integration qualification. (reviewed) |
| EDGE-0090 | [PROC-0102](#proc-0102) → USES_EQUIPMENT → [EQ-0102](#eq-0102) | General functional relationship; application requires material and integration qualification. (reviewed) |

<a id="eq-0102"></a>
## EQ-0102 — Deposition reactor category

Type: `equipment` · Status: **reviewed** · [Article](../10_deposition/deposition.md)

Deliver film-forming species under controlled surface and chamber conditions; method-specific tools differ.

Evidence: [ASM-ALD-001](../42_references/bibliography.md#asm-ald-001) — ALD process and thermal/plasma discussion

- Physical function: Deliver film-forming species under controlled surface and chamber conditions; method-specific tools differ.
- Control notes: Tool function only; process targets, models and supplier qualification not asserted.

| Edge | Directional relationship | Scope / condition |
|---|---|---|
| EDGE-0090 | [PROC-0102](#proc-0102) → USES_EQUIPMENT → [EQ-0102](#eq-0102) | General functional relationship; application requires material and integration qualification. (reviewed) |

<a id="proc-0103"></a>
## PROC-0103 — Pattern transfer etch

Type: `operation` · Status: **reviewed** · [Article](../11_etching/etching.md)

Remove selected exposed material while retaining required masking and underlying structures.

Purpose: Remove selected exposed material while retaining required masking and underlying structures.

Scope: General unit-process function; input/output states and compatible materials are specified in owner article. No complete logic/DRAM integration asserted.

Mechanism: Remove selected exposed material while retaining required masking and underlying structures.

Notes: Repeated operations require separately qualified instances in real flows. Numerical examples are hypothetical; no Rubin or supplier adoption asserted.

Evidence: [LAM-ETCH-001](../42_references/bibliography.md#lam-etch-001) — Etch process overview and process categories

| Edge | Directional relationship | Scope / condition |
|---|---|---|
| EDGE-0091 | [PROC-0103](#proc-0103) → PART_OF → [FAM-0100](#fam-0100) | General functional relationship; application requires material and integration qualification. (reviewed) |
| EDGE-0092 | [PROC-0103](#proc-0103) → USES_EQUIPMENT → [EQ-0103](#eq-0103) | General functional relationship; application requires material and integration qualification. (reviewed) |
| EDGE-0109 | [PROC-0103](#proc-0103) → CONSUMES → [MAT-0102](#mat-0102) | Illustrative positive-tone oxide pattern transfer only; no actual dimensions, qualified chemistry or universal device sequence implied. (reviewed) |
| EDGE-0110 | [PROC-0103](#proc-0103) → PRODUCES → [MAT-0103](#mat-0103) | Illustrative positive-tone oxide pattern transfer only; no actual dimensions, qualified chemistry or universal device sequence implied. (reviewed) |
| EDGE-0114 | [PROC-0101](#proc-0101) → PRECEDES → [PROC-0103](#proc-0103) | Illustrative positive-tone oxide pattern transfer only; no actual dimensions, qualified chemistry or universal device sequence implied. (reviewed) |
| EDGE-0115 | [PROC-0103](#proc-0103) → PRECEDES → [PROC-0106](#proc-0106) | Illustrative positive-tone oxide pattern transfer only; no actual dimensions, qualified chemistry or universal device sequence implied. (reviewed) |

<a id="eq-0103"></a>
## EQ-0103 — Plasma etch chamber

Type: `equipment` · Status: **reviewed** · [Article](../11_etching/etching.md)

Supply reactive species and ion assistance, control wafer conditions and remove reaction products.

Evidence: [LAM-ETCH-001](../42_references/bibliography.md#lam-etch-001) — Etch process overview and process categories

- Physical function: Supply reactive species and ion assistance, control wafer conditions and remove reaction products.
- Control notes: Tool function only; process targets, models and supplier qualification not asserted.

| Edge | Directional relationship | Scope / condition |
|---|---|---|
| EDGE-0092 | [PROC-0103](#proc-0103) → USES_EQUIPMENT → [EQ-0103](#eq-0103) | General functional relationship; application requires material and integration qualification. (reviewed) |

<a id="proc-0104"></a>
## PROC-0104 — Implant and activation sequence

Type: `operation` · Status: **reviewed** · [Article](../12_doping/doping.md)

Deliver dopant ions and apply a separately qualified activation treatment.

Purpose: Deliver dopant ions and apply a separately qualified activation treatment.

Scope: General unit-process function; input/output states and compatible materials are specified in owner article. No complete logic/DRAM integration asserted.

Mechanism: Deliver dopant ions and apply a separately qualified activation treatment.

Notes: Repeated operations require separately qualified instances in real flows. Numerical examples are hypothetical; no Rubin or supplier adoption asserted.

Evidence: [MIT-IMPLANT-001](../42_references/bibliography.md#mit-implant-001) — Opening diffusion slides and implantation equipment slides

| Edge | Directional relationship | Scope / condition |
|---|---|---|
| EDGE-0093 | [PROC-0104](#proc-0104) → PART_OF → [FAM-0100](#fam-0100) | General functional relationship; application requires material and integration qualification. (reviewed) |
| EDGE-0094 | [PROC-0104](#proc-0104) → USES_EQUIPMENT → [EQ-0104](#eq-0104) | General functional relationship; application requires material and integration qualification. (reviewed) |

<a id="eq-0104"></a>
## EQ-0104 — Ion implanter and anneal tools

Type: `equipment` · Status: **reviewed** · [Article](../12_doping/doping.md)

Select and deliver ions; a separate thermal tool supplies the activation exposure.

Evidence: [MIT-IMPLANT-001](../42_references/bibliography.md#mit-implant-001) — Opening diffusion slides and implantation equipment slides

- Physical function: Select and deliver ions; a separate thermal tool supplies the activation exposure.
- Control notes: Tool function only; process targets, models and supplier qualification not asserted.

| Edge | Directional relationship | Scope / condition |
|---|---|---|
| EDGE-0094 | [PROC-0104](#proc-0104) → USES_EQUIPMENT → [EQ-0104](#eq-0104) | General functional relationship; application requires material and integration qualification. (reviewed) |

<a id="proc-0105"></a>
## PROC-0105 — Thermal oxidation

Type: `operation` · Status: **reviewed** · [Article](../13_oxidation/oxidation.md)

React oxidant with silicon to grow oxide while consuming underlying silicon.

Purpose: React oxidant with silicon to grow oxide while consuming underlying silicon.

Scope: General unit-process function; input/output states and compatible materials are specified in owner article. No complete logic/DRAM integration asserted.

Mechanism: React oxidant with silicon to grow oxide while consuming underlying silicon.

Notes: Repeated operations require separately qualified instances in real flows. Numerical examples are hypothetical; no Rubin or supplier adoption asserted.

Evidence: [UALBERTA-OXIDE-001](../42_references/bibliography.md#ualberta-oxide-001) — Introduction and calculation details

| Edge | Directional relationship | Scope / condition |
|---|---|---|
| EDGE-0095 | [PROC-0105](#proc-0105) → PART_OF → [FAM-0100](#fam-0100) | General functional relationship; application requires material and integration qualification. (reviewed) |
| EDGE-0096 | [PROC-0105](#proc-0105) → USES_EQUIPMENT → [EQ-0105](#eq-0105) | General functional relationship; application requires material and integration qualification. (reviewed) |
| EDGE-0105 | [PROC-0105](#proc-0105) → CONSUMES → [MAT-0010](#mat-0010) | Illustrative positive-tone oxide pattern transfer only; no actual dimensions, qualified chemistry or universal device sequence implied. (reviewed) |
| EDGE-0106 | [PROC-0105](#proc-0105) → PRODUCES → [MAT-0101](#mat-0101) | Illustrative positive-tone oxide pattern transfer only; no actual dimensions, qualified chemistry or universal device sequence implied. (reviewed) |
| EDGE-0113 | [PROC-0105](#proc-0105) → PRECEDES → [PROC-0101](#proc-0101) | Illustrative positive-tone oxide pattern transfer only; no actual dimensions, qualified chemistry or universal device sequence implied. (reviewed) |

<a id="eq-0105"></a>
## EQ-0105 — Oxidation reactor

Type: `equipment` · Status: **reviewed** · [Article](../13_oxidation/oxidation.md)

Control temperature, oxidant ambient and exposure time.

Evidence: [UALBERTA-OXIDE-001](../42_references/bibliography.md#ualberta-oxide-001) — Introduction and calculation details

- Physical function: Control temperature, oxidant ambient and exposure time.
- Control notes: Tool function only; process targets, models and supplier qualification not asserted.

| Edge | Directional relationship | Scope / condition |
|---|---|---|
| EDGE-0096 | [PROC-0105](#proc-0105) → USES_EQUIPMENT → [EQ-0105](#eq-0105) | General functional relationship; application requires material and integration qualification. (reviewed) |

<a id="proc-0106"></a>
## PROC-0106 — Resist strip and surface clean

Type: `operation` · Status: **reviewed** · [Article](../14_cleaning/cleaning.md)

Remove compatible masking/residual material and qualify the resulting surface for the next operation.

Purpose: Remove compatible masking/residual material and qualify the resulting surface for the next operation.

Scope: General unit-process function; input/output states and compatible materials are specified in owner article. No complete logic/DRAM integration asserted.

Mechanism: Remove compatible masking/residual material and qualify the resulting surface for the next operation.

Notes: Repeated operations require separately qualified instances in real flows. Numerical examples are hypothetical; no Rubin or supplier adoption asserted.

Evidence: [UBC-CLEAN-001](../42_references/bibliography.md#ubc-clean-001) — Overview, solvent clean and oxide-removal discussion

| Edge | Directional relationship | Scope / condition |
|---|---|---|
| EDGE-0097 | [PROC-0106](#proc-0106) → PART_OF → [FAM-0100](#fam-0100) | General functional relationship; application requires material and integration qualification. (reviewed) |
| EDGE-0098 | [PROC-0106](#proc-0106) → USES_EQUIPMENT → [EQ-0106](#eq-0106) | General functional relationship; application requires material and integration qualification. (reviewed) |
| EDGE-0111 | [PROC-0106](#proc-0106) → CONSUMES → [MAT-0103](#mat-0103) | Illustrative positive-tone oxide pattern transfer only; no actual dimensions, qualified chemistry or universal device sequence implied. (reviewed) |
| EDGE-0112 | [PROC-0106](#proc-0106) → PRODUCES → [MAT-0104](#mat-0104) | Illustrative positive-tone oxide pattern transfer only; no actual dimensions, qualified chemistry or universal device sequence implied. (reviewed) |
| EDGE-0115 | [PROC-0103](#proc-0103) → PRECEDES → [PROC-0106](#proc-0106) | Illustrative positive-tone oxide pattern transfer only; no actual dimensions, qualified chemistry or universal device sequence implied. (reviewed) |

<a id="eq-0106"></a>
## EQ-0106 — Compatible strip and clean tools

Type: `equipment` · Status: **reviewed** · [Article](../14_cleaning/cleaning.md)

Provide material-specific residue removal, rinse and drying functions.

Evidence: [UBC-CLEAN-001](../42_references/bibliography.md#ubc-clean-001) — Overview, solvent clean and oxide-removal discussion

- Physical function: Provide material-specific residue removal, rinse and drying functions.
- Control notes: Tool function only; process targets, models and supplier qualification not asserted.

| Edge | Directional relationship | Scope / condition |
|---|---|---|
| EDGE-0098 | [PROC-0106](#proc-0106) → USES_EQUIPMENT → [EQ-0106](#eq-0106) | General functional relationship; application requires material and integration qualification. (reviewed) |

<a id="proc-0107"></a>
## PROC-0107 — Chemical mechanical planarization

Type: `operation` · Status: **reviewed** · [Article](../15_cmp/cmp.md)

Remove overburden and reduce topography using coupled chemical and mechanical action.

Purpose: Remove overburden and reduce topography using coupled chemical and mechanical action.

Scope: General unit-process function; input/output states and compatible materials are specified in owner article. No complete logic/DRAM integration asserted.

Mechanism: Remove overburden and reduce topography using coupled chemical and mechanical action.

Notes: Repeated operations require separately qualified instances in real flows. Numerical examples are hypothetical; no Rubin or supplier adoption asserted.

Evidence: [AMAT-CMP-001](../42_references/bibliography.md#amat-cmp-001) — CMP mechanism and control description

| Edge | Directional relationship | Scope / condition |
|---|---|---|
| EDGE-0099 | [PROC-0107](#proc-0107) → PART_OF → [FAM-0100](#fam-0100) | General functional relationship; application requires material and integration qualification. (reviewed) |
| EDGE-0100 | [PROC-0107](#proc-0107) → USES_EQUIPMENT → [EQ-0107](#eq-0107) | General functional relationship; application requires material and integration qualification. (reviewed) |

<a id="eq-0107"></a>
## EQ-0107 — CMP and post-clean system

Type: `equipment` · Status: **reviewed** · [Article](../15_cmp/cmp.md)

Control pad/slurry contact and wafer loading; clean and dry the resulting surface.

Evidence: [AMAT-CMP-001](../42_references/bibliography.md#amat-cmp-001) — CMP mechanism and control description

- Physical function: Control pad/slurry contact and wafer loading; clean and dry the resulting surface.
- Control notes: Tool function only; process targets, models and supplier qualification not asserted.

| Edge | Directional relationship | Scope / condition |
|---|---|---|
| EDGE-0100 | [PROC-0107](#proc-0107) → USES_EQUIPMENT → [EQ-0107](#eq-0107) | General functional relationship; application requires material and integration qualification. (reviewed) |

<a id="proc-0108"></a>
## PROC-0108 — Metrology and inspection

Type: `operation` · Status: **reviewed** · [Article](../16_metrology_and_inspection/metrology.md)

Measure selected properties or inspect for defects under a defined sampling and decision plan.

Purpose: Measure selected properties or inspect for defects under a defined sampling and decision plan.

Scope: General unit-process function; input/output states and compatible materials are specified in owner article. No complete logic/DRAM integration asserted.

Mechanism: Measure selected properties or inspect for defects under a defined sampling and decision plan.

Notes: Repeated operations require separately qualified instances in real flows. Numerical examples are hypothetical; no Rubin or supplier adoption asserted.

Evidence: [ASML-METRO-001](../42_references/bibliography.md#asml-metro-001) — Optical and electron-beam metrology sections

| Edge | Directional relationship | Scope / condition |
|---|---|---|
| EDGE-0101 | [PROC-0108](#proc-0108) → PART_OF → [FAM-0100](#fam-0100) | General functional relationship; application requires material and integration qualification. (reviewed) |
| EDGE-0102 | [PROC-0108](#proc-0108) → USES_EQUIPMENT → [EQ-0108](#eq-0108) | General functional relationship; application requires material and integration qualification. (reviewed) |
| EDGE-0116 | [PROC-0108](#proc-0108) → MEASURES → [CHAR-0101](#char-0101) | General functional relationship; application requires material and integration qualification. (reviewed) |
| EDGE-0117 | [PROC-0108](#proc-0108) → MEASURES → [CHAR-0102](#char-0102) | General functional relationship; application requires material and integration qualification. (reviewed) |
| EDGE-0118 | [FAIL-0101](#fail-0101) → DETECTED_BY → [PROC-0108](#proc-0108) | Requires a method and sampling plan sensitive to the relevant local geometry; detection is not guaranteed. (reviewed) |
| EDGE-0119 | [FAIL-0102](#fail-0102) → DETECTED_BY → [PROC-0108](#proc-0108) | Requires a method and sampling plan sensitive to the relevant local geometry; detection is not guaranteed. (reviewed) |

<a id="eq-0108"></a>
## EQ-0108 — Optical/electron measurement tools

Type: `equipment` · Status: **reviewed** · [Article](../16_metrology_and_inspection/metrology.md)

Obtain pattern or defect information with method-specific sensitivity and sampling.

Evidence: [ASML-METRO-001](../42_references/bibliography.md#asml-metro-001) — Optical and electron-beam metrology sections

- Physical function: Obtain pattern or defect information with method-specific sensitivity and sampling.
- Control notes: Tool function only; process targets, models and supplier qualification not asserted.

| Edge | Directional relationship | Scope / condition |
|---|---|---|
| EDGE-0102 | [PROC-0108](#proc-0108) → USES_EQUIPMENT → [EQ-0108](#eq-0108) | General functional relationship; application requires material and integration qualification. (reviewed) |

<a id="mat-0101"></a>
## MAT-0101 — Thermal oxide on silicon

Type: `material` · Status: **reviewed** · [Article](../13_oxidation/oxidation.md)

Illustrative planar silicon wafer with a thermally grown oxide.

Evidence: [UALBERTA-OXIDE-001](../42_references/bibliography.md#ualberta-oxide-001) — Introduction and calculation details

- Composition or state: Illustrative planar silicon wafer with a thermally grown oxide.
- Qualification notes: Teaching-route state; compatible materials and thicknesses are intentionally unspecified.

| Edge | Directional relationship | Scope / condition |
|---|---|---|
| EDGE-0106 | [PROC-0105](#proc-0105) → PRODUCES → [MAT-0101](#mat-0101) | Illustrative positive-tone oxide pattern transfer only; no actual dimensions, qualified chemistry or universal device sequence implied. (reviewed) |
| EDGE-0107 | [PROC-0101](#proc-0101) → CONSUMES → [MAT-0101](#mat-0101) | Illustrative positive-tone oxide pattern transfer only; no actual dimensions, qualified chemistry or universal device sequence implied. (reviewed) |

<a id="mat-0102"></a>
## MAT-0102 — Resist-patterned oxide wafer

Type: `material` · Status: **reviewed** · [Article](../09_photolithography/lithography.md)

Illustrative developed resist openings above oxide on silicon.

Evidence: [MACK-QUALITY-001](../42_references/bibliography.md#mack-quality-001) — Pattern-transfer and resist-property slides

- Composition or state: Illustrative developed resist openings above oxide on silicon.
- Qualification notes: Teaching-route state; compatible materials and thicknesses are intentionally unspecified.

| Edge | Directional relationship | Scope / condition |
|---|---|---|
| EDGE-0108 | [PROC-0101](#proc-0101) → PRODUCES → [MAT-0102](#mat-0102) | Illustrative positive-tone oxide pattern transfer only; no actual dimensions, qualified chemistry or universal device sequence implied. (reviewed) |
| EDGE-0109 | [PROC-0103](#proc-0103) → CONSUMES → [MAT-0102](#mat-0102) | Illustrative positive-tone oxide pattern transfer only; no actual dimensions, qualified chemistry or universal device sequence implied. (reviewed) |

<a id="mat-0103"></a>
## MAT-0103 — Etched oxide with remaining resist

Type: `material` · Status: **reviewed** · [Article](../11_etching/etching.md)

Illustrative selectively removed oxide regions; masking resist remains for strip.

Evidence: [LAM-ETCH-001](../42_references/bibliography.md#lam-etch-001) — Etch process overview and process categories

- Composition or state: Illustrative selectively removed oxide regions; masking resist remains for strip.
- Qualification notes: Teaching-route state; compatible materials and thicknesses are intentionally unspecified.

| Edge | Directional relationship | Scope / condition |
|---|---|---|
| EDGE-0110 | [PROC-0103](#proc-0103) → PRODUCES → [MAT-0103](#mat-0103) | Illustrative positive-tone oxide pattern transfer only; no actual dimensions, qualified chemistry or universal device sequence implied. (reviewed) |
| EDGE-0111 | [PROC-0106](#proc-0106) → CONSUMES → [MAT-0103](#mat-0103) | Illustrative positive-tone oxide pattern transfer only; no actual dimensions, qualified chemistry or universal device sequence implied. (reviewed) |

<a id="mat-0104"></a>
## MAT-0104 — Patterned oxide after strip

Type: `material` · Status: **reviewed** · [Article](../14_cleaning/cleaning.md)

Illustrative patterned oxide/silicon surface after a compatible resist strip; no device functionality asserted.

Evidence: [UBC-CLEAN-001](../42_references/bibliography.md#ubc-clean-001) — Overview, solvent clean and oxide-removal discussion

- Composition or state: Illustrative patterned oxide/silicon surface after a compatible resist strip; no device functionality asserted.
- Qualification notes: Teaching-route state; compatible materials and thicknesses are intentionally unspecified.

| Edge | Directional relationship | Scope / condition |
|---|---|---|
| EDGE-0112 | [PROC-0106](#proc-0106) → PRODUCES → [MAT-0104](#mat-0104) | Illustrative positive-tone oxide pattern transfer only; no actual dimensions, qualified chemistry or universal device sequence implied. (reviewed) |

<a id="char-0101"></a>
## CHAR-0101 — Film thickness

Type: `characteristic` · Status: **reviewed** · [Article](../16_metrology_and_inspection/metrology.md)

Thickness measured with a specified method and interpretation model.

Evidence: [NIST-ELLIPSO-001](../42_references/bibliography.md#nist-ellipso-001) — Publication metadata and abstract only

| Edge | Directional relationship | Scope / condition |
|---|---|---|
| EDGE-0116 | [PROC-0108](#proc-0108) → MEASURES → [CHAR-0101](#char-0101) | General functional relationship; application requires material and integration qualification. (reviewed) |

<a id="char-0102"></a>
## CHAR-0102 — Pattern placement

Type: `characteristic` · Status: **reviewed** · [Article](../16_metrology_and_inspection/metrology.md)

Relative pattern placement assessed by an appropriate overlay measurement.

Evidence: [ASML-METRO-001](../42_references/bibliography.md#asml-metro-001) — Optical and electron-beam metrology sections

| Edge | Directional relationship | Scope / condition |
|---|---|---|
| EDGE-0117 | [PROC-0108](#proc-0108) → MEASURES → [CHAR-0102](#char-0102) | General functional relationship; application requires material and integration qualification. (reviewed) |

<a id="fail-0101"></a>
## FAIL-0101 — Local stochastic pattern failure

Type: `failure_mode` · Status: **reviewed** · [Article](../09_photolithography/lithography.md)

Local missing or bridging patterns can escape an average dimensional metric.

Evidence: [IMEC-STOCH-001](../42_references/bibliography.md#imec-stoch-001) — Stochastic failures and inspection discussion

| Edge | Directional relationship | Scope / condition |
|---|---|---|
| EDGE-0118 | [FAIL-0101](#fail-0101) → DETECTED_BY → [PROC-0108](#proc-0108) | Requires a method and sampling plan sensitive to the relevant local geometry; detection is not guaranteed. (reviewed) |

<a id="fail-0102"></a>
## FAIL-0102 — CMP dishing or erosion

Type: `failure_mode` · Status: **reviewed** · [Article](../15_cmp/cmp.md)

Pattern-dependent excessive removal can change local surface geometry.

Evidence: [MACK-CMP-001](../42_references/bibliography.md#mack-cmp-001) — Pages 1–2: topography, pressure/speed and dishing/erosion

| Edge | Directional relationship | Scope / condition |
|---|---|---|
| EDGE-0119 | [FAIL-0102](#fail-0102) → DETECTED_BY → [PROC-0108](#proc-0108) | Requires a method and sampling plan sensitive to the relevant local geometry; detection is not guaranteed. (reviewed) |
