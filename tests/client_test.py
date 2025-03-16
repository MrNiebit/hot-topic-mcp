from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

server_params = StdioServerParameters(
    command="python",
    args=["../main.py"]
)

async def run():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            # 初始化
            print(await session.initialize())
            result = await session.list_tools()
            print(result)

            result = await session.call_tool(name="sina_weibo_hot_topic", arguments={"top": 5, "type": "all"})
            print(result)



if __name__ == "__main__":
    import asyncio
    asyncio.run(run())
