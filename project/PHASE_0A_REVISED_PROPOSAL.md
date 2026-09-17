# Phase 0A — Persistent manufacturing process map

Status: **Accepted by the user for implementation on 2026-09-16.** Completion is recorded in the map audit and phase roadmap; this document preserves the accepted requirements.

## 1. Purpose and relationship to the existing architecture

Extend the existing repository with a persistent, source-traceable manufacturing map. Preserve the numbered modules, canonical bibliography, claim register, templates and existing learning dependencies. Do not rebuild Phase 0 or duplicate technical chapters in map files.

The map answers: Where does this process, material, physical structure, machine or company participate in the path from quartz to a finished computing system, and what evidence supports that relationship?

Keep three distinct structures:

- Learning prerequisites: owned by the existing module catalog; acyclic.
- Manufacturing and assembly relationships: owned by the manufacturing map; branched and conditional, with explicit repeated operations where necessary.
- Economic, supplier and product-application relationships: linked overlays with their own evidence and scope.

## 2. Physical-flow conventions

Use material states and process operations as distinct node types. A conversion follows input material → operation → output material. A process family groups operations; it is not another operation in the same sequence.

At the highest level, show raw materials → refined silicon → crystal → wafer. Branch into logic manufacturing and memory manufacturing. Converge tested logic and memory components, interposer/bridge or other applicable interconnect structures, and package substrate at package integration. Connect tested packages and fabricated PCBs/components to module assembly, then server and rack integration.

Design and mask data are enabling inputs to fabrication. Supplier equipment enables operations. Substrates and PCBs have their own manufacturing paths; do not put them after a finished assembly as though that assembly turns into its input. Power, cooling and networking are parallel integration dependencies with boundary-specific assembly/test operations.

Do not show logic die → HBM, or crystal defect → pattern defect, as universal causal chains. Mark test results such as known-good-die as qualification states with defined coverage rather than unconditional guarantees.

All detailed process sequences require researched scope. Use route variants for differences in transistor integration, TSV/thinning/test order, stacking/bonding and package assembly. A high-level overview is not a production recipe.

## 3. Human-readable views

Create `manufacturing_map/` with:

```text
README.md
SCHEMA.md
master_process_map.md
process_nodes.md
materials_map.md
equipment_map.md
supplier_map.md
yield_map.md
economics_map.md
logic_path.md
hbm_path.md
packaging_path.md
system_path.md
rubin_manufacturing_path.md
AUDIT.md
data/
    entities.csv
    process_nodes.csv
    process_edges.csv
    materials.csv
    equipment.csv
    suppliers.csv
    evidence_links.csv
    routes.csv
    schema.json
```

Use levels 0–3 for whole chain, major stages, process families and individual operations. Materials/equipment and economics are selectable views across these levels, rather than deeper children of every process. This avoids duplicating shared materials, machines and suppliers under many operations.

Keep an overview small enough to read quickly. Link detailed submaps and provide text/table equivalents. Original visuals require titles, captions, legends, source/derivation, license and accessible descriptions under existing asset conventions.

## 4. Authoritative structured data

Use stable globally unique IDs independent of parent hierarchy or file location. Names can change without breaking IDs. Distinguish process families, operations, materials, intermediate/final artifacts, equipment categories, suppliers, failure modes, measured characteristics, test states and metrics. Add new types only when needed.

`entities.csv` owns identity and shared metadata:

```text
entity_id,entity_type,name,description,module_id,primary_article,status,last_reviewed
```

`process_nodes.csv` owns process-specific attributes, keyed to an existing operation or process-family entity:

```text
entity_id,purpose,scope,mechanism_summary,notes
```

Material/equipment/supplier tables own only type-specific attributes and use the same entity IDs. Do not duplicate names, upstream/downstream lists or supplier memberships across tables. Preserve supplier headquarters separately from production geography; location alone does not identify a customer relationship.

