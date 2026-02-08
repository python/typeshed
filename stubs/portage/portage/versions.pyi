from typing import Any, Literal
from typing_extensions import Self

def vercmp(ver1: str, ver2: str, silent: Literal[0, 1] = ...) -> int | None: ...

class _pkg_str(str):
    @property
    def stable(self) -> bool: ...
    def __new__(
        cls,
        cpv: str,
        metadata: dict[str, Any] | None = ...,
        settings: Any = ...,
        eapi: Any = ...,
        repo: str | None = ...,
        slot: str | None = ...,
        build_time: int | None = ...,
        build_id: str | None = ...,
        file_size: int | None = ...,
        mtime: int | None = ...,
        db: Any = ...,
        repoconfig: Any = ...,
    ) -> Self: ...
    def __init__(
        self,
        cpv: str,
        metadata: dict[str, Any] | None = ...,
        settings: Any = ...,
        eapi: Any = ...,
        repo: str | None = ...,
        slot: str | None = ...,
        build_time: int | None = ...,
        build_id: str | None = ...,
        file_size: int | None = ...,
        mtime: int | None = ...,
        db: Any = ...,
        repoconfig: Any = ...,
    ) -> None: ...
    @staticmethod
    def _long(var: Any, default: int) -> int: ...

def catpkgsplit(
    mydata: str | _pkg_str, silent: Literal[0, 1] = ..., eapi: str | None = ...
) -> tuple[str | None, str, str, str] | None: ...
