# Common Questions Template

A starter project demonstrating how to build a CogSol agent that uses FAQs (`BaseFAQ`) to provide consistent answers to common questions.

## Use Case

Use this template when you need an agent that handles frequently asked questions with predefined, consistent answers. FAQs are ideal for:

- Conceptual questions about your product or domain.
- Onboarding queries where users need consistent explanations.
- Any scenario where the agent should match user intent to a curated set of answers.

This template uses CogSol Framework documentation as sample content. Replace the FAQs with your own domain questions and answers.

## Prerequisites

- Python 3.9 or higher
- CogSol Framework installed (`pip install -e /path/to/cogsol-framework`)
- A CogSol API account with valid credentials

## Getting Started

```bash
# 1. Copy this template to your workspace
cp -r templates/common-questions my-project
cd my-project

# 2. Configure your environment
cp .env.example .env
# Edit .env with your CogSol API credentials

# 3. Generate migrations
python manage.py makemigrations

# 4. Deploy to CogSol API
python manage.py migrate

# 5. Test your agent
python manage.py chat --agent CommonQuestionsDocsAgent
```

## What Is Included

| File | Purpose |
|------|---------|
| `agents/commonquestions/agent.py` | Agent definition with QA generation config |
| `agents/commonquestions/faqs.py` | Seven FAQs covering CogSol conceptual topics |
| `agents/commonquestions/prompts/commonquestions.md` | System prompt tailored for conceptual documentation assistance |

### FAQs Included

| Question | Topic |
|----------|-------|
| What is the CogSol Framework? | Framework overview and purpose |
| What is an agent in CogSol? | Agent concept and role |
| How do migrations work in CogSol? | Migration system explanation |
| What are tools and how do agents use them? | Tools concept and usage |
| What is the difference between FAQs and fixed responses? | Feature comparison |
| What is the Content API used for? | Content API purpose |
| Can an agent have multiple tools at once? | Multi-tool agents |

## Customization Notes

- **Replace FAQs**: Edit `agents/commonquestions/faqs.py` to define questions and answers for your own domain. Each class needs a `question` and an `answer`.
- **Adjust the prompt**: Modify `agents/commonquestions/prompts/commonquestions.md` to match your use case and tone.
- **Rename the agent**: Update the class name in `agent.py` and `__init__.py`, adjust `Meta.name` and `Meta.chat_name`, then delete the existing migration file and run `python manage.py makemigrations` to generate a fresh migration.
