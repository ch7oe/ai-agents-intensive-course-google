from google.adk.agents import Agent
from google.adk.models.google_llm import Gemini
from google.adk.tools.google_search_tool import google_search
from .helpers import get_api_key, get_retry_config

get_api_key()


root_agent = Agent(
    name="helpful_assistant",
    model=Gemini(
        model="gemini-2.5-flash-lite",
        retry_options=get_retry_config()
    ),
    instruction="You are a helpful assistant. Use Google Search for current info or if unsure.",
    tools=[google_search]
)