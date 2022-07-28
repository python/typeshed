from emoji.core import (
    emojize as emojize,
    demojize as demojize,
    emoji_count as emoji_count,
    emoji_list as emoji_list,
    distinct_emoji_list as distinct_emoji_list,
    replace_emoji as replace_emoji,
    version as version,
    is_emoji as is_emoji,
)
from emoji.unicode_codes import EMOJI_DATA, STATUS, LANGUAGES

__all__ = [
    # emoji.core
    "emojize",
    "demojize",
    "emoji_count",
    "emoji_list",
    "distinct_emoji_list",
    "replace_emoji",
    "version",
    "is_emoji",
    # emoji.unicode_codes
    "EMOJI_DATA",
    "STATUS",
    "LANGUAGES",
]
__version__: str
__author__: str
__email__: str
__source__: str
__license__: str
