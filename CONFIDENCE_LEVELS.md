# Confidence-label system

Apply a label immediately beside every important company- or product-specific technical claim. One paragraph with mixed evidence must be split or labeled per claim. Labels describe evidence type and scope, not a probability or endorsement.

| Exact label | Use when | Required accompanying evidence |
|---|---|---|
| **CONFIRMED** | A reliable primary source directly supports the narrowly worded claim | Citation, locator, date and conditions; preserve company attribution for marketing or self-reported results |
| **INDUSTRY-STANDARD INFERENCE** | Exact implementation is undisclosed but a conclusion follows reasonably from established practice and known constraints | Cite premises, explain reasoning, alternatives and what would falsify it; explicitly say it is not disclosed implementation |
| **ANALYST ESTIMATE** | A named third party provides an estimate, teardown or supply-chain assessment | Identify analyst/organization, publication date, source and method/uncertainty where available |
| **UNKNOWN / PROPRIETARY** | Reliable public evidence is insufficient | State what is known, what remains unknown, plausible alternatives only if defensible, and evidence needed to resolve it |

## Wording patterns (templates, not claims)

- `CONFIRMED — [Company] states [specific specification] for [product/version] in [dated source], under [conditions]. Claim ID: …`
- `INDUSTRY-STANDARD INFERENCE — Given [cited premise A] and [cited premise B], [conclusion] is plausible because [reason]. [Alternative] remains possible; [evidence] would distinguish them. Claim ID: …`
- `ANALYST ESTIMATE — [Named source, date] estimates [value/range], using [method if stated]. This is not a company disclosure. Claim ID: …`
- `UNKNOWN / PROPRIETARY — Public evidence reviewed as of [date] does not establish [detail]. [Known fact] is insufficient to choose between [alternatives]. Claim ID: …`

## Important limits

A published patent does not confirm use in Rubin. A foundry capability does not confirm a customer's exact stack or recipe. A packaging brand does not confirm every subvariant. A standards-compliant interface does not identify a memory vendor. A company-reported performance number can be confirmed as a disclosed claim without being independently demonstrated performance.

Do not use `ANALYST ESTIMATE` for an invented classroom assumption. Label it **Hypothetical worked example** outside this evidence system. Unknown is an acceptable final research result; do not upgrade it for narrative completeness.

General principles need citations but not forced product-confidence tags. Company facts in ecosystem and investment pages use the same discipline as the case study. On review, downgrade stale or contradicted evidence with an explanation; never automatically promote repeated rumors to confirmation.
