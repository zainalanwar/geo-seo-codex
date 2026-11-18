# GEO for Codex

Adapted from [geo-seo-claude at 989cae0](https://github.com/zubair-trabzada/geo-seo-claude/tree/989cae01e8ebbc42a9ec798eb9e7cb423f5ec89c) under the bundled MIT license.

The entrypoint routes 17 workflows. The 15 upstream subskills are condensed into task guides in references/modules, and the five upstream agents are reference material in references/specialists. The original helper scripts, schema examples, report templates and white-label utilities accompany the port. Use references/scoring.md for the Codex diagnostic rubric.

To install this checkout on another machine, link its geo directory into the user's ~/.agents/skills directory under the name geo. Keep the checkout in place while that link is active. Invoke the skill with a request such as `$geo quick https://example.com`.
