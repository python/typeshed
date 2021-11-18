import redis
from ..helpers import nativestr as nativestr
from .commands import JSONCommands as JSONCommands
from .decoders import bulk_of_jsons as bulk_of_jsons, decode_list as decode_list
from typing import Any

class JSON(JSONCommands):
    MODULE_CALLBACKS: Any
    client: Any
    execute_command: Any
    MODULE_VERSION: Any
    __encoder__: Any
    __decoder__: Any
    def __init__(self, client, version: Any | None = ..., decoder=..., encoder=...): ...
    def pipeline(self, transaction: bool = ..., shard_hint: Any | None = ...): ...

class Pipeline(JSONCommands, redis.client.Pipeline): ...
