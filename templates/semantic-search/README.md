# Semantic Search

Starter template for a CogSol agent that performs **semantic search** over a document collection using `BaseRetrieval` and `BaseRetrievalTool`, without metadata filters.

Documents are matched by meaning, not by exact keywords. The agent uses embeddings to find the most relevant content based on natural-language queries.

> **Want to see this template in action?** Check out the [`semantic-search` example](../../examples/semantic-search/README.md), which uses this same pattern with a collection of sample recipes already included.

## Use Case

You have a set of documents (articles, manuals, FAQs, guides, etc.) and want an agent that lets users find relevant content by describing what they need in plain language. The agent retrieves the most relevant documents ranked by semantic similarity — no metadata filters are applied.

This template provides the full content pipeline ready to use. You only need to:

1. **Add your own documents** to the `data/documents/docs/` folder.
2. **Customize the agent prompt** in `agents/semanticsearch/prompts/semanticsearch.md` to fit your domain.

## Prerequisites

- Python 3.9 or higher
- CogSol Framework installed (`pip install -e /path/to/cogsol-framework`)
- A CogSol API account with valid credentials

## Getting Started

Follow these steps to get the template running with your own documents.

### 1. Configure your environment

```bash
cd templates/semantic-search
cp .env.example .env
```

Edit `.env` and fill in your CogSol API credentials (`COGSOL_API_BASE`, `COGSOL_CONTENT_API_BASE`, and optionally `COGSOL_API_KEY`).

### 2. Add your documents

Place your files inside the `data/documents/docs/` folder. Supported formats include Markdown (`.md`) and PDF (`.pdf`).

```
data/documents/docs/
├── your-first-document.md
├── your-second-document.md
└── ...
```

### 3. Customize the agent prompt

Edit `agents/semanticsearch/prompts/semanticsearch.md` to describe the agent's role and behavior for your specific domain. For example, if your documents are technical manuals:

```markdown
# Technical Support Assistant

You are a helpful assistant that finds answers in the product documentation.
When responding, always cite the source document.
```

### 4. Deploy the content pipeline

The content pipeline must be deployed **before** the agent, because the agent depends on the retrieval tool.

```bash
# Generate migrations (if you changed any class definitions)
python manage.py makemigrations

# Deploy topic, ingestion config, formatter, and retrieval to CogSol API
python manage.py migrate data
```

### 5. Deploy the agent

```bash
python manage.py migrate agents
```

### 6. Ingest your documents

This step uploads your documents to the CogSol Content API, where they are parsed, chunked, and embedded for semantic search.

```bash
python manage.py ingest documents data/documents/docs/ --ingestion-config document_ingestion --doc-type Markdown
```

> **Note:** Change `--doc-type` to match your file format. Use `Markdown` for `.md` files or `PDF` for `.pdf` files.

### 7. Chat with the agent

```bash
python manage.py chat --agent SemanticSearchAgent
```

The agent will use semantic search behind the scenes to find and return the most relevant content from your documents.

## What Is Included

| File | Purpose |
|------|---------|
| `agents/semanticsearch/agent.py` | Agent definition with the semantic search tool |
| `agents/searches.py` | `SemanticSearch` tool using `BaseRetrievalTool` |
| `agents/semanticsearch/prompts/semanticsearch.md` | System prompt for the agent (customize this) |
| `data/documents/__init__.py` | `DocumentsTopic` — the named document collection |
| `data/formatters.py` | `DocumentFormatter` — how references appear in responses |
| `data/ingestion.py` | `DocumentIngestionConfig` — document parsing and chunking settings |
| `data/retrievals.py` | `DocumentRetrieval` — semantic search configuration |
| `data/documents/docs/` | Place your documents here before ingestion |

### Content Pipeline

1. **Topic** (`BaseTopic`): Defines a named document collection in the Content API.
2. **Ingestion Config** (`BaseIngestionConfig`): Controls how uploaded files are parsed and split into searchable blocks.
3. **Reference Formatter** (`BaseReferenceFormatter`): Defines how document references appear in the agent's responses.
4. **Retrieval** (`BaseRetrieval`): Configures semantic search — number of results, similarity threshold, and formatter mapping.
5. **Retrieval Tool** (`BaseRetrievalTool`): Exposes the retrieval as a tool the agent can call during conversations.

## Customization Notes

- **Retrieval settings**: Edit `data/retrievals.py` to change `num_refs` (number of results returned), `threshold_similarity` (minimum similarity score, default 0.70), or enable reordering.
- **Chunking settings**: Edit `data/ingestion.py` to adjust `max_size_block` (block size in characters) and `chunk_overlap` (overlap between blocks).
- **Reference format**: Edit the `expression` in `data/formatters.py` to include page numbers, metadata, or timestamps in references.
- **Add metadata filters**: To enable filtering by custom fields (e.g. category, date, author), see the full pattern in the examples section of the cookbook.

## Related

- [`semantic-search` example](../../examples/semantic-search/README.md) — A complete, runnable demo of this template using a collection of sample recipes. Useful to see the end-to-end flow before customizing with your own documents.
