from cProfile import Profile as Profile, run as run, runctx as runctx
from types import CodeType
from typing_extensions import TypeAlias

__all__ = ["run", "runctx", "Profile"]

_Label: TypeAlias = tuple[str, int, str]

def label(code: str | CodeType) -> _Label: ...  # undocumented
