from .hot_topic_base import HotTopicBase, HotTopicItem
from .hot_topic_factory import register_hot_topic
import requests


@register_hot_topic(platform_name="zhihu_hot_topic")
class ZhihuHotTopics(HotTopicBase):

    def get_hot_topics(self, top: int = 10, type: str = "all") -> list[HotTopicItem]:
        """
        获取知乎热搜
        :param top: 热搜的数量
        :param type: 热搜的类型
        :return: 热搜的列表
        """
        url = f"https://www.zhihu.com/api/v3/feed/topstory/hot-lists/total?limit={top}&desktop=true"
        response = requests.get(url)
        try:
            hot_list = []
            for d in response.json()['data']:
                hot_list.append({
                    "title": d['target']['title'],
                    "url": d['target']['url']
                })
            return hot_list
        except:
            pass
        return []
    
    pass
