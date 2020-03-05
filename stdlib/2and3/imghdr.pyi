from typing import overload, Union, Text, IO, Optional, Any, List, Callable
import sys
import os


if sys.version_info >= (3, 6):
    _File = Union[Text, os.PathLike[Text], IO[bytes]]
else:
    _File = Union[Text, IO[bytes]]


@overload
def what(file: _File) -> Optional[str]: ...
@overload
def what(file: Any, h: bytes) -> Optional[str]: ...
tests: List[Callable[[bytes, IO[bytes]], Optional[str]]]
