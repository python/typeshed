from _typeshed import SupportsWrite
from abc import abstractmethod
from reprlib import Repr
from types import MethodType, ModuleType, TracebackType
from typing import IO, Any, AnyStr, Callable, Container, Mapping, MutableMapping, NoReturn, TypeVar

__all__ = ["help"]

# the return type of sys.exc_info(), used by ErrorDuringImport.__init__
_Exc_Info = tuple[type[BaseException] | None, BaseException | None, TracebackType | None]

_T = TypeVar("_T")

__author__: str
__date__: str
__version__: str
__credits__: str

def pathdirs() -> list[str]: ...
def getdoc(object: object) -> str: ...
def splitdoc(doc: AnyStr) -> tuple[AnyStr, AnyStr]: ...
def classname(object: object, modname: str) -> str: ...
def isdata(object: object) -> bool: ...
def replace(text: AnyStr, *pairs: AnyStr) -> AnyStr: ...
def cram(text: str, maxlen: int) -> str: ...
def stripid(text: str) -> str: ...
def allmethods(cl: type) -> MutableMapping[str, MethodType]: ...
def visiblename(name: str, all: Container[str] | None = ..., obj: object | None = ...) -> bool: ...
def classify_class_attrs(object: object) -> list[tuple[str, str, type, str]]: ...
def ispackage(path: str) -> bool: ...
def source_synopsis(file: IO[AnyStr]) -> AnyStr | None: ...
def synopsis(filename: str, cache: MutableMapping[str, tuple[int, str]] = ...) -> str | None: ...

class ErrorDuringImport(Exception):
    filename: str
    exc: type[BaseException] | None
    value: BaseException | None
    tb: TracebackType | None
    def __init__(self, filename: str, exc_info: _Exc_Info) -> None: ...

def importfile(path: str) -> ModuleType: ...
def safeimport(path: str, forceload: bool = ..., cache: MutableMapping[str, ModuleType] = ...) -> ModuleType: ...

class Doc:
    PYTHONDOCS: str
    def document(self, object: object, name: str | None = ..., *args: Any) -> str: ...
    def fail(self, object: object, name: str | None = ..., *args: Any) -> NoReturn: ...
    @abstractmethod
    def docmodule(self, object: object, name: str | None = ..., *args: Any) -> str: ...
    @abstractmethod
    def docclass(self, object: object, name: str | None = ..., *args: Any) -> str: ...
    @abstractmethod
    def docroutine(self, object: object, name: str | None = ..., *args: Any) -> str: ...
    @abstractmethod
    def docother(self, object: object, name: str | None = ..., *args: Any) -> str: ...
    @abstractmethod
    def docproperty(self, object: object, name: str | None = ..., *args: Any) -> str: ...
    @abstractmethod
    def docdata(self, object: object, name: str | None = ..., *args: Any) -> str: ...
    def getdocloc(self, object: object, basedir: str = ...) -> str | None: ...

class HTMLRepr(Repr):
    maxlist: int
    maxtuple: int
    maxdict: int
    maxstring: int
    maxother: int
    def __init__(self) -> None: ...
    def escape(self, text: str) -> str: ...
    def repr(self, object: object) -> str: ...
    def repr1(self, x: object, level: complex) -> str: ...
    def repr_string(self, x: str, level: complex) -> str: ...
    def repr_str(self, x: str, level: complex) -> str: ...
    def repr_instance(self, x: object, level: complex) -> str: ...
    def repr_unicode(self, x: AnyStr, level: complex) -> str: ...

class HTMLDoc(Doc):
    repr: Callable[[object], str]
    escape: Callable[[str], str]
    def page(self, title: str, contents: str) -> str: ...
    def heading(self, title: str, fgcol: str, bgcol: str, extras: str = ...) -> str: ...
    def section(
        self,
        title: str,
        fgcol: str,
        bgcol: str,
        contents: str,
        width: int = ...,
        prelude: str = ...,
        marginalia: str | None = ...,
        gap: str = ...,
    ) -> str: ...
    def bigsection(self, title: str, *args: Any) -> str: ...
    def preformat(self, text: str) -> str: ...
    def multicolumn(self, list: list[_T], format: Callable[[_T], str], cols: int = ...) -> str: ...
    def grey(self, text: str) -> str: ...
    def namelink(self, name: str, *dicts: MutableMapping[str, str]) -> str: ...
    def classlink(self, object: object, modname: str) -> str: ...
    def modulelink(self, object: object) -> str: ...
    def modpkglink(self, modpkginfo: tuple[str, str, bool, bool]) -> str: ...
    def markup(
        self,
        text: str,
        escape: Callable[[str], str] | None = ...,
        funcs: Mapping[str, str] = ...,
        classes: Mapping[str, str] = ...,
        methods: Mapping[str, str] = ...,
    ) -> str: ...
    def formattree(
        self, tree: list[tuple[type, tuple[type, ...]] | list[Any]], modname: str, parent: type | None = ...
    ) -> str: ...
    def docmodule(self, object: object, name: str | None = ..., mod: str | None = ..., *ignored: Any) -> str: ...
    def docclass(
        self,
        object: object,
        name: str | None = ...,
        mod: str | None = ...,
        funcs: Mapping[str, str] = ...,
        classes: Mapping[str, str] = ...,
        *ignored: Any,
    ) -> str: ...
    def formatvalue(self, object: object) -> str: ...
    def docroutine(  # type: ignore[override]
        self,
        object: object,
        name: str | None = ...,
        mod: str | None = ...,
        funcs: Mapping[str, str] = ...,
        classes: Mapping[str, str] = ...,
        methods: Mapping[str, str] = ...,
        cl: type | None = ...,
    ) -> str: ...
    def docproperty(self, object: object, name: str | None = ..., mod: str | None = ..., cl: Any | None = ...) -> str: ...  # type: ignore[override]
    def docother(self, object: object, name: str | None = ..., mod: Any | None = ..., *ignored: Any) -> str: ...
    def docdata(self, object: object, name: str | None = ..., mod: Any | None = ..., cl: Any | None = ...) -> str: ...  # type: ignore[override]
    def index(self, dir: str, shadowed: MutableMapping[str, bool] | None = ...) -> str: ...
    def filelink(self, url: str, path: str) -> str: ...

