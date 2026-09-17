# Fab-process comparisons

These are mechanism comparisons, not vendor rankings. Follow each owner chapter for source locators and conditions.

| Choice | Select when the interface needs… | Constraint to verify | Owner |
|---|---|---|---|
| DUV / EUV | A qualified imaging approach for the pattern | Wavelength alone does not determine usable resolution, overlay or defects | [Lithography](../09_photolithography/lithography.md) |
| CVD / ALD / sputter PVD | Reaction-based growth / saturating cycles / target-derived material | Thermal budget, coverage, nucleation, composition, throughput | [Deposition](../10_deposition/deposition.md) |
| Epitaxy / non-epitaxial film | Crystalline registry / a film without that registry requirement | Underlying surface, defects and material compatibility | [Deposition](../10_deposition/deposition.md) |
| Wet etch / RIE / Bosch DRIE / ALE | Compatible liquid removal / ion-assisted profile / deep cyclic etch / incremental control | Selectivity, damage, geometry and transport | [Etching](../11_etching/etching.md) |
| Implant / diffusion / in-situ doping | Ion delivery / thermal redistribution / incorporation during growth | Masking, profile, damage, activation and later heating | [Doping](../12_doping/doping.md) |
| Thermal oxide / deposited oxide | Silicon-consuming growth / supplied film material | Substrate compatibility, interface properties and temperature | [Oxidation](../13_oxidation/oxidation.md) |
| Wet clean / plasma strip | Compatible contaminant dissolution / reactive residue removal | Desired film loss, termination and feature damage | [Cleaning](../14_cleaning/cleaning.md) |
| CMP / etchback | Coupled polishing / material removal through etching | Global versus local topography and remaining-film requirements | [CMP](../15_cmp/cmp.md) |
| Optical / electron / surface spectroscopy | Pattern or film inference / imaging / chemical-state information | Sensitivity, model, area, sampling and measurement impact | [Metrology](../16_metrology_and_inspection/metrology.md) |

A method name does not specify a production recipe. Different variants of one method may outperform one another under different acceptance criteria.
