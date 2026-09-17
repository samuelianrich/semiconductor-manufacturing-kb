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
