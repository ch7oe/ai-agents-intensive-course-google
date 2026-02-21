"""runner with resumable app for shipping demo."""

import asyncio
import uuid
from google.genai import types
from google.adk.runners import Runner

from day_2.best_practices.app import shipping_app
from day_2.best_practices.session import session_service
from utils.helpers import get_api_key
from day_2.best_practices.runner_utils import (
    check_for_approval,
    create_approval_response,
    print_agent_response
)


shipping_runner = Runner(
    app=shipping_app,
    session_service=session_service
)

async def run_shipping_workflow(query: str, auto_approve: bool = True):
    """Runs a shipping workflow with approval handling.

    Args:
        query: User's shipping request
        auto_approve: Whether to auto-approve large orders (simulates human decision)
    """

    get_api_key()

    print(f"\n{'=' * 60}")
    print(f"User > {query}\n")

    # generate unique session ID
    session_id = f"order_{uuid.uuid4().hex[:8]}"

    # create session
    await session_service.create_session(
        app_name="shipping_coordinator",
        user_id="test_user",
        session_id=session_id
    )

    query_content = types.Content(role="user", parts=[types.Part(text=query)])
    events = []

    # STEP 1: send initial request to the Agent. 
    # If num_containers > 5, the Agent returns the special `adk_request_confirmation` event
    async for event in shipping_runner.run_async(
        user_id="test_user",
        session_id=session_id,
        new_message=query_content
    ):
        events.append(event)
    
    # STEP 2: loop through all the events generated and check if `adk_request_confirmation` is present
    approval_info = check_for_approval(events)

    # STEP 3: if the event is present, its a large order - HANDLE APPROVAL WORKFLOW
    if approval_info:
        print(f"⏸️  Pausing for approval...")
        print(f"🤔 Human Decision: {'APPROVE ✅' if auto_approve else 'REJECT ❌'}\n")

        # PATH A: resume the agent by calling run_async() again with the approval decision
        async for event in shipping_runner.run_async(
            user_id="test_user",
            session_id=session_id,
            new_message=create_approval_response(
                approval_info, auto_approve
            ),
            invocation_id=approval_info["invocation_id"] # important! same invocation_id tells ADK to RESUME
        ):
            if event.content and event.content.parts:
                for part in event.content.parts:
                    if part.text:
                        print(f"Agent > {part.text}")
    # PATH B: if the `adk_request_confirmation` is not present - no approval needed - order completed immediately
    else:
        print_agent_response(events)
    
    print(f"{'='*60}\n")



if __name__ == "__main__":
    user_query = "Ship 10 containers to Rotterdam"
    asyncio.run(run_shipping_workflow(
        user_query,
        auto_approve=True
    ))
