# Excel Query

A starting point for building a CogSol agent that reads and answers questions about Excel files uploaded to the conversation.

The user attaches an `.xlsx` file in the chat, asks a question, and the agent uses a script tool to parse the spreadsheet and reason over the data.

## Use Case

You need an agent that lets users upload Excel files and get answers about their content: totals, summaries, specific values, comparisons, etc.

This template provides the query tool ready to use. You only need to:

1. **Customize the agent prompt** in `agents/excelquery/prompts/excelquery.md` to fit your domain.

## Prerequisites

- Python 3.9 or higher
- CogSol Framework installed (`pip install -e /path/to/cogsol-framework`)
- A CogSol API account with valid credentials
- `openpyxl` available on the platform (used for Excel parsing)

## What Is Included

| File | Purpose |
|------|---------|
| `agents/tools.py` | `QueryExcelAttachment` script tool that reads an Excel file from a chat attachment |
| `agents/excelquery/agent.py` | Agent definition with the query tool |
| `agents/excelquery/prompts/excelquery.md` | System prompt for the agent (customize this) |

### How the Script Tool Works

The `QueryExcelAttachment` tool:

1. Retrieves the file attached to the last user message via the `MessageAttachment` model.
2. Loads the `.xlsx` content with `openpyxl`.
3. Reads the requested worksheet and cell range (or all data if not specified).
4. Returns the data as a Markdown table so the agent can analyze it.

The tool accepts two optional parameters:
- `sheet`: worksheet name (defaults to the first sheet)
- `cell_range`: cell range like `A1:D10` (defaults to all data)

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

> What is the total for column D?

The agent will read the spreadsheet and answer based on the data.

## Customization Notes

- **Specific sheets or ranges**: The agent decides which sheet and range to read based on the user's question. Adjust the system prompt to guide this behavior for your domain.
- **Large files**: For spreadsheets with many rows, consider adding instructions in the system prompt to request specific ranges rather than reading all data at once.
- **CSV support**: The tool currently handles `.xlsx` files. To support `.csv`, add a content type check and use Python's `csv` module as a fallback.
- **Add retrieval**: Uncomment the scaffold files in `data/` and `agents/searches.py` to add semantic search capabilities. See the [`semantic-search`](../semantic-search/README.md) template for the full pattern.
