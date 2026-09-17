# Phase 3 architecture and integration comparisons

| Choice | Physical distinction | Main integration constraints | Canonical explanation |
|---|---|---|---|
| Planar | Channel near a planar surface beneath a gate | Isolation, gate stack, lateral junction/spacer control | [Planar/FinFET](../17_transistor_fabrication/planar_and_finfet.md) |
| Tri-gate FinFET | Gate couples to top and sidewalls of a raised body | Fin geometry, isolation recess, conformal gate and source/drain access | [Planar/FinFET](../17_transistor_fabrication/planar_and_finfet.md) |
| Stacked nanosheet | Gate surrounds several thin horizontal channels | Alternating stack, inner spacers, release, stiction and inter-sheet gate fill | [Nanosheets](../17_transistor_fabrication/nanosheet_integration.md) |
| Gate-first / replacement gate | Functional gate retained earlier / temporary gate replaced later | Thermal compatibility versus removal/fill complexity | [Gate integration](../17_transistor_fabrication/planar_and_finfet.md) |
| Source/drain contact / gate contact / wiring via | Semiconductor carrier-transfer interface / gate-electrode access / connection between conductors | Different landing, interface and isolation requirements | [MOL](../17_transistor_fabrication/contacts_and_mol.md) |
| Cu / W / Co / Ru | Candidate conductor roles depend on geometry and process | Compare complete line/plug resistance, fill, etch and reliability under equal conditions | [Materials](../18_interconnects/materials_and_reliability.md) |
| Single / dual damascene | Separate feature fill / shared trench-via fill | Cavity sequence, barrier/seed and fill continuity | [BEOL](../19_back_end_of_line/beol_integration.md) |
| Damascene / subtractive route | Pattern dielectric then fill / pattern deposited metal | Metal-specific etch and gap-fill constraints; not a name-only substitution | [BEOL](../19_back_end_of_line/beol_integration.md) |
| Immediate defect / wear-out | Present at fabrication / evolves during relevant stress | Distinct sampling, localization and reliability evidence | [Reliability](../18_interconnects/materials_and_reliability.md) |

These are engineering comparisons, not node rankings, vendor performance tables or assertions about Rubin. Referenced research routes are not automatically high-volume product implementations.
