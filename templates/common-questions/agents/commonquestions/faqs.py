from cogsol.tools import BaseFAQ


class WhatIsCogsolFAQ(BaseFAQ):
    question = "What is the CogSol Framework?"
    answer = (
        "The CogSol Framework is a lightweight Python framework for building, "
        "managing, and deploying AI agents. It provides base classes for agents, "
        "tools, content management, and a migration system that syncs local "
        "definitions with the remote CogSol API. Think of it as a declarative "
        "way to define everything an agent needs: from its personality to its "
        "knowledge, entirely in Python code."
    )


class WhatIsAgentFAQ(BaseFAQ):
    question = "What is an agent in CogSol?"
    answer = (
        "An agent is the central entity in CogSol. It is a Python class that "
        "inherits from BaseAgent and defines a system prompt, generation config, "
        "and optional features like tools, FAQs, fixed responses, and lessons. "
        "When deployed via migrations, the agent is created in the CogSol API "
        "and becomes available for chat interactions."
    )


class HowMigrationsWorkFAQ(BaseFAQ):
    question = "How do migrations work in CogSol?"
    answer = (
        "Migrations detect differences between your local Python definitions "
        "and the remote API state. Running 'makemigrations' generates migration "
        "files that describe changes (create, update, delete). Running 'migrate' "
        "applies those changes by calling the CogSol API. State is tracked in "
        ".state.json and .applied.json files inside the migrations/ directory."
    )


class WhatAreToolsFAQ(BaseFAQ):
    question = "What are tools and how do agents use them?"
    answer = (
        "Tools are actions an agent can invoke during a conversation. Each tool "
        "is a Python class with a name, description, parameters, and a run() "
        "method. The agent's LLM decides when to call a tool based on the user's "
        "message. CogSol provides BaseTool for custom logic and "
        "BaseRetrievalTool for semantic search over ingested documents."
    )


class DifferenceFaqFixedFAQ(BaseFAQ):
    question = "What is the difference between FAQs and fixed responses?"
    answer = (
        "Both provide predefined content, but they serve different purposes. "
        "FAQs (BaseFAQ) are question-answer pairs that help the agent handle "
        "common questions with consistent answers. Fixed responses "
        "(BaseFixedResponse) are keyed blocks of text triggered by a specific "
        "identifier. FAQs are matched by semantic similarity to the user's "
        "question, while fixed responses are retrieved by their exact key."
    )


class WhatIsContentApiFAQ(BaseFAQ):
    question = "What is the Content API used for?"
    answer = (
        "The Content API manages document ingestion and semantic search. You "
        "define topics (BaseTopic) to organize documents, configure ingestion "
        "settings (BaseIngestionConfig) for PDF parsing and chunking, and create "
        "retrievals (BaseRetrieval) to enable agents to search over that content. "
        "It is separate from the Cognitive API that manages agents and tools."
    )


class CanAgentsHaveMultipleToolsFAQ(BaseFAQ):
    question = "Can an agent have multiple tools at once?"
    answer = (
        "Yes. An agent can have any combination of tools, FAQs, fixed responses, "
        "and lessons. List them in the agent class and the migration system will "
        "sync all of them. The agent's LLM will choose which tool to call based "
        "on the conversation context. Use max_consecutive_tool_calls to limit "
        "how many tool calls the agent can chain in a single turn."
    )
