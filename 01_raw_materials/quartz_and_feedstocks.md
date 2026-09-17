# Quartz, silica and qualified furnace feedstock

Status: **Reviewed — author self-review; specialist review pending**. Owner: repository author. Article type: foundation explainer. Scope: general engineering; no proprietary process recipe. Source review: 2026-09-16.

## Prerequisites

Introductory chemistry: elements, compounds and mass fractions. Start from the [physical overview](../manufacturing_map/master_process_map.md).

## Why this matters — 30-second explanation

A silicon wafer does not begin as a naturally occurring slab of electronic-grade silicon. Its silicon atoms are initially bound in minerals. Quartz is crystalline silicon dioxide, SiO₂; silica names the compound, while silicon names the element. Silicate minerals contain silicon too, but they are not interchangeable furnace feedstocks. USGS identifies quartz and quartzite as silica sources for silicon metal. [USGS-SILICON-001](../42_references/bibliography.md#usgs-silicon-001)

The first task is **qualification**: decide whether a particular mined material can serve a particular process. Being abundant in Earth's crust is different from being chemically clean, mechanically suitable and consistently deliverable.

## Intuition: composition and location both matter

Imagine sorting rice from stones. Loose stones can be separated; a contaminant embedded inside each grain is a different problem. For quartz, unwanted material may occur as separate minerals, surface contamination or inclusions enclosed within the quartz. Beneficiation means selectively removing unwanted constituents to upgrade an ore. A laboratory study of one Iranian deposit combined physical separation and chemical treatment; it also illustrates the tradeoff between cleaner product and recovered material. That result is not a universal smelter or semiconductor qualification. [CHEGINI-QUARTZ-001](../42_references/bibliography.md#chegini-quartz-001)

## From deposit to charge

A useful scope for the first process node is:

1. Characterize the deposit and sample its variability.
2. Extract material, then crush and screen it into controlled size fractions.
3. Remove unsuitable or impurity-rich fractions by the methods warranted by the ore.
4. Test the candidate feed for both composition and behavior during heating.
5. Accept, segregate for a different use, or reject the lot against the receiving process's specification.

This is a representative engineering organization of the work, not a claim that every mine uses a flotation or acid-leaching plant. NTNU's quartz research emphasizes that cracking and disintegration on heating can change furnace performance even when material is chemically quartz. [NTNU-QUARTZ-001](../42_references/bibliography.md#ntnu-quartz-001)

**Screening** separates particle sizes. **Scrubbing** removes loosely adhering material. **Magnetic separation** targets magnetic constituents; it does not remove every impurity. **Flotation** uses differences in surface behavior to separate minerals. Chemical purification is a further option for appropriate products and impurity forms, not a required treatment of every smelting charge. The selected sequence follows characterization. [CHEGINI-QUARTZ-001](../42_references/bibliography.md#chegini-quartz-001)

## Two quartz supply paths

Do not collapse these branches:

- **Silicon feedstock:** silica is chemically reduced to silicon in the next stage.
- **Quartzware feedstock:** suitably purified silica becomes fused-quartz crucibles or other process hardware that contacts or contains material.

**CONFIRMED — CLM-000001:** Elkem describes Tana as a quartzite extraction operation with quartz supplied for industrial alloy-related uses. **CONFIRMED — CLM-000002:** Sibelco describes its IOTA quartz as feedstock for fused-quartz crucibles used in CZ growth and for semiconductor quartzware. These establish different supplier roles, not an exclusive supply chain. [ELKEM-QUARTZ-001](../42_references/bibliography.md#elkem-quartz-001) [SIBELCO-QUARTZ-001](../42_references/bibliography.md#sibelco-quartz-001)

The crucible path joins [crystal growth](../03_crystal_growth/crystal_growth.md) as a process input; it does not mean every silicon atom in the growing crystal came from that crucible supplier.

## Materials, machines and controls

The charge includes carbon reductants as well as quartz. Coal, charcoal and petroleum coke are among the carbon sources discussed in primary silicon-furnace research. Carbon chemistry and furnace operation are developed in [metallurgical silicon](../02_silicon_refining/metallurgical_silicon.md). [NTNU-SMELTING-001](../42_references/bibliography.md#ntnu-smelting-001)

| Question | Relevant control or observation | Consequence to investigate |
|---|---|---|
| Is composition consistent? | Representative sampling and chemical assay | Averages may hide an unsuitable sublot |
| Is the size distribution suitable? | Crusher settings and screen fractions | Compare the selected product with the receiver's charge requirements |
| Does the quartz break up on heating? | Thermal-disintegration assessment | Determine whether nominally similar sources behave differently |
| Where are impurities located? | Mineralogical examination plus chemical analysis | Choose separation methods that can actually reach the impurity |

The first and last rows distinguish measuring *how much* impurity exists from understanding *where* it exists. Do not infer semiconductor trace-contamination limits from a bulk ore assay. [NTNU-QUARTZ-001](../42_references/bibliography.md#ntnu-quartz-001) [CHEGINI-QUARTZ-001](../42_references/bibliography.md#chegini-quartz-001)

## Worked example: grade and recovery are different

**Hypothetical mass-balance exercise.** Suppose a 100 kg feed contains 95 kg of silica. A separation gives 90 kg of product at 99% silica by mass.

$$
R_{\mathrm{SiO_2}}=\frac{m_p x_p}{m_f x_f}
=\frac{90\times0.99}{100\times0.95}=0.938
$$

Here $m_p,m_f$ are product/feed masses in kg, and $x_p,x_f$ are dimensionless silica mass fractions. Silica recovery is **93.8%**, although product grade is **99%**. Mass yield is 90%. These answer different questions: purity, retention of the desired constituent, and total mass retained. The numbers are invented to teach bookkeeping, not measurements from a mine.

The receiver must still ask which impurities make up the remaining 1%. A single percentage cannot establish electrical suitability.

## Handoff and checks for understanding

The output is an accepted feedstock category, with size and impurity requirements attached. The next operation changes the chemical compound, rather than merely sorting it.

Explain why: (1) two quartz sources with similar bulk chemistry may behave differently in a furnace; (2) higher product purity need not mean higher silica recovery; and (3) a crucible-quartz supplier cannot automatically be named as the source of a GPU's silicon atoms.

## Position in the manufacturing map

[MAT-0001](../manufacturing_map/process_nodes.md#mat-0001), [MAT-0002](../manufacturing_map/process_nodes.md#mat-0002), [PROC-0001](../manufacturing_map/process_nodes.md#proc-0001). These are process/material categories, not a tracked customer lot. Concept pages link to the operations they explain rather than inventing a physical manufacturing step.

## Rubin connection and evidence boundary

No mine, feedstock supplier, wafer specification, process recipe or transistor implementation is assigned to Rubin here. The [case-study plan](../38_case_studies/nvidia_rubin/README.md) and [Rubin map](../manufacturing_map/rubin_manufacturing_path.md) preserve that boundary. Company examples in these chapters are documented roles, not a Rubin bill of materials.

## Separate economics and further learning

Process cost drivers are recorded in the [Phase 1 evidence notes](../36_economics/phase1_cost_drivers.md); full [industry analysis](../37_investment_analysis/README.md) remains a later phase. Use the [glossary](../40_glossary/phase1_glossary.md) for definitions and the [learning sequence](../LEARNING_PATHS.md) for navigation.

## Sources and review

- [USGS-SILICON-001](../42_references/bibliography.md#usgs-silicon-001)
- [NTNU-QUARTZ-001](../42_references/bibliography.md#ntnu-quartz-001)
- [CHEGINI-QUARTZ-001](../42_references/bibliography.md#chegini-quartz-001)
- [ELKEM-QUARTZ-001](../42_references/bibliography.md#elkem-quartz-001)
- [SIBELCO-QUARTZ-001](../42_references/bibliography.md#sibelco-quartz-001)
- [NTNU-SMELTING-001](../42_references/bibliography.md#ntnu-smelting-001)

Source locators and limitations are in the canonical bibliography. Review scope: original synthesis, scoped mathematical examples and conceptual figures. Independent specialist review has not been performed. Final module review is recorded in [AUDIT_PHASE1.md](../AUDIT_PHASE1.md).
