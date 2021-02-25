from typing import Any, ContextManager, Optional, Text, overload
from typing_extensions import Literal

from .client import Pipeline, Redis

HIREDIS_AVAILABLE: bool
@overload
def from_url(url: Text, db: Optional[int] = ..., *, decode_responses: Literal[True], **kwargs: Any) -> Redis[str]: ...
@overload
def from_url(url: Text, db: Optional[int] = ..., *, decode_responses: Literal[False] = ..., **kwargs: Any) -> Redis[bytes]: ...
@overload
def str_if_bytes(value: bytes) -> str: ...
@overload
def str_if_bytes(value: object) -> object: ...
def safe_str(value: object) -> str: ...
def pipeline(redis_obj: Redis) -> ContextManager[Pipeline]: ...

class dummy: ...
