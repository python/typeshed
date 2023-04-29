from _typeshed import Incomplete
from typing_extensions import Self

from ...engine.result import FilterResult

class AsyncCommon(FilterResult):
    async def close(self) -> None: ...

class AsyncResult(AsyncCommon):
    def __init__(self, real_result) -> None: ...
    def keys(self): ...
    def unique(self, strategy: Incomplete | None = None) -> Self: ...
    def columns(self, *col_expressions): ...
    async def partitions(self, size: Incomplete | None = None) -> None: ...
    async def fetchone(self): ...
    async def fetchmany(self, size: Incomplete | None = None): ...
    async def all(self): ...
    def __aiter__(self): ...
    async def __anext__(self): ...
    async def first(self): ...
    async def one_or_none(self): ...
    async def scalar_one(self): ...
    async def scalar_one_or_none(self): ...
    async def one(self): ...
    async def scalar(self): ...
    async def freeze(self): ...
    def scalars(self, index: int = 0): ...
    def mappings(self): ...

class AsyncScalarResult(AsyncCommon):
    def __init__(self, real_result, index) -> None: ...
    def unique(self, strategy: Incomplete | None = None): ...
    async def partitions(self, size: Incomplete | None = None) -> None: ...
    async def fetchall(self): ...
    async def fetchmany(self, size: Incomplete | None = None): ...
    async def all(self): ...
    def __aiter__(self): ...
    async def __anext__(self): ...
    async def first(self): ...
    async def one_or_none(self): ...
    async def one(self): ...

class AsyncMappingResult(AsyncCommon):
    def __init__(self, result) -> None: ...
    def keys(self): ...
    def unique(self, strategy: Incomplete | None = None): ...
    def columns(self, *col_expressions): ...
    async def partitions(self, size: Incomplete | None = None) -> None: ...
    async def fetchall(self): ...
    async def fetchone(self): ...
    async def fetchmany(self, size: Incomplete | None = None): ...
    async def all(self): ...
    def __aiter__(self): ...
    async def __anext__(self): ...
    async def first(self): ...
    async def one_or_none(self): ...
    async def one(self): ...
