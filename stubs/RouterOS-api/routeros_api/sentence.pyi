import builtins
import re
from collections.abc import Iterable, Sequence
from typing_extensions import Self

from routeros_api.query import _Query

response_re: re.Pattern[bytes]  # undocumented
attribute_re: re.Pattern[bytes]  # undocumented
tag_re: re.Pattern[bytes]  # undocumented

class ResponseSentence:  # undocumented
    attributes: dict[bytes, bytes]
    # re, trap, fatal, empty or done.
    type: bytes
    tag: bytes | None
    def __init__(self, type: bytes) -> None: ...
    @classmethod
    def parse(cls, sentence: Sequence[bytes]) -> Self: ...
    def parse_attributes(self, serialized_attributes: Iterable[bytes]) -> None: ...
    def process_value(self, value: bytes) -> bytes: ...

class CommandSentence:  # undocumented
    path: bytes
    command: bytes
    # A None value sends the attribute with no value.
    attributes: dict[bytes, bytes | None]
    api_attributes: dict[bytes, bytes]
    queries: builtins.set[_Query]
    tag: bytes | None
    def __init__(self, path: bytes, command: bytes, tag: bytes | None = None) -> None: ...
    def get_api_format(self) -> list[bytes]: ...
    def set(self, key: bytes, value: bytes | None) -> None: ...
    # A positional argument without get_api_format is a key whose rows must have a value.
    def filter(self, *args: _Query | str | bytes, **kwargs: str | bytes) -> None: ...
