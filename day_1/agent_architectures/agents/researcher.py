from google.adk.agents import Agent
from google.adk.models.google_llm import Gemini
from google.adk.tools.google_search_tool import google_search

from utils.helpers import get_retry_config

# Research Agent: responsible only for gathering factual information via google_search tool
research_agent = Agent(
    name="ResearchAgent",
    model=Gemini(
        model="gemini-2.5-flash-lite",
        retry_options=get_retry_config()
    ),
    instruction="""You are a specialized research agent. 
    Your only job is to use the google_search tool to find 2-3 pieces of relevant information on the given topic and present the findings with citations.""",
    tools=[google_search],
    output_key="research_findings" # the result of this agent will be stored in the session state with this key
)