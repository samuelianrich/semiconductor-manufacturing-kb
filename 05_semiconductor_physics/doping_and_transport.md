# Doping, carrier concentration, mobility and resistivity

Status: **Reviewed — author self-review; specialist review pending**. Owner: repository author. Article type: foundation explainer. Scope: general engineering; no proprietary process recipe. Source review: 2026-09-16.

## Prerequisites

Read [bonding, bands and carriers](bonding_bands_and_carriers.md). Know Ohm’s law and electric-field direction.

## Why this matters — 30-second explanation

**[Doping](../40_glossary/phase1_glossary.md#doping)** deliberately introduces atoms that alter the carrier population. Donors can supply conduction electrons; acceptors produce a hole-dominated material. Current also depends on how readily carriers move, described by **mobility**. A wafer's resistivity therefore depends on carrier concentrations and transport, not just a total impurity count. [MIT-CARRIERS-001](../42_references/bibliography.md#mit-carriers-001) [MIT-TRANSPORT-001](../42_references/bibliography.md#mit-transport-001)

## Intuition and mechanism

A phosphorus donor in silicon has an additional valence electron compared with the silicon atom it replaces. In the introductory ionized-donor picture, it leaves a mobile electron and a positive fixed dopant ion. A boron acceptor supports a hole and becomes a negatively charged ion when it accepts an electron. The donor or acceptor is not itself a particle drifting through the circuit. [MIT-CARRIERS-001](../42_references/bibliography.md#mit-carriers-001)

**N-type** means electrons are the majority mobile carriers; **P-type** means holes are the majority. Neither means the entire macroscopic sample necessarily has net negative or positive charge. Fixed ion charge and mobile charge balance in a neutral bulk region.

**[Compensation](../40_glossary/phase1_glossary.md#compensation)** occurs when donors and acceptors oppose each other's carrier contribution. A chemical assay counting both types is not the same measurement as the net carrier concentration.

## Equilibrium carrier relationships

For a nondegenerate semiconductor in thermal equilibrium, with complete ionization and a neutral bulk region:

$$
np=n_i^2,\qquad n+N_A=p+N_D.
$$

$N_D$ and $N_A$ are donor and acceptor concentrations in cm⁻³; $n,p,n_i$ use cm⁻³. Both sides of the first equation have units cm⁻⁶. Under these assumptions, when $N_D-N_A\gg n_i$, $n\approx N_D-N_A$ and $p\approx n_i^2/n$. These approximations should not be used blindly inside a depletion region, under strong injection or at temperatures where dopants freeze out. [HU-PHYSICS-001](../42_references/bibliography.md#hu-physics-001)

**Hypothetical example:** choose $N_D=1.2\times10^{16}$, $N_A=2.0\times10^{15}$ and $n_i=10^{10}$ cm⁻³. Then $n\approx10^{16}$ cm⁻³ and $p\approx10^4$ cm⁻³. The same sample contains substantial fixed positive and negative dopant charge even though its net mobile population is electron-dominated.

## Drift, diffusion and mobility

**Drift** is average carrier motion driven by an electric field. Electrons drift opposite the field, holes along it. Conventional current due to either carrier has the field's direction in the low-field conductivity model. **Diffusion** results from a carrier concentration gradient and can exist without an externally applied field. [MIT-TRANSPORT-001](../42_references/bibliography.md#mit-transport-001)

For low electric fields in a uniform region:

$$
\sigma=q(n\mu_n+p\mu_p),\qquad \rho=1/\sigma,\qquad J_{\mathrm{drift}}=\sigma E.
$$

Here $q\approx1.60\times10^{-19}$ C is the positive elementary-charge magnitude; $\mu_n,\mu_p$ are mobilities in cm²/(V·s); $\sigma$ is conductivity in S/cm; $\rho$ is resistivity in Ω·cm; $E$ is electric field in V/cm; and $J$ is current density in A/cm². This $\rho$ denotes resistivity, not electrostatic charge density.

The unit check is $C\times\mathrm{cm}^{-3}\times\mathrm{cm}^2/(V\,s)=A/(V\,\mathrm{cm})$, which is S/cm. Resistivity is a material property under specified conditions; the resistance of a particular uniform bar is $R=\rho L/A$, with length $L$ in cm, area $A$ in cm² and resistance $R$ in Ω. [HU-TRANSPORT-001](../42_references/bibliography.md#hu-transport-001)

For the carrier example above, assume $\mu_n=1{,}000$ cm²/(V·s) and negligible hole conductivity. Then $\sigma=1.60$ S/cm and $\rho=0.625$ Ω·cm. A hypothetical bar with $L=0.1$ cm and $A=0.01$ cm² has $R=6.25$ Ω. These chosen inputs are not an accepted wafer specification or a transistor-channel mobility.

## Manufacturing reality

Mobility depends on scattering, including interactions with the lattice and ionized impurities; adding dopants does not leave it constant at all concentrations. At high fields, the simple proportional relation between drift velocity and field also needs refinement. [MIT-TRANSPORT-001](../42_references/bibliography.md#mit-transport-001) [HU-TRANSPORT-001](../42_references/bibliography.md#hu-transport-001)

During [crystal growth](../03_crystal_growth/crystal_growth.md), doping establishes starting-material properties. Later [implantation and activation](../12_doping/README.md) establish spatial device regions. Total introduced dopant and electrically active dopant are different concepts. **[Activation](../40_glossary/phase1_glossary.md#activation)** means achieving the intended electrically active incorporation, not merely detecting the chemical element. Detailed activation recipes remain in the later fab phase. [HU-FAB-001](../42_references/bibliography.md#hu-fab-001)

Failure or variation can therefore involve the wrong species, wrong spatial concentration, incomplete activation, unwanted compensation or altered transport. Resistivity helps characterize the electrical result, while a chemical measurement answers a different question. This distinction underpins the wafer [acceptance](../04_wafer_manufacturing/wafer_finishing_and_acceptance.md) boundary.

## Checks for understanding

Why is an n-type wafer usually neutral overall? Why can two samples with the same net carrier density have different mobilities? Which approximation fails first if the measurement is taken inside a junction depletion region? Explain why the assumed mobility in the worked example must not be applied unchanged to every GPU transistor.

## Position in the manufacturing map

[PROC-0006](../manufacturing_map/process_nodes.md#proc-0006), [MAT-0010](../manufacturing_map/process_nodes.md#mat-0010). These are process/material categories, not a tracked customer lot. Concept pages link to the operations they explain rather than inventing a physical manufacturing step.

## Rubin connection and evidence boundary

No mine, feedstock supplier, wafer specification, process recipe or transistor implementation is assigned to Rubin here. The [case-study plan](../38_case_studies/nvidia_rubin/README.md) and [Rubin map](../manufacturing_map/rubin_manufacturing_path.md) preserve that boundary. Company examples in these chapters are documented roles, not a Rubin bill of materials.

## Separate economics and further learning

Process cost drivers are recorded in the [Phase 1 evidence notes](../36_economics/phase1_cost_drivers.md); full [industry analysis](../37_investment_analysis/README.md) remains a later phase. Use the [glossary](../40_glossary/phase1_glossary.md) for definitions and the [learning sequence](../LEARNING_PATHS.md) for navigation.

## Sources and review

- [HU-FAB-001](../42_references/bibliography.md#hu-fab-001)

- [MIT-CARRIERS-001](../42_references/bibliography.md#mit-carriers-001)
- [MIT-TRANSPORT-001](../42_references/bibliography.md#mit-transport-001)
- [HU-PHYSICS-001](../42_references/bibliography.md#hu-physics-001)
- [HU-TRANSPORT-001](../42_references/bibliography.md#hu-transport-001)

Source locators and limitations are in the canonical bibliography. Review scope: original synthesis, scoped mathematical examples and conceptual figures. Independent specialist review has not been performed. Final module review is recorded in [AUDIT_PHASE1.md](../AUDIT_PHASE1.md).
