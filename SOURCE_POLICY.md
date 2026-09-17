# Citation and source policy

## Source hierarchy and fitness

Prefer peer-reviewed technical literature; IEEE/IEDM/ISSCC/VLSI proceedings; manufacturer and foundry documentation; equipment technical materials; university research; patents; SEMI and standards bodies; filings/investor presentations; credible engineering publications; research firms; teardown firms; analysts; and high-quality technical journalism, in that approximate order.

Fitness matters more than mechanical ranking: an official dated specification may be the best support for a product interface, while a peer-reviewed paper may best explain a mechanism. A patent establishes what was disclosed, not that a process was deployed. A standard establishes a definition or permitted interface, not which implementation a company selected. A filing's audited financial data and management's forward-looking commentary have different evidentiary status.

Avoid generic SEO material, unsourced social media and low-quality blogs. Wikipedia may orient a search but should not normally be the final technical citation. Distinguish marketing performance assertions from independently measured results.

## Stable IDs and canonical bibliography

Use `[ORG-TOPIC-NNN]`, with uppercase ASCII letters/digits and three or more serial digits, for example `ASML-EUV-001`. These are format examples only, not existing evidence. IDs are permanent: never reuse an ID for another document or recycle a deleted entry. Prefer a document's DOI/canonical identity when deduplicating; track editions/revisions separately when relevant.

The canonical registry is [42_references/bibliography.md](42_references/bibliography.md). Each record has an explicit HTML anchor matching the lowercase ID. Chapters cite it with a normal relative Markdown link such as `[ASML-EUV-001](../42_references/bibliography.md#asml-euv-001)` after the supported sentence. Add a section/page locator in prose. Do not insert an example link until that real record exists.

Each article's Sources section lists only used IDs with locators and short support notes; it links to canonical records instead of copying metadata. One source supporting several pages retains one ID. Cite precise claims at their point of use; a bibliography at the bottom alone is insufficient.

## Bibliography record fields

Required: stable ID; exact title; authors or corporate author; organization; publication; publication date or `not stated`; document version; URL; DOI where available; actual access date; relevant page/section locator; source type; claim scope; limitations; rights/access conditions. DOI and original publication URL are preferred over search links. Do not claim a document was accessed if only its abstract or snippet was read.

No external papers, standards or vendor figures are copied into this repository by default. Subdirectories store original reading notes and legal metadata. Store third-party full text or figures only when redistribution permission is documented.

## Claim traceability

Use stable claim IDs `CLM-000001` onward in [claims.csv](42_references/claims.csv). Required for important company/product claims and quantitative industrial claims. Capture exact claim, entity, product variant, scope/conditions, confidence label, source IDs, locator, source date, as-of date, review date and status. If no public evidence exists, mark unknown and record the search boundary.

A technical principle still needs an inline citation, even if it does not need a company-claim register entry. A hypothetical teaching example must say it is hypothetical and is not product data.

## Conflicts, corrections and aging

Present Claim A and Claim B with sources, dates and scope in an `Areas of Uncertainty` section. Explain whether definitions, product variants, measurement conditions, timing or evidence quality may cause disagreement. Do not average incompatible specifications or silently choose one. Update the claim register when resolving a conflict and retain the reason in Git history.

Treat announcements as announcements, targets as targets, and measured results as measurements. A press release confirms the company made the statement; it does not independently verify every performance assertion. Dates, qualifiers, and comparison baselines travel with the claim.

External link reachability does not prove factual support. Human review must read the cited passage and check its applicability to the actual sentence.
