# Pretools Template

A starter project demonstrating how to build a CogSol agent that uses pretools (`BaseTool` configured as pre-processing tools) to gather real-time context before responding.

## Use Case

Use this template when you need an agent that gathers information **before** the main response generation. Pretools are ideal for:

- Fetching real-time data (date, time, weather, exchange rates).
- Loading user or session context from external systems.
- Pre-classifying or enriching the user's message before the main LLM processes it.

Pretools use the same `BaseTool` base class as regular tools. The difference is configuration: they are listed in the agent's `pretools` attribute, use a separate `pregeneration_config`, and inject their results into `data['prompt_params']['context']` so the LLM receives them automatically.

This template includes four pretools that demonstrate different patterns: stdlib-only, external API call, local data rotation, and tool message injection.

## Prerequisites

- Python 3.9 or higher
- CogSol Framework installed (`pip install -e /path/to/cogsol-framework`)
- A CogSol API account with valid credentials
- Internet access (for the weather pretool to reach the Open-Meteo API)

## Getting Started

```bash
# 1. Copy this template to your workspace
cp -r templates/pretools my-project
cd my-project

# 2. Configure your environment
cp .env.example .env
# Edit .env with your CogSol API credentials

# 3. Generate migrations
python manage.py makemigrations

# 4. Deploy to CogSol API
python manage.py migrate

# 5. Test your agent
python manage.py chat --agent PretoolsAgent
```

## What Is Included

| File | Purpose |
|------|---------|
| `agents/pretools/agent.py` | Agent definition with `pretools` and `pregeneration_config` |
| `agents/tools.py` | Four pretool implementations using `BaseTool` |
| `agents/pretools/prompts/pretools.md` | System prompt for the agent |

### Pretools Included

| Tool | Injection Pattern | Description |
|------|-------------------|-------------|
| `CurrentDateTimeTool` | Prompt context | Returns current date, time, day of week, and period of day for Montevideo (UTC-3) |
| `WeatherInfoTool` | Prompt context | Fetches live weather from Open-Meteo (free, no API key) for Montevideo |
| `DailyTipTool` | Prompt context | Rotates through CogSol tips based on the current date |
| `PlatformStatusTool` | Tool messages | Checks platform status and injects the result as tool call/response messages |

### Two Ways to Inject Data

Pretools can inject data into the agent's flow in two ways:

**1. Prompt context**: Write to `data['prompt_params']['context']`. The data appears as key-value pairs in the system prompt. Simple and direct. Used by `CurrentDateTimeTool`, `WeatherInfoTool`, and `DailyTipTool`.

**2. Tool messages**: Create assistant (tool call) and tool (response) messages in the conversation history. The model sees a structured tool interaction, as if it already called a tool and received a result. Used by `PlatformStatusTool`.

### How Pretools Differ from Regular Tools

| Aspect | Regular Tools | Pretools |
|--------|---------------|----------|
| Agent attribute | `tools = [...]` | `pretools = [...]` |
| Generation config | `generation_config` | `pregeneration_config` |
| Execution phase | During main response | Before main response |
| Base class | `BaseTool` | `BaseTool` (same) |

### Viewing Pretool Executions

To see pretool executions and their results, go to **Activity > Troubleshoot** in the CogSol platform. Select a conversation to inspect the full message history, including:

- Tool call and tool response messages created by `PlatformStatusTool`
- The context data injected by the other pretools (visible in the system prompt)
- Pretool execution logs

## Customization Notes

- **Change location**: Update the `latitude`, `longitude`, and timezone offset in `agents/tools.py` to target a different city.
- **Add more pretools**: Create additional `BaseTool` subclasses in `agents/tools.py` and add them to the agent's `pretools` list.
- **Replace pretools**: Swap the example pretools with your own: user context loaders, session initializers, or any pre-processing logic your agent needs.
- **Rename the agent**: Update the class name in `agent.py` and `__init__.py`, adjust `Meta.name` and `Meta.chat_name`, then delete the existing migration file and run `python manage.py makemigrations` to generate a fresh migration.
