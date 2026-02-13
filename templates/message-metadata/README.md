# Message Metadata

A starter project demonstrating how to use message metadata to personalize an agent's responses. A pretool reads the `user_id` from the metadata attached to each user message, resolves the user profile, and injects context so the agent adapts its language, tone, and style.

## Use Case

Use this template when you need an agent that reads metadata sent by an external system (web app, CRM, API gateway) and uses it to drive behavior. Common scenarios:

- Personalizing responses based on user identity (name, language, role).
- Routing or branching conversation flows based on structured data.
- Passing session or transaction context from a frontend to the agent.

The pattern demonstrated here follows real production deployments: the frontend attaches a lightweight identifier (e.g. `user_id`) to the message, and a script tool resolves the full context by querying a data source.

## Prerequisites

- Python 3.9 or higher
- CogSol Framework installed (`pip install -e /path/to/cogsol-framework`)
- A CogSol API account with valid credentials

## Getting Started

```bash
# 1. Copy this template to your workspace
cp -r templates/message-metadata my-project
cd my-project

# 2. Configure your environment
cp .env.example .env
# Edit .env with your CogSol API credentials

# 3. Generate migrations
python manage.py makemigrations

# 4. Deploy to CogSol API
python manage.py migrate

# 5. Test your agent (without metadata, generic English responses)
python manage.py chat --agent MessageMetadataAgent
```

### Testing with Metadata (Platform UI)

The CLI does not support sending metadata. To test the full metadata flow:

1. Open the agent in the CogSol platform.
2. Tap the **{}** button next to the message input.
3. Add a metadata entry: key `user_id`, value `USR-001`.
4. Send any message and observe the personalized response.

Try different user IDs to see the agent adapt:

| user_id | Name | Language | Role | Communication Style |
|---------|------|----------|------|---------------------|
| `USR-001` | Maria Garcia | Spanish | developer | Technical and detailed |
| `USR-002` | John Smith | English | manager | Executive summary, high-level |
| `USR-003` | Ana Silva | Portuguese | analyst | Data-oriented and precise |

Sending a message without metadata produces a generic English response.

## What Is Included

| File | Purpose |
|------|---------|
| `agents/messagemetadata/agent.py` | Agent definition with `pretools` and `pregeneration_config` |
| `agents/tools.py` | `GetUserContext` pretool that reads message metadata |
| `agents/messagemetadata/prompts/messagemetadata.md` | System prompt for the agent |

### How It Works

1. A user (or frontend) sends a message with metadata: `{"user_id": "USR-001"}`.
2. Before the main response, the `GetUserContext` pretool runs automatically.
3. The pretool reads `.metadata` from the latest user message in the conversation.
4. It looks up the user profile in a hardcoded dictionary (replace with a real data source in production).
5. The resolved context (name, language, role, style) is injected into `data['prompt_params']['context']`.
6. The agent sees the context in its system prompt and personalizes its response accordingly.

### Metadata Format

The CogSol platform sends message metadata as a JSON object on the message. The tool handles two common formats:

- **Direct dict**: `{"user_id": "USR-001"}` (API calls)
- **List values**: `{"user_id": ["USR-001"]}` (platform UI)

### Viewing Pretool Executions

To inspect pretool execution and the metadata flow, go to **Activity > Troubleshoot** in the CogSol platform. Select a conversation to see:

- The raw metadata attached to each user message
- The pretool execution logs
- The resolved user context injected into the system prompt

## Customization Notes

- **Add more user profiles**: Extend the `USERS` dictionary in `agents/tools.py` or replace it with a call to your user database or CRM.
- **Read additional metadata keys**: Modify the tool to extract more fields from the metadata (e.g. `session_id`, `department`, `priority`).
- **Use chat metadata**: The `chat` object also has a `metadata` attribute set at chat creation time. Access it via `chat.metadata` for session-level context.
- **Add more pretools**: Create additional `BaseTool` subclasses in `agents/tools.py` and add them to the agent's `pretools` list.
- **Rename the agent**: Update the class name in `agent.py` and `__init__.py`, adjust `Meta.name` and `Meta.chat_name`, then delete the existing migration file and run `python manage.py makemigrations` to generate a fresh migration.
