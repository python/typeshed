from typing import Any, Tuple
from waitress.server import create_server

def serve(app: Any, **kw: Any) -> None: ...
def serve_paste(app: Any, global_conf: None, **kw: str) -> int: ...
def profile(cmd: Any, globals: Any, locals: Any, sort_order: Tuple[str, ...], callers: bool) -> None: ...
