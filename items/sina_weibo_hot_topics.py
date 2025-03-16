import requests
from .hot_topic_base import HotTopicBase, HotTopicItem
from .hot_topic_factory import register_hot_topic
from typing import List, Dict

type_dict = {
    "all": "新浪热榜",
    "hotcmnt": "热议榜",
    "minivideo": "视频热榜",
    "ent": "娱乐热榜",
    "ai": "AI热榜",
    "auto": "汽车热榜",
    "mother": "育儿热榜",
    "fashion": "时尚热榜",
    "travel": "旅游热榜",
    "esg": "ESG热榜",
}

@register_hot_topic(platform_name="sina_weibo_hot_topic")
class SinaWeiboHotTopics(HotTopicBase):
    
    def get_hot_topics(self, top: int = 10, type: str = "all") -> List[HotTopicItem]:
        """
        获取新浪微博热搜
        :param top: 热搜的数量
        :param type: 热搜的类型
        :return: 热搜的列表
        """
        url = f"https://newsapp.sina.cn/api/hotlist?newsId=HB-1-snhs%2Ftop_news_list-{type}"
        response = requests.get(url)
        try:
            host_list = []
            data = response.json()['data']['hotList']
            for d in data:
                url = d['base']['base']['url']
                title = d['base']['dynamicName']
                host_list.append({
                    "title": title,
                    "url": url
                })
            return host_list[:top]
        except:
            return []
