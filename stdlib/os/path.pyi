import os
import sys
from _typeshed import AnyPath, BytesPath, StrPath
from os import PathLike
from typing import AnyStr, List, Optional, Sequence, Tuple, Union, overload
from typing_extensions import Literal

# ----- os.path variables -----

if sys.platform == "win32":
    if sys.version_info >= (3, 10):
        @overload
        def realpath(path: PathLike[AnyStr], *, strict: bool = ...) -> AnyStr: ...
        @overload
        def realpath(path: AnyStr, *, strict: bool = ...) -> AnyStr: ...
    else:
        @overload
        def realpath(path: PathLike[AnyStr]) -> AnyStr: ...
        @overload
        def realpath(path: AnyStr) -> AnyStr: ...

if sys.version_info < (3, 7) and sys.platform == "win32":
    def splitunc(p: AnyStr) -> Tuple[AnyStr, AnyStr]: ...  # deprecated
