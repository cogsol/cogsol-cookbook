from cogsol.tools import BaseTool, tool_params


class CallExternalApi(BaseTool):
    """Script tool that calls an external API using secrets for configuration."""

    name = "call_external_api"
    description = (
        "Call an external API endpoint and return the response data. "
        "Use this when the user asks a question that requires live data from the API."
    )
    show_tool_message = False

    @tool_params(
        endpoint={
            "description": (
                "API endpoint path to append to the base URL "
                "(e.g. '/forecast', '/users/123')."
            ),
            "type": "string",
            "required": True,
        },
        query_params={
            "description": (
                "Query parameters as a JSON string "
                "(e.g. '{\"latitude\": 52.52, \"longitude\": 13.41}')."
            ),
            "type": "string",
            "required": False,
        },
    )
    def run(self, endpoint="", query_params="", chat=None, data=None, secrets=None, log=None):
        import json
        import requests

        base_url = secrets.get("API-BASE-URL", "")
        api_key = secrets.get("API-KEY", "")

        if not base_url:
            return "API-BASE-URL secret is not configured. Add it in the platform secrets."

        url = base_url.rstrip("/") + "/" + endpoint.lstrip("/")

        headers = {}
        if api_key:
            headers["Authorization"] = f"Bearer {api_key}"

        params = {}
        if query_params:
            try:
                params = json.loads(query_params)
            except json.JSONDecodeError:
                return "Invalid query_params format. Provide a valid JSON string."

        try:
            log.append(f"GET {url} params={params}")
            resp = requests.get(url, headers=headers, params=params, timeout=30)
            resp.raise_for_status()

            result = resp.json()
            log.append(f"Response status: {resp.status_code}")
            return json.dumps(result, indent=2, ensure_ascii=False)

        except requests.exceptions.Timeout:
            log.append("Request timed out")
            return "The API request timed out. Try again later."
        except requests.exceptions.HTTPError:
            log.append(f"HTTP error: {resp.status_code}")
            return f"API returned an error: {resp.status_code} {resp.reason}"
        except Exception as e:
            log.append(f"Request error: {str(e)}")
            return f"Could not reach the API: {str(e)}"
