# private module, we only expose what's needed

from typing import _ConcreteBinaryIO, Mapping, Optional
from types import TracebackType

class addinfourl(_ConcreteBinaryIO):
    headers = ...  # type: Mapping[str, str]
    url = ...  # type: str
    code = ...  # type: int
    def info(self) -> Mapping[str, str]: ...
    def geturl(self) -> str: ...
