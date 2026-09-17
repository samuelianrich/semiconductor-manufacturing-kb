# Repository conventions and quality gates

## Audience and writing

Write for a second-year undergraduate in electrical engineering. Follow intuition → mechanism → implementation → manufacturing reality → deeper detail. Define specialized vocabulary at first use, explain its purpose and link to its canonical explanation. Analogies must disclose their limits. Prefer accurate approachable prose to unqualified simplifications.

## Files and metadata

Use lowercase snake_case filenames, stable numbered module directories, UTF-8 Markdown and relative links within the repository. Each topic has one canonical owner. Do not create empty chapter files to imply progress. Put scope in indexes until research begins. Use explicit stable anchors when a citation or glossary term needs permanence.

Each article identifies status, owner, type, scope and last technical review date. Use ISO dates with a clear as-of meaning. Use SI units unless another convention is necessary; state conversions and unit prefixes. Equations define all symbols and assumptions next to the equation. Every quantitative example distinguishes real sourced data from teaching assumptions.

The module registry is the source of truth for module identifiers, paths, phases and prerequisite edges. When changing it, update the displayed graph and inventory in the same commit. When articles are scoped, add their own prerequisite and related links; run cycle review if promoting an edge to a mandatory prerequisite.

## Evidence and scope

Use [source policy](SOURCE_POLICY.md) and [confidence labels](CONFIDENCE_LEVELS.md). Do not make buy/sell recommendations, invent proprietary detail, turn announcements into shipment facts or treat a node name as a literal device dimension. Engineering stays in topic modules; cost models in 36; industry analysis in 37. Cross-link these layers.

## Human article review checklist

- Reader outcome and prerequisites are explicit; terminology is introduced and glossary links exist.
- Inline sources support actual claims and preserve measurement conditions and dates.
- Company/product claims carry appropriate labels and register entries; uncertainty is not hidden.
- Input/output, equipment, materials, variables, defects, yield effects and alternatives are covered where applicable.
- Upstream, downstream and lateral relationships are linked; canonical explanations are not duplicated.
- Diagrams have titles, captions, source/rights data, accessible explanations and scale/geometry caveats.
- Every equation defines variables, units, assumptions and a checked example when useful.
- Economics and investment interpretation are separate; Rubin examples do not distort general explanations.
- Conflicts, stale evidence and unknowns are visible; no unsupported marketing claims remain.

## Structural validation

Run `python3 scripts/validate.py`. It checks required files, module paths, prerequisite IDs and cycles, phase dependencies, graph synchronization, local Markdown link targets/explicit anchors, bibliography-ID uniqueness and registered asset paths. It is not a source validator, physics reviewer or proof of completeness. Phase 12 adds substantive source, glossary, contradiction, orphan and freshness review across actual articles.

## Git workflow

Use one coherent scope per commit: architecture/policy, an article and its assets, or a citation correction. Run checks before committing; inspect the staged diff. Use descriptive messages such as `Add Czochralski growth mechanism and process diagram`. Do not commit secrets, restricted PDKs, copyrighted PDFs without rights, build caches or unrelated files. A populated article should not be committed as reviewed until human checks pass.

For external collaboration, use a branch and pull request with problem, resulting content and validation. Preserve source IDs and file locations or provide link migrations. Record meaningful corrections in the maintenance log or commit message.
