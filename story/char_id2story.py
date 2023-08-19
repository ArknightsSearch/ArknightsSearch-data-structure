__all__ = ['char_id2story']

"""
char_id对应story_data.json中的序号
"""

char_id2story = dict[
    str,  # char_id
    list[
        str  # story_seq
    ]
]
