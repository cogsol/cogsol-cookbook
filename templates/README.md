# Templates

Reusable starter projects for the [CogSol Framework](https://github.com/cogsol/cogsol-framework).

Use templates when you want a quick base to start a new project.

Want to contribute one? Start with [`CONTRIBUTING.md`](../CONTRIBUTING.md).

## Template Index

| Template | Description | Status |
| --- | --- | --- |
| [`orchestrator-subagents`](orchestrator-subagents/README.md) | Orchestrator agent that delegates to specialist sub-agents via built-in assistant services. | Ready |
<!-- CI: templates/orchestrator-subagents/README.md -->
| [`support-escalation`](support-escalation/README.md) | Multi-layer escalation flow with fixed responses, FAQs, semantic search, and ticket creation. | Ready |
<!-- CI: templates/support-escalation/README.md -->

## Template Conventions

Each template should include:
1. A dedicated directory under `templates/`.
2. A `README.md` explaining:
   - what the template is for
   - prerequisites
   - setup and run steps
3. Any required config files with sensible defaults.

Use [`docs/template-readme-template.md`](../docs/template-readme-template.md) as a base for local template docs.
