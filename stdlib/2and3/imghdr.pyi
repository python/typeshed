import os
import sys
from typing import IO, Any, BinaryIO, Callable, List, Optional, Text, Union, overload

if sys.version_info >= (3, 6):
    _File = Union[Text, os.PathLike[Text], IO[bytes]]
else:
    _File = Union[Text, IO[bytes]]


@overload
def what(file: _File) -> Optional[str]: ...
@overload
def what(file: Any, h: bytes) -> Optional[str]: ...
tests: List[Callable[[bytes, Optional[BinaryIO]], Optional[str]]]
