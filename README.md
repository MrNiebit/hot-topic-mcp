# 项目简介

基于Model Context Protocol(MCP)实现获取各个平台热点的功能

- [x] 新浪热搜

- [ ] 知乎热搜
...

API参考项目：https://github.com/imsyy/DailyHotApi

# 项目结构

新增热搜类

1、继承 `HotTopicBase` 类，然后重写 `get_hot_topics` 方法
2、@register_hot_topic(platform_name="sina_weibo_hot_topic") platform 为tool name

