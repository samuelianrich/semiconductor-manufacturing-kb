# Knowledge and manufacturing dependency graphs

## Edge semantics

- `A → B` in the prerequisite graph means understand A before studying B. It does not mean A ships a physical material to B.
- Solid arrows in the physical graph mean material or assembly flow. They compress repeated process loops.
- Dashed arrows in the ecosystem graph mean enabling services or tooling. They are not a literal sequence of material conversion.
- Related links and design/manufacturing feedback may be cyclic; mandatory prerequisites must stay acyclic.

## Complete module prerequisite graph

This graph includes all 43 architectural modules. The glossary, tables and references are entry resources with no mandatory prerequisites; they link across the whole collection. Scope inside each node is enumerated in the [topic inventory](catalog/topic_inventory.md). This is complete at architecture/module granularity; article-level edges must be registered during scoping, not fabricated before research.

```mermaid
flowchart TD
  M00["M00: Orientation and physical chain"]
  M01["M01: Raw materials"]
  M02["M02: Silicon refining"]
  M03["M03: Single-crystal growth"]
  M04["M04: Wafer manufacturing"]
  M05["M05: Semiconductor physics"]
  M06["M06: MOSFETs and transistor evolution"]
  M07["M07: Design to tapeout"]
  M08["M08: Fab overview"]
  M09["M09: Photolithography"]
  M10["M10: Deposition"]
  M11["M11: Etching"]
  M12["M12: Doping and activation"]
  M13["M13: Thermal oxidation"]
  M14["M14: Cleaning and contamination control"]
  M15["M15: Chemical mechanical planarization"]
  M16["M16: Metrology and process control"]
  M17["M17: Transistor process integration"]
  M18["M18: Interconnect structures and physics"]
  M19["M19: BEOL process integration"]
  M20["M20: Wafer electrical test"]
  M21["M21: Yield engineering"]
  M22["M22: Dicing and die preparation"]
  M23["M23: DRAM fundamentals and fabrication"]
  M24["M24: HBM manufacturing"]
  M25["M25: Advanced packaging"]
  M26["M26: Package substrates"]
  M27["M27: Thermal management"]
  M28["M28: Power delivery"]
  M29["M29: GPU package assembly and qualification"]
  M30["M30: PCB and accelerator module"]
  M31["M31: Server integration"]
  M32["M32: Rack-scale systems"]
  M33["M33: Equipment ecosystem"]
  M34["M34: Materials ecosystem"]
  M35["M35: Supply-chain relationships"]
  M36["M36: Manufacturing economics"]
  M37["M37: Industry structure and value capture"]
  M38["M38: NVIDIA Rubin case study"]
  M39["M39: Historical transitions"]
  M40["M40: Glossary"]
  M41["M41: Reference tables"]
  M42["M42: Reference library"]
  M00 --> M01
  M01 --> M02
  M02 --> M03
  M03 --> M04
  M00 --> M05
  M05 --> M06
  M06 --> M07
  M08 --> M07
  M16 --> M07
  M04 --> M08
  M06 --> M08
  M08 --> M09
  M08 --> M10
  M08 --> M11
  M09 --> M11
  M05 --> M12
  M08 --> M12
  M09 --> M12
  M08 --> M13
  M08 --> M14
  M08 --> M15
  M10 --> M15
  M08 --> M16
  M09 --> M16
  M09 --> M17
  M10 --> M17
  M11 --> M17
  M12 --> M17
  M13 --> M17
  M14 --> M17
  M15 --> M17
  M16 --> M17
  M06 --> M18
  M10 --> M18
  M11 --> M18
  M17 --> M19
  M18 --> M19
  M15 --> M19
  M19 --> M20
  M21 --> M20
  M16 --> M21
  M20 --> M22
  M06 --> M23
  M08 --> M23
  M10 --> M23
  M11 --> M23
  M12 --> M23
  M16 --> M23
  M23 --> M24
  M20 --> M24
  M22 --> M24
  M19 --> M25
  M20 --> M25
  M22 --> M25
  M24 --> M25
  M18 --> M26
  M22 --> M26
  M06 --> M27
  M24 --> M27
  M25 --> M27
  M18 --> M28
  M25 --> M28
  M26 --> M28
  M25 --> M29
  M26 --> M29
  M29 --> M30
  M27 --> M30
  M28 --> M30
  M30 --> M31
  M31 --> M32
  M08 --> M33
  M20 --> M33
  M25 --> M33
  M02 --> M34
  M04 --> M34
  M09 --> M34
  M10 --> M34
  M15 --> M34
  M25 --> M34
  M26 --> M34
  M32 --> M35
  M33 --> M35
  M34 --> M35
  M07 --> M35
  M21 --> M36
  M29 --> M36
  M33 --> M36
  M34 --> M36
  M35 --> M37
  M36 --> M37
  M07 --> M38
  M24 --> M38
  M25 --> M38
  M26 --> M38
  M27 --> M38
  M28 --> M38
  M32 --> M38
  M35 --> M38
  M36 --> M38
  M00 --> M39

```

