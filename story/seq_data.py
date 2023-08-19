__all__ = ['seq_data']

"""
story中包含的char_id与char_seq
后端加载时会生成 char_id2seq char_name2seq
"""

seq_data = list[
    list[
        list[
            str  # char_id
        ],
        list[
            str  # char_name
        ]
    ]
]
