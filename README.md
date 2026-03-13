# CogSol Cookbook

Templates and runnable demos for building with the [CogSol Framework](https://github.com/cogsol/cogsol-framework).

## Repository Layout

Core content:
- [`templates/`](templates/README.md) contains reusable starter projects.
- [`examples/`](examples/README.md) contains specific demos, often more complete and complex than templates.

Supporting contributor infrastructure:
- [`docs/`](docs/) contains reusable README templates for contributors.
- [`.github/`](.github/) contains issue/PR templates and repository automation.
- [`CONTRIBUTING.md`](CONTRIBUTING.md) explains how to propose and submit community contributions.

## Catalog

### Templates

- [`semantic-search`](templates/semantic-search/README.md) — Starting point for building a semantic search agent over your own documents.
- [`orchestrator-subagents`](templates/orchestrator-subagents/README.md) — Orchestrator agent that delegates to specialist sub-agents via built-in assistant services.
- [`support-escalation`](templates/support-escalation/README.md) — Multi-layer escalation flow with fixed responses, FAQs, semantic search, and ticket creation.
- [`azure-storage-upload`](templates/azure-storage-upload/README.md) — Script tool that generates text documents and uploads them to Azure Blob Storage.
- [`external-api`](templates/external-api/README.md) — Script tool that calls an external API using `requests` and platform secrets.

See [`templates/README.md`](templates/README.md) for the template index and conventions.

### Examples

- [`message-metadata`](examples/message-metadata/README.md) — Agent that reads message metadata to personalize responses by language, name, and role.
- [`search-with-filters`](examples/search-with-filters/README.md) - Semantic search with metadata filters (genre, language, decade)
- [`semantic-search`](examples/semantic-search/README.md) — Semantic search without filters using `BaseRetrieval` and `BaseRetrievalTool`.
- [`pretools`](examples/pretools/README.md) — Agent with pre-processing tools for real-time context (date, weather, daily tips).
- [`common-questions`](examples/common-questions/README.md) — Agent with predefined FAQ answers using `BaseFAQ`.
- [`orchestrator-subagents`](examples/orchestrator-subagents/README.md) — Corporate travel assistant with orchestrator + sub-agents pattern.
- [`fixed-responses`](examples/fixed-responses/README.md) — Agent with predefined answers using `BaseFixedResponse`.
- [`search-selector`](examples/search-selector/README.md) - Script tool routing queries to multiple retrievals by topic
- [`lessons`](examples/lessons/README.md) — Agent with behavioral guidelines using `BaseLesson`.
- [`support-escalation`](examples/support-escalation/README.md) — IT help desk with fixed responses, FAQs, semantic search, and ticket creation.
- [`excel-query`](examples/excel-query/README.md) — Expense report review using a script tool that queries Excel attachments with pandas.

See [`examples/README.md`](examples/README.md) for the example index and conventions.

## Adding New Content

When adding a new template or example:
1. Create a dedicated folder under `templates/` or `examples/`.
2. Add a local `README.md` with purpose, setup, and run steps.
3. Register it in:
   - this root `README.md`
   - the corresponding index (`templates/README.md` or `examples/README.md`)

For full contribution steps, see [`CONTRIBUTING.md`](CONTRIBUTING.md).

## Community Workflow

1. Open a proposal issue (`Template Proposal` or `Example Proposal`) if scope is unclear.
2. Submit a pull request using the repository PR template.
3. Ensure local docs are present and index entries are updated.
4. Automated checks verify that new folders include `README.md` and are listed in catalogs.
