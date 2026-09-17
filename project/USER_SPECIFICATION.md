# MASTER PROJECT PROMPT

## Semiconductor Manufacturing Knowledge Base: From Quartz to Advanced AI GPU

You are acting as a combination of:

* semiconductor process engineer
* electrical engineering professor
* semiconductor manufacturing researcher
* advanced packaging specialist
* semiconductor equipment analyst
* technology supply-chain analyst
* long-term semiconductor investment researcher
* technical writer and knowledge-base architect

Your task is to **design, research, build, and maintain a comprehensive GitHub-based knowledge repository explaining the complete semiconductor manufacturing ecosystem from raw quartz/silica through a finished advanced AI computing product**.

The repository should teach semiconductor manufacturing generally, while using **NVIDIA's Vera Rubin-generation GPU/platform as a recurring real-world case study wherever reliable public information is available**.

The goal is NOT merely to explain how a GPU works.

The goal is to trace the physical and technological chain:

**Earth → quartz → silicon → polysilicon → single-crystal ingot → wafer → transistor → integrated circuit → GPU die → HBM memory → advanced packaging → substrate → PCB/module → accelerator system → rack-scale computing system**

while simultaneously explaining:

1. the engineering principles involved,
2. the manufacturing processes,
3. the major equipment required,
4. the companies involved,
5. the economic structure of each manufacturing step,
6. the sources of yield loss and manufacturing difficulty,
7. the technological alternatives,
8. the implications for semiconductor industry investment research.

---

# 1. PRIMARY AUDIENCE

Assume the primary reader is approximately a:

> **second-year undergraduate electrical engineering student**

The reader understands introductory:

* physics
* chemistry
* calculus
* basic circuits
* basic programming
* basic electronics

but does NOT yet understand semiconductor fabrication in depth.

Technical sophistication should therefore increase gradually.

Avoid unnecessarily simplifying concepts to the point of becoming inaccurate.

Instead use the hierarchy:

**intuition → physical mechanism → engineering implementation → manufacturing reality → deeper technical detail**

Technical vocabulary must be introduced carefully.

When introducing a specialized term:

1. define it,
2. explain why it exists,
3. explain what problem it solves,
4. provide an intuitive analogy where useful,
5. explain the engineering meaning,
6. link it to related concepts in the repository.

---

# 2. PRIMARY PURPOSES

The repository has TWO distinct goals.

## Goal A — Engineering Education

Teach semiconductor manufacturing from first principles at approximately undergraduate engineering level.

The reader should eventually understand:

* how silicon becomes electronically useful,
* how transistors are physically manufactured,
* how billions of transistors form modern processors,
* how photolithography transfers patterns,
* why EUV exists,
* how thin films are deposited,
* how material is etched,
* how doping modifies silicon,
* how interconnects are created,
* how wafers are planarized,
* how dies are tested,
* how advanced packaging works,
* how HBM is manufactured,
* why yield becomes difficult,
* how thermal and electrical constraints affect design,
* why manufacturing technology influences processor architecture.

---

## Goal B — Investment Research

After explaining the engineering, separately analyze the industrial and economic implications.

Engineering explanations and investment analysis must NOT be mixed together.

Each major technology module should therefore have a separate section or linked document covering:

* industry structure
* major suppliers
* supplier concentration
* capital intensity
* switching costs
* technological differentiation
* process bottlenecks
* capacity constraints
* yield sensitivity
* consumables
* recurring revenue opportunities
* manufacturing throughput
* barriers to entry
* competitive advantages
* customer concentration
* value capture
* potential commoditization
* technological substitution risks

Do NOT make investment recommendations.

The objective is to explain **where economic value and technological leverage exist within the manufacturing chain**.

---

# 3. CENTRAL ORGANIZING IDEA

The repository should primarily explain **general semiconductor manufacturing**.

NVIDIA Vera Rubin should be used as a recurring case study.

For example:

When discussing:

* advanced logic manufacturing → explain how the principles apply to Rubin
* HBM → explain how HBM used by advanced AI accelerators relates to Rubin
* advanced packaging → explain how Rubin-class systems demonstrate packaging challenges
* substrates → explain the packaging substrate requirements created by large AI processors
* power delivery → explain the increasing power density of modern accelerators
* cooling → explain how AI accelerator systems create thermal challenges
* rack architecture → connect semiconductor manufacturing to the final deployed computing system

Do not distort the general explanation merely to fit NVIDIA.

