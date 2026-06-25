from mcp.server.fastmcp import FastMCP
mcp = FastMCP("test")

def dynamic_tool() -> str:
    return "test"

mcp.add_tool(dynamic_tool, name="my_tool", description="A dynamic tool")
print("Tool added successfully!")
