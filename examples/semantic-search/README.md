# Semantic Search

A complete example of a CogSol agent that performs semantic search over a document collection using `BaseRetrieval` without metadata filters.

## Scenario

You have a knowledge base of documents and want users to find relevant content by describing what they need in natural language. The agent retrieves the most relevant documents ranked purely by semantic similarity — no metadata filters are applied.

This example uses a collection of 12 recipes as sample content. Users can search by ingredients, cuisine style, dish type, or any descriptive phrase (e.g. "something light with chicken" or "easy chocolate dessert").

## What This Demo Covers

- **`BaseTopic`**: Defining a named document collection in the Content API.
- **`BaseIngestionConfig`**: Configuring how uploaded files are parsed and split into searchable blocks.
- **`BaseReferenceFormatter`**: Controlling how document references appear in agent responses.
- **`BaseRetrieval`**: Setting up semantic search with result count, similarity threshold, and block context.
- **`BaseRetrievalTool`**: Exposing the retrieval as a tool the agent can call during conversations.

## Prerequisites

- Python 3.9 or higher
- CogSol Framework installed (`pip install -e /path/to/cogsol-framework`)
- A CogSol API account with valid credentials

## Run

```bash
# 1. Navigate to this example
cd examples/semantic-search

# 2. Configure your environment
cp .env.example .env
# Edit .env with your CogSol API credentials

# 3. Generate migrations
python manage.py makemigrations

# 4. Deploy content pipeline to CogSol API (must run before agents)
python manage.py migrate data

# 5. Deploy agent to CogSol API
python manage.py migrate agents

# 6. Ingest the sample recipes
python manage.py ingest recipes data/recipes/docs/ --ingestion-config recipe_ingestion --doc-type Markdown

# 7. Chat with the agent
python manage.py chat --agent RecipeSearchAgent
```

## Expected Outcome

After running the steps above, you can chat with `RecipeSearchAgent` and ask natural-language questions about recipes. The agent calls its search tool behind the scenes and returns relevant recipes with formatted references.

Example queries:
- "I want to cook something with chicken"
- "Quick vegetarian dinner ideas"
- "Suggest a dessert with chocolate"

The agent retrieves matching recipes from the ingested collection and includes references so the user knows which documents were consulted.

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

This example demonstrates the full content pipeline:

1. **Topic** (`BaseTopic`): Defines a named document collection ("recipes") in the Content API.
2. **Ingestion Config** (`BaseIngestionConfig`): Controls how uploaded files are parsed and split into searchable blocks.
3. **Reference Formatter** (`BaseReferenceFormatter`): Defines how document references appear in the agent's responses.
4. **Retrieval** (`BaseRetrieval`): Configures semantic search: number of results, similarity threshold, and formatter mapping.
5. **Retrieval Tool** (`BaseRetrievalTool`): Exposes the retrieval as a tool the agent can call during conversations.

### Sample Recipes

The example includes 12 recipes covering different cuisines and dish types:

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

## Next Steps

- **Replace the content**: Swap the recipe files in `data/recipes/docs/` with your own documents. Update the topic name and description in `data/recipes/__init__.py`.
- **Add metadata filters**: To enable filtering by fields like cuisine or dish type, see the [`search-with-filters`](../search-with-filters/README.md) example for the full pattern.
- **Adjust retrieval settings**: Edit `data/retrievals.py` to change `num_refs` (number of results), `threshold_similarity`, or enable reordering.
- **Change the formatter**: Edit the `expression` in `data/formatters.py` to include page numbers, metadata, or timestamps in references.
