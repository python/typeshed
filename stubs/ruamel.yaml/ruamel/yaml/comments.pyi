from _typeshed import Incomplete
from collections.abc import Mapping, MutableSet, Set as AbstractSet, Sized
from typing import Any, Iterator

from ruamel.yaml.compat import MutableSliceableSequence, ordereddict
from ruamel.yaml.tag import Tag

__all__ = [
    "CommentedSeq",
    "CommentedKeySeq",
    "CommentedMap",
    "CommentedOrderedMap",
    "CommentedSet",
    "comment_attrib",
    "merge_attrib",
    "TaggedScalar",
    "C_POST",
    "C_PRE",
    "C_SPLIT_ON_FIRST_BLANK",
    "C_BLANK_LINE_PRESERVE_SPACE",
]

C_POST: int
C_PRE: int
C_SPLIT_ON_FIRST_BLANK: int
C_BLANK_LINE_PRESERVE_SPACE: int

class IDX:
    def __init__(self) -> None: ...
    def __call__(self) -> Any: ...

comment_attrib: str
merge_attrib: str

class Comment:
    attrib = comment_attrib
    comment: Incomplete
    def __init__(self, old: bool = True) -> None: ...
    @property
    def items(self) -> Any: ...
    @property
    def end(self) -> Any: ...
    @end.setter
    def end(self, value: Any) -> None: ...
    @property
    def pre(self) -> Any: ...
    @pre.setter
    def pre(self, value: Any) -> None: ...
    def get(self, item: Any, pos: Any) -> Any: ...
    def set(self, item: Any, pos: Any, value: Any) -> Any: ...
    def __contains__(self, x: Any) -> Any: ...

class NotNone: ...

class Format:
    attrib = format_attrib
    def __init__(self) -> None: ...
    def set_flow_style(self) -> None: ...
    def set_block_style(self) -> None: ...
    def flow_style(self, default: Any | None = None) -> Any: ...

class LineCol:
    attrib = line_col_attrib
    line: Incomplete
    col: Incomplete
    data: Incomplete
    def __init__(self) -> None: ...
    def add_kv_line_col(self, key: Any, data: Any) -> None: ...
    def key(self, k: Any) -> Any: ...
    def value(self, k: Any) -> Any: ...
    def item(self, idx: Any) -> Any: ...
    def add_idx_line_col(self, key: Any, data: Any) -> None: ...

class CommentedBase:
    @property
    def ca(self) -> Any: ...
    def yaml_end_comment_extend(self, comment: Any, clear: bool = False) -> None: ...
    def yaml_key_comment_extend(self, key: Any, comment: Any, clear: bool = False) -> None: ...
    def yaml_value_comment_extend(self, key: Any, comment: Any, clear: bool = False) -> None: ...
    def yaml_set_start_comment(self, comment: Any, indent: Any = 0) -> None: ...
    def yaml_set_comment_before_after_key(
        self, key: Any, before: Any = None, indent: Any = 0, after: Any = None, after_indent: Any = None
    ) -> None: ...
    @property
    def fa(self) -> Any: ...
    def yaml_add_eol_comment(self, comment: Any, key: Any | None = ..., column: Any | None = None) -> None: ...
    @property
    def lc(self) -> Any: ...
    @property
    def anchor(self) -> Any: ...
    def yaml_anchor(self) -> Any: ...
    def yaml_set_anchor(self, value: Any, always_dump: bool = False) -> None: ...
    @property
    def tag(self) -> Any: ...
    def yaml_set_ctag(self, value: Tag) -> None: ...
    def copy_attributes(self, t: Any, memo: Any = None) -> Any: ...

