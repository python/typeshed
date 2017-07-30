from typing import Tuple, Pattern, List, Dict, Union

_DEFAULT_DELIMITER = ':'


def emojize(
    string: str,
    use_aliases: bool=False,
    delimiters: Tuple[str, str]=(_DEFAULT_DELIMITER, _DEFAULT_DELIMITER)
) -> str: ...


def demojize(
    string: str,
    delimiters: Tuple[str, str]=(_DEFAULT_DELIMITER, _DEFAULT_DELIMITER)
) -> str: ...


def get_emoji_regexp() -> Pattern: ...


def emoji_lis(string: str) -> List[Dict[str, Union[int, str]]]: ...
