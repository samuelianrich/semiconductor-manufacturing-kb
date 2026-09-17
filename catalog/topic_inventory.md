# Complete planned topic inventory

This inventory defines scope, not completion. Module-level prerequisites are machine-readable in [modules.json](modules.json). Topic-level prerequisites will be added before each article is drafted.

## M00 — [Orientation and physical chain](../00_overview/README.md)

Build phase 0.

- Reading paths
- physical material flow
- wafer versus die versus package versus system
- logic and memory branch
- confidence and scope

## M01 — [Raw materials](../01_raw_materials/README.md)

Build phase 1.

- Silicon abundance and geological deposits
- quartz and silica
- mining, crushing and beneficiation
- purity specifications
- carbon reductants and feedstock qualification

## M02 — [Silicon refining](../02_silicon_refining/README.md)

Build phase 1.

- Metallurgical silicon
- submerged arc furnace
- carbon reduction chemistry and energy
- chlorosilanes and trichlorosilane
- distillation
- Siemens process
- alternative reactors
- impurity budgets and electronic-grade qualification

## M03 — [Single-crystal growth](../03_crystal_growth/README.md)

Build phase 1.

- Crystal lattice and polycrystal versus single crystal
- seeds and orientation
- Czochralski puller
- float-zone growth
- dopant introduction
- oxygen and defects
- boule resistivity

## M04 — [Wafer manufacturing](../04_wafer_manufacturing/README.md)

Build phase 1.

- Crop, grind and orient
- slicing and edge grinding
- lapping and etching
- polishing and cleaning
- wafer inspection
- diameter, thickness, flatness and roughness
- edge exclusion
- epitaxial and SOI starting-wafer alternatives

## M05 — [Semiconductor physics](../05_semiconductor_physics/README.md)

Build phase 1.

- Atomic bonding and energy bands
- band gap and carriers
- intrinsic and extrinsic silicon
- donors and acceptors
- carrier concentration, mobility and conductivity
- electric fields
- PN junction and depletion
- MOS capacitor and inversion

## M06 — [MOSFETs and transistor evolution](../06_transistor_fundamentals/README.md)

Build phase 1.

- Field effect
- threshold voltage and switching
- planar MOSFET
- short-channel effects
- FinFET
- gate-all-around and nanosheets
- gate and parasitic capacitance
- drive current, leakage and power density
- CMOS logic bridge

## M07 — [Design to tapeout](../07_ic_design_and_tapeout/README.md)

Build phase 4.

- Architecture and microarchitecture
- RTL and simulation
- verification
- synthesis and standard cells
- place and route
- timing closure and power
- DRC and LVS
- PDK and design rules
- process-node terminology
- reticle limits and DTCO
- tapeout, mask data preparation and mask generation

## M08 — [Fab overview](../08_fab_overview/README.md)

Build phase 2.

- FEOL, middle-of-line and BEOL boundaries
- repeated unit-process loops
- wafer lots and carriers
- masks and recipes
- contamination zoning
- process integration
- cycle time versus tool throughput

## M09 — [Photolithography](../09_photolithography/README.md)

Build phase 2.

- Adhesion and resist coat
- soft bake, alignment, exposure and post-exposure bake
- development and inspection
- KrF, ArF and immersion
- EUV tin plasma, vacuum and mirrors
- Bragg reflection
- masks and pellicles
- resist chemistry and stochastic defects
- numerical aperture, resolution and depth of focus
- overlay, CD and CDU
- OPC and multiple patterning
- High-NA only as needed for current concepts

## M10 — [Deposition](../10_deposition/README.md)

Build phase 2.

- CVD
- PECVD
- LPCVD
- ALD
- PVD and sputtering
- epitaxy
- conformality and step coverage
- nucleation, stress and particles
- thermal oxidation comparison with a link to its canonical owner

## M11 — [Etching](../11_etching/README.md)

Build phase 2.

- Wet etch
- dry plasma etch
- RIE
- DRIE
- atomic-layer etch
- selectivity and anisotropy
- aspect ratio and profiles
- plasma chemistry
- loading and damage

## M12 — [Doping and activation](../12_doping/README.md)

Build phase 2.

- Diffusion
- ion implantation
- masks
- energy and dose
- channeling
- annealing and rapid thermal processing
- activation versus chemical concentration
- junction depth

