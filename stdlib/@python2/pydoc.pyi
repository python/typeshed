from _typeshed import SupportsWrite
from types import MethodType, ModuleType, TracebackType
from typing import (
    IO,
    Any,
    AnyStr,
    Callable,
    Container,
    Dict,
    List,
    Mapping,
    MutableMapping,
    NoReturn,
    Optional,
    Text,
    Tuple,
    Type,
)

from repr import Repr

# the return type of sys.exc_info(), used by ErrorDuringImport.__init__
_Exc_Info = Tuple[Optional[Type[BaseException]], Optional[BaseException], Optional[TracebackType]]

__author__: str
__date__: str
__version__: str
__credits__: str

def pathdirs() -> List[str]: ...
def getdoc(object: object) -> Text: ...
def splitdoc(doc: AnyStr) -> Tuple[AnyStr, AnyStr]: ...
def classname(object: object, modname: str) -> str: ...
def isdata(object: object) -> bool: ...
def replace(text: AnyStr, *pairs: AnyStr) -> AnyStr: ...
def cram(text: str, maxlen: int) -> str: ...
def stripid(text: str) -> str: ...
def allmethods(cl: type) -> MutableMapping[str, MethodType]: ...
def visiblename(name: str, all: Container[str] | None = ..., obj: object | None = ...) -> bool: ...
def classify_class_attrs(object: object) -> List[Tuple[str, str, type, str]]: ...
def ispackage(path: str) -> bool: ...
def source_synopsis(file: IO[AnyStr]) -> AnyStr | None: ...
def synopsis(filename: str, cache: MutableMapping[str, Tuple[int, str]] = ...) -> str | None: ...

class ErrorDuringImport(Exception):
    filename: str
    exc: Type[BaseException] | None
    value: BaseException | None
    tb: TracebackType | None
    def __init__(self, filename: str, exc_info: _Exc_Info) -> None: ...

def importfile(path: str) -> ModuleType: ...
def safeimport(path: str, forceload: bool = ..., cache: MutableMapping[str, ModuleType] = ...) -> ModuleType: ...

