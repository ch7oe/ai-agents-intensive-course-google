import asyncio
from .agent import enhanced_currency_agent
from utils.helpers import get_api_key, show_python_code_and_result
from google.adk.runners import InMemoryRunner


async def main(query: str):

    get_api_key()

    # currency_runner = InMemoryRunner(agent=currency_agent)
    # response = await currency_runner.run_debug(query)

    enhanced_runner = InMemoryRunner(agent=enhanced_currency_agent)
    response = await enhanced_runner.run_debug(query)

    # print("---EVENTS---\n")
    # for event in response:
    #     print(event)

    show_python_code_and_result(response)


if __name__ == "__main__":
    user_query = "Convert 1,250 USD to INR using a Bank Transfer. Show me the precise calculation."
    asyncio.run(main(user_query))