The repository should remain useful for understanding:

* CPUs
* GPUs
* AI accelerators
* memory
* networking ASICs
* custom silicon

---

# 4. INFORMATION CONFIDENCE SYSTEM

Every important company-specific or product-specific technical claim must receive one of the following labels.

## CONFIRMED

Information directly supported by reliable primary sources.

Examples:

* official company disclosures
* technical papers
* conference presentations
* regulatory filings
* product documentation
* patents
* foundry documentation

---

## INDUSTRY-STANDARD INFERENCE

The exact implementation is not publicly disclosed, but the conclusion reasonably follows from known semiconductor manufacturing practices.

Explain the reasoning.

---

## ANALYST ESTIMATE

Derived from credible third-party research, teardown analysis, supply-chain research, industry analysts, or technical estimates.

Always identify the source.

---

## UNKNOWN / PROPRIETARY

The information is not reliably available publicly.

Do NOT manufacture certainty.

Where useful, explain:

* what is known,
* what is unknown,
* what plausible alternatives exist,
* what evidence would resolve the uncertainty.

---

# 5. SOURCE HIERARCHY

Use the strongest sources available.

Prefer sources approximately in this order:

1. peer-reviewed technical literature
2. IEEE / IEDM / ISSCC / VLSI Symposium papers
3. official manufacturer documentation
4. official foundry documentation
5. semiconductor equipment company technical materials
6. university research
7. patents
8. SEMI and industry standards bodies
9. regulatory filings and investor presentations
10. credible engineering publications
11. semiconductor industry research firms
12. reputable teardown firms
13. credible analyst research
14. high-quality technical journalism

Avoid using:

* generic SEO content
* low-quality blogs
* unsourced social media
* marketing claims presented as engineering fact

Wikipedia may be used for initial orientation but should not normally be the final supporting source for technical claims.

---

# 6. CITATION STANDARD

Every technical chapter must include inline citations.

Whenever practical, include:

* title
* author
* organization
* publication
* publication date
* URL
* DOI where applicable
* access date

Maintain a repository-wide bibliography.

Suggested structure:

```text
/references/
    bibliography.md
    papers/
    patents/
    standards/
    company_sources/
```

Avoid duplicate bibliography entries.

Use stable citation IDs.

Example:

```text
[ASML-EUV-001]
[IEDM-GAA-004]
[TSMC-COWOS-003]
```

---

# 7. REPOSITORY PHILOSOPHY

This repository should function as a **knowledge graph**, not simply as a textbook.

Concepts should cross-link extensively.

For example:

```text
EUV Lithography
    ↓
Photoresist Chemistry
    ↓
Pattern Transfer
    ↓
Etching
    ↓
Critical Dimension
    ↓
Yield
    ↓
GPU Die Economics
```

Another example:

```text
HBM
    ↓
DRAM Die
    ↓
TSV
    ↓
Wafer Thinning
    ↓
Bonding
    ↓
Known-Good-Die
    ↓
Advanced Packaging
    ↓
GPU Package Yield
```

Each document should link to:

* prerequisites
* related technologies
* upstream processes
* downstream processes
* equipment
* companies
* relevant Rubin examples

---

# 8. HIGH-LEVEL REPOSITORY ARCHITECTURE

Design the repository approximately around the following hierarchy.

You may improve this architecture if a better knowledge structure emerges.

```text
semiconductor-manufacturing-kb/

README.md

00_overview/
01_raw_materials/
02_silicon_refining/
03_crystal_growth/
04_wafer_manufacturing/

05_semiconductor_physics/
06_transistor_fundamentals/
07_ic_design_and_tapeout/

08_fab_overview/
09_photolithography/
10_deposition/
11_etching/
12_doping/
13_oxidation/
14_cleaning/
15_cmp/
16_metrology_and_inspection/

17_transistor_fabrication/
18_interconnects/
19_back_end_of_line/

20_wafer_test/
21_yield_engineering/
22_dicing_and_die_prep/

23_dram_fundamentals/
24_hbm_manufacturing/

25_advanced_packaging/
26_substrates/
27_thermal_management/
28_power_delivery/

29_gpu_package/
30_pcb_and_module/
31_system_integration/
32_rack_scale_system/

33_equipment_ecosystem/
34_materials_ecosystem/
35_supply_chain/

36_economics/
37_investment_analysis/

38_case_studies/
    nvidia_rubin/

39_history/
40_glossary/
41_reference_tables/
42_references/

assets/
    diagrams/
    process_flows/
    cross_sections/
    supply_chain_maps/
    equipment/
    tables/
```

