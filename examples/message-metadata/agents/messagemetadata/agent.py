from cogsol.agents import BaseAgent, genconfigs
from cogsol.prompts import Prompts

from ..tools import GetUserContext


class MessageMetadataAgent(BaseAgent):
    system_prompt = Prompts.load("messagemetadata.md")
    generation_config = genconfigs.QA()
    pregeneration_config = genconfigs.QA()
    temperature = 0.3
    max_responses = 10
    max_msg_length = 2048
    max_consecutive_tool_calls = 3

    pretools = [GetUserContext()]

    initial_message = (
        "Hello! I am the Message Metadata Assistant. "
        "I personalize my responses based on user metadata attached to messages. "
        "To try it out, tap the {} button next to the message input, "
        "add a metadata entry with key user_id and one of these values: "
        "USR-001 (Maria, Spanish, developer), "
        "USR-002 (John, English, manager), or "
        "USR-003 (Ana, Portuguese, analyst). "
        "Then send any message and see how I adapt!"
    )
    forced_termination_message = (
        "We are ending this conversation to preserve security and integrity."
    )
    no_information_message = (
        "I don't have specific information about that topic. "
        "Please check the official documentation at https://docs.cogsol.ai."
    )

    class Meta:
        name = "MessageMetadataAgent"
        chat_name = "Message Metadata Assistant"