*Figure P0-02 — Planned learning dependencies. Original graph, source: project scope and architecture decisions; CC BY 4.0. Editable source: [prerequisites.mmd](assets/diagrams/prerequisites.mmd).*

## Physical chain and convergence

```mermaid
flowchart LR
  q[Quartz + carbon] --> mg[Metallurgical silicon]
  mg --> poly[Electronic-grade polysilicon]
  poly --> boule[Crystal ingot]
  boule --> wafer[Finished wafers]
  wafer --> lf[Logic FEOL / MOL / BEOL]
  wafer --> mf[DRAM wafer process]
  lf --> lt[Wafer probe and die prep]
  mf --> mt[Memory test / TSV / thinning]
  mt --> hs[Stack assembly and test]
  lt --> ap[Package integration]
  hs --> ap
  inter[Interposer or bridge fabrication] --> ap
  sub[Substrate fabrication] --> ap
  ap --> pt[Package test and qualification]
  pt --> mod[Board/module assembly and test]
  pcb[PCB fabrication + board components] --> mod
  mod --> sys[Server integration and test]
  net[Networking + power + cooling assemblies] --> sys
  sys --> rack[Rack integration and acceptance]

```

*Figure P0-03 — Material-to-system chain. Original scope schematic; not a qualified process recipe. TSV/test/thinning order is architecture-dependent and will be researched in the memory track. Source: project specification; CC BY 4.0. [Editable source](assets/process_flows/physical_chain.mmd).*

## Enabling ecosystem

```mermaid
flowchart TD
  raw[Raw-material suppliers] --> em[Electronic-material suppliers]
  em --> waf[Wafer suppliers]
  waf --> foundry[Logic foundries]
  waf --> mem[Memory manufacturers]
  eq[Equipment manufacturers] -. tools and service .-> foundry
  eq -. tools and service .-> mem
  eq -. assembly and test tools .-> pack[Foundry packaging / OSAT]
  eda[EDA and IP providers] -. design enablement .-> chip[Chip designers]
  chip -. design and masks .-> foundry
  em -. gases / chemicals / films .-> foundry
  em -. packaging materials .-> pack
  foundry --> pack
  mem --> pack
  subs[Substrate manufacturers] --> pack
  testing[Test equipment and test services] -. validation .-> pack
  pack --> board[Board manufacturers]
  board --> vendor[Accelerator vendors]
  vendor --> server[Server manufacturers]
  server --> dc[Datacenter integration]

```

*Figure P0-04 — Roles and enabling relationships. Original architecture schematic; no company or market-share assertions. Source: project specification; CC BY 4.0. [Editable source](assets/supply_chain_maps/enabling_inputs.mmd).*

## Required cross-links beyond the prerequisite graph

| From | To | Relationship and reader question |
|---|---|---|
| Lithography | Resist → etch → metrology → yield | How does a printed pattern become a controlled physical feature? |
| Design | PDK → process rules → fabrication | How does a manufacturable layout constrain architecture? |
| Cleaning | Deposition, etch, bonding, yield | Where can contamination enter and where is it detected? |
| Doping | Physics → transistor fabrication → parametric test | How do process settings change electrical behavior? |
| Interconnect | CMP → BEOL → RC → power → reliability | How does wiring constrain switching and lifetime? |
| DRAM | TSV → thinning → bonding → HBM test | How does a memory wafer become a usable stack? |
| Wafer test | Known-good-die → packaging → compound yield | What evidence justifies assembling expensive components? |
| Package | Substrate → PCB → signal/power integrity | How do connections cross physical scales? |
| Die power | Package thermal path → board cooling → rack heat rejection | Where does heat go, and what limits performance? |
| Metrology | Yield → throughput → cost per good unit | How do detection and process control change economics? |
| Equipment and materials | Every relevant process → supply chain → economics | Which enabling inputs are necessary and substitutable? |
| Rubin claim register | Every case-study page → general concept | Which actual implementation details are supported? |

## Feedback loops to show in articles

Metrology can trigger process adjustment; electrical test can reveal design or process weaknesses; thermal and power limits constrain floorplanning and packaging; yield learning can change process windows. These are related/design-control edges, not added prerequisite cycles. Each article must identify its upstream input, output, downstream consumer and control feedback where meaningful.
