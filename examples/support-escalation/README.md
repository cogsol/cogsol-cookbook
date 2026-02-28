# Support Escalation

A complete example of a CogSol agent that combines fixed responses, FAQs, semantic search, and ticket creation to demonstrate a multi-feature escalation flow.

## Scenario

You run a corporate IT help desk. Employees ask questions that range from quick reference lookups (office hours, contact info) to troubleshooting problems (network issues, printer setup) to requests that need human follow-up (hardware failures, access problems). A single agent handles the full escalation path:

1. **Fixed responses** answer exact-match lookups instantly (office hours, contact info, locations, emergency line).
2. **FAQs** handle common how-to questions via semantic similarity (password resets, VPN setup, equipment requests).
3. **Knowledge base search** finds relevant troubleshooting articles when FAQs don't cover the topic.
4. **Ticket creation** escalates unresolved issues to the IT team by calling a mock REST API.

## What This Demo Covers

- **`BaseFixedResponse`**: Quick reference answers triggered by exact key match.
- **`BaseFAQ`**: Predefined question-answer pairs matched by semantic similarity.
- **`BaseTopic`** + **`BaseRetrieval`** + **`BaseRetrievalTool`**: Semantic search over a knowledge base of IT articles.
- **`BaseTool`** (script tool): Calling an external API (`requests.post`) to create support tickets.
- **Escalation flow**: Combining all four feature types in a single agent.

## Prerequisites

- Python 3.9 or higher
- CogSol Framework installed (`pip install -e /path/to/cogsol-framework`)
- A CogSol API account with valid credentials

## Run

```bash
# 1. Navigate to this example
cd examples/support-escalation

# 2. Configure your environment
cp .env.example .env
# Edit .env with your CogSol API credentials

# 3. Deploy content pipeline to CogSol API (must run before agents)
python manage.py migrate data

# 4. Deploy agent to CogSol API
python manage.py migrate agents

# 5. Ingest the IT knowledge base articles
python manage.py ingest knowledgebase data/knowledgebase/docs/ --ingestion-config helpdesk_ingestion --doc-type Markdown

# 6. Chat with the agent
python manage.py chat --agent SupportEscalationAgent
```

## Expected Outcome

After deployment, you can chat with `SupportEscalationAgent` and exercise each layer of the escalation flow. Try these messages in order to see each escalation level in action:

| # | Send this message | What happens | Layer |
|---|-------------------|--------------|-------|
| 1 | `office_hours` | Returns the predefined schedule instantly, before the LLM is invoked. | Fixed response |
| 2 | `How do I reset my password?` | Matches the FAQ by semantic similarity and returns step-by-step instructions. | FAQ |
| 3 | `My printer shows offline` | The LLM calls the knowledge base search tool and returns the relevant troubleshooting article. | Semantic search |
| 4 | `My laptop keeps showing a blue screen with error code 0x0000007E every time I open Excel` | No article matches, so the agent creates a support ticket via the mock API and returns the ticket number. | Ticket creation |

Other fixed response keys you can try: `contact_info`, `office_locations`, `emergency_support`.

## What Is Included

| File | Purpose |
|------|---------|
| `agents/supportescalation/agent.py` | Agent definition with search and ticket tools |
| `agents/supportescalation/fixed.py` | 4 fixed responses (office hours, contact, locations, emergency) |
| `agents/supportescalation/faqs.py` | 6 FAQs (password, VPN, equipment, software, ticketing, mobile email) |
| `agents/supportescalation/lessons.py` | Lesson scaffold (commented out) |
| `agents/supportescalation/prompts/supportescalation.md` | System prompt for the agent |
| `agents/searches.py` | `HelpDeskSearch` retrieval tool |
| `agents/tools.py` | `CreateTicket` script tool (POST to mock API) |
| `data/knowledgebase/__init__.py` | `KnowledgeBaseTopic` defining the document collection |
| `data/formatters.py` | `HelpDeskFormatter` controlling reference appearance |
| `data/ingestion.py` | `HelpDeskIngestionConfig` for document parsing |
| `data/retrievals.py` | `HelpDeskRetrieval` configuring semantic search |
| `data/knowledgebase/docs/*.md` | 8 IT knowledge base articles |

### Escalation Flow

This example demonstrates a complete support escalation pipeline:

1. **Fixed responses** (`BaseFixedResponse`): Instant answers for reference lookups matched by exact key.
2. **FAQs** (`BaseFAQ`): Common questions handled by semantic similarity matching.
3. **Knowledge base search** (`BaseRetrievalTool`): Full-text semantic search over IT troubleshooting articles.
4. **Ticket creation** (`BaseTool`): Script tool that POSTs to an external API when no solution is found.

The platform processes fixed responses and FAQs before the message reaches the LLM. If neither matches, the LLM receives the message along with the search and ticket tools, and decides how to proceed.
