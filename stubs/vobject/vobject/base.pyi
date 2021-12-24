from collections.abc import Iterator
from _typeshed import SupportsWrite
from collections.abc import Iterable
from typing import Any, TypeVar, overload
from typing_extensions import Literal

DEBUG: bool
CR: str
LF: str
CRLF: str
SPACE: str
TAB: str
SPACEORTAB: str

_V = TypeVar("_V", bound=VBase)
_W = TypeVar("_W", bound=SupportsWrite[bytes])

class VBase:
    group: Any | None
    behavior: Any | None
    parentBehavior: Any | None
    isNative: bool
    def __init__(self, group: Any | None = ...) -> None: ...
    def copy(self, copyit: VBase) -> None: ...
    def validate(self, *args, **kwds) -> bool: ...
    def getChildren(self) -> list[Any]: ...
    def clearBehavior(self, cascade: bool = ...) -> None: ...
    def autoBehavior(self, cascade: bool = ...) -> None: ...
    def setBehavior(self, behavior, cascade: bool = ...) -> None: ...
    def transformToNative(self): ...
    def transformFromNative(self): ...
    def transformChildrenToNative(self) -> None: ...
    def transformChildrenFromNative(self, clearBehavior: bool = ...) -> None: ...
    @overload
    def serialize(self, buf: None = ..., lineLength: int = ..., validate: bool = ..., behavior: Any | None = ...) -> str: ...
    @overload
    def serialize(self, buf: _W, lineLength: int = ..., validate: bool = ..., behavior: Any | None = ...) -> _W: ...

def toVName(name, stripNum: int = ..., upper: bool = ...): ...

class ContentLine(VBase):
    name: Any
    encoded: Any
    params: Any
    singletonparams: Any
    isNative: Any
    lineNumber: Any
    value: Any
    def __init__(
        self,
        name,
        params,
        value,
        group: Any | None = ...,
        encoded: bool = ...,
        isNative: bool = ...,
        lineNumber: Any | None = ...,
        *args,
        **kwds,
    ) -> None: ...
    @classmethod
    def duplicate(cls, copyit): ...
    def copy(self, copyit) -> None: ...
    def __eq__(self, other): ...
    def __getattr__(self, name): ...
    def __setattr__(self, name, value) -> None: ...
    def __delattr__(self, name) -> None: ...
    def valueRepr(self): ...
    def __unicode__(self): ...
    def prettyPrint(self, level: int = ..., tabwidth: int = ...) -> None: ...

class Component(VBase):
    contents: dict[str, list[VBase]]
    name: Any
    useBegin: bool
    def __init__(self, name: Any | None = ..., *args, **kwds) -> None: ...
    @classmethod
    def duplicate(cls, copyit): ...
    def copy(self, copyit) -> None: ...
    def setProfile(self, name) -> None: ...
    def __getattr__(self, name): ...
    normal_attributes: Any
    def __setattr__(self, name, value) -> None: ...
    def __delattr__(self, name) -> None: ...
    def getChildValue(self, childName, default: Any | None = ..., childNumber: int = ...): ...
    @overload
    def add(self, objOrName: _V, group: str | None = ...) -> _V: ...
    @overload
    def add(self, objOrName: Literal["vevent"], group: str | None = ...) -> Component: ...
    @overload
    def add(
        self, objOrName: Literal["uid", "summary", "description", "dtstart", "dtend"], group: str | None = ...
    ) -> ContentLine: ...
    @overload
    def add(self, objOrName: str, group: str | None = ...) -> Any: ...  # returns VBase sub-class
    def remove(self, obj) -> None: ...
    def getChildren(self) -> list[Any]: ...
    def components(self) -> Iterable[Component]: ...
    def lines(self): ...
    def sortChildKeys(self): ...
    def getSortedChildren(self): ...
    def setBehaviorFromVersionLine(self, versionLine) -> None: ...
    def transformChildrenToNative(self) -> None: ...
    def transformChildrenFromNative(self, clearBehavior: bool = ...) -> None: ...
    def prettyPrint(self, level: int = ..., tabwidth: int = ...) -> None: ...

class VObjectError(Exception):
    msg: Any
    lineNumber: Any
    def __init__(self, msg, lineNumber: Any | None = ...) -> None: ...

class ParseError(VObjectError): ...
class ValidateError(VObjectError): ...
class NativeError(VObjectError): ...

patterns: Any
param_values_re: Any
params_re: Any
line_re: Any
begin_re: Any

def parseParams(string): ...
def parseLine(line, lineNumber: Any | None = ...): ...

wrap_re: Any
logical_lines_re: Any
testLines: str

def getLogicalLines(fp, allowQP: bool = ...) -> None: ...
def textLineToContentLine(text, n: Any | None = ...): ...
def dquoteEscape(param): ...
def foldOneLine(outbuf, input, lineLength: int = ...) -> None: ...
def defaultSerialize(obj, buf, lineLength): ...

class Stack:
    stack: Any
    def __init__(self) -> None: ...
    def __len__(self): ...
    def top(self): ...
    def topName(self): ...
    def modifyTop(self, item) -> None: ...
    def push(self, obj) -> None: ...
    def pop(self): ...

def readComponents(
    streamOrString, validate: bool = ..., transform: bool = ..., ignoreUnreadable: bool = ..., allowQP: bool = ...
) -> Iterator[Component]: ...
def readOne(stream, validate: bool = ..., transform: bool = ..., ignoreUnreadable: bool = ..., allowQP: bool = ...): ...
def registerBehavior(behavior, name: Any | None = ..., default: bool = ..., id: Any | None = ...) -> None: ...
def getBehavior(name, id: Any | None = ...): ...
def newFromBehavior(name, id: Any | None = ...): ...
def backslashEscape(s): ...
