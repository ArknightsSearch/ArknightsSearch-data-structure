__all__ = ['zone_name']

"""
区域名称
[!] 注意，对于名称数据，仅确保zh_CN存在
"""

from typing import Literal

zone_name = dict[
    str,  # 区域id
    dict[
        Literal['zh_CN', 'ja_JP', 'en_US'],  # 语种
        str  # 名称
    ]
]
