# Pretools

An agent that uses pre-processing tools to gather real-time context (date, weather, daily tips) before each response.

## Scenario

You need an assistant that automatically enriches every response with live data. Before the main LLM generation, three pretools run to collect the current date and time, weather conditions, and a rotating tip of the day. The agent then weaves this context naturally into its replies.

## What This Demo Covers

- **Pretools**: `BaseTool` subclasses configured as pre-processing tools via the agent's `pretools` attribute.
- **Prompt context injection**: writing to `data['prompt_params']['context']` so values appear in the system prompt.
- **`pregeneration_config`**: a separate generation config that controls the pre-processing phase.
- **External API call**: the weather pretool queries the free Open-Meteo API (no key required).

### Pretools Included

| Tool | Description |
|------|-------------|
| `CurrentDateTimeTool` | Returns current date, time, day of week, and period of day for Montevideo (UTC-3) |
| `WeatherInfoTool` | Fetches live weather from Open-Meteo (free, no API key) for Montevideo |
| `DailyTipTool` | Rotates through CogSol tips based on the current date |

### How Pretools Differ from Regular Tools

| Aspect | Regular Tools | Pretools |
|--------|---------------|----------|
| Agent attribute | `tools = [...]` | `pretools = [...]` |
| Generation config | `generation_config` | `pregeneration_config` |
| Execution phase | During main response | Before main response |
| Base class | `BaseTool` | `BaseTool` (same) |

## Prerequisites

- Python 3.9 or higher
- CogSol Framework installed (`pip install -e /path/to/cogsol-framework`)
- A CogSol API account with valid credentials
- Internet access (for the weather pretool to reach the Open-Meteo API)

## Run

```bash
cd examples/pretools

# 1. Configure your environment
cp .env.example .env
# Edit .env with your CogSol API credentials

# 2. Apply migrations
python manage.py migrate

# 3. Chat with the agent
python manage.py chat --agent PretoolsAgent
```

## Expected Outcome

When you send a message, the agent responds with real-time context woven into its answer:

```
[PretoolsAgent] Good afternoon! It's 2026-02-20 14:35, Thursday in Montevideo.
Currently 27°C with partly cloudy skies and 15 km/h winds.

**[Tip of the Day]** Pretools run before the main generation phase: use
them to gather context that enriches the agent's response.

How can I help you today?
```

To inspect pretool executions, go to **Activity > Troubleshoot** in the CogSol platform and select a conversation.

## Next Steps

- **Change location**: update `latitude`, `longitude`, and timezone offset in `agents/tools.py`.
- **Add more pretools**: create additional `BaseTool` subclasses and add them to the agent's `pretools` list.
- **Combine with other features**: add FAQs, lessons, or retrieval tools alongside pretools for a richer agent.
