# Search (No Filters) Template

A starter project demonstrating how to build a CogSol agent that performs semantic search over a document collection using `BaseRetrieval` without metadata filters.

## Use Case

Use this template when you need an agent that searches a knowledge base by meaning rather than exact keywords. Users type natural-language queries and the agent retrieves the most relevant documents.

This template uses a collection of recipes as sample content. Users can search by ingredients, cuisine style, dish type, or any descriptive phrase (e.g. "something light with chicken" or "easy chocolate dessert").

No metadata filters are applied: the retrieval returns results ranked purely by semantic similarity. For a version with filters, see the `search-with-filters` template.

## Prerequisites

- Python 3.9 or higher
- CogSol Framework installed (`pip install -e /path/to/cogsol-framework`)
- A CogSol API account with valid credentials

## Getting Started

```bash
# 1. Copy this template to your workspace
cp -r templates/search-no-filters my-project
cd my-project

# 2. Configure your environment
cp .env.example .env
# Edit .env with your CogSol API credentials

# 3. Generate migrations
python manage.py makemigrations

# 4. Deploy to CogSol API
python manage.py migrate

# 5. Ingest the sample recipes
python manage.py ingest recipes data/recipes/docs/ --ingestion-config recipe_ingestion --doc-type Markdown

# 6. Test your agent
python manage.py chat --agent RecipeSearchAgent
```

## What Is Included

| File | Purpose |
|------|---------|
| `agents/recipesearch/agent.py` | Agent definition with a retrieval-based search tool |
| `agents/searches.py` | `RecipeSearch` tool using `BaseRetrievalTool` |
| `agents/recipesearch/prompts/recipesearch.md` | System prompt for the agent |
| `data/recipes/__init__.py` | `RecipesTopic` defining the document collection |
| `data/formatters.py` | `RecipeFormatter` controlling how references appear |
| `data/ingestion.py` | `RecipeIngestionConfig` for document parsing and chunking |
| `data/retrievals.py` | `RecipeRetrieval` configuring semantic search behavior |
| `data/recipes/docs/*.md` | 12 sample recipe files in Markdown format |

### Content Pipeline

This template demonstrates the full content pipeline:

1. **Topic** (`BaseTopic`): Defines a named document collection ("recipes") in the Content API.
2. **Ingestion Config** (`BaseIngestionConfig`): Controls how uploaded files are parsed and split into searchable blocks.
3. **Reference Formatter** (`BaseReferenceFormatter`): Defines how document references appear in the agent's responses.
4. **Retrieval** (`BaseRetrieval`): Configures semantic search: number of results, similarity threshold, and formatter mapping.
5. **Retrieval Tool** (`BaseRetrievalTool`): Exposes the retrieval as a tool the agent can call during conversations.

### Sample Recipes

The template includes 12 recipes covering different cuisines and dish types:

| Recipe | Cuisine | Type |
|--------|---------|------|
| Pasta Carbonara | Italian | Main course |
| Chicken Tikka Masala | Indian | Main course |
| Caesar Salad | American | Salad |
| Beef Tacos | Mexican | Main course |
| Creamy Tomato Soup | American | Soup |
| Chocolate Brownies | American | Dessert |
| Grilled Salmon with Herbs | Mediterranean | Main course |
| Vegetable Stir-Fry | Asian | Main course |
| Banana Pancakes | American | Breakfast |
| Lentil Curry | Indian | Main course |
| Caprese Bruschetta | Italian | Appetizer |
| Lemon Garlic Shrimp | Mediterranean | Main course |

## Customization Notes

- **Replace the content**: Swap the recipe files in `data/recipes/docs/` with your own documents (PDF, DOCX, TXT, MD, or any supported format). Update the topic name and description in `data/recipes/__init__.py`.
- **Adjust retrieval settings**: Edit `data/retrievals.py` to change `num_refs` (number of results), `threshold_similarity`, or enable reordering.
- **Add metadata filters**: To enable filtering, define `BaseMetadataConfig` classes in `data/recipes/metadata.py`, add them to `RecipeRetrieval.filters`, and see the `search-with-filters` template for the full pattern.
- **Change the formatter**: Edit the `expression` in `data/formatters.py` to include page numbers, metadata, or timestamps in references.
- **Rename the agent**: Update the class name in `agent.py` and `__init__.py`, adjust `Meta.name` and `Meta.chat_name`, then delete the existing migration files and run `python manage.py makemigrations` to generate fresh migrations.
