# Learning sequence

Directory numbers are addresses, not mandatory reading order. Follow prerequisite links within each module. The complete technical scope is in the [inventory](catalog/topic_inventory.md).

## Main undergraduate path

| Stage | Modules | Reader outcome / comprehension check |
|---|---|---|
| Orientation | 00; glossary as needed | Distinguish wafer, die, memory stack, package, module and rack |
| Earth to wafer | 01 → 02 → 03 → 04 | Trace changes in purity, crystallinity, geometry and surface quality |
| Device foundations | 05 → 06, alongside the material path | Explain doping, a junction, inversion and a CMOS switching function |
| Fab vocabulary | 08 | Distinguish unit processes from an integrated flow |
| Unit processes | 09, 10, 13, 14; then 11, 12, 15, 16 | Explain pattern, add, remove, modify, planarize and measure |
| Device and wiring integration | 17, 18 → 19 | Follow a cross section from isolated transistors to wired circuits |
| Design interface | 07 | Explain why layout needs a PDK, verification and masks |
| Good-die evidence | 21 → 20 → 22 | Distinguish defect yield, electrical test coverage, binning and handling loss |
| Memory branch | 23 → 24 | Trace a DRAM cell through fabrication into a tested HBM stack |
| Package convergence | 26 and 25 → 29 | Explain integration of logic, memory, interposer and substrate |
| Power and heat | 27 and 28 | Follow electrical power in and heat out across scales |
| Deployed system | 30 → 31 → 32 | Trace package-to-module-to-server-to-rack assembly and test |
| Industrial map | 33, 34 → 35 | Distinguish material suppliers, tool suppliers, designers and manufacturers |
| Economic layer | 36 → 37 | Analyze good-unit cost, capacity and value capture without recommendations |
| Product reconstruction | 38 | Separate documented Rubin details from inference and unknowns |

The board stage requires both power and thermal understanding. Historical modules are optional sidebars read after the relevant technical concepts, even though their index is available from the beginning.

## Focused paths

- **Logic manufacturing:** 05 → 06 → 08 → unit processes → 17 → 18 → 19 → 21 → 20. Add 01–04 for starting-material context.
- **Memory and packaging:** foundations and unit processes → 23 → 20/22 → 24 → 25/26 → 29. General TSV/bonding primers should be linked at first use, then the memory page explains its application.
- **Equipment research:** read the corresponding process before its equipment-category profile; then 33 → 35 → 36 → 37.
- **Economic research:** engineering at the segment of interest → yield/test assumptions → 36 cost boundary → 37 industry structure. Do not start from a vendor moat claim and retrofit the science.
- **Rubin reader:** begin with the known/unknown register, then follow each supported implementation claim back to its general technical explanation. A missing disclosure is a learning boundary, not permission to invent a recipe.

## Phase 1 reading path

1. [Quartz, silica and qualified furnace feedstock](01_raw_materials/quartz_and_feedstocks.md)
2. [Metallurgical silicon: removing oxygen from silica](02_silicon_refining/metallurgical_silicon.md)
3. [Electronic-grade polysilicon: purification through chemistry](02_silicon_refining/electronic_grade_polysilicon.md)
4. [Single-crystal growth: giving silicon a continuous lattice](03_crystal_growth/crystal_growth.md)
5. [From ingot to accepted wafer: geometry, surface and qualification](04_wafer_manufacturing/wafer_finishing_and_acceptance.md)
6. [Bonding, energy bands, electrons and holes](05_semiconductor_physics/bonding_bands_and_carriers.md)
7. [Doping, carrier concentration, mobility and resistivity](05_semiconductor_physics/doping_and_transport.md)
8. [PN junctions: diffusion creates an internal electric field](05_semiconductor_physics/pn_junctions.md)
9. [From MOS capacitor to transistor: controlling a channel with a field](06_transistor_fundamentals/mos_capacitor_and_mosfet.md)
10. [CMOS logic and the move from planar gates to fins and nanosheets](06_transistor_fundamentals/cmos_and_transistor_evolution.md)

Read the carrier/doping primer just in time when crystal growth introduces resistivity. The full physics sequence then develops the models systematically. Both the wafer path and MOSFET path are prerequisites for Phase 2. [Glossary](40_glossary/phase1_glossary.md) · [Comparisons](41_reference_tables/phase1_comparisons.md).

## Phase 2 reading path

1. [Inside a fab: repeated operations and controlled interfaces](08_fab_overview/fab_flow.md)
2. [Photolithography: from optical image to usable resist pattern](09_photolithography/lithography.md)
3. [Deposition: choosing how a film reaches the surface](10_deposition/deposition.md)
4. [Etching: selective removal with a controlled profile](11_etching/etching.md)
5. [Doping and activation: placing atoms is only half the task](12_doping/doping.md)
6. [Thermal oxidation: growing oxide by consuming silicon](13_oxidation/oxidation.md)
7. [Cleaning: controlling contamination without damaging the stack](14_cleaning/cleaning.md)
8. [CMP: removing overburden while preserving useful structures](15_cmp/cmp.md)
9. [Metrology and inspection: evidence for process decisions](16_metrology_and_inspection/metrology.md)

Use the [unit-process map guide](manufacturing_map/phase2_unit_processes.md) to distinguish learning order from physical wafer flow. Continue to Phase 3 only after the film, pattern-transfer and measurement interfaces are clear.

## Phase 3 reading path

1. [Planar and FinFET integration: making a controllable channel](17_transistor_fabrication/planar_and_finfet.md)
2. [Nanosheet integration: release the channels, then surround them](17_transistor_fabrication/nanosheet_integration.md)
3. [Contacts and MOL: connecting the device without losing its advantage](17_transistor_fabrication/contacts_and_mol.md)
4. [Interconnect physics: geometry, resistance, capacitance and delay](18_interconnects/wire_rc.md)
5. [Wiring materials and reliability: qualify the whole stack](18_interconnects/materials_and_reliability.md)
6. [BEOL integration: building and protecting the multilevel wiring stack](19_back_end_of_line/beol_integration.md)

The [integration-map guide](manufacturing_map/phase3_integration.md) shows physical-state boundaries and alternatives. Next is Phase 4: design, PDKs, signoff and masks.
