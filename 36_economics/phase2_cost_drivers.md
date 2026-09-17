# Phase 2 process cost drivers — evidence notes

These are engineering dependencies for a later economic model. No prices, market shares, supplier margins or investment conclusions are estimated.

| Process | Driver to measure later | Engineering reason | Canonical evidence |
|---|---|---|---|
| Fab routing | Bottleneck capacity, availability, queue time, rework | Tool rate differs from route cycle time and qualified output | [Fab interfaces](../08_fab_overview/fab_flow.md) |
| Lithography | Exposure time, patterning steps, inspection and rework | Dose, overlay and stochastic acceptance interact | [Lithography](../09_photolithography/lithography.md) |
| Deposition | Cycles, precursor use, thermal exposure and chamber conditioning | Coverage and nucleation constrain useful film formation | [Deposition](../10_deposition/deposition.md) |
| Etch | Etch time, mask budget and chamber condition | Selectivity and profile constrain faster removal | [Etching](../11_etching/etching.md) |
| Implant/thermal | Qualified beam delivery and activation exposure | Dose throughput is distinct from usable activation | [Doping](../12_doping/doping.md) |
| Oxidation/clean | Qualified thermal and surface-preparation capacity | Interface acceptance cannot be replaced by elapsed time | [Oxidation](../13_oxidation/oxidation.md), [cleaning](../14_cleaning/cleaning.md) |
| CMP | Pad/slurry use, endpoint, cleaning and yield impact | Overburden removal competes with local damage constraints | [CMP](../15_cmp/cmp.md) |
| Measurement | Sample count, measurement time and missed-defect exposure | More coverage costs capacity; less coverage weakens evidence | [Metrology](../16_metrology_and_inspection/metrology.md) |

Phase 10 should attach measured data, a common output denominator and uncertainty before comparing cost. An engineering tradeoff is not evidence of a company's value capture; that analysis remains in [investment analysis](../37_investment_analysis/README.md).
