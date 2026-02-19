"""runnner entry point for image demo."""

import asyncio
from google.adk.runners import Runner
from day_2.best_practices.app import image_app
from utils.helpers import get_api_key
from day_2.best_practices.session import session_service

async def main(query: str):
    get_api_key()

    runner = Runner(
        app=image_app,
        session_service=session_service
        )
    async with runner:
        response = await runner.run_debug(
        query, 
        verbose=True
        )
    
    print("---EVENTS---\n")
    for event in response:
        print(event)

    
if __name__ == "__main__":
    user_query = "Provide a sample tiny image"
    asyncio.run(main(user_query))