## M13 — [Thermal oxidation](../13_oxidation/README.md)

Build phase 2.

- Oxide growth versus deposition
- silicon consumption
- dry and wet oxidation
- temperature and kinetics
- oxide quality and interfaces
- thermal budget

## M14 — [Cleaning and contamination control](../14_cleaning/README.md)

Build phase 2.

- Cleanrooms and particles
- metallic and organic contamination
- ultrapure water
- RCA cleaning
- solvents
- plasma cleaning
- surface termination
- material compatibility and damage

## M15 — [Chemical mechanical planarization](../15_cmp/README.md)

Build phase 2.

- Slurries, abrasives and reactions
- pads and conditioning
- removal rate and uniformity
- endpoint
- dishing, erosion and scratches
- multilayer planarity

## M16 — [Metrology and process control](../16_metrology_and_inspection/README.md)

Build phase 2.

- Optical and electron-beam inspection
- CD-SEM
- overlay
- ellipsometry
- profilometry
- thickness and composition
- sampling
- SPC, control charts and process windows
- excursions and fault detection

## M17 — [Transistor process integration](../17_transistor_fabrication/README.md)

Build phase 3.

- Isolation and wells
- planar integration
- FinFET integration
- GAA nanosheet integration
- gate stacks and spacers
- source/drain engineering
- contacts and middle-of-line boundary
- thermal-budget and variability tradeoffs

## M18 — [Interconnect structures and physics](../18_interconnects/README.md)

Build phase 3.

- Contacts and vias
- local and global wiring
- resistance, capacitance and RC delay
- copper, tungsten, cobalt and ruthenium roles
- barriers and liners
- low-k dielectrics
- electromigration and reliability

## M19 — [BEOL process integration](../19_back_end_of_line/README.md)

Build phase 3.

- Dielectric, pattern, etch, barrier, fill and CMP loop
- damascene and alternatives
- multilevel routing cross sections
- passivation and terminal metallization
- integration defects and thermal budgets

## M20 — [Wafer electrical test](../20_wafer_test/README.md)

Build phase 5.

- Wafer probing
- probe cards and automatic test equipment
- wafer maps
- functional and parametric tests
- test coverage and escapes
- binning
- known-good-die qualification

## M21 — [Yield engineering](../21_yield_engineering/README.md)

Build phase 5.

- Random and systematic defects
- defect density
- functional and parametric yield
- wafer and die yield denominators
- Poisson model and limitations
- area and cost
- redundancy, repair and salvage
- reliability versus yield

## M22 — [Dicing and die preparation](../22_dicing_and_die_prep/README.md)

Build phase 5.

- Temporary bonding and debonding
- backgrinding and thinning
- dicing alternatives
- inspection and traceability
- thin-die fracture and handling
- sequence differences for TSV processes

## M23 — [DRAM fundamentals and fabrication](../23_dram_fundamentals/README.md)

Build phase 6.

- One-transistor one-capacitor cell
- wordline and bitline
- sensing and refresh
- arrays and repair
- high-aspect-ratio capacitor fabrication
- DRAM process integration and testing

## M24 — [HBM manufacturing](../24_hbm_manufacturing/README.md)

Build phase 6.

- DRAM die and base/logic die roles
- TSV fabrication and reveal
- thinning and insulation
- microbump stacking
- hybrid bonding where applicable
- stack assembly and testing
- known-good-die
- bandwidth mathematics
- thermal limits

## M25 — [Advanced packaging](../25_advanced_packaging/README.md)

Build phase 7.

- Flip chip
- 2.5D and 3D integration
- fan-out
- chiplets as partitioning
- silicon and organic interposers
- bridges
- TSVs
- hybrid bonding
- bumps, copper pillars and RDL
- alignment
- underfill and molding
- warpage and stress
- CoWoS and comparable families
- compound yield and test

## M26 — [Package substrates](../26_substrates/README.md)

Build phase 7.

- ABF dielectric and build-up substrate
- laminate materials
- copper routing
- vias and microvias
- fabrication and qualification
- signal and power integrity
- warpage
- substrate capacity bottlenecks

## M27 — [Thermal management](../27_thermal_management/README.md)

Build phase 8.

