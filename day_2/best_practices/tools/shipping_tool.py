"""Shipping tool with approval logic"""

from google.adk.tools.tool_context import ToolContext


LARGE_ORDER_THRESHOLD = 5


def place_shipping_order(
        num_containers: int,
        destination: str,
        tool_context: ToolContext
) -> dict:
    """Places a shipping order. Requires approval if ordering more than 5 containers (LARGE_ORDER_THRESHOLD).

    Args:
        num_containers: Number of containers to ship
        destination: Shipping destination

    Returns:
        Dictionary with order status
    """

    # SCENARIO 1: small orders (<=5 containers) auto approve
    if num_containers <= LARGE_ORDER_THRESHOLD:
        return {
            "status": "approved",
            "order_id": f"ORD-{num_containers}-AUTO",
            "num_containers": num_containers,
            "destination": destination,
            "message": f"Order auto-approved: {num_containers} containers to {destination}",
        }
    
    # SCENARIO 2: first time this tool is called. Large orders need human approval - PAUSE here
    if not tool_context.tool_confirmation: # check approval status
        tool_context.request_confirmation( # requestion approval
            hint=f"⚠️ Large order: {num_containers} containers to {destination}. Do you want to approve?",
            payload={"num_containers": num_containers, "destination": destination},
        )

        return { # this is sent to the agent
            "status": "pending",
            "message": f"Order for {num_containers} containers requires approval",
        }
    
    # SCENARIO 3: the tool is called AGAIN and is now resuming. Handle approval response - RESUME here
    if tool_context.tool_confirmation.confirmed:
        return {
            "status": "approved",
            "order_id": f"ORD-{num_containers}-HUMAN",
            "num_containers": num_containers,
            "destination": destination,
            "message": f"Order approved: {num_containers} containers to {destination}",
        }
    else:
        return {
            "status": "rejected",
            "message": f"Order rejected: {num_containers} containers to {destination}",
        }