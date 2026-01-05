from google.adk.agents import Agent
from google.adk.models import Gemini

from utils.helpers import get_retry_config

# outline agent: creates the initial blog post outline
outline_agent = Agent(
    name="OutlineAgent",
    model=Gemini(
        model="gemini-2.5-flash-lite",
        retry_options=get_retry_config()
    ),
    instruction="""Create a blog outline for the given topic with:
    1. A catchy headline
    2. An introduction hook
    3. 3-5 main sections with 2-3 bullet points for each
    4. A concluding thought""",
    output_key="blog_outline" # result of this agent will stored in the session state with this key
)

