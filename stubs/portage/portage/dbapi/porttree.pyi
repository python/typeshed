from collections.abc import Sequence
from typing import Literal

from portage.dbapi import dbapi

class portdbapi(dbapi):
    def getFetchMap(
        self, mypkg: str, useflags: Sequence[str] | None = ..., mytree: str | None = ...
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
    def findname(self, mycpv: str, mytree: str | None = ..., myrepo: str | None = ...) -> str: ...
    def findname2(
        self, mycpv: str, mytree: str | None = ..., myrepo: str | None = ...
    ) -> tuple[None, Literal[0]] | tuple[str, str] | tuple[str, None]: ...

class portagetree:
    dbapi: portdbapi
