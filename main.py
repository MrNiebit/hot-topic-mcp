from mcp.server.lowlevel.server import Server, NotificationOptions
from mcp.server.models import InitializationOptions
from mcp.server.stdio import stdio_server
import mcp.types as types
from items.hot_topic_factory import HotTopicFactory
import json


server = Server("hot-topic-mcp")

TOOLS = [
    types.Tool(
        name="sina_weibo_hot_topic",
        description="这是一个用来获取新浪微博热搜的工具",
        inputSchema={
            "type": "object",
            "properties": {
                "top": {
                    "type": "integer",
                    "description": "热搜的数量",
                    "default": 10
                }
            }
        }
    ),
    types.Tool(
        name="zhihu_hot_topic",
        description="这是一个用来获取知乎热搜的工具",
        inputSchema={
            "type": "object",
            "properties": {
                "top": {
                    "type": "integer",
                    "description": "热搜的数量",
                    "default": 10
                }
            }
        }
    )
]
TOOLS_NAME_LIST = {tool.name: tool for tool in TOOLS}

@server.list_tools()
async def list_tools() -> list[types.Tool]:
    return TOOLS


@server.call_tool()
async def call_tool(name: str, arguments: dict | None) -> list[types.TextContent]:
    if name not in TOOLS_NAME_LIST:
        raise ValueError("未找到对应的工具")
    # print(arguments)
    result = HotTopicFactory.get_hot_topics(name, **arguments)

    # 这里返回的是列表
    return [types.TextContent(
        type="text",
        text=json.dumps(result, ensure_ascii=False)
    )]


async def run():
    async with stdio_server() as (read, write):
        await server.run(
            read_stream=read,
            write_stream=write,
            initialization_options=InitializationOptions(
                server_name="host-topic-mcp",
                server_version="2025.03.16",
                capabilities=server.get_capabilities(
                    notification_options=NotificationOptions(),
                    experimental_capabilities={}
                )
            )
        )


if __name__ == "__main__":
    import asyncio
    asyncio.run(run())
    pass
