# Common Questions

A runnable demo showing how to build a CogSol agent that answers frequently asked questions using `BaseFAQ`.

## Scenario

Your team maintains a knowledge base and users keep asking the same conceptual questions. Instead of relying solely on free-form generation, you configure a set of curated FAQ pairs so the agent delivers consistent, accurate answers every time.

This demo uses CogSol Framework documentation as sample content. Replace the FAQs with your own domain questions and answers.

## What This Demo Covers

- `BaseFAQ` for defining question-answer pairs.
- `BaseAgent` with `genconfigs.QA()` for a conversational Q&A agent.
- System prompt customization via `Prompts.load()`.
- Migration workflow to deploy FAQs to the CogSol API.

## Prerequisites

- Python 3.9 or higher
- CogSol Framework installed (`pip install -e /path/to/cogsol-framework`)
- A CogSol API account with valid credentials

## Run

```bash
cd examples/common-questions

# 1. Configure your environment
cp .env.example .env
# Edit .env with your CogSol API credentials

# 2. Apply migrations
python manage.py migrate

# 3. Chat with the agent
python manage.py chat --agent CommonQuestionsDocsAgent
```

## Expected Outcome

The agent responds to conceptual questions about the CogSol Framework using the seven predefined FAQs:

| Question | Topic |
|----------|-------|
| What is the CogSol Framework? | Framework overview and purpose |
| What is an agent in CogSol? | Agent concept and role |
| How do migrations work in CogSol? | Migration system explanation |
| What are tools and how do agents use them? | Tools concept and usage |
| What is the difference between FAQs and fixed responses? | Feature comparison |
| What is the Content API used for? | Content API purpose |
| Can an agent have multiple tools at once? | Multi-tool agents |

For questions outside the FAQ set, the agent falls back to its system prompt and general knowledge.

## Next Steps

- Replace the FAQs in `agents/commonquestions/faqs.py` with your own domain questions and answers.
- Adjust the system prompt in `agents/commonquestions/prompts/commonquestions.md` to match your use case.
- Combine FAQs with other features like fixed responses or lessons for richer agent behavior.
