from typing import Any

available = ...  # type: Any

class MergeStream:
    streams = ...  # type: Any
    def __init__(self, *streams): ...
    def write(self, data): ...

class ProfilerMiddleware:
    def __init__(self, app, stream=None, sort_by=..., restrictions=..., profile_dir=None): ...
    def __call__(self, environ, start_response): ...

def make_action(app_factory, hostname='', port=5000, threaded=False, processes=1, stream=None, sort_by=..., restrictions=...): ...
