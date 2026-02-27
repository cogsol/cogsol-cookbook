# Fixed Responses

A runnable demo showing how to build a CogSol agent that delivers predefined answers using `BaseFixedResponse`.

## Scenario

Your organization needs an assistant that provides exact, pre-approved responses for key topics — installation steps, CLI commands, environment setup — where consistency matters more than generative flexibility. Fixed responses guarantee the same answer every time a matching topic is triggered.

This demo uses CogSol Framework documentation as sample content. Replace the fixed responses with your own domain content.

## What This Demo Covers

- `BaseFixedResponse` for defining key-based predefined answers.
- `BaseAgent` with `genconfigs.QA()` for a conversational Q&A agent.
- System prompt customization via `Prompts.load()`.
- Migration workflow to deploy fixed responses to the CogSol API.

## Prerequisites

- Python 3.9 or higher
- CogSol Framework installed (`pip install -e /path/to/cogsol-framework`)
- A CogSol API account with valid credentials

## Run

```bash
cd examples/fixed-responses

# 1. Configure your environment
cp .env.example .env
# Edit .env with your CogSol API credentials

# 2. Apply migrations
python manage.py migrate

# 3. Chat with the agent
python manage.py chat --agent FixedResponsesDocsAgent
```

## Expected Outcome

The agent responds to documentation questions using the seven predefined fixed responses:

| Key | Topic |
|-----|-------|
| `installation` | How to install the CogSol Framework |
| `prerequisites` | Required tools and versions |
| `create_project` | Steps to create a new project |
| `create_agent` | Steps to create and deploy an agent |
| `migrations` | How the migration system works |
| `available_commands` | List of all CLI commands |
| `environment_setup` | How to configure the .env file |

For questions outside the fixed response set, the agent falls back to its system prompt and general knowledge.

## Next Steps

- Replace the fixed responses in `agents/fixedresponses/fixed.py` with your own domain content. Each class needs a `key` and a `response`.
- Adjust the system prompt in `agents/fixedresponses/prompts/fixedresponses.md` to match your use case.
- Combine fixed responses with FAQs or lessons for richer agent behavior.
