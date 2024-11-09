from _typeshed import Incomplete

from ...asyncio.client import Pipeline as AsyncioPipeline
from ...client import Pipeline as SyncPipeline

from .commands import SearchCommands, AsyncSearchCommands
from ...commands.core import _StrType

class Search(SearchCommands):
    class BatchIndexer:
        def __init__(self, client, chunk_size: int = 1000) -> None: ...
        def add_document(
            self,
            doc_id,
            nosave: bool = False,
            score: float = 1.0,
            payload: Incomplete | None = None,
            replace: bool = False,
            partial: bool = False,
            no_create: bool = False,
            **fields,
        ): ...
        def add_document_hash(self, doc_id, score: float = 1.0, replace: bool = False): ...
        def commit(self): ...

    def __init__(self, client, index_name: str = "idx") -> None: ...

class Pipeline(SearchCommands, SyncPipeline[_StrType]): ...

class AsyncPipeline(AsyncSearchCommands, AsyncioPipeline[_StrType], Pipeline[_StrType]): ...

class AsyncSearch(Search, AsyncSearchCommands):
    class BatchIndexer(Search.BatchIndexer):
        async def add_document(
            self,
            doc_id,
            nosave: bool = False,
            score: float = 1.0,
            payload: Incomplete | None = None,
            replace: bool = False,
            partial: bool = False,
            no_create: bool = False,
            **fields,
        ): ...
        async def commit(self): ...
    def pipeline(self, transaction: bool = True, shard_hint: Incomplete | None = None): ...
