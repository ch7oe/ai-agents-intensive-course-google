from google.adk.apps.app import App, ResumabilityConfig
from day_2.best_practices.agents.image_agent import image_agent


image_app = App(
    name="image_app",
    root_agent=image_agent,
    resumability_config=ResumabilityConfig(is_resumable=True),
)


