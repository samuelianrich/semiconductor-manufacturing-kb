# Persistent manufacturing process map

This is the manufacturing navigation layer. Learning prerequisites remain in the [module dependency graph](../DEPENDENCIES.md). The CSV files own entity identity and relationships; repeated diagrams and tables are generated from them.

Start with the [master overview](master_process_map.md), then choose a path:

- [Raw materials to wafer](wafer_path.md)
- [Logic die](logic_path.md) and [DRAM to HBM](hbm_path.md)
- [Package convergence](packaging_path.md)
- [Package to rack](system_path.md)

Explore cross-cutting views: [materials](materials_map.md), [equipment](equipment_map.md), [suppliers](supplier_map.md), [failure and detection](yield_map.md), [economics](economics_map.md), [Rubin evidence boundary](rubin_manufacturing_path.md).

[Full entity register](process_nodes.md) · [Schema and edge meanings](SCHEMA.md) · [Audit](AUDIT.md)

A **planned** node or edge defines intended research scope. It is not evidence of a generic production recipe, named supplier relationship or product implementation. Read the status and evidence columns. A **reviewed** assertion has received a recorded author self-review against its source, not independent peer review.

Run `python3 scripts/manufacturing_map.py` from the repository root after editing CSVs. Run `python3 scripts/manufacturing_map.py --check` to detect invalid references or stale views. Do not hand-edit generated blocks. Explain scientific limits and route conditions in the owning article; the map is an index, not a substitute for prose.

## Available Phase 1 content

Follow the [wafer route](wafer_path.md) through reviewed operations, or select [equipment](equipment_map.md), [materials](materials_map.md), [supplier roles](supplier_map.md), [failure/detection](yield_map.md) and [accounting metrics](economics_map.md). The [entity register](process_nodes.md) gives source evidence, neighboring entities and canonical articles. The source-backed physical path currently ends at the accepted-wafer boundary; later branches retain planned labels.