class CommentedSeq(MutableSliceableSequence, list, CommentedBase):
    def __init__(self, *args: Any, **kw: Any) -> None: ...
    def __getsingleitem__(self, idx: Any) -> Any: ...
    def __setsingleitem__(self, idx: Any, value: Any) -> None: ...
    def __delsingleitem__(self, idx: Any = None) -> Any: ...
    def __len__(self) -> int: ...
    def insert(self, idx: Any, val: Any) -> None: ...
    def extend(self, val: Any) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    def __deepcopy__(self, memo: Any) -> Any: ...
    def __add__(self, other: Any) -> Any: ...
    def sort(self, key: Any = None, reverse: bool = False) -> None: ...

class CommentedKeySeq(tuple, CommentedBase): ...

class CommentedMapView(Sized):
    def __init__(self, mapping: Any) -> None: ...
    def __len__(self) -> int: ...

class CommentedMapKeysView(CommentedMapView, AbstractSet):
    def __contains__(self, key: Any) -> Any: ...
    def __iter__(self) -> Any: ...

class CommentedMapItemsView(CommentedMapView, AbstractSet):
    def __contains__(self, item: Any) -> Any: ...
    def __iter__(self) -> Any: ...

class CommentedMapValuesView(CommentedMapView):
    def __contains__(self, value: Any) -> Any: ...
    def __iter__(self) -> Any: ...

class CommentedMap(ordereddict, CommentedBase):
    def __init__(self, *args: Any, **kw: Any) -> None: ...
    def update(self, *vals: Any, **kw: Any) -> None: ...
    def insert(self, pos: Any, key: Any, value: Any, comment: Any | None = None) -> None: ...
    def mlget(self, key: Any, default: Any = None, list_ok: Any = False) -> Any: ...
    def __getitem__(self, key: Any) -> Any: ...
    def __setitem__(self, key: Any, value: Any) -> None: ...
    def __contains__(self, key: Any) -> bool: ...
    def get(self, key: Any, default: Any = None) -> Any: ...
    def non_merged_items(self) -> Any: ...
    def __delitem__(self, key: Any) -> None: ...
    def __iter__(self) -> Any: ...
    def pop(self, key: Any, default: Any = ...) -> Any: ...
    def __len__(self) -> int: ...
    def __eq__(self, other: object) -> bool: ...
    def keys(self) -> Any: ...
    def values(self) -> Any: ...
    def items(self) -> Any: ...
    @property
    def merge(self) -> Any: ...
    def copy(self) -> Any: ...
    def add_referent(self, cm: Any) -> None: ...
    def add_yaml_merge(self, value: Any) -> None: ...
    def update_key_value(self, key: Any) -> None: ...
    def __deepcopy__(self, memo: Any) -> Any: ...

class CommentedKeyMap(CommentedBase, Mapping):
    def __init__(self, *args: Any, **kw: Any) -> None: ...
    __delitem__ = raise_immutable
    __setitem__ = raise_immutable
    clear = raise_immutable
    pop = raise_immutable
    popitem = raise_immutable
    setdefault = raise_immutable
    update = raise_immutable
    def __getitem__(self, index: Any) -> Any: ...
    def __iter__(self) -> Iterator[Any]: ...
    def __len__(self) -> int: ...
    def __hash__(self) -> Any: ...
    @classmethod
    def fromkeys(keys: Any, v: Any = None) -> Any: ...

class CommentedOrderedMap(CommentedMap): ...

class CommentedSet(MutableSet, CommentedBase):
    odict: Incomplete
    def __init__(self, values: Any = None) -> None: ...
    def add(self, value: Any) -> None: ...
    def discard(self, value: Any) -> None: ...
    def __contains__(self, x: Any) -> Any: ...
    def __iter__(self) -> Any: ...
    def __len__(self) -> int: ...

class TaggedScalar(CommentedBase):
    value: Incomplete
    style: Incomplete
    def __init__(self, value: Any = None, style: Any = None, tag: Any = None) -> None: ...
    def count(self, s: str, start: int | None = None, end: int | None = None) -> Any: ...
    def __getitem__(self, pos: int) -> Any: ...
