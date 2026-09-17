# Manufacturing map audit

Phase 0A architecture gate: structurally implemented; technical population progresses with each module. Review date: 2026-09-16. Review type: author self-review plus automated checks.

The model can represent engineering operations, material states, equipment, failures/detection, suppliers, metrics/economics and product application. Planned later-phase routes are explicitly separated from researched Phase 1 assertions. The overview branches logic and memory, converges packaging inputs, and receives PCBs and power/cooling through appropriate independent paths.

The generator checks references, endpoint types, route conditions, containment/sequence cycles, duplicate relationships, evidence links, source/claim consistency, typed extension tables, article targets, unexplained isolated entities, main-path reachability and stale generated files. Regression tests exercise malformed-data rejection. Human review of claim support and sequence applicability cannot be automated by this script.

No detailed later-phase recipe, supplier market share, Rubin implementation or investment analysis is asserted by the architectural seed. Fine-grained rework/recycling and product overlays are deferred until relevant research exists; their absence does not prevent Phase 1.

## Phase 1 population

Phase 1 adds evidence-backed raw-material/wafer operations and an FZ alternative, materials, equipment, seven representative supplier entities, characteristic/failure detection and boundary-specific accounting metrics. The graph has 71 entities and 86 relationships; later-phase seeds retain planned status. Generated entity pages expose evidence and incoming/outgoing navigation. See the [Phase 1 audit](../AUDIT_PHASE1.md).

## Phase 2 and Phase 3 population

Phase 2 added unit-process functions and an oxide-patterning teaching route. Phase 3 adds alternative device routes, a common compatible MOL boundary and a staged Cu wiring route ending at fabrication with test pending. The current graph has 118 entities and 164 relationships. Aggregate logic/test/die-preparation and downstream product routes retain their earlier planned scope. [Phase 2 audit](../AUDIT_PHASE2.md) · [Phase 3 audit](../AUDIT_PHASE3.md).
