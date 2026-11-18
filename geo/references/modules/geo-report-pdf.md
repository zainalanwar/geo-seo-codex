# GEO report pdf

Use an existing Markdown audit or generate it via the report workflow. Resolve templates/geo-report-template.html and templates/geo-report-style.css relative to the installed skill root. Check for pandoc and a Chromium/Chrome browser. Keep paths with spaces as single arguments.

Render a local HTML5 document via pandoc using --standalone, --embed-resources, --template and --css, with the reviewed local template and CSS. Pass verified brand_name, domain, date and any recorded score/label as separate --metadata arguments. Review external resource references before embedding. Print the resulting local HTML using Chromium headless with --print-to-pdf=<absolute-output> and a file URI. Use a temporary browser profile. Check that the resulting PDF opens, the title matches and all sections are present. If a renderer is missing, report the missing dependency and retain the Markdown deliverable.
