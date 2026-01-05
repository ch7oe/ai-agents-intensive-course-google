from google.adk.agents import Agent
from google.adk.models import Gemini

from utils.helpers import get_retry_config

# editor agent: edits and polishes the draft from the writer agent 
editor_agent = Agent(
    name="EditorAgent",
    model=Gemini(
        model="gemini-2.5-flash-lite",
        retry_options=get_retry_config()
    ),
    # recevies {blog_draft} from the writer agent's output
    instruction="""Edit this draft: {blog_draft}
    Your task is to polish the text by fixing any grammatical errors, improving the flow and sentence structure, and enhancing overall clarity.""",
    output_key="final_blog"
)