"""Currency agent with custom function tools"""

from google.adk.agents.llm_agent import LlmAgent
from google.adk.models.google_llm import Gemini
from utils.helpers import get_retry_config
from .tools import get_fee_for_payment_method, get_exchange_rate


currency_agent = LlmAgent(
    name="currency_agent",
    model=Gemini(
        model="gemini-2.5-flash-lite",
        retry_options=get_retry_config()
    ),
    instruction="""You are a smart currency conversion assistant.

    For currency conversion requests:
    1. Use `get_fee_for_payment_method()` to find transaction fees
    2. Use `get_exchange_rate()` to get currency conversion rates
    3. Check the "status" field in each tool's response for errors
    4. Calculate the final amount after fees based on the output from `get_fee_for_payment_method` and `get_exchange_rate` methods and provide a clear breakdown.
    5. First, state the final converted amount.
        Then, explain how you got that result by showing the intermediate amounts. Your explanation must include: the fee percentage and its
        value in the original currency, the amount remaining after the fee, and the exchange rate used for the final conversion.

    If any tool returns status "error", explain the issue to the user clearly.
    """,
    tools=[get_fee_for_payment_method, get_exchange_rate],
)
