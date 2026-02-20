# Message Metadata

A runnable demo showing how to use message metadata to personalize an agent's responses by language, name, and communication style.

## Scenario

Your organization deploys an assistant behind a web app, CRM, or API gateway that attaches structured metadata to each user message (e.g. `{"user_id": "USR-001"}`). A pretool reads the metadata, resolves the user profile from a data source, and injects context so the agent adapts its language, tone, and style automatically.

This demo uses a hardcoded user dictionary. In production, replace it with a call to your user database, CRM, or identity provider.

## What This Demo Covers

- `BaseTool` used as a **pretool** that runs before the agent generates a response.
- Reading `.metadata` from user messages in the conversation history.
- Injecting resolved context into `data['prompt_params']['context']` for system prompt personalization.
- `pretools` and `pregeneration_config` on `BaseAgent`.
- Handling two metadata formats: direct dict (API calls) and list values (platform UI).

## Prerequisites

- Python 3.9 or higher
- CogSol Framework installed (`pip install -e /path/to/cogsol-framework`)
- A CogSol API account with valid credentials

## Run

```bash
cd examples/message-metadata

# 1. Configure your environment
cp .env.example .env
# Edit .env with your CogSol API credentials

# 2. Apply migrations
python manage.py migrate

# 3. Chat with the agent
python manage.py chat --agent MessageMetadataAgent
```

### Testing with Metadata (Platform UI)

The CLI does not support sending metadata. To test the full metadata flow:

1. Open the agent in the CogSol platform.
2. Tap the **{}** button next to the message input.
3. Add a metadata entry: key `user_id`, value `USR-001`.
4. Send any message and observe the personalized response.

## Expected Outcome

Without metadata, the agent responds in generic English. With a `user_id` in the message metadata, the agent personalizes its response:

| user_id | Name | Language | Role | Communication Style |
|---------|------|----------|------|---------------------|
| `USR-001` | Maria Garcia | Spanish | developer | Technical and detailed |
| `USR-002` | John Smith | English | manager | Executive summary, high-level |
| `USR-003` | Ana Silva | Portuguese | analyst | Data-oriented and precise |

To inspect pretool execution and the metadata flow, go to **Activity > Troubleshoot** in the CogSol platform.

## Next Steps

- Replace the hardcoded `USERS` dictionary in `agents/tools.py` with a call to your user database or CRM.
- Read additional metadata keys (e.g. `session_id`, `department`, `priority`) by extending the pretool.
- Access chat-level metadata via `chat.metadata` for session context set at chat creation time.
- Combine with other features like fixed responses, FAQs, or lessons for richer agent behavior.
