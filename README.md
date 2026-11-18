# GEO for Codex

A Codex skill for auditing how a website presents its content to search engines and AI search services. Findings include the inspected URL, observed evidence and a way to verify the change. AI citation measurements require sampled answers from the relevant service.

## Install

Clone the repository, then copy the bundled skill into a project's skill directory. Run these commands from the target project. The destination must be available.

```sh
git clone https://github.com/zainalanwar/geo-seo-codex.git
mkdir -p .agents/skills
test ! -e .agents/skills/geo && cp -R geo-seo-codex/geo .agents/skills/
```

Open Codex in the target project and enter:

```text
$geo audit https://example.com
```

Use `$geo quick` for a single URL, `$geo crawlers` to inspect search access, or `$geo report-pdf` with a saved Markdown audit. See all 17 workflows in the [skill instructions](geo/SKILL.md).

## Dependencies and tests

The Python helpers require Python 3.10+ and [core dependencies](geo/requirements.txt). The optional CRM dashboard uses [additional packages](geo/requirements-crm.txt). PDF rendering requires Pandoc and Chrome or Chromium. The release test also requires Poppler's pdftotext on PATH. Set CHROME_BIN to the browser executable if needed.

From a checkout with uv installed, run:

```sh
uv run --isolated --with pytest --with-requirements geo/requirements.txt python -m pytest -q geo/tests
```

The release test serves a temporary site over HTTP, runs the installed helper scripts, builds a report from fetched evidence and checks the text in the rendered PDF. Other tests cover HTML decoding, server-rendered content and crawler directives.

Adapted from Zubair Trabzada's geo-seo-claude. [Provenance](geo/PROVENANCE.md) · [MIT license](geo/LICENSE)