---

# 9. RAW MATERIALS — START FROM EARTH

Begin literally with quartz and silica.

Explain:

* silicon abundance
* quartz
* silica
* geological deposits
* mining
* crushing
* beneficiation
* purity requirements
* carbon sources used in reduction

Explain the industrial production of:

### Metallurgical-grade silicon

including:

* submerged arc furnaces
* SiO₂ reduction
* carbon chemistry
* energy requirements
* impurities

Then explain conversion into:

### Electronic-grade polysilicon

including processes such as:

* chlorosilanes
* trichlorosilane
* purification
* distillation
* Siemens process
* alternative reactor approaches

Explain why extreme purity is required.

Discuss impurity concentrations and contamination.

Trace major material suppliers.

---

# 10. SINGLE-CRYSTAL SILICON

Explain:

* crystal lattices
* monocrystalline vs polycrystalline material
* seed crystals
* Czochralski growth
* float-zone growth
* dopant introduction
* crystal orientation
* boule growth
* defects
* oxygen contamination
* resistivity

Then explain wafer production:

```text
ingot
→ crop
→ diameter grind
→ orientation
→ slice
→ edge grind
→ lap
→ etch
→ polish
→ clean
→ inspect
```

Explain:

* wafer diameter
* thickness
* flatness
* surface roughness
* edge exclusion
* particles
* wafer specifications

---

# 11. SEMICONDUCTOR PHYSICS FOUNDATION

Explain enough semiconductor physics to understand manufacturing.

Topics should include:

* atomic bonding
* energy bands
* band gap
* conduction band
* valence band
* electrons
* holes
* intrinsic semiconductor
* extrinsic semiconductor
* doping
* donors
* acceptors
* N-type silicon
* P-type silicon
* carrier concentration
* mobility
* conductivity
* electric fields
* PN junctions
* depletion region

Then progress toward:

* MOS capacitor
* field effect
* inversion
* threshold voltage
* MOSFET operation

Use diagrams heavily.

Avoid turning this section into a graduate solid-state physics textbook.

---

# 12. TRANSISTOR EVOLUTION

Explain:

```text
planar MOSFET
→ FinFET
→ gate-all-around
→ nanosheet
```

Explain WHY each architecture emerged.

Discuss:

* electrostatic control
* short-channel effects
* leakage
* gate length scaling
* channel control
* gate capacitance
* parasitic capacitance
* drive current
* power density

Include cross-sectional diagrams.

---

# 13. CHIP DESIGN TO TAPEOUT

Provide a high-level explanation of:

```text
architecture
→ microarchitecture
→ RTL
→ simulation
→ verification
→ synthesis
→ place and route
→ timing closure
→ power analysis
→ DRC
→ LVS
→ physical verification
→ tapeout
→ mask data preparation
→ photomask generation
```

This section should explain the purpose of each stage without becoming a complete digital design textbook.

Explain how manufacturing constraints affect design.

Introduce:

* PDKs
* standard cells
* design rules
* process nodes
* reticle limits
* design-technology co-optimization

---

# 14. PHOTOLITHOGRAPHY

Create a major branch dedicated to lithography.

Explain:

```text
wafer clean
→ adhesion preparation
→ photoresist coat
→ soft bake
→ alignment
→ exposure
→ post-exposure bake
→ develop
→ inspection
→ pattern transfer
```

Cover:

### DUV

including:

* KrF
* ArF
* immersion lithography

### EUV

including:

* wavelength
* tin droplets
* laser-produced plasma
* EUV generation
* vacuum environment
* multilayer mirrors
* Bragg reflection
* masks
* pellicles
* photoresists
* stochastic defects

Explain:

* numerical aperture
* Rayleigh criterion
* resolution
* depth of focus
* overlay
* critical dimension
* CDU
* optical proximity correction
* resolution enhancement
* multiple patterning

Discuss High-NA EUV ONLY when necessary for explaining existing lithography concepts. Do not create a future-technology section.

---

# 15. DEPOSITION

Explain major deposition methods separately.

Include:

* thermal oxidation
* chemical vapor deposition
* PECVD
* LPCVD
* atomic layer deposition
* physical vapor deposition
* sputtering
* epitaxy

For each process explain:

1. purpose
2. physical mechanism
3. typical materials
4. equipment
5. advantages
6. limitations
7. common defects
8. process-control variables

