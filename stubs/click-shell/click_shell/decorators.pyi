from typing import Any, Callable

from .core import Shell

def shell(name: str | None = None, **attrs: Any) -> Callable[[Any], Shell]: ...
