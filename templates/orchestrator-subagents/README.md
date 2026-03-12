# Orchestrator Sub-Agents Template

A starter project demonstrating how to build a CogSol orchestrator agent that delegates tasks to specialized sub-agents using a script tool and the platform's built-in assistant services.

## Use Case

Use this template when you need a main agent that coordinates multiple specialist agents to handle complex, multi-domain requests. Instead of a single agent trying to handle everything, the orchestrator calls each sub-agent via the platform's built-in `create_chat_parallel` service, collects their responses in parallel, and returns a consolidated result to the user.

This pattern is useful when:
- Your domain naturally splits into distinct specialties (e.g., flights + hotels, diagnosis + treatment).
- Each specialist benefits from its own knowledge base, tools, or prompt tuning.
- You want a single user-facing agent that hides the internal routing.

This template includes an orchestrator and two generic specialist sub-agents. The orchestrator's script tool calls both sub-agents internally and returns a single consolidated response.

## Prerequisites

- Python 3.9 or higher
- CogSol Framework installed (`pip install -e /path/to/cogsol-framework`)
- A CogSol API account with valid credentials

## Getting Started

```bash
# 1. Copy this template to your workspace
cp -r templates/orchestrator-subagents my-project
cd my-project

# 2. Configure your environment
cp .env.example .env
# Edit .env with your CogSol API credentials

# 3. Generate migrations
python manage.py makemigrations

# 4. Deploy sub-agents first
python manage.py migrate agents

# 5. Note sub-agent IDs from agents/migrations/.state.json
#    Update agent_ids in agents/tools.py with the real IDs

# 6. Regenerate and redeploy with updated IDs
python manage.py makemigrations
python manage.py migrate agents

# 7. Test your agent
python manage.py chat --agent OrchestratorAgent
```

## What Is Included

| File | Purpose |
|------|---------|
| `agents/tools.py` | `ConsultSpecialists` script tool that calls all sub-agents in parallel and returns a consolidated response |
| `agents/orchestrator/agent.py` | Orchestrator agent with the script tool |
| `agents/orchestrator/prompts/orchestrator.md` | System prompt for the orchestrator |
| `agents/specialista/agent.py` | First specialist sub-agent (customize for your domain) |
| `agents/specialistb/agent.py` | Second specialist sub-agent (customize for your domain) |
| `agents/searches.py` | Scaffold for retrieval tools (activate if sub-agents need search) |
| `data/` | Scaffold data layer (activate if sub-agents need Content API) |

### Orchestrator Pattern

1. **The orchestrator receives a request** from the user.
2. **The LLM calls the `ConsultSpecialists` tool** with the user's request.
3. **The tool calls all sub-agents in parallel** using the platform's built-in `create_chat_parallel` service ([docs](https://docs.cogsol.ai/docs/Tools/Script%20tools#talk-to-assistants)), each in a separate chat session.
4. **The tool returns a single consolidated response** with sections from each specialist.
5. **The orchestrator presents** the result to the user.

### Two-Phase Deployment

Sub-agent IDs are assigned by the platform at deploy time. The orchestrator's script tool needs these IDs to call the sub-agents. This requires deploying twice:
1. First deploy creates all agents and assigns IDs.
2. Update `agents/tools.py` with the real IDs, then redeploy.

## Customization Notes

- **Rename agents**: Update class names, `Meta.name`, `Meta.chat_name`, directory names, and `__init__.py` imports. Delete existing migration files and run `python manage.py makemigrations`.
- **Add more sub-agents**: Create a new agent directory, add it to the `agent_ids` map in `agents/tools.py`, and redeploy.
- **Add search to sub-agents**: Activate the scaffold files in `agents/searches.py`, `data/retrievals.py`, and the rest of the data layer. Import the retrieval tool in the sub-agent's `agent.py`. See the [orchestrator-subagents example](../../examples/orchestrator-subagents/README.md) for a complete implementation.
- **Change the tool behavior**: Edit the `run` method in `agents/tools.py` to add conditional routing, result formatting, or error handling logic.