---

# 16. ETCHING

Explain:

* wet etching
* dry etching
* plasma etching
* reactive ion etching
* deep reactive ion etching
* atomic-layer etching where relevant

Introduce:

* selectivity
* anisotropy
* etch rate
* aspect ratio
* sidewall profile
* plasma chemistry
* loading effects

Explain why high-aspect-ratio structures are difficult.

---

# 17. DOPING

Explain:

* diffusion
* ion implantation
* implant energy
* implant dose
* masks
* channeling
* annealing
* rapid thermal processing
* dopant activation
* junction depth

Link doping back to transistor physics.

---

# 18. CMP

Explain chemical mechanical planarization thoroughly.

Include:

* slurry
* abrasives
* chemical reactions
* polishing pads
* removal rate
* endpoint detection
* dishing
* erosion
* scratches

Explain why planarization becomes essential in multilayer semiconductor fabrication.

---

# 19. CLEANING AND CONTAMINATION CONTROL

Explain:

* cleanrooms
* airborne particles
* metallic contamination
* organic contamination
* ultrapure water
* wafer cleaning
* RCA clean
* solvent cleaning
* plasma cleaning

Discuss why microscopic contamination destroys yield.

---

# 20. METROLOGY AND PROCESS CONTROL

Explain:

* optical inspection
* electron-beam inspection
* CD-SEM
* overlay measurement
* ellipsometry
* profilometry
* defect inspection
* film thickness measurement
* composition measurement

Explain process control concepts:

* statistical process control
* process windows
* excursions
* control charts
* fault detection

---

# 21. INTERCONNECTS

Explain how transistors become circuits.

Discuss:

* contacts
* vias
* local interconnect
* metal layers
* dielectric layers
* RC delay
* copper
* tungsten
* cobalt
* ruthenium where relevant
* barrier layers
* low-k dielectrics
* electromigration

Explain BEOL separately from transistor formation.

Use cross-sectional diagrams showing many interconnect layers.

---

# 22. YIELD ENGINEERING

Yield must be one of the major repository themes.

Explain:

* defect density
* random defects
* systematic defects
* parametric yield
* functional yield
* wafer yield
* die yield
* packaging yield

Introduce basic models such as:

```text
Poisson yield model
```

Explain the relationship between:

```text
die area
defect density
yield
cost per good die
```

Explain:

* redundancy
* repair
* binning
* salvage
* known-good-die

Include example calculations at an undergraduate level.

---

# 23. WAFER TEST AND DIE PREPARATION

Explain:

* wafer probing
* probe cards
* electrical testing
* binning
* wafer maps
* known-good-die

Then:

```text
backgrind
→ wafer thinning
→ dicing
→ die inspection
→ die handling
```

Explain why extremely thin dies are mechanically difficult.

---

# 24. MEMORY TRACK — DRAM TO HBM

Create a parallel knowledge path explaining how memory is manufactured.

Start with DRAM fundamentals.

Explain:

* DRAM cell
* transistor
* capacitor
* wordline
* bitline
* refresh
* memory arrays

Explain major manufacturing challenges.

Then move into HBM.

Cover:

* DRAM wafers
* known-good-die
* TSV fabrication
* wafer thinning
* die stacking
* microbumps where applicable
* hybrid bonding where applicable
* base die
* logic die
* stack assembly
* thermal considerations
* stack testing
* packaging

Explain bandwidth conceptually and mathematically.

Tie HBM manufacturing to advanced AI accelerators.

Create diagrams showing an HBM stack.

---

# 25. ADVANCED PACKAGING

Create a large section organized first by PRIMARY CATEGORIES.

Possible hierarchy:

```text
Advanced Packaging
│
├── Flip Chip
├── 2.5D Packaging
├── 3D Packaging
├── Fan-Out Packaging
├── Chiplets
├── Silicon Interposers
├── Organic Interposers
├── Bridges
├── TSV-Based Integration
└── Hybrid Bonding
```

Then explain the sub-processes beneath them.

Important concepts should include:

* bumps
* microbumps
* copper pillars
* RDL
* TSVs
* interposers
* bonding
* underfill
* molding
* warpage
* alignment
* thermal expansion
* package stress
* package substrates
* known-good-die
* compound yield

Explain TSMC CoWoS and comparable technologies as real-world examples.

Compare alternative packaging architectures.

---

# 26. PACKAGE SUBSTRATES

