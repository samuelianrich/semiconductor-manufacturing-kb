# Phase 2 process-map guide

The [teaching oxide-patterning route](oxide_pattern_transfer.md) follows physical wafer states: accepted silicon → thermally oxidized wafer → developed resist pattern → etched oxide with resist → patterned oxide after strip. It is an educational example, not a qualified recipe or complete transistor flow. Positive resist tone is explicit in its original cross-section diagram.

The [entity register](process_nodes.md#fam-0100) groups eight operations under a fab process family. PART_OF expresses membership; it does not express chronology. Deposition, implant/activation, CMP and metrology are not forced into this example merely to put every topic on one line. Their interfaces are documented in their owning chapters. The implant node aggregates two separately qualified operations and its equipment entry names both functions.

[Equipment roles](equipment_map.md) connect tool functions to operations. [Failure and measurement relationships](yield_map.md) include film thickness, overlay, stochastic pattern failures and CMP topography. Detection edges require suitable methods and sampling; they do not guarantee detection. Supplier relationships are not added from generic technology descriptions.

Family ENABLES edges connect to the fabrication portions of the still-planned logic and DRAM paths. They do not promote tested dies, memory products, packaging or rack systems to researched status. A future detailed integration route should create scoped operation instances where the same process repeats with different materials or conditions.

All Phase 2 descriptions and reviewed relationships have source locators in [evidence links](data/evidence_links.csv). Route composition is an explicit author teaching choice; no source is represented as disclosing this complete production sequence.
