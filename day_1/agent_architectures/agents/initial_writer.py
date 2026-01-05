from google.adk.agents import Agent
from google.adk.models import Gemini

from utils.helpers import get_retry_config

# initial writer agent runs ONCE at the beginning to create first draft
initial_writer = Agent(
    name="InitialWriterAgent",
    model=Gemini(
        model="gemini-2.5-flash-lite",
        retry_options=get_retry_config()
    ),
    instruction="""Based on the user's prompt, write the first draft of a short story (around 100-150 words).
    Output only the story text, with no introduction or explanation.""",
    output_key="current_story" # stores first draft in state
)