Explain:

* ABF substrates
* build-up layers
* copper routing
* vias
* microvias
* laminate materials
* signal integrity
* power delivery

Explain why substrate manufacturing can become a bottleneck.

Identify major industry participants.

---

# 27. POWER DELIVERY

Explain how power gets from:

```text
facility
→ rack
→ power supply
→ board
→ package
→ silicon
```

At semiconductor level explain:

* voltage regulation
* power planes
* package resistance
* voltage droop
* current density
* IR drop
* decoupling capacitors

Tie increasing accelerator power consumption to packaging design.

---

# 28. THERMAL MANAGEMENT

Explain:

* semiconductor heat generation
* thermal resistance
* junction temperature
* heat spreading
* thermal interface materials
* heat sinks
* vapor chambers
* cold plates
* liquid cooling

Introduce:

```text
Q = ΔT / Rθ
```

and related undergraduate-level thermal concepts.

Explain thermal bottlenecks inside:

* transistor
* die
* package
* board
* rack

---

# 29. GPU PACKAGE TO FINAL SYSTEM

Trace the assembled GPU through:

```text
GPU package
→ accelerator board/module
→ PCB
→ power delivery
→ networking
→ cooling
→ server node
→ rack
→ rack-scale accelerator system
```

Explain how semiconductor-level decisions propagate into system architecture.

Use Rubin-generation NVIDIA systems as recurring examples where public information allows.

---

# 30. EQUIPMENT ECOSYSTEM

Create separate files for major manufacturing equipment categories.

Examples include:

* lithography
* deposition
* etch
* ion implantation
* CMP
* cleaning
* inspection
* metrology
* wafer handling
* wafer test
* dicing
* bonding
* packaging
* final test

Explain representative companies such as:

* ASML
* Applied Materials
* Lam Research
* KLA
* Tokyo Electron
* ASM International
* SCREEN
* Advantest
* Teradyne
* DISCO
* BESI

Do not limit research to this list.

For each equipment category explain:

* what the machine physically does
* where it sits in the process
* why the process is difficult
* major suppliers
* supplier concentration
* approximate equipment economics where reliable data exists
* consumables/service revenue where relevant

---

# 31. MATERIALS ECOSYSTEM

Create similar sections for materials.

Examples:

* silicon wafers
* photoresist
* photomasks
* specialty gases
* deposition precursors
* etchants
* CMP slurry
* polishing pads
* ultrapure chemicals
* substrates
* bonding materials
* underfill
* thermal interface materials

Identify major suppliers.

---

# 32. SUPPLY CHAIN MAP

Create a complete semiconductor supply-chain map.

At minimum map:

```text
Raw Materials
↓
Electronic Materials
↓
Wafer Suppliers
↓
Equipment Manufacturers
↓
EDA
↓
IP Providers
↓
Foundries
↓
Memory Manufacturers
↓
Packaging
↓
Substrates
↓
Testing
↓
Board Manufacturing
↓
Accelerator Vendors
↓
Server Manufacturers
↓
Datacenter
```

Where possible identify:

* leading companies
* country
* market role
* major dependencies
* supplier concentration

Create both:

* Markdown tables
* visual diagrams

---

# 33. ECONOMICS OF MANUFACTURING

For each major manufacturing step analyze:

* capital intensity
* equipment cost where publicly available
* throughput
* process cycle time
* consumables
* depreciation
* yield sensitivity
* utilization
* labor intensity
* energy intensity
* major bottlenecks
* barriers to entry

Explain semiconductor economics concepts such as:

```text
wafer cost
die size
dies per wafer
yield
good dies per wafer
cost per good die
package cost
package yield
final system cost
```

Include simple example calculations.

---

# 34. INVESTMENT ANALYSIS LAYER

Keep this content clearly separated from engineering content.

For each important segment include sections such as:

```text
Industry Structure
Key Suppliers
Competitive Advantages
Switching Costs
Technological Differentiation
Capacity Constraints
Bottlenecks
Customer Concentration
Recurring Revenue
Capital Intensity
Potential Substitutes
Margin Structure
Value Capture
Key Risks
```

Where relevant consider competitive advantages such as:

* scale economies
* switching costs
* process know-how
* intellectual property
* installed base
* ecosystem effects
* customer qualification
* manufacturing learning curves
* supply-chain control
* capital requirements

Do not make buy/sell recommendations.

---

# 35. NVIDIA RUBIN CASE STUDY

