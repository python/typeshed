from _typeshed import Incomplete
from collections import defaultdict
from collections.abc import Callable, Container, Iterable
from types import ModuleType
from typing import Final, Literal, TextIO, TypedDict
from typing_extensions import NotRequired, TypeAlias, TypeGuard, Unpack

IS_INTERACTIVE: bool

__author__: Final[str]
__copyright__: Final[str]
__license__: Final[str]
__version__: Final[str]
__date__: Final[str]

# GraphViz has types, but does not include the py.typed file.
# See https://github.com/xflr6/graphviz/pull/180
_GraphvizSource: TypeAlias = Incomplete
_Filter: TypeAlias = Callable[[object], bool]

class _StateDict(TypedDict):
    old: NotRequired[defaultdict[str, set[int]]]
    current: NotRequired[defaultdict[str, set[int]]]
    new: NotRequired[defaultdict[str, set[int]]]
    shortnames: NotRequired[bool]

class _ChainKeywords(TypedDict):
    obj: NotRequired[object]
    predicate: NotRequired[_Filter]
    max_depth: NotRequired[int]
    extra_ignore: NotRequired[Iterable[int]]

def count(typename: str, objects: Iterable[object] | None = None) -> int: ...
def typestats(
    objects: Iterable[object] | None = None, shortnames: bool = True, filter: _Filter | None = None
) -> dict[str, int]: ...
def most_common_types(
    limit: int = 10, objects: Iterable[object] | None = None, shortnames: bool = True, filter: _Filter | None = None
) -> list[tuple[str, int]]: ...
def show_most_common_types(
    limit: int = 10,
    objects: Iterable[object] | None = None,
    shortnames: bool = True,
    file: TextIO | None = None,
    filter: _Filter | None = None,
) -> None: ...
def growth(
    limit: int = 10, peak_stats: dict[str, int] = {}, shortnames: bool = True, filter: _Filter | None = None
) -> list[tuple[str, int]]: ...
def show_growth(
    limit: int = 10,
    peak_stats: dict[str, int] | None = None,
    shortnames: bool = True,
    file: TextIO | None = None,
    filter: _Filter | None = None,
) -> None: ...
def get_new_ids(
    skip_update: bool = False,
    limit: int = 10,
    sortby: Literal["old", "current", "new", "deltas"] = "deltas",
    shortnames: bool | None = None,
    file: TextIO | None = None,
    _state: _StateDict = {},
) -> defaultdict[str, set[int]]: ...
def get_leaking_objects(objects: Iterable[object] | None = None) -> list[object]: ...
def by_type(typename: str, objects: Iterable[object] | None = None) -> list[object]: ...
def at(addr: int) -> object | None: ...
def at_addrs(address_set: Container[int]) -> list[object]: ...
def find_ref_chain(obj: object, predicate: _Filter, max_depth: int = 20, extra_ignore: Iterable[int] = ()) -> list[object]: ...
def find_backref_chain(
    obj: object, predicate: _Filter, max_depth: int = 20, extra_ignore: Iterable[int] = ()
) -> list[object]: ...
def show_backrefs(
    objs: object | list[object] | tuple[object],
    max_depth: int = 3,
    extra_ignore: Iterable[int] = (),
    filter: _Filter | None = None,
    too_many: int = 10,
    highlight: object | None = None,
    filename: str | None = None,
    extra_info: Callable[[object], str] | None = None,
    refcounts: bool = False,
    shortnames: bool = True,
    output: TextIO | None = None,
    extra_node_attrs: Callable[[object], dict[str, str]] | None = None,
) -> None | _GraphvizSource: ...
def show_refs(
    objs: object | list[object] | tuple[object],
    max_depth: int = 3,
    extra_ignore: Iterable[int] = (),
    filter: _Filter | None = None,
    too_many: int = 10,
    highlight: object | None = None,
    filename: str | None = None,
    extra_info: Callable[[object], str] | None = None,
    refcounts: bool = False,
    shortnames: bool = True,
    output: TextIO | None = None,
    extra_node_attrs: Callable[[object], dict[str, str]] | None = None,
) -> None | _GraphvizSource: ...
def show_chain(*chains: list[object], **kw: Unpack[_ChainKeywords]) -> None: ...
def is_proper_module(obj: object) -> TypeGuard[ModuleType]: ...
