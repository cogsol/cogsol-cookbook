from cogsol.tools import BaseLesson


class ProjectStructureLesson(BaseLesson):
    name = "Project Structure"
    content = (
        "A CogSol project has two main directories: agents/ for the Cognitive "
        "API (agents, tools, FAQs, fixed responses, lessons) and data/ for the "
        "Content API (topics, ingestion configs, retrievals). Each agent lives "
        "in its own subdirectory under agents/ with an __init__.py, agent.py, "
        "and a prompts/ folder. Keep this separation clean — agent logic in "
        "agents/, content configuration in data/."
    )


class NamingConventionsLesson(BaseLesson):
    name = "Naming Conventions"
    content = (
        "Use PascalCase for class names: MyAgent, SearchTool, InstallationFAQ. "
        "Use snake_case for project names and file names: my_project, agent.py. "
        "Agent directory names should be lowercase without underscores: "
        "myagent/, not my_agent/. Tool names in Meta.name should be concise "
        "and descriptive, as the LLM uses them to decide when to invoke a tool."
    )


class MigrationBestPracticesLesson(BaseLesson):
    name = "Migration Best Practices"
    content = (
        "Always run makemigrations after changing agent definitions, tools, "
        "FAQs, fixed responses, or lessons. Review generated migration files "
        "before applying them with migrate. Never manually edit .state.json "
        "or .applied.json — these are managed by the framework. If you need "
        "to start fresh, delete the migration files and state files, then "
        "regenerate with makemigrations."
    )


class PromptDesignLesson(BaseLesson):
    name = "Prompt Design"
    content = (
        "Write system prompts in Markdown and store them in the prompts/ "
        "directory. Start with a clear role definition, then list guidelines "
        "as numbered rules. Keep prompts focused — the agent should know its "
        "boundaries. Use Prompts.load('filename.md') to load them. Avoid "
        "embedding long content directly in the prompt; use FAQs, fixed "
        "responses, or lessons for structured knowledge instead."
    )


class ToolDesignLesson(BaseLesson):
    name = "Tool Design"
    content = (
        "Each tool should do one thing well. Define clear parameter schemas "
        "using tool_params() so the LLM knows what inputs to provide. Keep "
        "tool descriptions concise but precise — the LLM reads them to decide "
        "when to call the tool. Always include logging in the run() method "
        "for debugging. Return structured results that the agent can easily "
        "incorporate into its response."
    )


class ErrorHandlingLesson(BaseLesson):
    name = "Error Handling"
    content = (
        "In tool run() methods, catch exceptions and return user-friendly "
        "error messages rather than letting them propagate. Log the full "
        "traceback for debugging but return a clean message to the agent. "
        "Use the no_information_message agent attribute to handle cases "
        "where the agent cannot find relevant information. Set "
        "max_consecutive_tool_calls to prevent infinite tool-call loops."
    )


class TestingAgentsLesson(BaseLesson):
    name = "Testing Agents"
    content = (
        "Use 'python manage.py chat --agent AgentName' to interactively "
        "test an agent after deploying it. Test each tool, FAQ, fixed "
        "response, and lesson individually. Verify that the agent stays "
        "within the boundaries defined by its system prompt. Check edge "
        "cases: what happens when the user asks something outside the "
        "agent's scope? The no_information_message should handle it."
    )
