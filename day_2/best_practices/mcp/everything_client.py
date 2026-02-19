"""MCP integration with Everything Server"""

from google.adk.tools.mcp_tool.mcp_toolset import McpToolset
from google.adk.tools.mcp_tool.mcp_session_manager import StdioConnectionParams
from mcp import StdioServerParameters

mcp_image_server = McpToolset(
    connection_params=StdioConnectionParams(
        server_params=StdioServerParameters(
            command="npx", # run mcp server via npx
            args=[
                "-y", # argument for npx to auto-confirm install
                "@modelcontextprotocol/server-everything",
                ],
            tool_filter=["getTinyImage"],
        ),
        timeout=30,
    )
)