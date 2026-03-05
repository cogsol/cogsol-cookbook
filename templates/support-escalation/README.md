# Support Escalation Template

A starter project for building a CogSol agent with a multi-layer support escalation flow: fixed responses, FAQs, semantic search over a knowledge base, and ticket creation via a script tool.

## Use Case

Use this template when you need an agent that handles support requests through progressively deeper resolution layers. The escalation flow works as follows:

1. **Fixed responses** (`BaseFixedResponse`) answer exact-match lookups instantly (e.g., office hours, contact info).
2. **FAQs** (`BaseFAQ`) handle common questions via semantic similarity matching.
3. **Knowledge base search** (`BaseRetrievalTool`) finds relevant articles when FAQs don't cover the topic.
4. **Ticket creation** (`BaseTool`) escalates unresolved issues by calling an external API.

The platform processes fixed responses and FAQs before the message reaches the LLM. If neither matches, the LLM receives the message along with the search and ticket tools, and decides how to proceed.

This pattern is useful when:
- Your support domain has a mix of quick reference answers, common questions, and deeper troubleshooting content.
- Some requests cannot be resolved automatically and need human follow-up.
- You want a single agent that handles the full escalation path.

## Prerequisites

- Python 3.9 or higher
- CogSol Framework installed (`pip install -e /path/to/cogsol-framework`)
- A CogSol API account with valid credentials

## Getting Started

```bash
# 1. Copy this template to your workspace
cp -r templates/support-escalation my-project
cd my-project

# 2. Configure your environment
cp .env.example .env
# Edit .env with your CogSol API credentials

# 3. Generate migrations
python manage.py makemigrations

# 4. Deploy content pipeline to CogSol API (must run before agents)
python manage.py migrate data

# 5. Deploy agent to CogSol API
python manage.py migrate agents

# 6. Add your knowledge base documents to data/knowledgebase/docs/

# 7. Ingest documents
python manage.py ingest knowledgebase data/knowledgebase/docs/ --ingestion-config escalation_ingestion --doc-type Markdown

# 8. Chat with the agent
python manage.py chat --agent SupportEscalationAgent
```

## What Is Included

| File | Purpose |
|------|---------|
| `agents/supportescalation/agent.py` | Agent definition with search and ticket tools |
| `agents/supportescalation/fixed.py` | Scaffold for fixed responses (uncomment to activate) |
| `agents/supportescalation/faqs.py` | Scaffold for FAQs (uncomment to activate) |
| `agents/supportescalation/lessons.py` | Scaffold for lessons (uncomment to activate) |
| `agents/supportescalation/prompts/supportescalation.md` | System prompt for the agent |
| `agents/searches.py` | `EscalationSearch` retrieval tool |
| `agents/tools.py` | `CreateTicket` script tool (POST to mock API) |
| `data/knowledgebase/__init__.py` | `KnowledgeBaseTopic` defining the document collection |
| `data/formatters.py` | `EscalationFormatter` controlling reference appearance |
| `data/ingestion.py` | `EscalationIngestionConfig` for document parsing |
| `data/retrievals.py` | `EscalationRetrieval` configuring semantic search |
| `data/knowledgebase/docs/` | Empty directory for your knowledge base articles |

### Escalation Flow

1. **Fixed responses** (`BaseFixedResponse`): Instant answers for reference lookups matched by exact key.
2. **FAQs** (`BaseFAQ`): Common questions handled by semantic similarity matching.
3. **Knowledge base search** (`BaseRetrievalTool`): Semantic search over your document collection.
4. **Ticket creation** (`BaseTool`): Script tool that POSTs to an external API when no solution is found.

## Customization Notes

- **Add fixed responses**: Uncomment the scaffold in `agents/supportescalation/fixed.py` and add your own key-response pairs. Delete existing migration files and run `python manage.py makemigrations`.
- **Add FAQs**: Uncomment the scaffold in `agents/supportescalation/faqs.py` and add your own question-answer pairs. Delete existing migration files and run `python manage.py makemigrations`.
- **Add lessons**: Uncomment the scaffold in `agents/supportescalation/lessons.py` and add behavioral guidelines. Delete existing migration files and run `python manage.py makemigrations`.
- **Add knowledge base articles**: Place Markdown or PDF files in `data/knowledgebase/docs/` and run the ingest command.
- **Change the ticket API**: Edit the `run` method in `agents/tools.py` to call your real ticketing system instead of the mock API.
- **Tune search**: Adjust `num_refs`, `threshold_similarity`, and chunking settings in `data/retrievals.py` and `data/ingestion.py`.
- **Rename the agent**: Update class names, `Meta.name`, `Meta.chat_name`, directory names, and the prompt filename. Delete existing migration files and run `python manage.py makemigrations`.

See the [support-escalation example](../../examples/support-escalation/README.md) for a complete implementation with IT help desk content.
