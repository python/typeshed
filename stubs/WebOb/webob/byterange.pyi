from typing import NamedTuple
from typing_extensions import Self

class Range(NamedTuple):
    start: int | None
    end: int | None
    def range_for_length(self, length: int | None) -> tuple[int, int] | None: ...
    def content_range(self, length: int | None) -> ContentRange | None: ...
    @classmethod
    def parse(cls, header: str | None) -> Self: ...

class ContentRange(NamedTuple):
    start: int | None
    stop: int | None
    length: int | None
    @classmethod
    def parse(cls, value: str | None) -> Self: ...