class Doc:
    PYTHONDOCS: str
    def document(self, object: object, name: str | None = ..., *args: Any) -> str: ...
    def fail(self, object: object, name: str | None = ..., *args: Any) -> NoReturn: ...
    def docmodule(self, object: object, name: str | None = ..., *args: Any) -> str: ...
    def docclass(self, object: object, name: str | None = ..., *args: Any) -> str: ...
    def docroutine(self, object: object, name: str | None = ..., *args: Any) -> str: ...
    def docother(self, object: object, name: str | None = ..., *args: Any) -> str: ...
    def docproperty(self, object: object, name: str | None = ..., *args: Any) -> str: ...
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
    def repr_string(self, x: Text, level: complex) -> str: ...
    def repr_str(self, x: Text, level: complex) -> str: ...
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
    def multicolumn(self, list: List[Any], format: Callable[[Any], str], cols: int = ...) -> str: ...
    def grey(self, text: str) -> str: ...
    def namelink(self, name: str, *dicts: MutableMapping[str, str]) -> str: ...
    def classlink(self, object: object, modname: str) -> str: ...
    def modulelink(self, object: object) -> str: ...
    def modpkglink(self, modpkginfo: Tuple[str, str, bool, bool]) -> str: ...
    def markup(
        self,
        text: str,
        escape: Callable[[str], str] | None = ...,
        funcs: Mapping[str, str] = ...,
        classes: Mapping[str, str] = ...,
        methods: Mapping[str, str] = ...,
    ) -> str: ...
    def formattree(
        self, tree: List[Tuple[type, Tuple[type, ...]] | List[Any]], modname: str, parent: type | None = ...
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
    def docroutine(
        self,
        object: object,
        name: str | None = ...,
        mod: str | None = ...,
        funcs: Mapping[str, str] = ...,
        classes: Mapping[str, str] = ...,
        methods: Mapping[str, str] = ...,
        cl: type | None = ...,
        *ignored: Any,
    ) -> str: ...
    def docproperty(
        self, object: object, name: str | None = ..., mod: str | None = ..., cl: Any | None = ..., *ignored: Any
    ) -> str: ...
    def docother(self, object: object, name: str | None = ..., mod: Any | None = ..., *ignored: Any) -> str: ...
    def docdata(
        self, object: object, name: str | None = ..., mod: Any | None = ..., cl: Any | None = ..., *ignored: Any
    ) -> str: ...
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
        self, tree: List[Tuple[type, Tuple[type, ...]] | List[Any]], modname: str, parent: type | None = ..., prefix: str = ...
    ) -> str: ...
    def docmodule(self, object: object, name: str | None = ..., mod: Any | None = ..., *ignored: Any) -> str: ...
    def docclass(self, object: object, name: str | None = ..., mod: str | None = ..., *ignored: Any) -> str: ...
    def formatvalue(self, object: object) -> str: ...
    def docroutine(
        self, object: object, name: str | None = ..., mod: str | None = ..., cl: Any | None = ..., *ignored: Any
    ) -> str: ...
    def docproperty(
        self, object: object, name: str | None = ..., mod: Any | None = ..., cl: Any | None = ..., *ignored: Any
    ) -> str: ...
    def docdata(
        self, object: object, name: str | None = ..., mod: str | None = ..., cl: Any | None = ..., *ignored: Any
    ) -> str: ...
    def docother(
        self,
        object: object,
        name: str | None = ...,
        mod: str | None = ...,
        parent: str | None = ...,
        maxlen: int | None = ...,
        doc: Any | None = ...,
        *ignored: Any,
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

def resolve(thing: str | object, forceload: bool = ...) -> Tuple[object, str] | None: ...
def render_doc(thing: str | object, title: str = ..., forceload: bool = ..., renderer: Doc | None = ...) -> str: ...
def doc(thing: str | object, title: str = ..., forceload: bool = ..., output: SupportsWrite[str] | None = ...) -> None: ...
def writedoc(thing: str | object, forceload: bool = ...) -> None: ...
def writedocs(dir: str, pkgpath: str = ..., done: Any | None = ...) -> None: ...

class Helper:
    keywords: Dict[str, str | Tuple[str, str]]
    symbols: Dict[str, str]
    topics: Dict[str, str | Tuple[str, ...]]
    def __init__(self, input: IO[str] | None = ..., output: IO[str] | None = ...) -> None: ...
    input: IO[str]
    output: IO[str]
    def __call__(self, request: str | Helper | object = ...) -> None: ...
    def interact(self) -> None: ...
    def getline(self, prompt: str) -> str: ...
    def help(self, request: Any) -> None: ...
    def intro(self) -> None: ...
    def list(self, items: List[str], columns: int = ..., width: int = ...) -> None: ...
    def listkeywords(self) -> None: ...
    def listsymbols(self) -> None: ...
    def listtopics(self) -> None: ...
    def showtopic(self, topic: str, more_xrefs: str = ...) -> None: ...
    def showsymbol(self, symbol: str) -> None: ...
    def listmodules(self, key: str = ...) -> None: ...

help: Helper

# See Python issue #11182: "remove the unused and undocumented pydoc.Scanner class"
# class Scanner:
#     roots = ...  # type: Any
#     state = ...  # type: Any
#     children = ...  # type: Any
#     descendp = ...  # type: Any
#     def __init__(self, roots, children, descendp) -> None: ...
#     def next(self): ...

class ModuleScanner:
    quit: bool
    def run(
        self,
        callback: Callable[[str | None, str, str], None],
        key: Any | None = ...,
        completer: Callable[[], None] | None = ...,
        onerror: Callable[[str], None] | None = ...,
    ) -> None: ...

def apropos(key: str) -> None: ...
def ispath(x: Any) -> bool: ...
def cli() -> None: ...
def serve(port: int, callback: Callable[[Any], None] | None = ..., completer: Callable[[], None] | None = ...) -> None: ...
def gui() -> None: ...
