from cogsol.tools import BaseTool, tool_params


class SearchInformation(BaseTool):
    """Script tool that dynamically routes queries to the correct retrieval."""

    name = "search_information"
    description = (
        "Search for travel information across different destination regions. "
        "Available topics: europe, asia, americas."
    )
    show_tool_message = False

    @tool_params(
        topic={
            "description": (
                "Topic(s) to search. Available: europe, asia, americas. "
                "Use '|' to search multiple topics at once."
            ),
            "type": "string",
            "required": True,
        },
        question={
            "description": "The search query about travel destinations.",
            "type": "string",
            "required": True,
        },
    )
    def run(self, topic="", question="", chat=None, data=None, log=None):
        from django.apps import apps

        Retrieval = apps.get_model("assistant", "Retrieval")

        topics = topic.split("|")
        params_ret = {"question": question}
        response = ""

        for t in topics:
            normalized = t.strip().lower()
            retrieval_name = f"search_selector_{normalized}"
            log.append(f"Searching in topic: {normalized}")

            try:
                func = Retrieval.objects.get(name=retrieval_name)
                result = func.run(chat, params_ret)
                content = result.get("response", "")

                last_msg = chat.messages.all().order_by("msg_num").last()
                last_msg.delete()

                response += f"# Information from {normalized}:\n{content}\n\n"
                log.append(f"Found results for {normalized}")
            except Retrieval.DoesNotExist:
                response += f"No information available for topic: {normalized}\n"
                log.append(f"No retrieval found for: {retrieval_name}")

        return response
