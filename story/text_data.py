__all__ = ['text_data']

"""
纯文本数据
"""

from typing import Literal

text_data = dict[
    Literal['zh_CN'],  # 目前仅支持简体中文
    str  # 文本
]
