# Stubs for py_compile (Python 2 and 3)
import sys

from typing import Optional, List

class PyCompileError(Exception):
    exc_type_name = ...  # type: str
    exc_value = ...  # type: BaseException
    file = ...  # type: str
    msg = ...  # type: str
    def __init__(self, exc_type: str, exc_value: BaseException, file: str, msg: str = ...) -> None: ...

if sys.version_info >= (3, 2):
    def compile(file: str, cfile: Optional[str] = ..., dfile: Optional[str] = ..., doraise: bool = ..., optimize: int = ...) -> None: ...
else:
    def compile(file: str, cfile: Optional[str] = ..., dfile: Optional[str] = ..., doraise: bool = ...) -> None: ...

def main(args: Optional[List[str]] = ...): ...
