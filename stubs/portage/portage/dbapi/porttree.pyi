from _typeshed import Incomplete
from collections.abc import Sequence
from typing import Literal

from portage.dbapi import dbapi

class portdbapi(dbapi):
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

class portagetree:
    dbapi: portdbapi

def __getattr__(name: str) -> Incomplete: ...  # incomplete module
