from typing import Any, Iterable, List, Optional, Union, Tuple, TypeVar

_T = TypeVar('_T')

__all__ = ...  # type: List[str]

class Popen3:
    sts = ...  # type: int
    cmd = ...  # type: Iterable
    pid = ...  # type: int
    tochild = ...  # type: file
    fromchild = ...  # type: file
    childerr = ...  # type: Optional[file]
    def __init__(self, cmd: Iterable = ..., capturestderr: bool = ..., bufsize: int = ...) -> None: ...
    def __del__(self) -> None: ...
    def poll(self, _deadstate: _T = ...) -> Union[int, _T]: ...
    def wait(self) -> int: ...

class Popen4(Popen3):
    childerr = ...  # type: Optional[file]
    cmd = ...  # type: Iterable
    pid = ...  # type: int
    tochild = ...  # type: file
    fromchild = ...  # type: file
    def __init__(self, cmd: Iterable = ..., bufsize: int = ...) -> None: ...

def popen2(cmd: Iterable = ..., bufsize: int = ..., mode: str = ...) -> Tuple[file, file]: ...
def popen3(cmd: Iterable = ..., bufsize: int = ..., mode: str = ...) -> Tuple[file, file, file]: ...
def popen4(cmd: Iterable = ..., bufsize: int = ..., mode: str = ...) -> Tuple[file, file]: ...
