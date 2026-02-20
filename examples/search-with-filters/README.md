# Search With Filters

A runnable demo showing how to build a CogSol agent that performs semantic search with metadata filters using `BaseRetrieval`, `BaseMetadataConfig`, and `BaseRetrievalTool`.

## Scenario

A movie recommendation assistant lets users search a catalog of 12 films by plot, theme, or mood. Users can optionally narrow results by genre, language, or decade (e.g. "a suspenseful movie set in space" or "a French comedy from the 2000s").

For a simpler version without filters, see the `semantic-search` example.

## What This Demo Covers

- **`BaseTopic`**: Defining a named document collection in the Content API.
- **`BaseMetadataConfig`**: Declaring structured fields (genre, language, decade) attached to documents and used as search filters.
- **`BaseIngestionConfig`**: Configuring how uploaded files are parsed and split into searchable blocks.
- **`BaseReferenceFormatter`**: Controlling how document references appear in the agent's responses.
- **`BaseRetrieval`**: Setting up semantic search with a `filters` list linking to the metadata configs.
- **`BaseRetrievalTool`**: Exposing the retrieval as a tool with `parameters` that map to the available filters.
- **Custom ingestion script**: Uploading documents with per-document metadata via the `CogSolClient` API.

## Prerequisites

- Python 3.9 or higher
- CogSol Framework installed (`pip install -e /path/to/cogsol-framework`)
- A CogSol API account with valid credentials

## Run

```bash
# 1. Copy this example to your workspace
cp -r examples/search-with-filters my-project
cd my-project

# 2. Configure your environment
cp .env.example .env
# Edit .env with your CogSol API credentials

# 3. Generate migrations
python manage.py makemigrations

# 4. Deploy to CogSol API (data first, then agents)
python manage.py migrate data
python manage.py migrate agents

# 5. Ingest movies with metadata
python scripts/ingest_movies.py

# 6. Test your agent
python manage.py chat --agent MovieSearchAgent
```

## Expected Outcome

- The agent responds to natural-language movie queries with relevant results from the ingested catalog.
- When filters are provided (genre, language, decade), results are narrowed accordingly.
- Each result includes a formatted reference showing the movie name.

## What Is Included

| File | Purpose |
|------|---------|
| `agents/moviesearch/agent.py` | Agent definition with a filtered retrieval tool |
| `agents/searches.py` | `MovieSearch` tool using `BaseRetrievalTool` with filter parameters |
| `agents/moviesearch/prompts/moviesearch.md` | System prompt for the agent |
| `data/movies/__init__.py` | `MoviesTopic` defining the document collection |
| `data/movies/metadata.py` | Three `BaseMetadataConfig` classes: genre, language, decade |
| `data/formatters.py` | `MovieFormatter` controlling how references appear |
| `data/ingestion.py` | `MovieIngestionConfig` for document parsing and chunking |
| `data/retrievals.py` | `MovieRetrieval` configuring semantic search with filters |
| `data/movies/docs/*.md` | 12 sample movie synopses in Markdown format |
| `scripts/ingest_movies.py` | Script to upload movies with per-document metadata |

### Metadata Filters

| Filter | Type | Possible Values |
|--------|------|-----------------|
| genre | STRING | Action, Comedy, Drama, Horror, Sci-Fi, Romance, Thriller, Animation |
| language | STRING | English, Spanish, French, Japanese, Korean |
| decade | STRING | 1990s, 2000s, 2010s, 2020s |

### Sample Movies

| Movie | Genre | Language | Decade |
|-------|-------|----------|--------|
| The Shawshank Redemption | Drama | English | 1990s |
| Pulp Fiction | Thriller | English | 1990s |
| Spirited Away | Animation | Japanese | 2000s |
| Amelie | Comedy | French | 2000s |
| The Dark Knight | Action | English | 2000s |
| Pan's Labyrinth | Drama | Spanish | 2000s |
| Inception | Sci-Fi | English | 2010s |
| Parasite | Thriller | Korean | 2010s |
| Get Out | Horror | English | 2010s |
| The Grand Budapest Hotel | Comedy | English | 2010s |
| Dune | Sci-Fi | English | 2020s |
| Everything Everywhere All at Once | Action | English | 2020s |

### Why a Custom Ingestion Script?

The standard `manage.py ingest` command uploads documents but does not support per-document metadata values. The `scripts/ingest_movies.py` script uses the `CogSolClient` API directly to upload each movie with its genre, language, and decade metadata attached. This is a common pattern when documents need individual metadata.

## Next Steps

- Replace the movie files in `data/movies/docs/` with your own documents and update the metadata mapping in `scripts/ingest_movies.py`.
- Add or modify metadata fields in `data/movies/metadata.py`. Update `MovieRetrieval.filters` and `MovieSearch.parameters` to match.
- Adjust retrieval settings in `data/retrievals.py` (`num_refs`, `threshold_similarity`, reordering).
- See the `semantic-search` example for a simpler version without metadata filtering.
