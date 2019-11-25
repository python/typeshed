# Stubs for warnings

import sys
from typing import Any, Dict, List, NamedTuple, Optional, overload, TextIO, Tuple, Type, Union
from types import ModuleType, TracebackType

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

@overload
def warn(message: str, category: Optional[Type[Warning]] = ..., stacklevel: int = ...) -> None: ...
@overload
def warn(message: Warning, category: Any = ..., stacklevel: int = ...) -> None: ...
@overload
def warn_explicit(message: str, category: Type[Warning],
                  filename: str, lineno: int, module: Optional[str] = ...,
                  registry: Optional[Dict[Union[str, Tuple[str, Type[Warning], int]], int]] = ...,
                  module_globals: Optional[Dict[str, Any]] = ...) -> None: ...
@overload
def warn_explicit(message: Warning, category: Any,
                  filename: str, lineno: int, module: Optional[str] = ...,
                  registry: Optional[Dict[Union[str, Tuple[str, Type[Warning], int]], int]] = ...,
                  module_globals: Optional[Dict[str, Any]] = ...) -> None: ...
def showwarning(message: str, category: Type[Warning], filename: str,
                lineno: int, file: Optional[TextIO] = ...,
                line: Optional[str] = ...) -> None: ...
def formatwarning(message: str, category: Type[Warning], filename: str,
                  lineno: int, line: Optional[str] = ...) -> str: ...
def filterwarnings(action: str, message: str = ...,
                   category: Type[Warning] = ..., module: str = ...,
                   lineno: int = ..., append: bool = ...) -> None: ...
def simplefilter(action: str, category: Type[Warning] = ..., lineno: int = ...,
                 append: bool = ...) -> None: ...
def resetwarnings() -> None: ...

class _Record(NamedTuple):
    message: str
    category: Type[Warning]
    filename: str
    lineno: int
    file: Optional[TextIO]
    line: Optional[str]

class catch_warnings:
    @overload
    def __new__(cls, *, record: Literal[False] = ..., module: Optional[ModuleType] = ...) -> _catch_warnings_without_records: ...
    @overload
    def __new__(cls, *, record: Literal[True], module: Optional[ModuleType] = ...) -> _catch_warnings_with_records: ...
    @overload
    def __new__(cls, *, record: bool, module: Optional[ModuleType] = ...) -> catch_warnings: ...
    def __enter__(self) -> Optional[List[_Record]]: ...
    def __exit__(self, exc_type: Optional[Type[BaseException]],
                 exc_val: Optional[BaseException],
                 exc_tb: Optional[TracebackType]) -> None: ...

class _catch_warnings_without_records(catch_warnings):
    def __enter__(self) -> None: ...

class _catch_warnings_with_records(catch_warnings):
    def __enter__(self) -> List[_Record]: ...
