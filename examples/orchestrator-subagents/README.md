# Orchestrator + Sub-Agents

A runnable demo showing how to build a CogSol orchestrator agent that delegates tasks to specialized sub-agents using a script tool and the platform's built-in assistant services.

## Scenario

A corporate travel assistant helps employees plan business trips. The user describes their travel needs in natural language. An orchestrator agent calls a single script tool that internally consults three specialized sub-agents (flights, hotels, expense policies), each with its own knowledge base. The tool consolidates all responses and returns a unified travel plan.

## What This Demo Covers

- **Orchestrator pattern**: A main agent that coordinates multiple specialized sub-agents to handle complex requests.
- **Agent-to-agent communication**: A `BaseTool` script tool that calls other CogSol agents at runtime using the platform's built-in `create_chat_parallel` service ([docs](https://docs.cogsol.ai/docs/Tools/Script%20tools#talk-to-assistants)).
- **Multiple agents in one project**: Four `BaseAgent` subclasses deployed from a single CogSol project.
- **Independent knowledge bases**: Three `BaseTopic` collections (flights, hotels, policies), each backing a separate sub-agent with its own `BaseRetrieval`.
- **Two-phase deployment**: Sub-agents are deployed first, then the orchestrator is updated with their IDs.

## Prerequisites

- Python 3.9 or higher
- CogSol Framework installed (`pip install -e /path/to/cogsol-framework`)
- A CogSol API account with valid credentials

## Run

This example requires a two-phase deployment because the orchestrator's script tool needs the sub-agent IDs, which are assigned by the platform at deploy time.

### Phase 1: Deploy all agents and data

```bash
# 1. Navigate to this example
cd examples/orchestrator-subagents

# 2. Configure your environment
cp .env.example .env
# Edit .env with your CogSol API credentials

# 3. Deploy content pipeline (must run before agents)
python manage.py migrate data

# 4. Ingest sample documents
python manage.py ingest flights data/flights/docs/ --doc-type Markdown
python manage.py ingest hotels data/hotels/docs/ --doc-type Markdown
python manage.py ingest policies data/policies/docs/ --doc-type Markdown

# 5. Deploy all four agents
python manage.py migrate agents
```

After step 5, open `agents/migrations/.state.json` and note the IDs assigned to `FlightSearchAgent`, `HotelSearchAgent`, and `ExpensePolicyAgent`.

### Phase 2: Update orchestrator with sub-agent IDs

1. Open `agents/tools.py` and update the `agent_ids` dictionary inside the `run()` method with the real IDs from `.state.json`.
2. Re-deploy:

```bash
python manage.py makemigrations
python manage.py migrate agents
```

### Chat

```bash
# Chat with the orchestrator
python manage.py chat --agent TravelOrchestratorAgent

# Or chat with individual sub-agents
python manage.py chat --agent FlightSearchAgent
python manage.py chat --agent HotelSearchAgent
python manage.py chat --agent ExpensePolicyAgent
```

## Expected Outcome

After completing both phases, you can chat with `TravelOrchestratorAgent` and make natural-language travel requests.

Example query:
- "I need to fly from Buenos Aires to Madrid next Monday, returning March 7. I'd like a hotel near Castellana."

The orchestrator's `PlanTravel` tool will internally consult all three sub-agents (flights, hotels, policies) and return a single consolidated travel plan. You can also chat with each sub-agent individually to verify their knowledge bases work correctly.

## What Is Included

| File | Purpose |
|------|---------|
| `agents/tools.py` | `PlanTravel` script tool that calls all three sub-agents in parallel and returns a consolidated plan |
| `agents/searches.py` | Three `BaseRetrievalTool` subclasses (flights, hotels, policies) |
| `agents/travelorchestrator/agent.py` | Orchestrator agent with the script tool |
| `agents/flightsearch/agent.py` | Flight search sub-agent with retrieval tool |
| `agents/hotelsearch/agent.py` | Hotel search sub-agent with retrieval tool |
| `agents/expensepolicy/agent.py` | Expense policy sub-agent with retrieval tool |
| `data/flights/docs/*.md` | 6 flight route documents (Buenos Aires, London, New York, Bogota, Mexico City, Sao Paulo to Madrid) |
| `data/hotels/docs/*.md` | 6 hotel documents across Madrid (business district, city center, airport area) |
| `data/policies/docs/*.md` | 5 corporate travel policy documents (flights, hotels, meals, approvals, expense reporting) |
| `data/retrievals.py` | Three `BaseRetrieval` subclasses, one per topic |
| `data/formatters.py` | Shared `TravelFormatter` for document references |
| `data/ingestion.py` | Shared `TravelIngestionConfig` for document parsing |

### Orchestrator Pattern

This example demonstrates agent-to-agent communication:

1. **The orchestrator receives a natural-language request** from the user (e.g., "plan my trip to Madrid").
2. **The LLM calls the `PlanTravel` tool** with the user's full request.
3. **The tool consults all three sub-agents in parallel** (flights, hotels, policies) using the platform's built-in `create_chat_parallel` service ([docs](https://docs.cogsol.ai/docs/Tools/Script%20tools#talk-to-assistants)), each in a separate chat session.
4. **The tool returns a single consolidated response** with sections for each specialist.
5. **The orchestrator presents** the travel plan to the user.

### Content Pipeline

Each sub-agent has its own knowledge base:

| Topic | Documents | Content |
|-------|-----------|---------|
| `flights` | 6 route files | Airlines, schedules, prices, airports for routes to Madrid |
| `hotels` | 6 hotel files | Locations, rates, amenities, corporate rates in Madrid |
| `policies` | 5 policy files | Flight class rules, hotel limits, meal allowances, approvals, expense reporting |

## Next Steps

- **Add more sub-agents**: Create a new agent with its own retrieval, add it to the `agent_ids` map in the script tool, and redeploy.
- **Change the domain**: Replace the travel content with your own documents and adjust agent prompts accordingly.
- **Explore other features**: Combine this pattern with [pretools](../pretools/README.md) to inject user context before orchestration, or with [search-with-filters](../search-with-filters/README.md) to add metadata filtering to sub-agent retrievals.
