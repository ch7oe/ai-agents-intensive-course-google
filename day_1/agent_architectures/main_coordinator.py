import asyncio
from google.adk.runners import InMemoryRunner
from day_1.agent_architectures.agents.coordinator import root_agent

from utils.helpers import get_api_key

async def main(query: str):

    get_api_key()

    runner = InMemoryRunner(agent=root_agent)
    response = await runner.run_debug(query)

    print("---EVENTS---\n")
    for event in response:
        print(event)


if __name__ == "__main__":
    user_query = "What are the latest advancements in quantum computing and what do they mean for AI"
    asyncio.run(main(user_query))