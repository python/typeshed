from typing import Any, Optional, Text, Union

greenlet = ...  # type: Any

class IterIO:
    def __new__(cls, obj, sentinel: Union[Text, bytes] = ...): ...
    def __iter__(self): ...
    def tell(self): ...
    def isatty(self): ...
    def seek(self, pos, mode: int = ...): ...
    def truncate(self, size: Optional[Any] = ...): ...
    def write(self, s): ...
    def writelines(self, list): ...
    def read(self, n: int = ...): ...
    def readlines(self, sizehint: int = ...): ...
    def readline(self, length: Optional[Any] = ...): ...
    def flush(self): ...
    def __next__(self): ...

class IterI(IterIO):
    sentinel: Any
    def __new__(cls, func, sentinel: Union[Text, bytes] = ...): ...
    closed = ...  # type: Any
    def close(self): ...
    def write(self, s): ...
    def writelines(self, list): ...
    def flush(self): ...

class IterO(IterIO):
    sentinel: Any
    closed = ...  # type: Any
    pos = ...  # type: Any
    def __new__(cls, gen, sentinel: Union[Text, bytes] = ...): ...
    def __iter__(self): ...
    def close(self): ...
    def seek(self, pos, mode: int = ...): ...
    def read(self, n: int = ...): ...
    def readline(self, length: Optional[Any] = ...): ...
    def readlines(self, sizehint: int = ...): ...
