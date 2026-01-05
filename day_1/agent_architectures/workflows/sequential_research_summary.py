from google.adk.agents import SequentialAgent

from day_1.agent_architectures.agents.outline import outline_agent
from day_1.agent_architectures.agents.writer import writer_agent
from day_1.agent_architectures.agents.editor import editor_agent

root_agent = SequentialAgent(
    name="BlogPipeline",
    sub_agents=[outline_agent, writer_agent, editor_agent]
)
