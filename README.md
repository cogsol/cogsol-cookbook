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

- [`search-selector`](templates/search-selector/README.md) — Agent with a script tool that dynamically routes queries to retrievals by topic.

See [`templates/README.md`](templates/README.md) for the template index and conventions.

### Examples

No examples yet.

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