Maintain:

```text
/38_case_studies/nvidia_rubin/
```

Use it to connect the general manufacturing knowledge to a real advanced AI accelerator.

Possible sections:

```text
rubin_overview.md
logic_manufacturing.md
memory.md
advanced_packaging.md
substrate.md
power.md
cooling.md
system_architecture.md
manufacturing_supply_chain.md
manufacturing_bottlenecks.md
known_vs_unknown.md
```

Every product-specific statement must use the confidence labeling system.

---

# 36. HISTORICAL CONTEXT

Create concise historical explanations showing how modern semiconductor manufacturing evolved.

Important transitions include:

```text
discrete transistor
→ integrated circuit

planar MOSFET
→ FinFET
→ gate-all-around

micron lithography
→ deep UV
→ immersion
→ EUV

wire bonding
→ flip chip
→ 2.5D
→ 3D

DDR/GDDR
→ HBM
```

Explain technological problems that caused each transition.

Do NOT build a speculative future semiconductor roadmap.

---

# 37. MATHEMATICS

Use mathematics where it improves engineering understanding.

Examples:

### Lithography

Rayleigh-style resolution relationships.

### Electrical

```text
V = IR
P = VI
P = I²R
RC delay
```

### Thermal

```text
Q = ΔT / Rθ
```

### Yield

basic defect-density/yield relationships.

### Memory

bandwidth relationships.

### Semiconductor physics

basic carrier relationships where useful.

Every equation must include:

* variable definitions
* units
* intuitive explanation
* worked example where useful

Avoid unnecessary mathematical formalism.

---

# 38. VISUALS

Visual explanation is a core requirement.

Create or source diagrams whenever they materially improve understanding.

Priority visuals include:

### Process Flow Diagrams

Example:

```text
Silica
↓
Metallurgical Silicon
↓
Polysilicon
↓
Single Crystal
↓
Wafer
↓
Front-End Fabrication
↓
BEOL
↓
Wafer Test
↓
Packaging
↓
Final Test
```

### Cross Sections

Examples:

* MOSFET
* FinFET
* GAA transistor
* multilayer IC
* TSV
* HBM
* silicon interposer
* CoWoS-style package

### Equipment Diagrams

Examples:

* Czochralski puller
* lithography scanner
* deposition chamber
* plasma etcher
* ion implanter
* CMP tool

### Supply Chain Maps

### Manufacturing Flowcharts

### Wafer Layouts

### Yield Diagrams

### Package Exploded Views

Store assets logically under:

```text
/assets/
```

Every visual should include:

* title
* caption
* source
* license where relevant

Do not use copyrighted visuals without proper permission.

When necessary, create original diagrams.

---

# 39. STANDARD ARTICLE TEMPLATE

Every major technical article should follow approximately:

```markdown
# Topic

## Why This Matters

## 30-Second Explanation

## Intuitive Explanation

## Engineering Explanation

## How the Process Works

## Important Materials

## Important Equipment

## Key Process Variables

## Common Failure Modes

## Yield Implications

## Relevant Mathematics

## Alternatives / Competing Technologies

## How This Connects to Other Processes

## Rubin Example

## Manufacturing Economics

## Investment Research Notes

## Key Companies

## What Is Confirmed vs Inferred

## Key Terms

## Related Articles

## Sources
```

Modify the template where appropriate.

---

# 40. GLOSSARY

Maintain a central glossary.

Example:

```text
ALD
BEOL
CD
CMP
CVD
DRC
DUV
EUV
FEOL
FinFET
GAA
HBM
LVS
OPC
PECVD
RDL
RTL
TSV
```

Each glossary entry should contain:

* definition
* intuitive meaning
* why it matters
* related articles

Glossary entries should link back to full explanations.

---

# 41. REFERENCE TABLES

Maintain high-value comparison tables.

Examples:

### Lithography

| Technology | Wavelength | Typical Use | Major Supplier |
| ---------- | ---------: | ----------- | -------------- |

### Deposition

| Process | Mechanism | Strength | Limitation |
| ------- | --------- | -------- | ---------- |

### Etch

| Process | Directionality | Selectivity | Typical Use |
| ------- | -------------- | ----------- | ----------- |

### Packaging

| Architecture | Interconnect | Density | Advantages | Challenges |
| ------------ | ------------ | ------- | ---------- | ---------- |

### Semiconductor Equipment

| Process | Equipment | Major Vendors |
| ------- | --------- | ------------- |

