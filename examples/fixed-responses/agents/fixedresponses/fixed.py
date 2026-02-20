from cogsol.tools import BaseFixedResponse


class InstallationFixed(BaseFixedResponse):
    key = "installation"
    response = (
        "To install the CogSol Framework:\n\n"
        "1. Clone the repository:\n"
        "   git clone <repository-url> cogsol-framework\n"
        "   cd cogsol-framework\n"
        "   pip install -e .\n\n"
        "2. Verify the installation:\n"
        "   cogsol-admin\n\n"
        "You should see the list of available commands: chat, importagent, "
        "ingest, makemigrations, migrate, startagent, startproject, "
        "starttopic, topics."
    )


class PrerequisitesFixed(BaseFixedResponse):
    key = "prerequisites"
    response = (
        "Before using CogSol, ensure you have:\n\n"
        "- Python 3.9 or higher\n"
        "- pip (Python package installer)\n"
        "- A CogSol API account (for deployment)\n"
        "- Git (recommended for version control)\n\n"
        "Check your Python version with: python --version"
    )


class CreateProjectFixed(BaseFixedResponse):
    key = "create_project"
    response = (
        "To create a new CogSol project:\n\n"
        "1. Run: cogsol-admin startproject my_assistant\n"
        "2. Navigate to the project: cd my_assistant\n"
        "3. Copy the environment file: cp .env.example .env\n"
        "4. Update .env with your CogSol API credentials\n"
        "5. Verify setup: python manage.py\n\n"
        "Your project will include an agents/ directory for the Cognitive API "
        "and a data/ directory for the Content API."
    )


class CreateAgentFixed(BaseFixedResponse):
    key = "create_agent"
    response = (
        "To create a new agent:\n\n"
        "1. Run: python manage.py startagent MyAgent\n"
        "2. Edit agents/myagent/agent.py to configure the agent\n"
        "3. Customize the system prompt in agents/myagent/prompts/myagent.md\n"
        "4. Add tools, FAQs, fixed responses, or lessons as needed\n"
        "5. Generate migrations: python manage.py makemigrations\n"
        "6. Deploy: python manage.py migrate"
    )


class MigrationsFixed(BaseFixedResponse):
    key = "migrations"
    response = (
        "CogSol uses a migration system similar to Django:\n\n"
        "- python manage.py makemigrations: Detects changes in your Python "
        "class definitions and generates migration files.\n"
        "- python manage.py migrate: Applies pending migrations and syncs "
        "with the remote CogSol API.\n\n"
        "Migration files are stored in agents/migrations/ and "
        "data/migrations/. State is tracked in .applied.json and "
        ".state.json files."
    )


class AvailableCommandsFixed(BaseFixedResponse):
    key = "available_commands"
    response = (
        "Available CogSol CLI commands:\n\n"
        "- startproject: Create a new project\n"
        "- startagent: Create an agent scaffold\n"
        "- starttopic: Create a topic for documents\n"
        "- makemigrations: Generate migration files\n"
        "- migrate: Apply migrations and sync with the API\n"
        "- chat: Interactive chat with a deployed agent\n"
        "- ingest: Upload documents to a topic\n"
        "- importagent: Import an agent from the remote API\n"
        "- topics: List available topics\n\n"
        "Run python manage.py <command> --help for details on each command."
    )


class EnvironmentSetupFixed(BaseFixedResponse):
    key = "environment_setup"
    response = (
        "To configure your environment, create a .env file with:\n\n"
        "COGSOL_ENV=local\n"
        "COGSOL_API_BASE=https://api.cogsol.ai/cognitive/\n"
        "COGSOL_CONTENT_API_BASE=https://api.cogsol.ai/content/\n"
        "COGSOL_API_KEY=your-api-key\n\n"
        "Optional Azure AD B2C credentials:\n"
        "COGSOL_AUTH_CLIENT_ID=your-client-id\n"
        "COGSOL_AUTH_SECRET=your-client-secret"
    )
