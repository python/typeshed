from .commands import SearchCommands as SearchCommands
from typing import Any

class Search(SearchCommands):
    class BatchIndexer:
        client: Any
        execute_command: Any
        pipeline: Any
        total: int
        chunk_size: Any
        current_chunk: int
        def __init__(self, client, chunk_size: int = ...) -> None: ...
        def __del__(self) -> None: ...
        def add_document(self, doc_id, nosave: bool = ..., score: float = ..., payload: Any | None = ..., replace: bool = ..., partial: bool = ..., no_create: bool = ..., **fields) -> None: ...
        def add_document_hash(self, doc_id, score: float = ..., replace: bool = ...) -> None: ...
        def commit(self) -> None: ...
    client: Any
    index_name: Any
    execute_command: Any
    pipeline: Any
    def __init__(self, client, index_name: str = ...) -> None: ...