`process_edges.csv` is the authoritative relationship table; its endpoints may be any permitted entity types, not only processes:

```text
edge_id,source_id,relationship,target_id,route_id,conditions,status,last_reviewed
```

Define every relationship's direction, valid endpoint types and scope in `SCHEMA.md` and encode rules in `schema.json`. Initial relationships:

- `PART_OF`: child → parent; hierarchy only.
- `PRECEDES`: operation → operation within a specified route; order, not necessarily material conversion or direct adjacency.
- `CONSUMES` / `PRODUCES`: operation → material/artifact.
- `USES_EQUIPMENT`: operation → equipment category.
- `SUPPLIED_BY`: documented material/equipment/service → supplier.
- `ENABLES`: enabling entity → operation/assembly.
- `CAN_CAUSE`: documented cause → failure mode/effect, under stated conditions.
- `DETECTED_BY`: failure mode → inspection/test operation.
- `MEASURES`: measurement operation → characteristic.
- `AFFECTS`: variable/failure/metric → characteristic or metric, with the mechanism explained.
- `ALTERNATIVE_TO`: comparable entities under a shared purpose and boundary.
- `INTEGRATED_INTO`: artifact → assembly, where applicable.

Do not also store `FOLLOWS`; derive inverse views from `PRECEDES`. Derive parent/upstream/downstream/supplier navigation from edges. Store symmetric alternative relationships once using a deterministic ordering of IDs. Do not use an undefined `REQUIRES` to mix reading prerequisites, bill-of-material requirements and process sequencing.

`routes.csv` identifies route/variant names, parent routes, scope, article and status. `route_id` may be empty only for a genuinely route-independent relationship. Repeated use of one process primitive can be represented with route-specific operation instances linked to the shared process family. Explicitly label rework, recycle and feedback edges if introduced; do not forbid all cycles in the entire manufacturing graph.

## 5. Evidence and uncertainty belong to assertions

Reuse `42_references/bibliography.md` and `42_references/claims.csv`. Do not create a second bibliography or copy Rubin claims into independent map records.

`evidence_links.csv` connects evidence to a specific entity field or edge:

```text
record_id,record_type,field,source_id,locator,claim_id,evidence_role
```

An entity's existence does not substantiate every relationship involving it. Cite general technical relationships as well as company-specific ones. Use claim IDs and the established four confidence labels for company/product assertions. Keep sourcing status separate from confidence: `planned`, `researched` and `reviewed` describe work completion, not certainty.

Do not give an entire node a blanket inference label. A generic process can be well documented while its relevance to a particular Rubin variant remains unknown. Product application is an overlay referencing exact product/variant, claim ID, date and evidence. Lack of disclosure does not automatically justify industry-standard inference.

Blank values mean not yet entered; record `unknown after research`, `not applicable` and `proprietary/undisclosed` explicitly when appropriate. Do not let a completed-looking table hide missing research.

## 6. Yield, controls and economics views

Represent yield as cause → physical/electrical effect → detection → process or acceptance outcome. Distinguish where a defect originates, where it is detected and where value is lost. Include repair/salvage only where supported. Define the tested population, denominator, process boundary and test coverage for yield claims.

Separate controllable process settings from measured outcomes. Each variable/metric definition has units, conditions and an owner article. Avoid modeling a correlation or a list of cost drivers as an unconditional causal sequence.

Economics views link to the separate economics and industry-analysis modules. A model records cost boundary, output unit, currency/date, utilization, yield assumptions, throughput constraints and source/hypothetical status. Do not equate one tool's throughput with factory wafer-start capacity. Do not populate unavailable equipment prices, market shares or supplier economics with guesses.

Before Phase 10, record sourced operating/cost drivers and open research questions only. Full investment analysis remains behind the engineering-first gate.

## 7. Synchronization and validation

Structured data owns map identities and relationships. Generate repeated node tables, relationship lists and Mermaid blocks from it. Keep explanatory prose editable outside generated sections. Provide a deterministic generation command and a check mode that fails if generated views are stale.

