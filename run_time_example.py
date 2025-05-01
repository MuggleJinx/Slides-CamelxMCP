import asyncio
from camel.toolkits.mcp_toolkit import MCPToolkit
from camel.agents import ChatAgent
from camel.models import ModelFactory

from camel.types import ModelPlatformType, ModelType


async def run_example():
    # Initialize the MCPToolkit with your configuration file
    mcp_toolkit = MCPToolkit(config_path="config/time.json")

    # Connect to all configured MCP servers
    await mcp_toolkit.connect()

    model = ModelFactory.create(
        model_platform=ModelPlatformType.ANTHROPIC,
        model_type=ModelType.CLAUDE_3_5_SONNET,
    )

    camel_agent = ChatAgent(
        model=model,
        tools=[*mcp_toolkit.get_tools()],
    )
    response = await camel_agent.astep("What time is it now?")
    print(response.msgs[0].content)
    print(response.info['tool_calls'])

    # Disconnect from all servers
    await mcp_toolkit.disconnect()

asyncio.run(run_example())