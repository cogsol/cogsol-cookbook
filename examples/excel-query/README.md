# Excel Query

A runnable example of a CogSol agent that queries Excel files uploaded to the conversation using pandas. This example deploys the [`excel-query` template](../../templates/excel-query/README.md) with an expense report review scenario.

## Scenario

You are a finance manager reviewing employee expense reports. Employees submit `.xlsx` files with columns for employee name, date, category, description, amount, and approval status. The agent lets you ask questions about the data without downloading or opening the spreadsheet manually.

## What This Demo Covers

- **`BaseTool`** (script tool): Reading Excel attachments via `message.attachments` and querying them with pandas.
- **Four query operations**: `describe`, `filter`, `aggregate`, and `lookup`.
- **Targeted queries**: The agent never sends the entire spreadsheet to the model — it runs specific operations and returns only the relevant results.

## Prerequisites

- Python 3.9 or higher
- CogSol Framework installed (`pip install -e /path/to/cogsol-framework`)
- A CogSol API account with valid credentials
- `pandas` and `openpyxl` available on the platform

## What Is Included

| File | Purpose |
|------|---------|
| `agents/tools.py` | `QueryExcelAttachment` script tool that queries an Excel attachment with pandas |
| `agents/expensereview/agent.py` | `ExpenseReviewAgent` with the query tool |
| `agents/expensereview/prompts/expensereview.md` | System prompt for the expense review domain |
| `sample-data/expense-report.xlsx` | Sample expense report (17 rows, 3 employees, 5 categories) |

### Sample Data

The included `expense-report.xlsx` contains expense entries for February 2026:

- **Employees**: Alice, Bob, Carol
- **Categories**: Travel, Meals, Office Supplies, Software, Training
- **Statuses**: Approved, Pending, Rejected

## Run

```bash
# 1. Navigate to this example
cd examples/excel-query

# 2. Configure your environment
cp .env.example .env
# Edit .env with your CogSol API credentials

# 3. Deploy agent to CogSol API
python manage.py migrate agents

# 4. Chat with the agent
python manage.py chat --agent ExpenseReviewAgent
```

## Expected Outcome

After deployment, open the chat in the platform, upload `sample-data/expense-report.xlsx`, and try these queries:

| # | Send this message | What happens | Operation |
|---|-------------------|--------------|-----------|
| 1 | `What's in this file?` | Agent calls the tool with `describe` and returns column names, types, row count, and a 5-row sample. | describe |
| 2 | `Show expenses by Alice` | Filters the Employee column for "Alice" and returns her 4 expense entries. | filter |
| 3 | `Total amount by category` | Aggregates the Amount column grouped by Category and returns the totals. | aggregate |
| 4 | `Find anything about Uber` | Searches across all columns for "Uber" and returns the matching row. | lookup |
