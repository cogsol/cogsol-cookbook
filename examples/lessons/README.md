# Lessons

An agent that uses lessons (`BaseLesson`) to internalize best practices and behavioral guidelines about the CogSol platform.

## Scenario

You need an agent that follows specific guidelines during conversations. Unlike FAQs (matched to user questions) or fixed responses (triggered by keys), lessons are always available to the agent as background knowledge that shapes its responses.

This demo uses six lessons about CogSol platform best practices. Each lesson includes a `context_of_application` field that tells the model when to apply that knowledge.

## What This Demo Covers

- Defining lessons with `BaseLesson`, including the optional `context_of_application` attribute.
- Attaching lessons to an agent so they are available as persistent background knowledge.
- Writing a system prompt that leverages internalized guidelines.

## Prerequisites

- Python 3.9 or higher
- CogSol Framework installed (`pip install -e /path/to/cogsol-framework`)
- A CogSol API account with valid credentials

## Run

```bash
cd examples/lessons

# Configure your environment
cp .env.example .env
# Edit .env with your CogSol API credentials

# Apply migrations
python manage.py migrate

# Chat with the agent
python manage.py chat --agent LessonsDocsAgent
```

## Expected Outcome

The agent responds to questions about the CogSol platform by drawing on its internalized lessons. Ask about topics like assistant configuration, content management, or troubleshooting and the agent will provide guidance shaped by its lesson knowledge.

## Next Steps

- Replace the sample lessons in `agents/lessons/lessons.py` with guidelines for your own domain.
- Adjust the system prompt in `agents/lessons/prompts/lessons.md` to match your use case.
- Combine lessons with other features like FAQs (`common-questions` example) or fixed responses (`fixed-responses` example) for richer agent behavior.
