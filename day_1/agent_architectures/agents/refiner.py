from google.adk.agents import Agent
from google.adk.models import Gemini
from google.adk.tools.function_tool import FunctionTool

from utils.helpers import get_retry_config


def exit_loop():
    """Call this function ONLY when the critique is 'APPROVED', 
    indicating the story is finished and no more changes are needed."""
    
    return {
        "status": "approved",
        "message": "Story approved. Exiting refinement loop."
    }


# refiner agent: refines the story based on critique OR calls the exit_loop function
refiner_agent = Agent(
    name="RefinerAgent",
    model=Gemini(
        model="gemini-2.5-flash-lite",
        retry_options=get_retry_config()
    ),
    instruction="""You are a story refiner. You have a story draft and critique.
    
    Story Draft: {current_story}
    Critique: {critique}
    
    Your task is to analyze the critique.
    - IF the critique is EXACTLY "APPROVED", you MUST call the `exit_loop` function and nothing else.
    - OTHERWISE, rewrite the story draft to fully incorporate the feedback from the critique.""",
    output_key="current_story", # overwrites story with new, refined version
    tools=[FunctionTool(exit_loop)]
)