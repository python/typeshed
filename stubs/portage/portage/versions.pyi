from _typeshed import Incomplete
from typing import Literal
from typing_extensions import Self

from .package.ebuild.config import config

def vercmp(ver1: str, ver2: str, silent: Literal[0, 1] = 1) -> int | None: ...

class _pkg_str(str):
    @property
    def stable(self) -> bool: ...
    def __new__(
        cls,
        cpv: str,
        metadata: dict[str, Incomplete] | None = None,
        settings: config | None = None,
        eapi: str | None = None,
        repo: str | None = None,
        slot: str | None = None,
        build_time: int | None = None,
        build_id: str | None = None,
        file_size: int | None = None,
        mtime: int | None = None,
        db=...,
        repoconfig=...,
    ) -> Self: ...
    def __init__(
        self,
        cpv: str,
        metadata: dict[str, Incomplete] | None = None,
        settings: config | None = None,
        eapi: str | None = None,
        repo: str | None = None,
        slot: str | None = None,
        build_time: int | None = None,
        build_id: str | None = None,
        file_size: int | None = None,
        mtime: int | None = None,
        db=...,
        repoconfig=...,
    ) -> None: ...
    @staticmethod
    def _long(var, default: int) -> int: ...

def catpkgsplit(
    mydata: str | _pkg_str, silent: Literal[0, 1] = 1, eapi: str | None = None
) -> tuple[str | None, str, str, str] | None: ...
def __getattr__(name: str) -> Incomplete: ...  # incomplete module
