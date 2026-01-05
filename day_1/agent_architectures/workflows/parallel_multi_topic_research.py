from google.adk.agents import ParallelAgent, SequentialAgent
from day_1.agent_architectures.agents.tech_researcher import tech_researcher
from day_1.agent_architectures.agents.health_researcher import health_researcher
from day_1.agent_architectures.agents.finance_researcher import finance_researcher
from day_1.agent_architectures.agents.aggregator import aggregator

# Parallel Agent runs all its sub-agents simutaneously
parallel_research_team = ParallelAgent(
    name="ParallelResearchTeam",
    sub_agents=[tech_researcher, health_researcher, finance_researcher]
)

# this Sequential Agent defines the high-level workflow:
# run the parallel team first, then run the aggregator
root_agent = SequentialAgent(
    name="ResearchSystem",
    sub_agents=[parallel_research_team, aggregator]
)