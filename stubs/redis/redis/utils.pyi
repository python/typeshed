from typing import Any, ContextManager, Optional, Text, overload
from typing_extensions import Literal

from . import Redis
from .client import Pipeline

HIREDIS_AVAILABLE: Any
@overload
def from_url(url: Text, db: Optional[int] = ..., *, decode_responses: Literal[True], **kwargs) -> Redis[str]: ...
@overload
def from_url(url: Text, db: Optional[int] = ..., *, decode_responses: Literal[False] = ..., **kwargs) -> Redis[bytes]: ...
@overload
def str_if_bytes(value: bytes) -> str: ...
@overload
def str_if_bytes(value: object) -> object: ...
@overload
def safe_str(value: bytes) -> str: ...
@overload
def safe_str(value: object) -> str: ...
def pipeline(redis_obj: Redis) -> ContextManager[Pipeline]: ...

class dummy: ...
