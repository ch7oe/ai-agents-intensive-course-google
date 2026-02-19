from google.adk.agents import LlmAgent
from google.adk.models.google_llm import Gemini
from utils.helpers import get_retry_config
from day_2.best_practices.mcp.everything_client import mcp_image_server


# image agent with mcp integration 
image_agent = LlmAgent(
    model=Gemini(
        model="gemini-2.5-flash-lite", retry_options=get_retry_config()
    ),
    name="image_agent",
    instruction="Use the MCP Tool to generate images for user queries",
    tools=[mcp_image_server]
)
 
 