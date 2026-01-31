"""Currency agent with custom function tools"""

from google.adk.agents.llm_agent import LlmAgent
from google.adk.models.google_llm import Gemini
from google.adk.code_executors import BuiltInCodeExecutor
from google.adk.tools.agent_tool import AgentTool
from utils.helpers import get_retry_config
from .tools import get_fee_for_payment_method, get_exchange_rate


# currency_agent = LlmAgent(
#     name="currency_agent",
#     model=Gemini(
#         model="gemini-2.5-flash-lite",
#         retry_options=get_retry_config()
#     ),
#     instruction="""You are a smart currency conversion assistant.

#     For currency conversion requests:
#     1. Use `get_fee_for_payment_method()` to find transaction fees
#     2. Use `get_exchange_rate()` to get currency conversion rates
#     3. Check the "status" field in each tool's response for errors
#     4. Calculate the final amount after fees based on the output from `get_fee_for_payment_method` and `get_exchange_rate` methods and provide a clear breakdown.
#     5. First, state the final converted amount.
#         Then, explain how you got that result by showing the intermediate amounts. Your explanation must include: the fee percentage and its
#         value in the original currency, the amount remaining after the fee, and the exchange rate used for the final conversion.

#     If any tool returns status "error", explain the issue to the user clearly.
#     """,
#     tools=[get_fee_for_payment_method, get_exchange_rate],
# )


calculation_agent = LlmAgent(
    name="CalculationAgent",
    model= Gemini(
        model="gemini-2.5-flash-lite",
        retry_options=get_retry_config()
    ),
    instruction="""You are a specialized calculator that ONLY responds with Python code. You are forbidden from providing any text, explanations, or conversational responses.
 
     Your task is to take a request for a calculation and translate it into a single block of Python code that calculates the answer.
     
     **RULES:**
    1.  Your output MUST be ONLY a Python code block.
    2.  Do NOT write any text before or after the code block.
    3.  The Python code MUST calculate the result.
    4.  The Python code MUST print the final result to stdout.
    5.  You are PROHIBITED from performing the calculation yourself. Your only job is to generate the code that will perform the calculation.
   
    Failure to follow these rules will result in an error.
       """,
    code_executor=BuiltInCodeExecutor() # gives agent code execution capabilities
)


enhanced_currency_agent = LlmAgent(
    name="enhanced_currency_agent",
    model=Gemini(
        model="gemini-2.5-flash-lite",
        retry_options=get_retry_config()
    ),
    # updated instruction
    instruction="""You are a smart currency conversion assistant. You must strictly follow these steps and use the available tools.

  For any currency conversion request:

   1. Get Transaction Fee: Use the get_fee_for_payment_method() tool to determine the transaction fee.
   2. Get Exchange Rate: Use the get_exchange_rate() tool to get the currency conversion rate.
   3. Error Check: After each tool call, you must check the "status" field in the response. If the status is "error", you must stop and clearly explain the issue to the user.
   4. Calculate Final Amount (CRITICAL): You are strictly prohibited from performing any arithmetic calculations yourself. You must use the calculation_agent tool to generate Python code that calculates the final converted amount. This 
      code will use the fee information from step 1 and the exchange rate from step 2.
   5. Provide Detailed Breakdown: In your summary, you must:
       * State the final converted amount.
       * Explain how the result was calculated, including:
           * The fee percentage and the fee amount in the original currency.
           * The amount remaining after deducting the fee.
           * The exchange rate applied.
    """,
    tools=[
        get_fee_for_payment_method,
        get_exchange_rate,
        AgentTool(agent=calculation_agent), # using another agent as a tool
    ],
)