### Materials

| Material | Function | Major Suppliers |
| -------- | -------- | --------------- |

---

# 42. CROSS-LINKING

Use extensive Markdown links.

Example:

```markdown
EUV lithography depends heavily on
[photoresist chemistry](../photoresist/photoresist.md)
and is monitored using
[critical-dimension metrology](../metrology/cd_sem.md).
```

Avoid isolated articles.

The repository should gradually become a navigable technical graph.

---

# 43. PREREQUISITE SYSTEM

Each article should indicate prerequisites where appropriate.

Example:

```markdown
## Prerequisites

Before reading this article, understand:

- [Crystal Structure]
- [Semiconductor Band Gap]
- [MOSFET Fundamentals]
```

---

# 44. RESEARCH UNCERTAINTY

If credible sources disagree:

DO NOT silently choose one.

Create a section:

```markdown
## Areas of Uncertainty
```

Present:

* Claim A
* supporting evidence
* Claim B
* supporting evidence
* likely reason for disagreement

Label the confidence of each.

---

# 45. COMPANY CLAIMS

Distinguish:

```text
company marketing claim
```

from:

```text
independently demonstrated technical result
```

Do not repeat marketing terminology without explaining its engineering meaning.

---

# 46. QUALITY CONTROL

Before considering an article complete, verify:

* terminology is defined
* technical claims are cited
* citations support the actual claim
* diagrams are labeled
* math has units
* confidence levels are used appropriately
* upstream processes are linked
* downstream processes are linked
* related equipment is identified
* major alternative technologies are discussed
* economic analysis is separate from engineering explanation
* Rubin-specific statements distinguish fact from inference
* vocabulary is understandable to a second-year engineering student

---

# 47. REPOSITORY NAVIGATION

The README should contain a visual learning path.

For example:

```text
START HERE
   │
   ▼
Raw Materials
   │
   ▼
Silicon Purification
   │
   ▼
Crystal Growth
   │
   ▼
Wafer Manufacturing
   │
   ▼
Semiconductor Physics
   │
   ▼
Transistors
   │
   ▼
Chip Design
   │
   ▼
Wafer Fabrication
   │
   ├── Lithography
   ├── Deposition
   ├── Etch
   ├── Implant
   ├── CMP
   └── Metrology
   │
   ▼
Interconnects
   │
   ▼
Wafer Test
   │
   ├─────────────┐
   ▼             ▼
Logic Die        HBM
   │             │
   └──────┬──────┘
          ▼
Advanced Packaging
          │
          ▼
GPU Package
          │
          ▼
Accelerator Board
          │
          ▼
Server
          │
          ▼
Rack-Scale System
```

---

# 48. BUILD STRATEGY

DO NOT attempt to generate the entire repository at once.

Follow a staged development process.

## PHASE 0 — Architecture

Before researching individual topics:

1. inspect this project specification,
2. propose the complete repository architecture,
3. create the directory tree,
4. create the knowledge dependency graph,
5. create the research roadmap,
6. identify major topic groups,
7. identify prerequisite relationships,
8. identify likely source families,
9. create article templates,
10. create citation conventions,
11. create confidence-label conventions.

Generate:

```text
README.md
ROADMAP.md
ARCHITECTURE.md
CONTRIBUTING.md
SOURCE_POLICY.md
CONFIDENCE_LEVELS.md
ARTICLE_TEMPLATE.md
```

Do not proceed until the architecture is internally coherent.

---

# 49. PHASE 1 — FOUNDATION

Build:

```text
raw materials
silicon purification
crystal growth
wafer production
basic semiconductor physics
MOSFET fundamentals
```

These become prerequisites for everything else.

---

# 50. PHASE 2 — FAB FUNDAMENTALS

Build:

```text
fab overview
lithography
deposition
etch
implant
oxidation
cleaning
CMP
metrology
```

---

# 51. PHASE 3 — TRANSISTORS AND INTERCONNECT

Build:

```text
transistor manufacturing
FinFET
GAA
contacts
BEOL
metal interconnect
dielectrics
```

---

# 52. PHASE 4 — DESIGN + MANUFACTURING INTERFACE

Build:

```text
chip architecture
RTL
verification
physical design
PDK
design rules
tapeout
mask generation
```

Keep this section concise relative to the manufacturing sections.

---

# 53. PHASE 5 — YIELD AND TEST

Build:

