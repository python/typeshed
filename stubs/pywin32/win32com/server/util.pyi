from _typeshed import Incomplete

import _win32typing
from win32com.server import policy as policy
from win32com.server.exception import COMException as COMException

def wrap(ob, iid: Incomplete | None = ..., usePolicy: Incomplete | None = ..., useDispatcher: Incomplete | None = ...): ...
def unwrap(ob): ...

class ListEnumerator:
    index: Incomplete
    def __init__(self, data, index: int = ..., iid=...) -> None: ...
    def Next(self, count): ...
    def Skip(self, count) -> None: ...
    def Reset(self) -> None: ...
    def Clone(self): ...

class ListEnumeratorGateway(ListEnumerator):
    def Next(self, count): ...

def NewEnum(seq, cls=..., iid=..., usePolicy: Incomplete | None = ..., useDispatcher: Incomplete | None = ...): ...

class Collection:
    data: Incomplete
    def __init__(self, data: Incomplete | None = ..., readOnly: int = ...) -> None: ...
    def Item(self, *args): ...
    def Count(self): ...
    def Add(self, value) -> None: ...
    def Remove(self, index) -> None: ...
    def Insert(self, index, value) -> None: ...

def NewCollection(seq, cls=...): ...

class FileStream:
    file: Incomplete
    def __init__(self, file: _win32typing.Pymmapfile) -> None: ...
    def Read(self, amount): ...
    def Write(self, data): ...
    def Clone(self): ...
    def CopyTo(self, dest, cb): ...
    def Seek(self, offset: int, origin: int) -> int: ...
