from google.adk.apps.app import App, ResumabilityConfig
from day_2.best_practices.agents.image_agent import image_agent
from day_2.best_practices.agents.shipping_agent import shipping_agent


image_app = App(
    name="image_app",
    root_agent=image_agent,
    resumability_config=ResumabilityConfig(is_resumable=True),
)

# wrap shipping_agent in resumable app - KEY for long-running operations
shipping_app = App(
    name="shipping_coordinator",
    root_agent=shipping_agent,
    resumability_config=ResumabilityConfig(is_resumable=True),
)
