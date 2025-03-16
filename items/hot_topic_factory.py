from typing import Dict, Type, Optional, List
from .hot_topic_base import HotTopicBase, HotTopicItem
# from .sina_weibo_hot_topics import SinaWeiboHotTopics
import sys
import pkgutil
import importlib
import inspect

class HotTopicFactory:
    _platfroms: Dict[str, Type[HotTopicBase]] = {}

    @classmethod
    def register(cls, platform: str, hot_topic: Type[HotTopicBase]):
        cls._platfroms[platform] = hot_topic
    
    @classmethod
    def get_platform(cls, platform: str) -> Optional[Type[HotTopicBase]]:
        """
        获取平台的类
        :param platform: 平台名称
        :return: 平台的类
        """
        if platform not in cls._platfroms:
            return None
        return cls._platfroms.get(platform)()

    @classmethod
    def get_hot_topics(cls, platform_name: str, top: int = 10, type: str = "all") -> List[HotTopicItem]:
        """
        获取指定平台的热搜
        
        Args:
            platform_name: 平台名称
            top: 热搜数量
            type: 热搜类型
            
        Returns:
            热搜列表，如果平台不存在则返回空列表
        """
        platform = cls.get_platform(platform_name)
        if platform:
            return platform.get_hot_topics(top=top, type=type)
        return []


    @classmethod
    def get_all_platforms(cls) -> List[str]:
        """
        获取所有已注册的平台名称
        
        Returns:
            平台名称列表
        """
        return list(cls._platforms.keys())

    @classmethod
    def auto_discover(cls):
        """
        自动发现并注册所有的热搜平台
        """
        # 获取当前包
        package_name = __name__.split('.')[0]
        package = sys.modules[package_name]

        for _, module_name, _ in pkgutil.iter_modules(package.__path__, package.__name__ + '.'):
            # 导入模块
            module = importlib.import_module(module_name)
            
            # 查找模块中的所有类
            for name, obj in inspect.getmembers(module, inspect.isclass):
                # 检查是否是HotTopicBase的子类，但不是HotTopicBase本身
                if issubclass(obj, HotTopicBase) and obj != HotTopicBase:
                    # 从类名生成平台名称（转换为蛇形命名）
                    platform_name = ''.join(['_' + c.lower() if c.isupper() else c for c in name]).lstrip('_')
                    if platform_name.endswith('_hot_topics'):
                        platform_name = platform_name[:-11]  # 移除_hot_topics后缀
                    
                    # 注册平台
                    cls.register(platform_name, obj)
            

# 注册现有的热搜平台
# HotTopicFactory.register("sina_weibo", SinaWeiboHotTopics)

def register_hot_topic(platform_name=None):
    def decorator(cls):
        if not platform_name:
            # 从类名生成平台名称（转换为蛇形命名）
            name = ''.join(['_' + c.lower() if c.isupper() else c for c in cls.__name__]).lstrip('_')
            if name.endswith('_hot_topics'):
                name = name[:-11]  # 移除_hot_topics后缀
        else:
            name = platform_name
        HotTopicFactory.register(name, cls)
        return cls
    return decorator

# 初始化时自动发现并注册所有平台
HotTopicFactory.auto_discover()
