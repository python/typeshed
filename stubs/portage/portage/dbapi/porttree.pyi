from collections.abc import Sequence

from portage.dbapi import dbapi

class portdbapi(dbapi):
    def getFetchMap(
        self, mypkg: str, useflags: Sequence[str] | None = ..., mytree: str | None = ...
    ) -> dict[str, tuple[str, ...]]: ...

class portagetree:
    dbapi: portdbapi
