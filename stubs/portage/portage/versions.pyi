from _typeshed import Incomplete
from typing import Literal
from typing_extensions import Self

from .package.ebuild.config import config

def vercmp(ver1: str, ver2: str, silent: Literal[0, 1] = ...) -> int | None: ...

class _pkg_str(str):
    @property
    def stable(self) -> bool: ...
    def __new__(
        cls,
        cpv: str,
        metadata: dict[str, Incomplete] | None = ...,
        settings: config = ...,
        eapi=...,
        repo: str | None = ...,
        slot: str | None = ...,
        build_time: int | None = ...,
        build_id: str | None = ...,
        file_size: int | None = ...,
        mtime: int | None = ...,
        db=...,
        repoconfig=...,
    ) -> Self: ...
    def __init__(
        self,
        cpv: str,
        metadata: dict[str, Incomplete] | None = ...,
        settings: config = ...,
        eapi=...,
        repo: str | None = ...,
        slot: str | None = ...,
        build_time: int | None = ...,
        build_id: str | None = ...,
        file_size: int | None = ...,
        mtime: int | None = ...,
        db=...,
        repoconfig=...,
    ) -> None: ...
    @staticmethod
    def _long(var, default: int) -> int: ...

def catpkgsplit(
    mydata: str | _pkg_str, silent: Literal[0, 1] = ..., eapi: str | None = ...
) -> tuple[str | None, str, str, str] | None: ...
def __getattr__(name: str) -> Incomplete: ...  # incomplete module
