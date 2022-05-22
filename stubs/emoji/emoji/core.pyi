from collections.abc import Callable
from typing import Pattern
from typing_extensions import Literal

_DEFAULT_DELIMITER: str

class _DeprecatedParameter: ...

def emojize(
    string: str,
    use_aliases: bool | type[_DeprecatedParameter] = ...,
    delimiters: tuple[str, str] = ...,
    variant: Literal["text_type", "emoji_type", None] = ...,
    language: str = ...,
    version: float | None = ...,
    handle_version: str | Callable[[str, dict[str, str]], str] | None = ...,
) -> str: ...
def demojize(
    string: str,
    use_aliases: bool | type[_DeprecatedParameter] = ...,
    delimiters: tuple[str, str] = ...,
    language: str = ...,
    version: float | None = ...,
    handle_version: str | Callable[[str, dict[str, str]], str] | None = ...,
) -> str: ...
def replace_emoji(
    string: str,
    replace: str | Callable[[str, dict[str, str]], str] = ...,
    language: str | type[_DeprecatedParameter] = ...,
    version: float | None = ...,
) -> str: ...
def get_emoji_regexp(language: str | None = ...) -> Pattern[str]: ...
def emoji_lis(string: str, language: str | type[_DeprecatedParameter] = ...) -> list[dict[str, int | str]]: ...
def emoji_list(string: str) -> list[dict[str, int | str]]: ...
def distinct_emoji_lis(string: str, language: str | type[_DeprecatedParameter] = ...) -> list[str]: ...
def distinct_emoji_list(string: str) -> list[str]: ...
def emoji_count(string: str, unique: bool = ...) -> int: ...
def version(string: str) -> float: ...
