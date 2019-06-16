from typing import Any, Optional

available: Any

class MergeStream:
    streams: Any
    def __init__(self, *streams): ...
    def write(self, data): ...

class ProfilerMiddleware:
    def __init__(self, app, stream: Optional[Any] = ..., sort_by=..., restrictions=..., profile_dir: Optional[Any] = ...): ...
    def __call__(self, environ, start_response): ...

def make_action(
    app_factory,
    hostname: str = ...,
    port: int = ...,
    threaded: bool = ...,
    processes: int = ...,
    stream: Optional[Any] = ...,
    sort_by=...,
    restrictions=...,
): ...
