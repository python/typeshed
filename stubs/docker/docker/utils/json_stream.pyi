import json
from collections.abc import Callable, Generator, Iterator
from typing import Any
from typing_extensions import TypeAlias

json_decoder: json.JSONDecoder

# Type alias for JSON, explained at:
# https://github.com/python/typing/issues/182#issuecomment-1320974824.
_JSON: TypeAlias = dict[str, _JSON] | list[_JSON] | str | int | float | bool | None

def stream_as_text(stream: Iterator[str | bytes]) -> Generator[str, None, None]: ...
def json_splitter(buffer: str) -> tuple[_JSON, str] | None: ...
def json_stream(stream: Iterator[str]) -> Generator[_JSON, None, None]: ...
def line_splitter(buffer: str, separator: str = "\n") -> tuple[str, str] | None: ...
def split_buffer(
    stream: Iterator[str | bytes],
    splitter: Callable[[str], tuple[str, str]] | None = None,
    decoder: Callable[[str], Any] = ...,
) -> Generator[Any, None, None]: ...
