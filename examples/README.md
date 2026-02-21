# Examples

Runnable, scenario-driven demos for the [CogSol Framework](https://github.com/cogsol/cogsol-framework).

Examples are typically more specific and more complete than templates.
They can combine multiple features to demonstrate realistic workflows.

Want to contribute one? Start with [`CONTRIBUTING.md`](../CONTRIBUTING.md).

## Example Index

| Example | Description | Status |
| --- | --- | --- |
| [search-with-filters](search-with-filters/README.md) | Semantic search with metadata filters using `BaseRetrieval`, `BaseMetadataConfig`, and `BaseRetrievalTool` | Ready |
<!-- CI: examples/search-with-filters/README.md -->

## Example Conventions

Each example should include:
1. A dedicated directory under `examples/`.
2. A `README.md` explaining:
   - what the example demonstrates
   - the scenario and expected outcome
   - prerequisites
   - setup and run steps
3. Code that is explicit and runnable, even if the demo is multi-step or more complex than a template.

Use [`docs/example-readme-template.md`](../docs/example-readme-template.md) as a base for local example docs.
