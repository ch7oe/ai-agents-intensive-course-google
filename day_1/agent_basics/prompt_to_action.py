import asyncio
from google.adk.agents import Agent
from google.adk.models.google_llm import Gemini
from google.adk.runners import InMemoryRunner
from google.adk.tools.google_search_tool import google_search
from utils.helpers import get_retry_config, get_api_key

async def main(query: str):
    
    get_api_key() # validate if api key exists. ADK picks up the key automatically from env vars
    retry_config = get_retry_config()

    #  define agent 
    root_agent = Agent(
        name="helpful_assistant",
        model=Gemini(
            model="gemini-2.5-flash-lite",
            retry_options=retry_config,
        ),
        description="A simple agent that can answer general questions.",
        instruction="You are a helpful assistant. Use Google Search for current info or if unsure.",
        tools=[google_search]
    )

    runner = InMemoryRunner(agent=root_agent)
    response = await runner.run_debug(query) # debug mode returns list of events/messages capturing every step in interaction

    print("\n--- EVENTS ---")
    for event in response:
        print(event)


if __name__ == "__main__":
    user_query = "What is today's date?"
    asyncio.run(main(user_query))