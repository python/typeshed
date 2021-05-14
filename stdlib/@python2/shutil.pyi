import os
import sys
from _typeshed import StrPath, SupportsRead, SupportsWrite
from typing import (
    Any,
    AnyStr,
    Callable,
    Iterable,
    List,
    NamedTuple,
    Optional,
    Sequence,
    Set,
    Tuple,
    Type,
    TypeVar,
    Union,
    overload,
)

elif sys.version_info >= (3,):
    _AnyStr = str
    _AnyPath = str
    _PathReturn = str
else:
    _AnyStr = TypeVar("_AnyStr", str, unicode)
    _AnyPath = TypeVar("_AnyPath", str, unicode)
    _PathReturn = Type[None]

class Error(EnvironmentError): ...
class SpecialFileError(EnvironmentError): ...
class ExecError(EnvironmentError): ...

def copyfileobj(fsrc: SupportsRead[AnyStr], fdst: SupportsWrite[AnyStr], length: int = ...) -> None: ...

def copyfile(src: StrPath, dst: StrPath) -> None: ...
def copymode(src: StrPath, dst: StrPath) -> None: ...
def copystat(src: StrPath, dst: StrPath) -> None: ...
def copy(src: StrPath, dst: StrPath) -> _PathReturn: ...
def copy2(src: StrPath, dst: StrPath) -> _PathReturn: ...

def ignore_patterns(*patterns: StrPath) -> Callable[[Any, List[_AnyStr]], Set[_AnyStr]]: ...

elif sys.version_info >= (3,):
    def copytree(
        src: StrPath,
        dst: StrPath,
        symlinks: bool = ...,
        ignore: Union[None, Callable[[str, List[str]], Iterable[str]], Callable[[StrPath, List[str]], Iterable[str]]] = ...,
        copy_function: Callable[[str, str], None] = ...,
        ignore_dangling_symlinks: bool = ...,
    ) -> _PathReturn: ...

else:
    def copytree(
        src: AnyStr,
        dst: AnyStr,
        symlinks: bool = ...,
        ignore: Union[None, Callable[[AnyStr, List[AnyStr]], Iterable[AnyStr]]] = ...,
    ) -> _PathReturn: ...

def rmtree(
    path: _AnyPath, ignore_errors: bool = ..., onerror: Optional[Callable[[Any, _AnyPath, Any], Any]] = ...
) -> None: ...

_CopyFn = Union[Callable[[str, str], None], Callable[[StrPath, StrPath], None]]

elif sys.version_info >= (3, 5):
    # See https://bugs.python.org/issue32689
    def move(src: str, dst: StrPath, copy_function: _CopyFn = ...) -> _PathReturn: ...

else:
    def move(src: StrPath, dst: StrPath) -> _PathReturn: ...

elif sys.version_info >= (3,):
    def which(cmd: StrPath, mode: int = ..., path: Optional[StrPath] = ...) -> Optional[str]: ...

def make_archive(
    base_name: _AnyStr,
    format: str,
    root_dir: Optional[StrPath] = ...,
    base_dir: Optional[StrPath] = ...,
    verbose: bool = ...,
    dry_run: bool = ...,
    owner: Optional[str] = ...,
    group: Optional[str] = ...,
    logger: Optional[Any] = ...,
) -> _AnyStr: ...
def get_archive_formats() -> List[Tuple[str, str]]: ...
def register_archive_format(
    name: str,
    function: Callable[..., Any],
    extra_args: Optional[Sequence[Union[Tuple[str, Any], List[Any]]]] = ...,
    description: str = ...,
) -> None: ...
def unregister_archive_format(name: str) -> None: ...

