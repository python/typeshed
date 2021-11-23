from typing import Any

from .commands import JSONCommands
from ...client import Pipeline as ClientPipeline

class JSON(JSONCommands):
    MODULE_CALLBACKS: dict[str, Any]
    client: Any
    execute_command: Any
    MODULE_VERSION: Any | None
    def __init__(
        self,
        client,
        version: Any | None=...,
        decoder=...,
        encoder=...
    ) -> None: ...
    def pipeline(self, transaction: bool = ..., shard_hint: Any | None = ...) -> Pipeline: ...

class Pipeline(JSONCommands, ClientPipeline): ...  # type: ignore
