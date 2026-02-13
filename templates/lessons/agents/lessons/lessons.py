from cogsol.tools import BaseLesson


class PlatformOverviewLesson(BaseLesson):
    name = "Platform Overview"
    context_of_application = (
        "When the user is exploring what CogSol is, evaluating the platform, "
        "or asking about its capabilities and use cases."
    )
    content = (
        "Cognitive Solutions is a B2B platform for building and governing "
        "specialized AI agents. It supports chat-based assistants, realtime "
        "speech-to-speech voice agents, and complex workflow agents. The "
        "platform is accessible through APIs, developer-friendly SDKs, and "
        "a graphical interface, and integrates with tools like Microsoft "
        "Teams and WhatsApp. Key components include: Assistants (the main "
        "entity that interacts with users), Tools (scripts or functions the "
        "assistant can invoke), Searches (semantic information retrieval), "
        "Topics and Documents (organized knowledge base), FAQs, Fixed "
        "Questions, and Lessons."
    )


class AssistantConfigurationLesson(BaseLesson):
    name = "Assistant Configuration"
    context_of_application = (
        "When the user is setting up a new assistant, configuring its "
        "behavior, or asking about prompts, messages, and parameters."
    )
    content = (
        "To configure an assistant: (1) Write a system prompt that defines "
        "its role, scope, and boundaries. (2) Set up messages: an initial "
        "welcome message, a forced termination message for inappropriate "
        "queries, and a no-information message for unknown topics. "
        "(3) Choose a generation configuration optimized for the task (e.g. "
        "QA, complex reasoning, image-based). (4) Adjust parameters: "
        "temperature (0-2) controls creativity, max interactions limits "
        "the conversation length, message size sets the token limit, and "
        "max consecutive tool calls caps recursive LLM calls."
    )


class ToolsAndSearchesLesson(BaseLesson):
    name = "Tools and Searches"
    context_of_application = (
        "When the user asks about adding capabilities to an assistant, "
        "creating tools, configuring searches, or retrieving information."
    )
    content = (
        "Tools let an assistant perform actions: each tool is a Python "
        "script with defined parameters (name, description, type, required). "
        "The script assigns its result to the 'response' variable and has "
        "access to 'params' (parameter dictionary) and 'chat' (chat info). "
        "Searches are a specific type of tool for semantic information "
        "retrieval: configure them with a name, the topic they belong to, "
        "and a detailed description so the model knows when to use them. "
        "Retrieval techniques, reordering strategies, and reference formats "
        "are fully configurable."
    )


class ContentManagementLesson(BaseLesson):
    name = "Content Management"
    context_of_application = (
        "When the user asks about documents, topics, uploading information, "
        "organizing knowledge, or managing the content that an assistant uses."
    )
    content = (
        "Content is organized hierarchically using Topics, which form a "
        "tree structure. Documents (PDF, websites, or videos) are uploaded "
        "into topics and automatically split into Blocks, each with its own "
        "embeddings for semantic search. Key configuration points: chunk "
        "size controls how documents are segmented, overlap settings affect "
        "context continuity between blocks, and custom separators allow "
        "fine-tuning of the splitting process. Metadata can be added to "
        "documents and blocks to provide additional context for retrieval."
    )


class TroubleshootingLesson(BaseLesson):
    name = "Troubleshooting"
    context_of_application = (
        "When the user reports a problem, an error, unexpected behavior, "
        "or asks how to debug or fix an assistant."
    )
    content = (
        "Common problem types: (1) Information problems: missing or "
        "inconsistent documents; fix by adding or reformatting content. "
        "(2) Chunking problems: bad segmentation; adjust chunk size, "
        "overlap, or separators. (3) Retrieval problems: irrelevant "
        "results; apply reranking, date-based reordering, or topic-scoped "
        "searches. (4) Context problems: assistant lacks background; use "
        "lessons for general context or metadata for document-specific "
        "context. (5) Flow problems: poor interaction style; adjust the "
        "system prompt or add FAQs. (6) Generation problems: reasoning "
        "errors; switch models or prompting techniques. Use the platform's "
        "Activity > Troubleshoot module to inspect full conversation logs."
    )


class EvaluationAndImprovementLesson(BaseLesson):
    name = "Evaluation and Improvement"
    context_of_application = (
        "When the user asks about measuring performance, improving an "
        "assistant's quality, or iterating on their implementation."
    )
    content = (
        "The platform provides evaluation tools using LLM-based metrics, "
        "embedding-based metrics, and traditional NLP metrics to measure "
        "assistant performance. Define acceptance criteria and "
        "visualizations for reports when creating an assistant. Use "
        "Self-Improvement Mode (SIM) in non-production environments to "
        "interactively add common questions based on real conversations. "
        "The methodology centers on domain experts driving continuous "
        "improvement: evaluate, identify problem areas using the "
        "troubleshooting module, adjust configuration (prompt, tools, "
        "content, lessons), and re-evaluate."
    )
