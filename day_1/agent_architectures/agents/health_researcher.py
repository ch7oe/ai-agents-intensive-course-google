from google.adk.agents import Agent
from google.adk.models import Gemini
from google.adk.tools.google_search_tool import google_search

from utils.helpers import get_retry_config

# health researcher: focuses on medical breakthroughs
health_researcher = Agent(
    name="HealthResearcher",
    model=Gemini(
        model="gemini-2.5-flash-lite",
        retry_options=get_retry_config()
    ),
    instruction="""Research recent medical breakthroughs. Include 3 significant advances, their practical applications, and estimated timelines. Keep the report concise (100 words).""",
tools=[google_search],
output_key="health_research"
)