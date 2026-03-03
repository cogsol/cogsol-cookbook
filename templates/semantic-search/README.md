# Semantic Search

A starting point for building a CogSol agent with semantic search over your own documents.

Documents are matched by meaning, not by exact keywords. The agent uses embeddings to find the most relevant content based on natural-language queries. No metadata filters are applied — results are ranked purely by semantic similarity.

> **See also:** The [`semantic-search` example](../../examples/semantic-search/README.md) is a complete, runnable demo of this template using a collection of sample recipes. Check it out to see the end-to-end flow before customizing with your own documents.

## Use Case

You have a set of documents (articles, manuals, FAQs, guides, etc.) and want an agent that lets users find relevant content by describing what they need in plain language.

This template provides the full content pipeline ready to use. You only need to:

1. **Add your own documents** to the `data/documents/docs/` folder.
2. **Customize the agent prompt** in `agents/semanticsearch/prompts/semanticsearch.md` to fit your domain.

## Prerequisites

- Python 3.9 or higher
- CogSol Framework installed (`pip install -e /path/to/cogsol-framework`)
- A CogSol API account with valid credentials

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

## Getting Started

Follow these steps to get the template running with your own documents.

### Step 1. Configure your environment

```bash
cd templates/semantic-search
cp .env.example .env
```

Edit `.env` and fill in your CogSol API credentials (`COGSOL_API_BASE`, `COGSOL_CONTENT_API_BASE`, and optionally `COGSOL_API_KEY`).

### Step 2. Prepare your documents

Place your files inside the `data/documents/docs/` folder. Supported formats include Markdown (`.md`) and PDF (`.pdf`).

```
data/documents/docs/
├── your-first-document.md
├── your-second-document.md
└── ...
```

### Step 3. Customize the system prompt

Edit `agents/semanticsearch/prompts/semanticsearch.md` to describe the agent's role and behavior for your specific domain. For example, if your documents are technical manuals:

```markdown
# Technical Support Assistant

You are a helpful assistant that finds answers in the product documentation.
When responding, always cite the source document.
```

### Step 4. Deploy

The content pipeline must be deployed **before** the agent, because the agent depends on the retrieval tool.

```bash
# Generate migrations
python manage.py makemigrations

# Deploy content pipeline to CogSol API
python manage.py migrate data

# Deploy agent to CogSol API
python manage.py migrate agents

# Ingest your documents
python manage.py ingest documents data/documents/docs/ --ingestion-config document_ingestion --doc-type Markdown
```

> **Note:** Change `--doc-type` to match your file format. Use `Markdown` for `.md` files or `PDF` for `.pdf` files.

### Step 5. Test

```bash
python manage.py chat --agent SemanticSearchAgent
```

The agent will use semantic search behind the scenes to find and return the most relevant content from your documents.

## Customization Notes

- **Rename to your domain**: Update the agent name, topic name, and prompt to match your project. For example, rename `SemanticSearchAgent` to `PolicySearchAgent` and `DocumentsTopic` to `PoliciesTopic`.
- **Retrieval settings**: Edit `data/retrievals.py` to change `num_refs` (number of results returned), `threshold_similarity` (minimum similarity score, default 0.70), or enable reordering.
- **Chunking settings**: Edit `data/ingestion.py` to adjust `max_size_block` (block size in characters) and `chunk_overlap` (overlap between blocks).
- **Reference format**: Edit the `expression` in `data/formatters.py` to include page numbers, metadata, or timestamps in references.
- **Add metadata filters**: To enable filtering by custom fields (e.g. category, date, author), see the [`search-with-filters`](../../examples/search-with-filters/README.md) example for the full pattern.
