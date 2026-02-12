# Fixed Responses Template

A starter project demonstrating how to build a CogSol agent that uses fixed responses (`BaseFixedResponse`) to provide predefined answers for specific topics.

## Use Case

Use this template when you need an agent that delivers consistent, pre-approved responses for common questions. Fixed responses are ideal for:

- Standardized answers that must not vary (e.g., legal disclaimers, policies).
- Frequently asked questions with definitive answers.
- Controlled information delivery where accuracy is critical.

This template uses CogSol Framework documentation as sample content. Replace the fixed responses with your own domain content.

## Prerequisites

- Python 3.9 or higher
- CogSol Framework installed (`pip install -e /path/to/cogsol-framework`)
- A CogSol API account with valid credentials

## Getting Started

```bash
# 1. Copy this template to your workspace
cp -r templates/fixed-responses my-project
cd my-project

# 2. Configure your environment
cp .env.example .env
# Edit .env with your CogSol API credentials

# 3. Generate migrations
python manage.py makemigrations

# 4. Deploy to CogSol API
python manage.py migrate

# 5. Test your agent
python manage.py chat --agent FixedResponsesDocsAgent
```

## What Is Included

| File | Purpose |
|------|---------|
| `agents/fixedresponses/agent.py` | Agent definition with QA generation config |
| `agents/fixedresponses/fixed.py` | Seven fixed responses covering CogSol documentation topics |
| `agents/fixedresponses/prompts/fixedresponses.md` | System prompt tailored for documentation assistance |
| `settings.py` | Project configuration |
| `manage.py` | CLI entry point |
| `.env.example` | Environment variable template |

### Fixed Responses Included

| Key | Topic |
|-----|-------|
| `installation` | How to install the CogSol Framework |
| `prerequisites` | Required tools and versions |
| `create_project` | Steps to create a new project |
| `create_agent` | Steps to create and deploy an agent |
| `migrations` | How the migration system works |
| `available_commands` | List of all CLI commands |
| `environment_setup` | How to configure the .env file |

## Customization Notes

- **Replace fixed responses**: Edit `agents/fixedresponses/fixed.py` to define responses for your own domain. Each class needs a `key` (trigger identifier) and a `response` (predefined text).
- **Adjust the prompt**: Modify `agents/fixedresponses/prompts/fixedresponses.md` to match your use case and tone.
- **Rename the agent**: Update the class name in `agent.py` and `__init__.py`, adjust `Meta.name` and `Meta.chat_name`, then delete any existing migration files and run `python manage.py makemigrations` to generate a fresh migration.
