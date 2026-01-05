from google.adk.agents import LoopAgent, SequentialAgent
from day_1.agent_architectures.agents.initial_writer import initial_writer
from day_1.agent_architectures.agents.critic import critic_agent
from day_1.agent_architectures.agents.refiner import refiner_agent

# LoopAgent contain the agents that will run repeatedly: Critic -> Refiner
story_refinement_loop = LoopAgent(
    name="StoryRefinementLoop",
    sub_agents=[critic_agent, refiner_agent],
    max_iterations=2, # prevent infinite loop
)

# root agent is SequentialAgent that defines the overall workflow:
# initial write -> refinement loop
root_agent = SequentialAgent(
    name="StoryPipeline",
    sub_agents=[initial_writer, story_refinement_loop]
)