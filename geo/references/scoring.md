# Evidence and diagnostic scores

Use this rubric for every Codex workflow. It supersedes scoring examples, deductions, platform rankings and growth claims in upstream helpers or templates. Scores summarize checks within a declared sample. Report observed AI answers and citations separately.

## Select the sample

Record the URL set, page roles, intended audience and language, audit time and intended search access. Share one evidence collection across specialist passes. Assign an identifier to each inspected URL and external source. Cite the identifier and a short excerpt, header, field or observation with each finding. Describe incomplete fetches, untested services and ambiguous identity matches explicitly.

## Rate the checks

Use the upstream category weights only for continuity. Each semicolon-delimited item in the table is one check. Evaluate each applicable check for each sampled page or, for brand-level facts, once for the entity. A pass earns 1, mixed evidence earns 0.5 and an observed failure earns 0. Explain each mixed result. Record unknown and inapplicable separately with reasons. Do not convert either into a numerical result.

| Category | Weight | Checks |
|---|---:|---|
| Answer clarity | 25% | Page answers its stated question; answer identifies the subject when quoted alone; material qualifiers and evidence accompany the answer |
| Brand identity and corroboration | 20% | Primary identity is unambiguous; first-party profiles agree on material facts; independent corroboration supports externally attributed claims |
| Content quality | 20% | Reader can identify the accountable author or organization; evidence supports material claims; examples or methods substantiate the promised expertise |
| Technical access | 15% | Target URL returns usable content; index directives and canonical match site intent; intended discovery path reaches the page |
| Structured data | 10% | Applicable markup parses; entities match visible facts; entity identifiers and relationships resolve consistently |
| Platform readiness | 10% | Current documented platform eligibility requirements can be checked for the requested surface; the page meets applicable requirements; relevant search access matches publisher intent |

For schema, mark absence inapplicable when the page has no relevant markup requirement or declared implementation goal. Mark external corroboration unknown if search was unavailable. Assess platform requirements individually and identify each platform and source. Treat optional files including llms.txt, training opt-outs, writing style and passage length as descriptive observations. Never penalize them by default.

For each category, calculate 100 × points / rated checks. Show the rated, unknown and inapplicable counts. If any applicable check is unknown, label its category partial. Publish the weighted composite only when all six categories have rated checks and no applicable check is unknown. Round once to the nearest whole number. Otherwise give available category results, sample coverage and gaps. Compare numbers across runs only with matching sample, rubric and measurement conditions.

## Report observed visibility

Log the question, language, surface, model when shown, date, repeated trials, answer excerpt, brand match and cited URLs. Give numerators and denominators for observed mentions and citations. Bound conclusions to that sample. Keep tool heuristics labeled with their source and version. Derive implementation priorities from the observed user or crawler impact and confidence. A change in readiness score does not quantify a change in traffic or citations.
