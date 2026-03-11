# External API

A starting point for building a CogSol agent that calls an external API using a script tool with `requests` and platform secrets.

The user asks a question, the agent calls the configured API endpoint, and returns the response.

## Use Case

You need an agent that retrieves live data from an external HTTP API: a weather service, a public dataset, an internal microservice, or any REST endpoint.

This template provides the API call tool ready to use. You only need to:

1. **Configure secrets** in the platform with your API's base URL and key.
2. **Customize the agent prompt** to describe the API and guide parameter usage.

## Prerequisites

- Python 3.9 or higher
- CogSol Framework installed (`pip install -e /path/to/cogsol-framework`)
- A CogSol API account with valid credentials
- `requests` available on the platform (pre-installed)

## What Is Included

| File | Purpose |
|------|---------|
| `agents/tools.py` | `CallExternalApi` script tool that calls an external API using secrets |
| `agents/externalapi/agent.py` | Agent definition with the API call tool |
| `agents/externalapi/prompts/externalapi.md` | System prompt for the agent (customize this) |

### How the Script Tool Works

The `CallExternalApi` tool:

1. Reads `API-BASE-URL` and `API-KEY` from platform secrets.
2. Builds the full URL by appending the `endpoint` parameter to the base URL.
3. If `API-KEY` is configured, adds an `Authorization: Bearer` header.
4. Parses optional `query_params` from a JSON string into query parameters.
5. Makes a GET request with a 30-second timeout.
6. Returns the JSON response for the agent to interpret.

The tool accepts two parameters:
- `endpoint` (required): API path to append to the base URL (e.g. `/forecast`)
- `query_params` (optional): query parameters as a JSON string

### Secrets

Configure these in the CogSol platform under the agent's secret settings:

| Secret | Required | Description |
|--------|----------|-------------|
| `API-BASE-URL` | Yes | Base URL of the external API (e.g. `https://api.open-meteo.com/v1`) |
| `API-KEY` | No | API key sent as `Authorization: Bearer` header. Omit if the API is public. |

## Getting Started

### Step 1. Configure your environment

```bash
cd templates/external-api
cp .env.example .env
```

Edit `.env` and fill in your CogSol API credentials.

### Step 2. Configure secrets

In the CogSol platform, add the secrets for your target API:

- `API-BASE-URL`: the base URL (no trailing slash)
- `API-KEY`: your API key (leave empty for public APIs)

### Step 3. Customize the system prompt

Edit `agents/externalapi/prompts/externalapi.md` to describe what the API provides and how to use it. Keep it simple: the agent will infer which tool to use on its own.

### Step 4. Deploy

```bash
# Generate migrations
python manage.py makemigrations

# Deploy agent to CogSol API
python manage.py migrate agents
```

### Step 5. Test

```bash
python manage.py chat --agent ExternalApiAgent
```

### Quick test with Open-Meteo

[Open-Meteo](https://open-meteo.com/) is a free weather API that requires no API key, useful for verifying the template works end-to-end.

**1. Set the secret** in the platform:
- `API-BASE-URL` = `https://api.open-meteo.com/v1`

**2. Replace the system prompt** in `agents/externalapi/prompts/externalapi.md` with:

```markdown
# Weather Assistant

You provide weather information using the Open-Meteo forecast API.

The forecast endpoint is `/forecast`. It requires `latitude` and `longitude` as query parameters, and `current_weather` set to `true` to get current conditions.
```

**3. Redeploy** (`makemigrations` + `migrate agents`) and ask:

> What is the weather in Berlin?

## Customization Notes

- **Authentication**: The default uses `Bearer` token auth. To use a different scheme (API key header, basic auth), modify the `headers` dict in `agents/tools.py`.
- **POST requests**: Replace `requests.get()` with `requests.post()` and add a `body` parameter for APIs that require POST.
- **Multiple endpoints**: The tool already supports any endpoint path. Add descriptions of available endpoints in the system prompt so the agent knows what to call.
- **Response formatting**: The tool returns raw JSON. Add post-processing in the tool's `run()` method to extract specific fields or format the output.
- **Add retrieval**: Uncomment the scaffold files in `data/` and `agents/searches.py` to add semantic search capabilities alongside API calls.
