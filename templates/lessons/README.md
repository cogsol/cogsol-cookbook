# Lessons Template

A starter project demonstrating how to build a CogSol agent that uses lessons (`BaseLesson`) to internalize best practices and behavioral guidelines.

## Use Case

Use this template when you need an agent that follows specific guidelines or best practices during conversations. Lessons are ideal for:

- Behavioral instructions the agent should always follow.
- Domain-specific best practices and design patterns.
- Style guides, coding standards, or operational procedures.

Unlike FAQs (matched to user questions) or fixed responses (triggered by keys), lessons are always available to the agent as background knowledge that shapes its responses.

This template uses CogSol Framework best practices as sample content. Replace the lessons with your own domain guidelines.

## Prerequisites

- Python 3.9 or higher
- CogSol Framework installed (`pip install -e /path/to/cogsol-framework`)
- A CogSol API account with valid credentials

## Getting Started

```bash
# 1. Copy this template to your workspace
cp -r templates/lessons my-project
cd my-project

# 2. Configure your environment
cp .env.example .env
# Edit .env with your CogSol API credentials

# 3. Generate migrations
python manage.py makemigrations

# 4. Deploy to CogSol API
python manage.py migrate

# 5. Test your agent
python manage.py chat --agent LessonsDocsAgent
```

## What Is Included

| File | Purpose |
|------|---------|
| `agents/lessons/agent.py` | Agent definition with QA generation config |
| `agents/lessons/lessons.py` | Seven lessons covering CogSol best practices |
| `agents/lessons/prompts/lessons.md` | System prompt tailored for best-practice guidance |

### Lessons Included

| Name | Topic |
|------|-------|
| Project Structure | How to organize a CogSol project |
| Naming Conventions | Naming standards for agents, tools, and files |
| Migration Best Practices | Working safely with the migration system |
| Prompt Design | Writing effective system prompts |
| Tool Design | Principles for building agent tools |
| Error Handling | Handling errors in tools and agents |
| Testing Agents | How to test agents during development |

## Customization Notes

- **Replace lessons**: Edit `agents/lessons/lessons.py` to define guidelines for your own domain. Each class needs a `name` and a `content`.
- **Adjust the prompt**: Modify `agents/lessons/prompts/lessons.md` to match your use case and tone.
- **Rename the agent**: Update the class name in `agent.py` and `__init__.py`, adjust `Meta.name` and `Meta.chat_name`, then delete the existing migration file and run `python manage.py makemigrations` to generate a fresh migration.