- Heat generation and spreading
- thermal resistance and junction temperature
- interface materials
- heat sinks and vapor chambers
- cold plates and liquid cooling
- die-to-rack thermal path
- flow and facility heat rejection boundaries

## M28 — [Power delivery](../28_power_delivery/README.md)

Build phase 8.

- Facility-to-silicon power path
- supplies and regulation
- board planes and package impedance
- IR drop and current density
- transient droop and decoupling
- power loss and conversion efficiency

## M29 — [GPU package assembly and qualification](../29_gpu_package/README.md)

Build phase 8.

- Logic plus HBM assembly
- package assembly flow and exploded view
- final package test
- burn-in where applicable
- reliability qualification and failure analysis
- mechanical and electrical interfaces

## M30 — [PCB and accelerator module](../30_pcb_and_module/README.md)

Build phase 8.

- PCB fabrication, stackup and routing
- surface mount assembly
- module connectors
- signal integrity and power integrity
- board testing
- networking and high-speed links

## M31 — [Server integration](../31_system_integration/README.md)

Build phase 8.

- CPU and accelerator coordination
- memory and networking interfaces
- server assembly and validation
- firmware boundary
- cooling and power integration
- serviceability and system acceptance

## M32 — [Rack-scale systems](../32_rack_scale_system/README.md)

Build phase 8.

- Rack interconnects and switching
- scale-up versus scale-out
- power distribution
- cooling distribution and facility interfaces
- rack assembly, test and deployment
- manufacturing constraints propagated into architecture

## M33 — [Equipment ecosystem](../33_equipment_ecosystem/README.md)

Build phase 9.

- Lithography
- deposition
- etch
- implantation
- oxidation and thermal processing
- CMP
- cleaning
- inspection
- metrology
- wafer handling
- wafer test
- thinning and dicing
- bonding
- packaging
- final test

## M34 — [Materials ecosystem](../34_materials_ecosystem/README.md)

Build phase 9.

- Silicon wafers
- photoresists
- masks
- gases
- precursors
- etchants
- slurry
- pads
- ultrapure chemicals
- substrate materials
- bonding materials
- underfill
- thermal interface materials

## M35 — [Supply-chain relationships](../35_supply_chain/README.md)

Build phase 9.

- Raw and electronic materials
- wafer suppliers
- equipment
- EDA and IP
- foundries
- memory
- OSAT and foundry packaging
- substrates
- testing
- board manufacturing
- accelerator and server vendors
- datacenters
- geography and dependencies

## M36 — [Manufacturing economics](../36_economics/README.md)

Build phase 10.

- Cost boundaries and denominators
- wafer cost and die area
- gross and good dies
- utilization and throughput
- cycle time and depreciation
- consumables, labor and energy
- compound package yield
- final-system cost
- sensitivity calculations

## M37 — [Industry structure and value capture](../37_investment_analysis/README.md)

Build phase 10.

- Supplier concentration
- switching costs and qualification
- differentiation
- capacity constraints
- installed base and recurring revenue
- customer concentration
- capital intensity
- margins with segment boundaries
- substitutes, commoditization and risks
- no recommendations

## M38 — [NVIDIA Rubin case study](../38_case_studies/README.md)

Build phase 11.

- Rubin overview
- logic manufacturing
- memory
- advanced packaging
- substrate
- power
- cooling
- system architecture
- manufacturing supply chain
- bottlenecks
- known versus unknown

## M39 — [Historical transitions](../39_history/README.md)

Build phase 1.

- Discrete to integrated devices
- planar to FinFET to GAA
- micron lithography to DUV, immersion and EUV
- wire bond to flip chip, 2.5D and 3D
- DDR/GDDR and HBM use cases
- no speculative roadmap

## M40 — [Glossary](../40_glossary/README.md)

Build phase 0.

- Definitions, intuition, purpose and canonical article links
- acronyms and symbols
- terminology consistency

## M41 — [Reference tables](../41_reference_tables/README.md)

Build phase 0.

- Lithography comparison
- deposition comparison
- etch comparison
- packaging comparison
- equipment matrix
- materials matrix
- units and model assumptions

## M42 — [Reference library](../42_references/README.md)

Build phase 0.

- Canonical bibliography
- papers
- patents
- standards
- company sources
- access and rights metadata
- stable IDs
