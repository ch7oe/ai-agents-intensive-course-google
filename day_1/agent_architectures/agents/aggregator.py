from google.adk.agents import Agent
from google.adk.models import Gemini
from utils.helpers import get_retry_config

# aggregator agent: runs AFTER the parallel step to combine the results 
aggregator = Agent(
    name="AggregatorAgent",
    model=Gemini(
        model="gemini-2.5-flash-lite",
        retry_options=get_retry_config()
    ),
    # uses placeholders to inject the outputs from the parallel agents 
    instruction="""Combine these three research findings into a single executive summary:

    **Technology Trends:**
    {tech_research}
    
    **Health Breakthroughs:**
    {health_research}
    
    **Finance Innovations:**
    {finance_research}
    
    Your summary should highlight common themes, surprising connections, 
    and the most important key takeaways from all three reports. The final summary should be around 200 words.""",
    output_key="final_summary"
) 