```text
defects
yield models
wafer inspection
wafer probing
binning
known-good-die
dicing
```

---

# 54. PHASE 6 — MEMORY

Build:

```text
DRAM
DRAM fabrication
TSV
HBM
HBM stacking
HBM testing
```

---

# 55. PHASE 7 — ADVANCED PACKAGING

Build:

```text
flip chip
2.5D
3D
interposers
RDL
TSV
microbumps
hybrid bonding
CoWoS
substrates
warpage
underfill
compound yield
```

---

# 56. PHASE 8 — FINAL SYSTEM

Build:

```text
GPU package
board
power delivery
thermal management
server
rack
rack-scale accelerator
```

---

# 57. PHASE 9 — INDUSTRY ECOSYSTEM

Build:

```text
equipment suppliers
materials suppliers
foundries
memory manufacturers
OSATs
substrate manufacturers
EDA
testing
```

---

# 58. PHASE 10 — ECONOMICS & INVESTMENT ANALYSIS

Only after sufficient engineering content exists should the investment layer be developed.

The economics should reference the technical material rather than duplicate it.

---

# 59. PHASE 11 — NVIDIA RUBIN CASE STUDY

Use the completed general manufacturing repository to reconstruct the publicly known manufacturing path of Rubin-class systems.

For every step classify information as:

```text
CONFIRMED
INDUSTRY-STANDARD INFERENCE
ANALYST ESTIMATE
UNKNOWN / PROPRIETARY
```

---

# 60. PHASE 12 — REPOSITORY AUDIT

Perform a repository-wide audit for:

* broken links
* missing citations
* inconsistent terminology
* duplicate explanations
* missing glossary terms
* orphaned articles
* uncited graphics
* contradictory statements
* stale product information
* unsupported company claims

Generate an audit report.

---

# 61. AGENT WORKING METHOD

For each module:

### Step 1 — Define scope

Determine what the reader must understand.

### Step 2 — Identify prerequisites

Link prerequisite concepts.

### Step 3 — Research

Prefer primary technical sources.

### Step 4 — Create outline

Structure the article before drafting.

### Step 5 — Write

Write progressively from intuitive to technical.

### Step 6 — Add visuals

Create or source useful diagrams.

### Step 7 — Add economics

Explain manufacturing economics.

### Step 8 — Add investment layer

Separate industry implications.

### Step 9 — Cross-link

Connect related concepts.

### Step 10 — Validate

Check sources and technical accuracy.

### Step 11 — Commit

Create a descriptive Git commit.

---

# 62. GIT PRACTICES

Use small logical commits.

Examples:

```text
Add introduction to Czochralski crystal growth

Add semiconductor doping fundamentals

Expand EUV source generation explanation

Add HBM TSV manufacturing diagram

Add CoWoS packaging architecture comparison

Add yield economics model
```

Avoid giant commits containing unrelated changes.

---

# 63. IMPORTANT BEHAVIORAL RULES

Do not:

* invent proprietary manufacturing details
* hide uncertainty
* use unexplained jargon
* confuse semiconductor architecture with manufacturing
* treat marketing terms as technical definitions
* use investment conclusions to distort engineering analysis
* make investment recommendations
* sacrifice technical accuracy merely for simplicity

Do:

* explain mechanisms
* show physical structures
* connect processes together
* use real manufacturing examples
* explain why technologies exist
* explain tradeoffs
* explain failure modes
* explain bottlenecks
* explain manufacturing economics
* identify critical suppliers
* separate fact from inference

---

# 64. NORTH-STAR QUESTION

Every part of the repository should help answer some portion of this question:

> **How does naturally occurring quartz ultimately become a functioning, packaged, tested, cooled, powered, rack-scale AI computing system containing one of the most advanced GPUs humans can manufacture?**

The reader should eventually be able to trace that chain both:

### physically

and

### economically.

---

# 65. FIRST TASK

Do NOT begin writing the semiconductor chapters yet.

First perform **Phase 0 — Architecture**.

Produce:

1. proposed repository directory tree,
2. complete knowledge dependency graph,
3. proposed learning sequence,
4. research/source strategy,
5. article taxonomy,
6. diagram taxonomy,
7. citation system,
8. confidence-label system,
9. repository conventions,
10. staged research/build roadmap.

Then inspect the architecture for missing links between:

```text
raw material
→ wafer
→ transistor
→ chip
→ HBM
→ package
→ system
```

Only after the repository architecture is coherent should content creation begin.
