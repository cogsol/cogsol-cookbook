# Excel Query

A starting point for building a CogSol agent that queries Excel files uploaded to the conversation using pandas.

The user attaches an `.xlsx` file in the chat, asks a question, and the agent uses a script tool to run targeted queries on the data and return only the relevant results.

## Use Case

You need an agent that lets users upload Excel files and get answers about their content: totals, summaries, specific values, comparisons, etc. — without sending the entire spreadsheet to the language model.

This template provides the query tool ready to use. You only need to:

1. **Customize the agent prompt** in `agents/excelquery/prompts/excelquery.md` to fit your domain.

## Prerequisites

- Python 3.9 or higher
- CogSol Framework installed (`pip install -e /path/to/cogsol-framework`)
- A CogSol API account with valid credentials
- `pandas` and `openpyxl` available on the platform

## What Is Included

| File | Purpose |
|------|---------|
| `agents/tools.py` | `QueryExcelAttachment` script tool that queries an Excel attachment with pandas |
| `agents/excelquery/agent.py` | Agent definition with the query tool |
| `agents/excelquery/prompts/excelquery.md` | System prompt for the agent (customize this) |

### How the Script Tool Works

The `QueryExcelAttachment` tool:

1. Retrieves the file attached to the last user message via the `MessageAttachment` model.
2. Loads the `.xlsx` content into a pandas DataFrame.
3. Executes the requested operation and returns only the relevant results.

The tool supports four operations:

- **`describe`**: Returns a dataset overview — column names, types, row count, and the first 5 rows. Use this first to understand the structure.
- **`filter`**: Returns rows where a column matches a value (exact match for numbers, case-insensitive substring for text).
- **`aggregate`**: Runs `sum`, `mean`, `count`, `min`, or `max` on a column, with optional `group_by`.
- **`lookup`**: Searches for a value across all columns.

Parameters:
- `operation` (required): one of `describe`, `filter`, `aggregate`, `lookup`
- `sheet`: worksheet name (defaults to the first sheet)
- `column`: column to operate on (required for `filter` and `aggregate`)
- `value`: value to match (required for `filter` and `lookup`)
- `agg_function`: aggregation function (required for `aggregate`)
- `group_by`: column to group by (optional, for `aggregate`)

## Getting Started

### Step 1. Configure your environment

```bash
cd templates/excel-query
cp .env.example .env
```

Edit `.env` and fill in your CogSol API credentials.

### Step 2. Customize the system prompt

Edit `agents/excelquery/prompts/excelquery.md` to describe the agent's role. For example, if the agent analyzes sales reports:

```markdown
# Sales Report Analyst

You analyze sales data from Excel spreadsheets and provide insights, summaries, and answers about the numbers.
```

### Step 3. Deploy

```bash
# Generate migrations
python manage.py makemigrations

# Deploy agent to CogSol API
python manage.py migrate agents
```

### Step 4. Test

```bash
python manage.py chat --agent ExcelQueryAgent
```

In the platform, upload an Excel file and ask a question like:

> What is the total revenue by region?

The agent will first describe the dataset, then run the appropriate aggregation query.

## Customization Notes

- **Adding operations**: Extend the tool by adding new methods (e.g., `_sort`, `_top_n`) following the existing pattern.
- **Row limits**: Filter and lookup results are capped at 50 rows. Adjust `max_rows` in the tool if needed.
- **CSV support**: To support `.csv`, add a content type check and use `pd.read_csv` as a fallback.
- **Add retrieval**: Uncomment the scaffold files in `data/` and `agents/searches.py` to add semantic search capabilities. See the [`semantic-search`](../semantic-search/README.md) template for the full pattern.
