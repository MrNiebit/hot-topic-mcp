from pydantic import BaseModel
from abc import ABC, abstractmethod
from typing import List, Dict, Any, Optional, TypedDict

class HotTopicItem(TypedDict):
    """ 热搜条目 """
    title: str
    url: str


# 继承ABC，可以使用@abstractmethod 装饰器来定义抽象方法，这些方法必须由子类实现
class HotTopicBase(ABC):
    """ 热搜平台抽象基类 """

    @abstractmethod
    def get_hot_topics(self, top: int = 10, type: str = "all") -> List[HotTopicItem]:
        """
        获取热搜条目
        :param top: 热搜数量
        :param type: 热搜类型
        :return: 热搜条目列表
        """
        
