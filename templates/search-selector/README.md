# Search Selector Template

A starter project demonstrating how to build a CogSol agent that uses a single script tool to dynamically route queries to different retrievals based on topic parameters.

## Use Case

Use this template when you have multiple document collections (topics) and want a single tool to select which retrieval to query at runtime. Instead of exposing each retrieval as a separate tool on the agent, a script tool receives the topic name, looks up the corresponding retrieval via Django ORM, executes the search, and aggregates results.

This pattern is useful when:
- You have many topics and don't want to pollute the agent's tool list.
- You want to search across multiple topics in a single tool call using the `|` separator.
- You need centralized control over how retrievals are selected and results are combined.

This template uses a travel guide with three regions (Europe, Asia, Americas) as sample content. Users can ask about destinations and the tool automatically searches the correct region.

## Prerequisites

- Python 3.9 or higher
- CogSol Framework installed (`pip install -e /path/to/cogsol-framework`)
- A CogSol API account with valid credentials

## Getting Started

```bash
# 1. Copy this template to your workspace
cp -r templates/search-selector my-project
cd my-project

# 2. Configure your environment
cp .env.example .env
# Edit .env with your CogSol API credentials

# 3. Generate migrations
python manage.py makemigrations

# 4. Deploy to CogSol API (data first, then agents)
python manage.py migrate data
python manage.py migrate agents

# 5. Ingest the sample travel documents
python manage.py ingest europe data/europe/docs/ --doc-type Markdown
python manage.py ingest asia data/asia/docs/ --doc-type Markdown
python manage.py ingest americas data/americas/docs/ --doc-type Markdown

# 6. Test your agent
python manage.py chat --agent SearchSelectorAgent
```

## What Is Included

| File | Purpose |
|------|---------|
| `agents/tools.py` | `SearchInformation` script tool that routes queries to retrievals by topic name |
| `agents/searches.py` | Three `BaseRetrievalTool` subclasses that register retrievals in the Cognitive API |
| `agents/searchselector/agent.py` | Agent definition with the script tool and retrieval tools |
| `agents/searchselector/prompts/searchselector.md` | System prompt for the agent |
| `data/europe/__init__.py` | `EuropeTopic` defining the European destinations collection |
| `data/asia/__init__.py` | `AsiaTopic` defining the Asian destinations collection |
| `data/americas/__init__.py` | `AmericasTopic` defining the Americas destinations collection |
| `data/formatters.py` | `TravelFormatter` controlling how references appear |
| `data/ingestion.py` | `TravelIngestionConfig` for document parsing and chunking |
| `data/retrievals.py` | Three `BaseRetrieval` subclasses with predictable names for runtime lookup |
| `data/*/docs/*.md` | 12 sample travel destination files in Markdown format |

### Search Selector Pattern

This template demonstrates a key architectural pattern:

1. **Retrieval tools are registered on the agent** so the Cognitive API creates `Retrieval` records that the script tool can look up at runtime. The model may see these tools but routing is handled by the script tool.
2. **A single script tool** (`SearchInformation`) receives `topic` and `question` parameters from the model.
3. **At runtime**, the tool looks up the retrieval by its predictable name (`search_selector_{topic}`) using Django ORM (`Retrieval.objects.get(name=...)`).
4. **Multi-topic search** is supported via the `|` separator (e.g., `europe|asia`), enabling cross-region queries in a single call.

### Sample Destinations

The template includes 12 travel guides across three regions:

| Region | Destinations |
|--------|-------------|
| Europe | Paris, Rome, Barcelona, London |
| Asia | Tokyo, Bangkok, Bali, Seoul |
| Americas | New York, Buenos Aires, Mexico City, Rio de Janeiro |

## Customization Notes

- **Add more topics**: Create a new directory under `data/` with a `BaseTopic` subclass, a matching `BaseRetrieval` in `data/retrievals.py`, and a `BaseRetrievalTool` in `agents/searches.py`. Add the new retrieval tool to the agent's `tools` list. The retrieval name must follow the `search_selector_{topic}` convention.
- **Change the routing logic**: Edit the `run` method in `agents/tools.py` to implement custom selection rules, fallbacks, or result formatting.
- **Adjust retrieval settings**: Edit `data/retrievals.py` to change `num_refs`, `threshold_similarity`, or enable reordering.
- **Replace the content**: Swap the travel docs with your own documents. Update topic names and descriptions accordingly.
- **Rename the agent**: Update the class name in `agent.py` and `__init__.py`, adjust `Meta.name` and `Meta.chat_name`, then delete existing migration files and run `python manage.py makemigrations`.