class TextRepr(Repr):
    maxlist: int
    maxtuple: int
    maxdict: int
    maxstring: int
    maxother: int
    def __init__(self) -> None: ...
    def repr1(self, x: object, level: complex) -> str: ...
    def repr_string(self, x: str, level: complex) -> str: ...
    def repr_str(self, x: str, level: complex) -> str: ...
    def repr_instance(self, x: object, level: complex) -> str: ...

class TextDoc(Doc):
    repr: Callable[[object], str]
    def bold(self, text: str) -> str: ...
    def indent(self, text: str, prefix: str = ...) -> str: ...
    def section(self, title: str, contents: str) -> str: ...
    def formattree(
        self, tree: list[tuple[type, tuple[type, ...]] | list[Any]], modname: str, parent: type | None = ..., prefix: str = ...
    ) -> str: ...
    def docmodule(self, object: object, name: str | None = ..., mod: Any | None = ...) -> str: ...  # type: ignore[override]
    def docclass(self, object: object, name: str | None = ..., mod: str | None = ..., *ignored: Any) -> str: ...
    def formatvalue(self, object: object) -> str: ...
    def docroutine(self, object: object, name: str | None = ..., mod: str | None = ..., cl: Any | None = ...) -> str: ...  # type: ignore[override]
    def docproperty(self, object: object, name: str | None = ..., mod: Any | None = ..., cl: Any | None = ...) -> str: ...  # type: ignore[override]
    def docdata(self, object: object, name: str | None = ..., mod: str | None = ..., cl: Any | None = ...) -> str: ...  # type: ignore[override]
    def docother(  # type: ignore[override]
        self,
        object: object,
        name: str | None = ...,
        mod: str | None = ...,
        parent: str | None = ...,
        maxlen: int | None = ...,
        doc: Any | None = ...,
    ) -> str: ...

def pager(text: str) -> None: ...
def getpager() -> Callable[[str], None]: ...
def plain(text: str) -> str: ...
def pipepager(text: str, cmd: str) -> None: ...
def tempfilepager(text: str, cmd: str) -> None: ...
def ttypager(text: str) -> None: ...
def plainpager(text: str) -> None: ...
def describe(thing: Any) -> str: ...
def locate(path: str, forceload: bool = ...) -> object: ...

text: TextDoc
html: HTMLDoc

class _OldStyleClass: ...

def resolve(thing: str | object, forceload: bool = ...) -> tuple[object, str] | None: ...
def render_doc(thing: str | object, title: str = ..., forceload: bool = ..., renderer: Doc | None = ...) -> str: ...
def doc(thing: str | object, title: str = ..., forceload: bool = ..., output: SupportsWrite[str] | None = ...) -> None: ...
def writedoc(thing: str | object, forceload: bool = ...) -> None: ...
def writedocs(dir: str, pkgpath: str = ..., done: Any | None = ...) -> None: ...

_list = list  # "list" conflicts with method name

class Helper:
    keywords: dict[str, str | tuple[str, str]]
    symbols: dict[str, str]
    topics: dict[str, str | tuple[str, ...]]
    def __init__(self, input: IO[str] | None = ..., output: IO[str] | None = ...) -> None: ...
    input: IO[str]
    output: IO[str]
    def __call__(self, request: str | Helper | object = ...) -> None: ...
    def interact(self) -> None: ...
    def getline(self, prompt: str) -> str: ...
    def help(self, request: Any) -> None: ...
    def intro(self) -> None: ...
    def list(self, items: _list[str], columns: int = ..., width: int = ...) -> None: ...
    def listkeywords(self) -> None: ...
    def listsymbols(self) -> None: ...
    def listtopics(self) -> None: ...
    def showtopic(self, topic: str, more_xrefs: str = ...) -> None: ...
    def showsymbol(self, symbol: str) -> None: ...
    def listmodules(self, key: str = ...) -> None: ...

help: Helper

class ModuleScanner:
    quit: bool
    def run(
        self,
        callback: Callable[[str | None, str, str], None],
        key: str | None = ...,
        completer: Callable[[], None] | None = ...,
        onerror: Callable[[str], None] | None = ...,
    ) -> None: ...

def apropos(key: str) -> None: ...
def ispath(x: Any) -> bool: ...
def cli() -> None: ...
