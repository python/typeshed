from _typeshed import Incomplete
from .data_dict import EMOJI_DATA as EMOJI_DATA, STATUS as STATUS, LANGUAGES as LANGUAGES

__all__ = ["get_emoji_unicode_dict", "get_aliases_unicode_dict", "EMOJI_DATA", "STATUS", "LANGUAGES"]

def get_emoji_unicode_dict(lang: str) -> Incomplete: ...
def get_aliases_unicode_dict() -> dict[str, str]: ...
