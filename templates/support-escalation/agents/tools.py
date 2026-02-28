from cogsol.tools import BaseTool, tool_params


class CreateTicket(BaseTool):
    """Script tool that creates a support ticket via a mock REST API."""

    name = "create_ticket"
    description = (
        "Create a support ticket when the user's issue cannot be resolved "
        "with existing knowledge base articles or FAQs. Use this as a last "
        "resort after searching the knowledge base."
    )
    show_tool_message = False

    @tool_params(
        subject={
            "description": "Short summary of the issue for the ticket title.",
            "type": "string",
            "required": True,
        },
        description={
            "description": "Detailed description of the issue including steps to reproduce.",
            "type": "string",
            "required": True,
        },
        priority={
            "description": "Ticket priority: low, medium, or high.",
            "type": "string",
            "required": False,
        },
    )
    def run(self, subject="", description="", priority="medium", chat=None, data=None, log=None):
        import json
        import requests

        url = "https://jsonplaceholder.typicode.com/posts"

        payload = {
            "title": subject,
            "body": f"Priority: {priority}\n\n{description}",
            "userId": 1,
        }

        try:
            log.append(f"POST {url}")
            resp = requests.post(url, json=payload, timeout=30)
            resp.raise_for_status()

            result = resp.json()
            ticket_id = result.get("id", "N/A")
            log.append(f"Ticket created: #{ticket_id}")
            return f"Ticket #{ticket_id} created: {subject}"

        except requests.exceptions.Timeout:
            log.append("Request timed out")
            return "Could not create the ticket: request timed out. Please try again later."
        except requests.exceptions.HTTPError:
            log.append(f"HTTP error: {resp.status_code}")
            return f"Could not create the ticket: API returned {resp.status_code}."
        except Exception as e:
            log.append(f"Request error: {str(e)}")
            return f"Could not create the ticket: {str(e)}"
