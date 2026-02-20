from cogsol.tools import BaseTool


class GetUserContext(BaseTool):
    """Reads user_id from message metadata and resolves the user profile.

    This pretool demonstrates the core metadata pattern used in production:
    1. A frontend or external system attaches metadata to the user message
       (e.g. ``{"user_id": "USR-001"}``).
    2. The tool reads the metadata from the latest user message.
    3. It looks up the user profile in a data source (hardcoded here,
       but in production this would call a CRM, database, or API).
    4. The resolved context is injected into the system prompt so the
       agent can personalize its response.
    """

    name = "get_user_context"
    description = (
        "Reads user_id from the latest user message metadata "
        "and returns the user profile for personalization."
    )
    show_tool_message = False

    def run(self, chat=None, data=None, secrets=None, log=None):
        import json

        log.append("Reading metadata from latest user message")

        # Hardcoded user profiles. In production, replace this with a call
        # to your user database, CRM, or identity provider.
        USERS = {
            "USR-001": {
                "name": "Maria Garcia",
                "language": "es",
                "role": "developer",
                "plan": "Enterprise",
                "projects": ["API Gateway v2", "Auth Service"],
                "open_tickets": 2,
                "last_deploy": "2026-02-12",
                "api_usage": "12,450 / 50,000 calls this month",
            },
            "USR-002": {
                "name": "John Smith",
                "language": "en",
                "role": "manager",
                "plan": "Enterprise",
                "team_members": 8,
                "active_projects": 3,
                "monthly_budget_used": "72%",
                "next_review": "2026-03-01",
            },
            "USR-003": {
                "name": "Ana Silva",
                "language": "pt",
                "role": "analyst",
                "plan": "Professional",
                "dashboards": ["Usage Trends", "Error Rates", "Cost Analysis"],
                "reports_generated": 14,
                "data_sources_connected": 5,
                "last_export": "2026-02-10",
            },
        }

        LANGUAGE_NAMES = {"es": "Spanish", "en": "English", "pt": "Portuguese"}

        ROLE_STYLES = {
            "developer": "technical and detailed",
            "manager": "executive summary, high-level",
            "analyst": "data-oriented and precise",
        }

        # --- Read metadata from user messages (scan backwards) ---
        # The frontend may only attach metadata on the first message.
        # Scan from newest to oldest to find the most recent user_id.
        user_messages = chat.messages.filter(role="user").order_by("-msg_num")

        if not user_messages.exists():
            log.append("No user messages found")
            data["prompt_params"]["context"]["User context"] = (
                "No user identified. Respond in English with a general tone."
            )
            return

        user_id = None
        for msg in user_messages:
            metadata = getattr(msg, "metadata", None)
            if not metadata:
                continue

            if isinstance(metadata, dict):
                user_id = metadata.get("user_id")
            elif isinstance(metadata, str):
                try:
                    parsed = json.loads(metadata)
                    if isinstance(parsed, dict):
                        user_id = parsed.get("user_id")
                except (json.JSONDecodeError, TypeError):
                    pass

            # Platform UI stores values as lists: {"user_id": ["USR-001"]}
            if isinstance(user_id, list):
                user_id = user_id[0] if user_id else None

            if user_id:
                log.append(f"Found user_id={user_id} in message #{msg.msg_num}")
                break

        if not user_id:
            log.append("No user_id found in any message metadata")
            data["prompt_params"]["context"]["User context"] = (
                "No user metadata provided. Respond in English with a general tone."
            )
            return

        # --- Look up user profile ---
        user = USERS.get(user_id)

        if not user:
            log.append(f"Unknown user_id: {user_id}")
            data["prompt_params"]["context"]["User context"] = (
                f"Unknown user_id: {user_id}. Respond in English with a general tone."
            )
            return

        language_name = LANGUAGE_NAMES.get(user["language"], "English")
        role_style = ROLE_STYLES.get(user["role"], "general")

        # Build profile summary
        profile_lines = [
            f"Name: {user['name']} (ID: {user_id})",
            f"Language: {language_name}",
            f"Role: {user['role']}",
            f"Plan: {user.get('plan', 'N/A')}",
        ]

        # Add role-specific account details
        if user["role"] == "developer":
            profile_lines.append(f"Projects: {', '.join(user.get('projects', []))}")
            profile_lines.append(f"Open tickets: {user.get('open_tickets', 0)}")
            profile_lines.append(f"Last deploy: {user.get('last_deploy', 'N/A')}")
            profile_lines.append(f"API usage: {user.get('api_usage', 'N/A')}")
        elif user["role"] == "manager":
            profile_lines.append(f"Team members: {user.get('team_members', 0)}")
            profile_lines.append(f"Active projects: {user.get('active_projects', 0)}")
            profile_lines.append(f"Monthly budget used: {user.get('monthly_budget_used', 'N/A')}")
            profile_lines.append(f"Next review: {user.get('next_review', 'N/A')}")
        elif user["role"] == "analyst":
            profile_lines.append(f"Dashboards: {', '.join(user.get('dashboards', []))}")
            profile_lines.append(f"Reports generated: {user.get('reports_generated', 0)}")
            profile_lines.append(f"Data sources connected: {user.get('data_sources_connected', 0)}")
            profile_lines.append(f"Last export: {user.get('last_export', 'N/A')}")

        profile_summary = "; ".join(profile_lines)

        context = (
            f"{profile_summary}. "
            f"Respond in {language_name}, address the user by name, "
            f"and use a {role_style} communication style."
        )

        data["prompt_params"]["context"]["User context"] = context
        log.append(f"User context resolved: {user['name']} ({user['role']}, {user['language']})")
