import asyncio
from google.adk.runners import InMemoryRunner
from utils.helpers import get_api_key
from day_1.agent_architectures.workflows.loop_story_refinement import root_agent

async def main(query: str):

    get_api_key()

    runner = InMemoryRunner(agent=root_agent)
    response = await runner.run_debug(query)

    print("---EVENTS---\n")
    for event in response:
        print(event)


if __name__ == "__main__":
    user_query = "Write a short story about a magic unicorn " \
    "who is having fun adventures outside with their friends."
    asyncio.run(main(user_query))

