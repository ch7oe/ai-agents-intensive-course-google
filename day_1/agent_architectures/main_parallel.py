import asyncio
from google.adk.runners import InMemoryRunner
from day_1.agent_architectures.workflows.parallel_multi_topic_research import root_agent

from utils.helpers import get_api_key

async def main(query: str):

    get_api_key()
    
    runner = InMemoryRunner(agent=root_agent)
    response = await runner.run_debug(query)

    
    print("---EVENTS---\n")
    for event in response:
        print(event)


if __name__ == "__main__":
    user_query = "Run the daily executive briefing on Tech, Health, and Finance"
    asyncio.run(main(user_query))