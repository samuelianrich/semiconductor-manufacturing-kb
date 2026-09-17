# Manufacturing graph schema

Schema version 1. [Machine-readable rules](data/schema.json) · [Accepted requirements](../project/PHASE_0A_REVISED_PROPOSAL.md)

## Sources of truth

| File | Responsibility |
|---|---|
| entities.csv | Stable ID, type, name, description, owning module/article, work status and review date |
| process_nodes.csv | Process-only purpose, scope, mechanism summary and notes |
| process_edges.csv | Relationship identity, endpoints, route, conditions and review state |
| materials.csv / equipment.csv / suppliers.csv | Type-specific attributes, keyed to entity IDs |
| evidence_links.csv | Source/locator and optional claim ID supporting a specific field or edge |
| routes.csv | Scope and identity of a route/variant; optional parent route |
| views.json | View selectors and captions; no duplicate relationships |
| schema.json | Types, allowed endpoints, required fields and declared graph exceptions |

IDs never encode current parent or filename; moving an article must not rename its entities. CSV values use UTF-8, standard quoting and one record per relationship. Empty means not entered; `not applicable` and researched `unknown` must be explicit in explanatory fields. No confidence is inferred from blank data.

## Relationship direction

`CONSUMES` points from operation to input in the data. Diagrams reverse that arrow to show input → operation. `PRODUCES` points from operation to output. `PRECEDES` expresses route-specific ordering, not material conversion; it is omitted from material-flow diagrams to avoid duplicate arrows. `PART_OF` is containment. `USES_EQUIPMENT` connects an operation to a machine category. `SUPPLIED_BY` connects an input or machine to a documented supplier. `ENABLES` is an enabling dependency. `CAN_CAUSE`, `DETECTED_BY`, `MEASURES` and `AFFECTS` express failure/control relationships; the conditions explain the mechanism. `ALTERNATIVE_TO` is stored once with IDs in ascending order. `INTEGRATED_INTO` connects a component to its assembly.

Endpoint types and required route/condition fields are enforced by schema.json. No `FOLLOWS` is stored; inverse views are derived. No unqualified `REQUIRES` mixes learning, sequence and material requirements. Containment and route-specific PRECEDES edges are acyclic. If researched rework/recycling becomes necessary, add a separately typed, conditioned relationship and its validation rule rather than weakening sequence checks.

## Evidence and lifecycle

`planned → researched → reviewed` is work status. It is separate from the four company/product confidence labels in [CONFIDENCE_LEVELS.md](../CONFIDENCE_LEVELS.md). Reviewed entity descriptions and reviewed edges require evidence links with a bibliography source ID and exact locator. Supplier edges additionally require a claim ID. The existing [claim register](../42_references/claims.csv) remains authoritative for confidence and product scope. General process citations do not need artificial product labels.

Process summaries and material/equipment attributes summarize the same scoped evidence as their entity descriptions; new independently disputable assertions require a separate field-level evidence link or a new edge/claim. Phase 1 article review checks these prose fields in addition to automated reference existence checks. Sources of unit/metric claims must define the measurement boundary and conditions.

## Route and projection limits

The overview collapses intermediate operations from the physical graph until the next selected material/artifact. It preserves branch reachability, not every assembly input or every substep. The detailed views and evidence tables restore those inputs. Material entities are classes, not the same physical wafer traveling simultaneously down both logic and memory paths.

A reached assembly in this simple graph is a navigational result, not a solver proving all required inputs, capacity, timing and yield are feasible. Planned substrate/board roots are intentional later-phase boundaries. Any completely disconnected node needs an explicit exception in schema.json.

## Review commands

`python3 scripts/manufacturing_map.py` generates views. `python3 scripts/manufacturing_map.py --check` validates references and freshness. `python3 -m unittest discover -s tests` exercises rejection of malformed graphs. The repository validator invokes the map checks too. Human source and technical review remains necessary.
