from _typeshed import Incomplete
from typing_extensions import deprecated

class BaseQuery:
    counters: Incomplete
    paths: Incomplete
    active: int
    curpaths: Incomplete
    def __init__(self, paths: Incomplete | None = ...) -> None: ...
    def addcounterbybrowsing(self, flags=..., windowtitle: str = ...) -> None: ...
    def rawaddcounter(
        self, object, counter, instance: Incomplete | None = ..., inum: int = ..., machine: Incomplete | None = ...
    ) -> None: ...
    def addcounter(
        self, object, counter, instance: Incomplete | None = ..., inum: int = ..., machine: Incomplete | None = ...
    ): ...
    def open(self): ...
    def killbase(self, base: Incomplete | None = ...) -> None: ...
    def close(self) -> None: ...
    __del__: Incomplete
    def collectdata(self, format=...): ...
    def collectdataslave(self, format=...): ...
    def __getinitargs__(self): ...

class Query(BaseQuery):
    volatilecounters: Incomplete
    def __init__(self, *args, **namedargs) -> None: ...
    @deprecated("Use of addcounterbybrowsing instead as its considerably more flexible and general.")
    def addperfcounter(self, object, counter, machine=None): ...
    def addinstcounter(
        self, object, counter, machine: Incomplete | None = ..., objtype: str = ..., volatile: int = ..., format=...
    ) -> None: ...
    def getinstpaths(self, object, counter, machine: Incomplete | None = ..., objtype: str = ..., format=...): ...
    def open(self, *args, **namedargs) -> None: ...
    curresults: Incomplete
    def collectdatafor(self, totalperiod, period: int = ...) -> None: ...
    collectdatawhile_active: int
    def collectdatawhile(self, period: int = ...) -> None: ...
    def collectdatawhile_stop(self) -> None: ...
    def collectdatawhile_slave(self, period) -> None: ...
    def __getinitargs__(self): ...

class QueryError(Exception):
    query: Incomplete
    def __init__(self, query) -> None: ...
