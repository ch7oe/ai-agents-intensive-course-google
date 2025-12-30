import os
from pathlib import Path
from dotenv import load_dotenv
from google.genai import types


def setup_api_key():
    """Configure Gemini API key from .env file.
    Finds .env in project root directory
    """
    project_root = Path(__file__).resolve().parent.parent
    env_path = project_root / ".env"

    load_dotenv(dotenv_path=env_path)

    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise ValueError("GOOGLE_API_KEY not found.")
    
    print("Gemini API key setup complete.")

    return api_key


def get_retry_config():
    """Retry logic for all labs."""

    return types.HttpRetryOptions(
        attempts=5, # Maximum rety attemps
        exp_base=7, # Delay multiplier
        initial_delay=1, # Initial delay before first retry (in seconds)
        http_status_codes=[429, 500, 503, 504] # Retry on these HTTP errors
    )
