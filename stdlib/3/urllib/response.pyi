# private module, we only expose what's needed

from io import BufferedRandom
from typing import Mapping, Optional
from types import TracebackType

class addinfourl(BufferedRandom):
    headers = ...  # type: Mapping[str, str]
    url = ...  # type: str
    code = ...  # type: int
    def info(self) -> Mapping[str, str]: ...
    def geturl(self) -> str: ...
