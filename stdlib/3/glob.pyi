# Stubs for glob
# Based on http://docs.python.org/3/library/glob.html

import sys
from typing import AnyStr, Iterator, List, Union

if sys.version_info >= (3, 6):
    def glob0(dirname: AnyStr, pattern: AnyStr) -> List[AnyStr]: ...

else:
    def glob0(dirname: AnyStr, basename: AnyStr) -> List[AnyStr]: ...

def glob1(dirname: AnyStr, pattern: AnyStr) -> List[AnyStr]: ...

if sys.version_info >= (3, 5):
    def glob(pathname: AnyStr, *, recursive: bool = ...) -> List[AnyStr]: ...
    def iglob(pathname: AnyStr, *, recursive: bool = ...) -> Iterator[AnyStr]: ...

else:
    def glob(pathname: AnyStr) -> List[AnyStr]: ...
    def iglob(pathname: AnyStr) -> Iterator[AnyStr]: ...

def escape(pathname: AnyStr) -> AnyStr: ...
def has_magic(s: Union[str, bytes]) -> bool: ...  # undocumented
