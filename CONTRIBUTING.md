# Contributing to CogSol Cookbook

Thanks for helping grow the cookbook.

This repository accepts community contributions for:
- new templates
- new examples
- improvements to docs and structure

## Quick Start

1. Fork the repository.
2. Create a branch with a descriptive name.
3. Add your template or example.
4. Update the indexes:
- `README.md`
- `templates/README.md` or `examples/README.md`
5. Open a pull request.

## Add a Template

1. Create a folder: `templates/<template-slug>/`
2. Add `templates/<template-slug>/README.md`
3. Include runnable starter files needed for the template.
4. Add a row to `templates/README.md`.
5. Add a link to the global catalog in `README.md`.

Use `docs/template-readme-template.md` as a starting point for the local README.

## Add an Example

1. Create a folder: `examples/<example-slug>/`
2. Add `examples/<example-slug>/README.md`
3. Build a runnable demo for a specific scenario (it can span multiple features).
4. Add a row to `examples/README.md`.
5. Add a link to the global catalog in `README.md`.

Use `docs/example-readme-template.md` as a starting point for the local README.

## Quality Checklist

Before opening a PR, confirm:
- The contribution has a clear purpose and title.
- The local README has setup and run instructions.
- The relevant index README is updated.
- The root README catalog is updated.
- Paths and commands in docs are correct.

## Proposals and Discussion

If you are unsure about scope, open an issue first using:
- `Template Proposal`
- `Example Proposal`

This helps align on direction before implementation.
