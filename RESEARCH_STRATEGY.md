# Research strategy and source families

Phase 0 identifies where and how to research. **No source below has yet been retrieved or evaluated for a specific technical claim.** These are candidate organizations and publication families, not bibliography entries or evidence of a Rubin supplier relationship.

## Research matrix

| Topic group | First source families to investigate | Evidence to extract / caution |
|---|---|---|
| Geology and raw silicon | USGS mineral publications; peer-reviewed extractive metallurgy; furnace-operator technical disclosures | Mineral identity, feedstock specifications, reduction mechanism; distinguish geological abundance from economically usable feedstock |
| Purification | Peer-reviewed chemical engineering; WACKER and Hemlock technical disclosures; process patents | Chlorosilane process, purification and reactor alternatives; separate solar and electronic grades; patent is not deployment evidence |
| Crystals and wafers | Crystal-growth journals; university materials courses; SUMCO, Shin-Etsu and Siltronic technical documentation; SEMI wafer standards | Growth/finishing sequence and specifications; identify wafer type and standard revision |
| Physics and transistors | University semiconductor-device courses; peer-reviewed device literature; IEEE and IEDM/VLSI proceedings | Introductory mechanism and device evidence; distinguish simplified models from scaled-device behavior |
| Design and tapeout | Foundry public PDK documentation; EDA vendor manuals and technical papers; public design-rule examples | Design interfaces and signoff meanings; never upload restricted PDK content |
| Lithography | ASML technical materials; SPIE proceedings; resist/mask technical literature; university optics | Wavelength, numerical aperture, source/mirror physics and stochastic limits; vendor performance claims retain attribution |
| Films, etch, doping and oxidation | Peer-reviewed process papers; Applied Materials, Lam Research, Tokyo Electron, ASM International and implant-tool technical disclosures | Mechanisms, variables, selectivity and damage; no invented proprietary recipes |
| Cleaning and CMP | SCREEN and equipment documentation; slurry/pad technical papers; contamination literature | Chemistry/material compatibility, defect modes and endpoint control; laboratory result is not production qualification |
| Metrology and control | KLA documentation; measurement-science papers; SEMI and statistical-control references | Detection limits, sampling, accuracy versus precision; advertised capability needs conditions |
| Integration and BEOL | IEDM/VLSI/IEEE papers; foundry technical papers; interconnect reliability literature | Structure and sequence evidence; material names must be tied to a node/layer before making company-specific claims |
| Test and die preparation | IEEE test literature; Advantest, Teradyne, probe-card and DISCO technical materials | Test coverage, escape risk, thinning and singulation; KGD is bounded test evidence |
| DRAM and HBM | JEDEC specifications/announcements; ISSCC and memory-device papers; SK hynix, Samsung and Micron documentation | Interface generation, die/stack organization, bandwidth conditions; standard permission is not proof of adoption |
| Packaging and substrates | IEEE ECTC; TSMC packaging documentation; OSAT technical papers; BESI bonding documentation; substrate suppliers and material manufacturers | Architecture, interconnect and qualification; separate brand family from verified product variant |
| Power, thermal, PCB and systems | IEEE power/packaging literature; IPC/JEDEC/ASHRAE standards where relevant; engineering papers; board/server product manuals | Boundary conditions, electrical losses, thermal network and interfaces; avoid comparing incompatible measurement conditions |
| Equipment and materials ecosystem | Official product portfolios; annual reports and filings; segment disclosures | Supplier role, geography and economic scope; product availability alone does not establish market share |
| Economics | SEC or home-market filings; dated earnings disclosures; industry capacity data with methodology | Capex, depreciation, service share, capacity units and denominators; prices and margins need dates and segment boundaries |
| Rubin case study | NVIDIA product documentation, official announcements and technical presentations; explicitly named partner disclosures | Exact product/generation, announcement versus shipment status, claim text and measurement conditions; never infer all BOM vendors from generic ecosystem roles |
| Historical context | Original papers, archived proceedings, patents and institutional histories | Event versus announcement dates; avoid treating parallel technologies as a universal replacement sequence |

## Search and evidence workflow

Form questions before searching: what changes physically, why, with which input/output, under which conditions, and how could it fail? Search by mechanism and implementation, not only by product brand. For foundational claims prefer a teachable authoritative reference plus a technical source where useful. For changing company/product claims prefer a dated primary disclosure and corroboration where available.

Record document title, named authors, organization, publication, date, DOI if any, canonical URL, actual access date, exact section/page/table/figure and source limitations. A search snippet is a discovery aid, not supporting evidence. Read the full relevant passage and surrounding conditions before citing.

Maintain the research question, candidate source family, selected source IDs, contradictory evidence, missing evidence and next action in the [research queue](42_references/research_queue.md). Do not populate source records with guessed metadata. Use `not stated` for missing publication dates; use the actual retrieval date for access.

## Supplier table schema

Use company, legal entity/segment, headquarters country, manufacturing geography (separate field), role, process dependency, documented products, claim IDs, as-of date, source IDs, and limitations. Distinguish equipment producer, consumable supplier, foundry, memory maker, OSAT, integrator and customer. Mark lists as representative unless market coverage is demonstrated.

Concentration requires a defined product market, period, geography and metric (revenue, shipments or capacity); never label a segment concentrated merely because several famous suppliers were found. Unknown market shares stay unknown. Customer qualification and switching costs need evidence rather than generic moat language.

## Quantitative research rules

A price needs currency, date, configuration and transaction/list/estimate status. Capacity needs a physical unit and time basis; wafer starts, completed wafers, packaged units and racks are not interchangeable. Yield needs numerator, denominator, process boundary and bin definition. A model input is a hypothetical assumption unless sourced; do not disguise assumptions as analyst estimates.
