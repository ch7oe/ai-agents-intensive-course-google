from google.adk.agents import Agent
from google.adk.models import Gemini

from utils.helpers import get_retry_config

# writer agent: writes the full blog post based on the outline from the previous agent
writer_agent = Agent(
    name="WriterAgent",
    model=Gemini(
        model="gemini-2.5-flash-lite",
        retry_options=get_retry_config()
    ),
    # receives {blog_outline} from the outline agent's output
    instruction="""Following this outline strictly: {blog_outline}
    Write a brief, 200 to 300-word blog post with an engaging and informative tone.""",
    output_key="blog_draft",
)