# Stubs for pickle

# NOTE: These are incomplete!

from typing import Any, IO

def dumps(obj: Any, protocol: int = ..., *,
          fix_imports: bool = ...) -> bytes: ...
def loads(p: bytes, *, fix_imports: bool = ...,
          encoding: str = ..., errors: str = ...) -> Any: ...
def load(file: IO[bytes], *, fix_imports: bool = ..., encoding: str = ...,
         errors: str = ...) -> Any: ...
