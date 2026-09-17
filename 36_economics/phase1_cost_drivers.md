# Phase 1 operating and cost-driver evidence notes

Reviewed: 2026-09-16. Scope: engineering-derived questions for later cost models. No prices, margins, market shares or investment conclusions are supplied. Full economics remains Phase 10. The relationships below are qualitative inferences from the cited process mechanisms unless explicitly described as disclosures.

| Process boundary | Engineering fact | Cost-model implication to investigate | Missing data |
|---|---|---|---|
| Qualified feed leaving beneficiation | Grade and recovered mass are different measures | Compare cost per qualified tonne, including discarded material, instead of cost per mined tonne | Deposit assays, recovery, energy, logistics, contract specification |
| Accepted metallurgical silicon | Furnace uses electrical input and carbon chemistry | Account for electricity, reductants, accepted mass and recovery at the same boundary | Metered energy, off-gas treatment, feed prices, utilization, accepted output |
| Clean packaged polysilicon | Chemical purification, deposition and clean handling are separate operations | Model chemical recovery, thermal/electrical input and contamination-related loss separately | Actual recycle fractions, reactor uptime, consumables, purity qualification |
| Usable crystal | Growth controls shape, dopants and defect outcomes | Track usable crystal output after cropping and qualification, not gross pulled mass | Yield distribution, cycle time, crucible life, maintenance |
| Accepted wafer | Slicing consumes kerf; finishing and inspection add operations | Separate material loss, finishing consumables, inspection and rejected wafers | Lot-specific geometry, removal allowance, accepted count, throughput bottleneck |

Technical basis: [feedstock](../01_raw_materials/quartz_and_feedstocks.md), [furnace](../02_silicon_refining/metallurgical_silicon.md), [purification](../02_silicon_refining/electronic_grade_polysilicon.md), [growth](../03_crystal_growth/crystal_growth.md), [wafer finishing](../04_wafer_manufacturing/wafer_finishing_and_acceptance.md). Sources: [NTNU-SMELTING-001](../42_references/bibliography.md#ntnu-smelting-001), [WACKER-POLY-001](../42_references/bibliography.md#wacker-poly-001), [SUMCO-WAFER-001](../42_references/bibliography.md#sumco-wafer-001). These observations do not establish an industrial cost ratio.

## Definitions required before a numerical model

State the process boundary, accounting period, output unit, currency and price date, utilization, accepted-yield denominator, capacity bottleneck and treatment of rework/recovery. A tool's nominal cycle rate is not factory wafer-start capacity. No currency or production period applies to the present hypothetical arithmetic because it is energy/mass accounting only.

The furnace chapter's invented 1,000 kWh divided by 80 kg gives 12.5 kWh/kg; holding energy fixed while accepted output falls to 70 kg gives about 14.3 kWh/kg. This is arithmetic illustrating the denominator, not a measured furnace benchmark. The wafer chapter's kerf example similarly isolates material geometry and omits crop, grind, rejection and process-time losses.

## Yield boundary

Accepted wafer fraction means accepted wafer count divided by inspected wafer count for the same lot, inspection coverage and specification. An out-of-spec measured condition can lower that count under the chosen disposition policy. It does not reveal the origin of every defect or predict good-die yield after fabrication. [Wafer acceptance](../04_wafer_manufacturing/wafer_finishing_and_acceptance.md) and [map yield view](../manufacturing_map/yield_map.md).

## Open research for Phase 10

Obtain comparable energy boundaries, actual material recovery, uptime and utilization assumptions before estimating unit cost. Reconcile customer acceptance with the vendor's stated output unit. Supplier profitability, geography, concentration and customer dependence require separate dated evidence in the [industry-analysis module](../37_investment_analysis/README.md).
