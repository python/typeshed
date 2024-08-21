import abc
import collections.abc
import io
from _typeshed import Incomplete
from abc import abstractmethod
from typing import Any

from ordereddict import OrderedDict
from ruamel.yaml.docinfo import Version

SupportsIndex = int
StreamType = Any
StreamTextType = StreamType
VersionType = str | tuple[int, int] | list[int] | Version | None

class ordereddict(OrderedDict):
    def insert(self, pos: int, key, value) -> None: ...

StringIO = io.StringIO
BytesIO = io.BytesIO
builtins_module: str

def with_metaclass(meta, *bases): ...

DBG_TOKEN: int
DBG_EVENT: int
DBG_NODE: int

class ObjectCounter:
    map: Incomplete
    def __init__(self) -> None: ...
    def __call__(self, k) -> None: ...
    def dump(self) -> None: ...

object_counter: Incomplete

def dbg(val: Incomplete | None = None): ...

class Nprint:
    def __init__(self, file_name: Incomplete | None = None) -> None: ...
    def __call__(self, *args, **kw) -> None: ...
    def set_max_print(self, i: int) -> None: ...
    def fp(self, mode: str = "a"): ...

nprint: Incomplete
nprintf: Incomplete

def check_namespace_char(ch) -> bool: ...
def check_anchorname_char(ch) -> bool: ...
def version_tnf(t1, t2: Incomplete | None = None): ...

class MutableSliceableSequence(collections.abc.MutableSequence, metaclass=abc.ABCMeta):
    def __getitem__(self, index): ...
    def __setitem__(self, index, value) -> None: ...
    def __delitem__(self, index) -> None: ...
    @abstractmethod
    def __getsingleitem__(self, index): ...
    @abstractmethod
    def __setsingleitem__(self, index, value) -> None: ...
    @abstractmethod
    def __delsingleitem__(self, index) -> None: ...
