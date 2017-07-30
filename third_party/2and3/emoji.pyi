from typing import Tuple, Pattern, List, Dict, Union

_DEFAULT_DELIMITER = ...  # type: str


def emojize(
    string: str,
    use_aliases: bool=...,
    delimiters: Tuple[str, str]=...
) -> str: ...


def demojize(
    string: str,
    delimiters: Tuple[str, str]=...
) -> str: ...


def get_emoji_regexp() -> Pattern: ...


def emoji_lis(string: str) -> List[Dict[str, Union[int, str]]]: ...
