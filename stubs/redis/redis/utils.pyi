from typing import Any, ContextManager

from . import Redis
from .client import Pipeline

HIREDIS_AVAILABLE: Any

def from_url(url, db=..., **kwargs): ...
def pipeline(redis_obj: Redis) -> ContextManager[Pipeline]: ...

class dummy: ...
