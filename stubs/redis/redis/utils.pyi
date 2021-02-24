from typing import Any, ContextManager, Optional, Text, overload
from typing_extensions import Literal

from . import Redis
from .client import Pipeline

HIREDIS_AVAILABLE: Any
@overload
def from_url(url: Text, db: Optional[int] = ..., *, decode_responses: Literal[True], **kwargs) -> Redis[str]: ...
@overload
def from_url(url: Text, db: Optional[int] = ..., *, decode_responses: Literal[False] = ..., **kwargs) -> Redis[bytes]: ...
def pipeline(redis_obj: Redis) -> ContextManager[Pipeline]: ...

class dummy: ...
