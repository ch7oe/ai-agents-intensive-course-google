from google.adk.agents import Agent
from google.adk.models import Gemini
from google.adk.tools.google_search_tool import google_search

from utils.helpers import get_retry_config

# tech researcher: focuses on AI and ML trends
tech_researcher = Agent(
    name="TechResearcher",
    model=Gemini(
        model="gemini-2.5-flash-lite",
        retry_options=get_retry_config()
    ),
    instruction="""Research the latest AI/ML trends. Include 3 key developments,
    the main companies involved, and the potential impact. Keep the report very concise (100 words).""",
    tools=[google_search],
    output_key="tech_research" 
)