# Phase 1 comparisons

Reviewed: 2026-09-16, author self-review. These tables compare mechanisms and qualification boundaries; they do not rank suppliers or substitute for customer specifications.

## Silicon forms are different qualification problems

| Form | Main distinction | What purity alone does not establish | Owner |
|---|---|---|---|
| Silica/quartz feed | Silicon remains chemically bonded to oxygen | Thermal behavior, texture or furnace suitability | [Feedstocks](../01_raw_materials/quartz_and_feedstocks.md) |
| Metallurgical silicon | Oxygen removed through furnace reduction | Electronic impurity limits | [Smelting](../02_silicon_refining/metallurgical_silicon.md) |
| Electronic polysilicon | Chemically purified silicon with many grains | Wafer geometry or a single crystal | [Purification](../02_silicon_refining/electronic_grade_polysilicon.md) |
| Single-crystal ingot | Continuous oriented crystal | Finished wafer surface or final device yield | [Growth](../03_crystal_growth/crystal_growth.md) |
| Accepted wafer | Material, geometry and surface evaluated against a specification | Defect-free finished circuitry | [Wafer acceptance](../04_wafer_manufacturing/wafer_finishing_and_acceptance.md) |

Sources: [USGS-SILICON-001](../42_references/bibliography.md#usgs-silicon-001), [WACKER-POLY-001](../42_references/bibliography.md#wacker-poly-001), [SUMCO-WAFER-001](../42_references/bibliography.md#sumco-wafer-001). Qualification distinctions are the chapter synthesis.

## Growth methods

| Dimension | Czochralski | Float zone |
|---|---|---|
| Melt containment | Contained bulk melt | Traveling localized molten zone |
| Crystal initiation | Oriented seed | Oriented seed |
| Quartz contact | Quartz crucible contacts melt | No contacting melt crucible |
| Oxygen consideration | Crucible/melt interaction must be controlled | Lower-oxygen material is a disclosed product characteristic |
| Application choice | Select diameter, doping, defects and electrical specification together | Select diameter, doping, defects and electrical specification together |
| Comparison limit | No universal best method; actual qualification and geometry matter | Feed-rod preparation and product-specific constraints matter |

Sources: [PVA-CZ-001](../42_references/bibliography.md#pva-cz-001), [KIEL-GROWTH-001](../42_references/bibliography.md#kiel-growth-001), [SILTRONIC-FZ-001](../42_references/bibliography.md#siltronic-fz-001). Siltronic-specific role is **CONFIRMED as a company disclosure**, CLM-000007, reviewed 2026-09-16; no market-wide or Rubin implication.

## Measurements that should not be substituted for one another

| Measurement | Quantity | Required context | Cannot by itself establish |
|---|---|---|---|
| Chemical assay | Element/species concentration | Sampling, detection limit, mass versus atomic basis | Electrically active dopant concentration |
| Resistivity | Electrical transport property, Ω·cm | Temperature, measurement method, mobility and spatial variation | Total concentration of all impurities |
| TTV | Thickness range | Measurement area and edge exclusion | Wafer bow or warp |
| Bow/warp | Median-surface shape | Reference plane and support conditions | Microscopic surface roughness |
| Roughness | Small-scale topography | Statistic and spatial bandwidth | Global flatness |
| Surface scattering | Detected optical events | Sensitivity, calibration and classification | Identity of every particle or bulk-defect absence |

Sources: [HU-TRANSPORT-001](../42_references/bibliography.md#hu-transport-001), [SEMI-TERMS-001](../42_references/bibliography.md#semi-terms-001), [SEMI-WAFER-001](../42_references/bibliography.md#semi-wafer-001), [UCSB-INSPECT-001](../42_references/bibliography.md#ucsb-inspect-001). Full normative wafer acceptance limits were not accessed.

## Transistor geometry vocabulary

Planar describes control from above a surface channel. A FinFET adds gate control along exposed fin sides. GAA describes surrounding control; nanosheets are one GAA channel shape. These are geometric descriptions, not a one-to-one mapping to marketed process-node names or Rubin variants. See [the original geometry figure and explanation](../06_transistor_fundamentals/cmos_and_transistor_evolution.md), [HU-SCALING-001](../42_references/bibliography.md#hu-scaling-001), and the historical IBM disclosure [IBM-NANOSHEET-001](../42_references/bibliography.md#ibm-nanosheet-001), CLM-000009.
