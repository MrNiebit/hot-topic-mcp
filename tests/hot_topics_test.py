import os
import sys
# 将项目根目录添加到Python路径
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from items.hot_topic_factory import HotTopicFactory
import json


result = HotTopicFactory.get_hot_topics("新浪微博热搜")
print(result)

print(json.dumps(result, ensure_ascii=False))