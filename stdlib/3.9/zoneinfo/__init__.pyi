from __future__ import annotations

import os
import typing
from datetime import datetime, tzinfo
from typing import IO, Optional, Sequence, Type, Union

class ZoneInfo(tzinfo):
    _T = typing.TypeVar("_T", bound="ZoneInfo")
    key: str
    def __init__(self, key: str) -> None: ...
    @classmethod
    def no_cache(cls: Type[_T], key: str) -> _T: ...
    @classmethod
    def from_file(
        cls: Type[_T], fobj: IO[bytes], /, key: Optional[str] = None
    ) -> _T: ...
    @classmethod
    def clear_cache(cls, *, only_keys=Sequence[str]) -> None: ...

# Note: Both here and in clear_cache, the types allow the use of `str` where
# a sequence of strings is required. This should be remedied if a solution
# to this typing bug is found: https://github.com/python/typing/issues/256
def reset_tzpath(
    to: Optional[Sequence[Union[os.PathLike, str]]] = None
) -> None: ...
def available_timezones() -> typing.Set[str]: ...

TZPATH: Sequence[str]
