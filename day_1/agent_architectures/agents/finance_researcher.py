from google.adk.agents import Agent
from google.adk.models import Gemini
from google.adk.tools.google_search_tool import google_search

from utils.helpers import get_retry_config

# finance researcher: focuses on fintech trends
finance_researcher = Agent(
    name="FinanceResearcher",
    model=Gemini(
        model="gemini-2.5-flash-lite",
        retry_options=get_retry_config()
    ), instruction="""Research current fintech trends. Include 3 key trends, 
    their market implications, and the future outlook. Keep the report concise (100 words).""",
    tools=[google_search],
    output_key="finance_research"
)