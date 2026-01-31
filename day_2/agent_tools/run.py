import asyncio
from .agent import currency_agent
from utils.helpers import get_api_key
from google.adk.runners import InMemoryRunner


async def main(query: str):

    get_api_key()

    currency_runner = InMemoryRunner(agent=currency_agent)
    response = await currency_runner.run_debug(query)

    print("---EVENTS---\n")
    for event in response:
        print(event)


if __name__ == "__main__":
    user_query = "I want to convert 500 US Dollars to Euros using my Platinum Credit Card. How much will I receive?"
    asyncio.run(main(user_query))