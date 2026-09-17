# Phase 3 engineering cost-driver notes

| Engineering interface | Quantities a later cost model would need | Why the engineering matters |
|---|---|---|
| [Device integration](../17_transistor_fabrication/planar_and_finfet.md) | Qualified operation count, throughput, rework and parametric yield | A geometry gain can create tighter spacer/gate/thermal constraints |
| [Nanosheet release and gate](../17_transistor_fabrication/nanosheet_integration.md) | Epitaxy, selective-etch and conformal-fill control; defect distribution | More effective channel perimeter does not establish economic yield |
| [MOL contacts](../17_transistor_fabrication/contacts_and_mol.md) | Interface/plug resistance distributions, landing margin and fill defects | Resistance can limit useful performance even with no opens |
| [Wiring](../18_interconnects/wire_rc.md) | Layer-specific geometry, routing demand and extracted RC | Wider wires and added levels use different resources and area |
| [Materials/reliability](../18_interconnects/materials_and_reliability.md) | Qualified stack cost, defect/reliability evidence, replacement process requirements | Bulk metal price or resistivity alone cannot rank integrated options |
| [BEOL repetition](../19_back_end_of_line/beol_integration.md) | Per-level process time, consumables, acceptance and cumulative yield | More levels multiply interface obligations; simple step counts omit yield effects |

No equipment prices, foundry costs, supplier margins or investment conclusions are estimated. Full models remain Phase 10; [investment analysis](../37_investment_analysis/README.md) is separate. Source-supported mechanisms live in the owner chapters; this table states data requirements for future analysis.
