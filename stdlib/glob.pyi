import sys
from _typeshed import StrOrBytesPath
from typing import AnyStr, Iterator, List, Optional, Union

def glob0(dirname: AnyStr, pattern: AnyStr) -> List[AnyStr]: ...
def glob1(dirname: AnyStr, pattern: AnyStr) -> List[AnyStr]: ...

if sys.version_info >= (3, 10):
    def glob(
        pathname: AnyStr, *, root_dir: StrOrBytesPath | None = ..., dir_fd: int | None = ..., recursive: bool = ...
    ) -> List[AnyStr]: ...
    def iglob(
        pathname: AnyStr, *, root_dir: StrOrBytesPath | None = ..., dir_fd: int | None = ..., recursive: bool = ...
    ) -> Iterator[AnyStr]: ...

else:
    def glob(pathname: AnyStr, *, recursive: bool = ...) -> List[AnyStr]: ...
    def iglob(pathname: AnyStr, *, recursive: bool = ...) -> Iterator[AnyStr]: ...

def escape(pathname: AnyStr) -> AnyStr: ...
def has_magic(s: str | bytes) -> bool: ...  # undocumented
