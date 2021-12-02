from typing import Any

def is_global_tracer_registered() -> bool: ...

is_tracer_registered: bool = ...

def __getattr__(name: str) -> Any: ...  # incomplete