Extend existing validation to check:

- Unique IDs, valid entity types and valid foreign keys.
- Relationship endpoint types and required route/condition fields.
- Duplicate edges, including inverted duplicates of symmetric edges.
- Acyclic containment and learning prerequisites; route-specific sequence checks with declared loop exceptions.
- Resolvable article, bibliography and claim references.
- Evidence coverage for reviewed assertions and required product labels.
- Registered assets and generated-view freshness.
- Disconnected nodes, with explicit exceptions for planned scope and supporting utilities.
- Reachability of the selected main material/assembly route at the intended overview level.

A script can verify evidence references exist; human review must verify they actually support the assertion. Structural validation does not certify a proprietary process sequence or mathematical model.

## 8. Proportionate map update rule

Every completed article includes a short “Position in the manufacturing map” section with its entity IDs, input/output and upstream/downstream links.

An article change must either update affected entities/edges/evidence/views in the same commit or record “no map change needed” with a brief reason. Do not require all map files to change for every article. Concept-only articles may link to existing nodes without inventing manufacturing operations.

For a researched operation, require identity, scope, purpose, applicable input/output, route relationships, canonical article, evidence, status and reviewed alternatives/uncertainties. Materials, equipment, controls, failure modes and metrology must be populated or explicitly dispositioned when relevant. Supplier/economics/Rubin detail is conditional on available evidence and current phase.

## 9. Bounded Phase 0A delivery gate

Create the schema, map navigation, high-level branching topology, generator and validation integration. Seed the high-level architecture from existing reviewed architecture decisions, clearly labeled as planned technical scope where source research remains outstanding. Do not invent hundreds of detailed process records or fully populate later-phase maps.

Audit that engineering, materials, equipment, yield, suppliers, economics and product application can all be represented. All seven must be representable; they do not all need researched content before Phase 1 begins. Reconcile existing process diagrams so they become views of the new map instead of competing manually maintained sources of truth. Preserve the separate learning-prerequisite registry.

## 10. Phase 1 scope and exit gates

Preserve the original foundation scope as two work packages:

**Phase 1A — Raw materials to prime silicon wafer:** modules 01–04. Research and write quartz/feedstock qualification; metallurgical reduction; electronic-grade purification; crystal growth; wafer slicing/finishing/cleaning/inspection. Include rejection criteria, relevant utilities and contamination controls where supported. Trace the accepted output and qualification boundary; avoid implying that all device flows use an identical starting wafer. Include a concise sourced orientation to specialized wafer variants without prematurely expanding deposition or device fabrication chapters.

**Phase 1B — Semiconductor physics and MOSFET fundamentals:** modules 05–06. Develop bonding/bands, carriers, doping, junctions, inversion and switching. Add a small just-in-time doping/resistivity primer during 1A if its material requires it. Both work packages must finish before Phase 2's full prerequisites are satisfied.

Every researched Phase 1 operation updates its map representation and evidence. Complete the physical path and articles progressively, one coherent module at a time. Require cited prose, appropriate original diagrams, defined terminology, map integration, checked units/examples and recorded review before declaring a module complete.

## Review basis

The topology and data-model edits above are architectural recommendations. Two primary sources were checked to ground the most relevant physical-interface corrections:

- SUMCO, “Production Processes,” undated, accessed 2026-09-16: distinguishes crystal growth, wafer forming, and additional specialized processing. [Source](https://www.sumcosi.com/english/products/process/).
- TSMC, “CoWoS,” undated, accessed 2026-09-16: describes integration of logic chiplets and HBM with interposer-based packaging. This supports branching/convergence in the generic map; it does not establish a Rubin-specific implementation. [Source](https://3dfabric.tsmc.com/english/dedicatedFoundry/technology/cowos.htm).

These review references are not substitutes for the chapter-level research and source registration required during implementation.
