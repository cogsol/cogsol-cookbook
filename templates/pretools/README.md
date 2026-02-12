# Pretools Template

A starter project demonstrating how to build a CogSol agent that uses pretools (`BaseTool` configured as pre-processing tools) to gather real-time context before responding.

## Use Case

Use this template when you need an agent that gathers information **before** the main response generation. Pretools are ideal for:

- Fetching real-time data (date, time, weather, exchange rates).
- Loading user or session context from external systems.
- Pre-classifying or enriching the user's message before the main LLM processes it.

Pretools use the same `BaseTool` base class as regular tools. The difference is configuration: they are listed in the agent's `pretools` attribute, use a separate `pregeneration_config`, and inject their results into `data['prompt_params']['context']` so the LLM receives them automatically.

This template includes three pretools that demonstrate different patterns: stdlib-only, external API call, and local data rotation.

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
| `agents/tools.py` | Three pretool implementations using `BaseTool` |
| `agents/pretools/prompts/pretools.md` | System prompt that instructs the agent to use pretool context |

### Pretools Included

| Tool | Pattern | Description |
|------|---------|-------------|
| `CurrentDateTimeTool` | stdlib (`datetime`) | Returns current date, time, day of week, and period of day for Montevideo (UTC-3) |
| `WeatherInfoTool` | External API (`urllib`) | Fetches live weather from Open-Meteo (free, no API key) for Montevideo |
| `DailyTipTool` | Local data rotation | Rotates through CogSol tips based on the current date |

### How Pretools Differ from Regular Tools

| Aspect | Regular Tools | Pretools |
|--------|---------------|----------|
| Agent attribute | `tools = [...]` | `pretools = [...]` |
| Generation config | `generation_config` | `pregeneration_config` |
| Execution phase | During main response | Before main response |
| Context injection | LLM calls tools explicitly | Write to `data['prompt_params']['context']` |
| Base class | `BaseTool` | `BaseTool` (same) |

## Customization Notes

- **Change location**: Update the `latitude`, `longitude`, and timezone offset in `agents/tools.py` to target a different city.
- **Add more pretools**: Create additional `BaseTool` subclasses in `agents/tools.py` and add them to the agent's `pretools` list.
- **Replace pretools**: Swap the example pretools with your own — user context loaders, session initializers, or any pre-processing logic your agent needs.
- **Rename the agent**: Update the class name in `agent.py` and `__init__.py`, adjust `Meta.name` and `Meta.chat_name`, then delete the existing migration file and run `python manage.py makemigrations` to generate a fresh migration.
