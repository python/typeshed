from _typeshed import Incomplete
from collections.abc import Sequence
from typing import Literal

from portage.dbapi import _MyListString, dbapi
from portage.repository.config import RepoConfigLoader

class portdbapi(dbapi):
    repositories: RepoConfigLoader
    def getFetchMap(
        self, mypkg: str, useflags: Sequence[str] | None = None, mytree: str | None = None
    ) -> dict[str, tuple[str, ...]]: ...
    def xmatch(
        self,
        level: Literal[
            "bestmatch-visible",
            "match-all-cpv-only",
            "match-all",
            "match-visible",
            "minimum-all",
            "minimum-visible",
            "minimum-all-ignore-profile",
        ],
        origdep: str,
    ) -> list[str] | str: ...
    def findname(self, mycpv: str, mytree: str | None = None, myrepo: str | None = None) -> str: ...
    def findname2(
        self, mycpv: str, mytree: str | None = None, myrepo: str | None = None
    ) -> tuple[None, Literal[0]] | tuple[str, str] | tuple[str, None]: ...
    # This method overrides in an incompatible way
    def aux_get(  # type: ignore[override]
        self, mycpv: str, mylist: Sequence[_MyListString], mytree: str | None = None, myrepo: str | None = None
    ) -> list[str]: ...
    def match(self, mydep: str, use_cache: Literal[0, 1] = 1) -> list[str] | str: ...

class portagetree:
    dbapi: portdbapi

def __getattr__(name: str) -> Incomplete: ...  # incomplete module
