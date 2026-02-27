# Search Selector

A runnable demo showing how to build a CogSol agent that uses a script tool to dynamically route queries to different retrievals based on topic parameters.

## Scenario

A travel guide assistant helps users find information about destinations across three regions: Europe, Asia, and the Americas. Instead of exposing each retrieval as a separate tool to the model, a single script tool receives the topic name and question, looks up the corresponding retrieval via Django ORM, executes the search, and returns aggregated results. Users can ask about a single region or search multiple regions in one query using the `|` separator (e.g., `europe|asia`).

For a generic version of this pattern, see the [`search-selector` template](../../templates/search-selector/README.md).

## What This Demo Covers

- **Script tool routing**: A single `BaseTool` subclass that dynamically selects which retrieval to query at runtime based on a topic parameter.
- **Multiple `BaseTopic` collections**: Three independent document collections (Europe, Asia, Americas), each with its own topic and retrieval.
- **`BaseRetrieval` with predictable naming**: Retrievals named `search_selector_{topic}` so the script tool can look them up by convention.
- **`BaseRetrievalTool`**: Retrieval tools registered on the agent so the Cognitive API creates `Retrieval` records accessible via Django ORM.
- **Multi-topic search**: Querying multiple retrievals in a single tool call and combining results.

## Prerequisites

- Python 3.9 or higher
- CogSol Framework installed (`pip install -e /path/to/cogsol-framework`)
- A CogSol API account with valid credentials

## Run

```bash
# 1. Navigate to this example
cd examples/search-selector

# 2. Configure your environment
cp .env.example .env
# Edit .env with your CogSol API credentials

# 3. Deploy content pipeline to CogSol API (must run before agents)
python manage.py migrate data

# 4. Deploy agent to CogSol API
python manage.py migrate agents

# 5. Ingest the sample travel documents (one command per region)
python manage.py ingest europe data/europe/docs/ --doc-type Markdown
python manage.py ingest asia data/asia/docs/ --doc-type Markdown
python manage.py ingest americas data/americas/docs/ --doc-type Markdown

# 6. Chat with the agent
python manage.py chat --agent TravelGuideAgent
```

## Expected Outcome

After running the steps above, you can chat with `TravelGuideAgent` and ask natural-language questions about travel destinations. The script tool automatically routes queries to the correct region's retrieval and returns relevant results with formatted references.

Example queries:
- "What are the best things to do in Paris?" (single-region, Europe)
- "Compare beaches in Rio de Janeiro and Bali" (multi-region, Americas + Asia)
- "Tell me about street food in Bangkok and Mexico City" (multi-region, Asia + Americas)

Off-topic queries (e.g., "What is the recipe for chocolate cake?") are handled gracefully by the agent.

## What Is Included

| File | Purpose |
|------|---------|
| `agents/tools.py` | `SearchInformation` script tool that routes queries to retrievals by topic name |
| `agents/searches.py` | Three `BaseRetrievalTool` subclasses that register retrievals in the Cognitive API |
| `agents/travelguide/agent.py` | Agent definition with the script tool and retrieval tools |
| `agents/travelguide/prompts/travelguide.md` | System prompt for the agent |
| `data/europe/__init__.py` | `EuropeTopic` defining the European destinations collection |
| `data/asia/__init__.py` | `AsiaTopic` defining the Asian destinations collection |
| `data/americas/__init__.py` | `AmericasTopic` defining the Americas destinations collection |
| `data/formatters.py` | `TravelFormatter` controlling how references appear |
| `data/ingestion.py` | `TravelIngestionConfig` for document parsing and chunking |
| `data/retrievals.py` | Three `BaseRetrieval` subclasses with predictable names for runtime lookup |
| `data/*/docs/*.md` | 12 sample travel destination files in Markdown format |

### Search Selector Pattern

This example demonstrates a key architectural pattern:

1. **Retrieval tools are registered on the agent** so the Cognitive API creates `Retrieval` records that the script tool can look up at runtime. The model may see these tools but routing is handled by the script tool.
2. **A single script tool** (`SearchInformation`) receives `topic` and `question` parameters from the model.
3. **At runtime**, the tool looks up the retrieval by its predictable name (`search_selector_{topic}`) using Django ORM (`Retrieval.objects.get(name=...)`).
4. **Multi-topic search** is supported via the `|` separator (e.g., `europe|asia`), enabling cross-region queries in a single call.

### Sample Destinations

The example includes 12 travel guides across three regions:

| Region | Destinations |
|--------|-------------|
| Europe | Paris, Rome, Barcelona, London |
| Asia | Tokyo, Bangkok, Bali, Seoul |
| Americas | New York, Buenos Aires, Mexico City, Rio de Janeiro |

## Next Steps

- **Add more topics**: Create a new directory under `data/` with a `BaseTopic` subclass, a matching `BaseRetrieval` in `data/retrievals.py`, and a `BaseRetrievalTool` in `agents/searches.py`. Add the new retrieval tool to the agent's `tools` list. The retrieval name must follow the `search_selector_{topic}` convention.
- **Add metadata filters**: To enable filtering by fields like country or climate, see the [`search-with-filters`](../search-with-filters/README.md) example for the full pattern.
- **Adjust retrieval settings**: Edit `data/retrievals.py` to change `num_refs`, `threshold_similarity`, or enable reordering.
- **Replace the content**: Swap the travel docs with your own documents. Update topic names and descriptions accordingly.
