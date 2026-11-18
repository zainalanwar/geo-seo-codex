# GEO prospect

Support new, list [stage], show, audit, note, status, won, lost and pipeline. Use the user's designated local CRM file, or the upstream compatible ~/.geo-prospects/prospects.json for an explicitly requested CRM operation. Listing a missing store returns an empty pipeline. Use the existing array of records with id, domain, company, status, notes, audit_file and updated_at. Preserve other keys. Accept a record by ID or normalized domain. Stages are lead, qualified, proposal, won and lost.

For new, reject duplicate domains and allocate an unused PRO-NNN ID. For note append dated text. For status/won/lost store the requested stage, supplied value/currency or loss reason. For audit produce the report before linking it to the record. For pipeline group by stage, separate confirmed and potential values by currency, and label forecasts and assumptions.

Use a file lock across read, validation, update and atomic replacement in the same directory. Refuse to overwrite malformed data. Keep private CRM records local. Only modify records for requested operations. Avoid filling in missing contacts, currency, values or notes by inference.
