# GEO schema

Extract every JSON-LD script from each sampled page, including arrays and @graph. Check parse errors, @context, @type, identifier reuse, URL normalization, sameAs identity, and consistency with visible text. Report the exact script or node and URL. If markup is client-rendered, distinguish it from the initial HTML.

Select types describing genuine content such as Person, Organization, Article, Product or LocalBusiness. Verify applicable type properties and current search-provider feature requirements before recommending rich results. Draft minimal JSON-LD using only verified attributes. Validate resulting JSON and entity relationships. Consult ../specialists/geo-schema.md. Record provider validator outcomes only when actually run.
