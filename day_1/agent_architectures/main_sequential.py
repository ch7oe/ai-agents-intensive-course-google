import asyncio
from google.adk.runners import InMemoryRunner
from day_1.agent_architectures.workflows.sequential_research_summary import root_agent
from utils.helpers import get_api_key

async def main(query: str):

    get_api_key()

    runner = InMemoryRunner(agent=root_agent)
    response = await runner.run_debug(query)

    print("---EVENTS---\n")
    for event in response:
        print(event)


if __name__ == "__main__":
    user_query = "Write a blog post about the benefits of multi-agent systems for software developers"
    asyncio.run(main(user_query))

