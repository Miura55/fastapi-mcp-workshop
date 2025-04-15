from fastapi_mcp import FastApiMCP
import api


mcp = FastApiMCP(
    api.app,
    name="My API MCP",
    description="My API description",
    base_url="http://localhost:8000",
)

# Mount the MCP server directly to your FastAPI app
mcp.mount()

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(api.app, host="0.0.0.0", port=8000)
