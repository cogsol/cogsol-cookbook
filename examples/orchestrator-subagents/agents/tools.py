from cogsol.tools import BaseTool, tool_params


class PlanTravel(BaseTool):
    """Script tool that consults all sub-agents in parallel and returns a consolidated travel plan."""

    name = "plan_travel"
    description = (
        "Plan a business trip by consulting flight, hotel, and expense policy specialists. "
        "Returns a consolidated travel plan with all relevant information."
    )
    show_tool_message = False

    @tool_params(
        query={
            "description": "The full travel request with destination, dates, origin, and preferences",
            "type": "string",
            "required": True,
        },
    )
    def run(self, query="", chat=None, data=None, secrets=None, log=None):
        from assistant.services.chat import create_chat_parallel

        # Update these IDs after deploying sub-agents (see README)
        agent_ids = {
            "flights": 0,
            "hotels": 0,
            "policies": 0,
        }

        # Separate configured from unconfigured agents
        chat_data_list = []
        configured_names = []
        unconfigured = []

        for name, agent_id in agent_ids.items():
            if not agent_id:
                unconfigured.append(f"## {name.title()}\nNot configured (agent ID is 0).\n")
                continue
            configured_names.append(name)
            chat_data_list.append({
                "assistant": agent_id,
                "message": query,
                "chat_metadata": {"delegated_from": chat.id},
            })

        if not chat_data_list:
            return "No specialists configured (all agent IDs are 0)."

        log.append(f"Consulting {len(chat_data_list)} specialists in parallel...")
        responses = create_chat_parallel(
            chat_data_list=chat_data_list,
            max_threads=len(chat_data_list),
            timeout=60,
        )

        results = []
        for name, result in zip(configured_names, responses):
            label = name.title()
            if isinstance(result, dict) and "error" in result:
                log.append(f"{label} failed: {result['error']}")
                results.append(f"## {label}\nCould not retrieve information.\n")
                continue
            try:
                messages = result.data.get("messages", [])
                content = (
                    messages[-1].get("content")
                    if messages
                    else None
                )
                if content:
                    log.append(f"{label} responded successfully")
                    results.append(f"## {label}\n{content}\n")
                else:
                    log.append(f"{label} returned no content")
                    results.append(f"## {label}\nNo response received.\n")
            except Exception as e:
                log.append(f"{label} error: {str(e)}")
                results.append(f"## {label}\nCould not retrieve information.\n")

        results.extend(unconfigured)
        return "\n".join(results)
