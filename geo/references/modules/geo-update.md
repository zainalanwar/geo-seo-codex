# GEO update

Identify the installed Codex port, its source workspace and pinned upstream commit from its provenance. Resolve the upstream Git HEAD and compare commits in a temporary checkout. Summarize changed modules, helpers, dependencies, license and local port conflicts. Preserve local adaptations and report available changes on an update check.

For an explicit upgrade, stage changes to the Codex port in a separate checkout, review the diff, run the port's validations, then use its own installation method. Never execute the upstream Claude installer as a Codex upgrade. Preserve the previous installation, local modifications and CRM data. Report old/new revisions and validation results.
