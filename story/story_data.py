__all__ = ['story_data']

"""
故事数据
"""

from typing import TypedDict, Literal


class StoryData(TypedDict):
    # id
    id: str
    # 种类
    type: Literal['Main', 'Activity', 'Rogue', 'Memory']
    # 名称
    name: dict[
        Literal['zh_CN', 'ja_JP', 'en_US'],  # 语种
        str
    ]
    # 对于Memory是角色名，对于其他是区域id
    zone: str


story_data = dict[
    str,  # story_seq
    StoryData
]
