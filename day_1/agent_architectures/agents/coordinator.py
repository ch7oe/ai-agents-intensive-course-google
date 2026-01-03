from google.adk.agents import Agent
from google.adk.models.google_llm import Gemini
from google.adk.tools.agent_tool import AgentTool

from day_1.agent_architectures.agents.researcher import research_agent
from day_1.agent_architectures.agents.summarizer import summarizer_agent

from utils.helpers import get_retry_config

# Root coordinator: orchestrates the workflow by calling the sub-agents as tools
root_agent = Agent(
    name="ResearchCoordinator",
    model=Gemini(
        model="gemini-2.5-flash-lite",
        retry_options=get_retry_config()
    ),
    # tells the root agent HOW to use its tools (which are the other agents)
    instruction="""You are a research coordinator. Your goal is to answer the user's query by orchestrating a workflow.
    1. First, you MUST call the `ResearchAgent` tool to find relevant information on the topic provided by the user.
    2. Next, after receiving the research findings, you MUST call the `SummarizerAgent` tool to create a concise summary.
    3. Finally, present the final summary clearly to the user as your response.""",
    # wrap the sub-agents in AgentTool() to make them callable tools for the root agent
    tools=[AgentTool(research_agent), AgentTool(summarizer_agent)]
)
