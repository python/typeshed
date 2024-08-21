from _typeshed import Incomplete
from collections.abc import Generator, Mapping, MutableSet, Set as AbstractSet, Sized
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
    def __call__(self): ...

comment_attrib: str
merge_attrib: str

class Comment:
    attrib = comment_attrib
    comment: Incomplete
    def __init__(self, old: bool = True) -> None: ...
    @property
    def items(self): ...
    @property
    def end(self): ...
    @end.setter
    def end(self, value) -> None: ...
    @property
    def pre(self): ...
    @pre.setter
    def pre(self, value) -> None: ...
    def get(self, item, pos): ...
    def set(self, item, pos, value) -> None: ...
    def __contains__(self, x) -> bool: ...

class NotNone: ...

class Format:
    attrib = format_attrib
    def __init__(self) -> None: ...
    def set_flow_style(self) -> None: ...
    def set_block_style(self) -> None: ...
    def flow_style(self, default: Incomplete = None): ...

class LineCol:
    attrib = line_col_attrib
    line: Incomplete
    col: Incomplete
    data: Incomplete
    def __init__(self) -> None: ...
    def add_kv_line_col(self, key, data) -> None: ...
    def key(self, k): ...
    def value(self, k): ...
    def item(self, idx): ...
    def add_idx_line_col(self, key, data) -> None: ...

class CommentedBase:
    @property
    def ca(self) -> Any: ...
    def yaml_end_comment_extend(self, comment, clear: bool = False) -> None: ...
    def yaml_key_comment_extend(self, key, comment, clear: bool = False) -> None: ...
    def yaml_value_comment_extend(self, key, comment, clear: bool = False) -> None: ...
    def yaml_set_start_comment(self, comment, indent: int = 0) -> None: ...
    def yaml_set_comment_before_after_key(
        self,
        key,
        before: Incomplete | None = None,
        indent: int = 0,
        after: Incomplete | None = None,
        after_indent: Incomplete | None = None,
    ) -> None: ...
    @property
    def fa(self): ...
    def yaml_add_eol_comment(self, comment, key: Incomplete = ..., column: Incomplete = None) -> None: ...
    @property
    def lc(self): ...
    @property
    def anchor(self): ...
    def yaml_anchor(self): ...
    def yaml_set_anchor(self, value, always_dump: bool = False) -> None: ...
    @property
    def tag(self): ...
    def yaml_set_ctag(self, value: Tag) -> None: ...
    def copy_attributes(self, t, memo: Incomplete | None = None): ...

class CommentedSeq(MutableSliceableSequence, list, CommentedBase):
    def __init__(self, *args, **kw) -> None: ...
    def __getsingleitem__(self, idx): ...
    def __setsingleitem__(self, idx, value) -> None: ...
    def __delsingleitem__(self, idx: Incomplete | None = None) -> None: ...
    def __len__(self) -> int: ...
    def insert(self, idx, val) -> None: ...
    def extend(self, val) -> None: ...
    def __eq__(self, other) -> bool: ...
    def __deepcopy__(self, memo): ...
    def __add__(self, other): ...
    def sort(self, key: Incomplete | None = None, reverse: bool = False) -> None: ...

class CommentedKeySeq(tuple, CommentedBase): ...

class CommentedMapView(Sized):
    def __init__(self, mapping) -> None: ...
    def __len__(self) -> int: ...

class CommentedMapKeysView(CommentedMapView, AbstractSet):
    def __contains__(self, key) -> bool: ...
    def __iter__(self): ...

class CommentedMapItemsView(CommentedMapView, AbstractSet):
    def __contains__(self, item) -> bool: ...
    def __iter__(self): ...

class CommentedMapValuesView(CommentedMapView):
    def __contains__(self, value) -> bool: ...
    def __iter__(self): ...

class CommentedMap(ordereddict, CommentedBase):
    def __init__(self, *args, **kw) -> None: ...
    def update(self, *vals, **kw) -> None: ...
    def insert(self, pos, key, value, comment: Incomplete = None) -> None: ...
    def mlget(self, key, default: Incomplete | None = None, list_ok: bool = False): ...
    def __getitem__(self, key): ...
    def __setitem__(self, key, value) -> None: ...
    def __contains__(self, key) -> bool: ...
    def get(self, key, default: Incomplete | None = None): ...
    def non_merged_items(self) -> Generator[Incomplete, None, None]: ...
    def __delitem__(self, key) -> None: ...
    def __iter__(self): ...
    def pop(self, key, default=...): ...
    def __len__(self) -> int: ...
    def __eq__(self, other) -> bool: ...
    def keys(self): ...
    def values(self): ...
    def items(self): ...
    @property
    def merge(self): ...
    def copy(self): ...
    def add_referent(self, cm) -> None: ...
    def add_yaml_merge(self, value) -> None: ...
    def update_key_value(self, key) -> None: ...
    def __deepcopy__(self, memo): ...

class CommentedKeyMap(CommentedBase, Mapping):
    def __init__(self, *args, **kw) -> None: ...
    __delitem__ = raise_immutable
    __setitem__ = raise_immutable
    clear = raise_immutable
    pop = raise_immutable
    popitem = raise_immutable
    setdefault = raise_immutable
    update = raise_immutable
    def __getitem__(self, index): ...
    def __iter__(self) -> Iterator: ...
    def __len__(self) -> int: ...
    def __hash__(self): ...
    @classmethod
    def fromkeys(keys, v: Incomplete | None = None): ...

class CommentedOrderedMap(CommentedMap): ...

class CommentedSet(MutableSet, CommentedBase):
    odict: Incomplete
    def __init__(self, values: Incomplete | None = None) -> None: ...
    def add(self, value) -> None: ...
    def discard(self, value) -> None: ...
    def __contains__(self, x) -> bool: ...
    def __iter__(self): ...
    def __len__(self) -> int: ...

class TaggedScalar(CommentedBase):
    value: Incomplete
    style: Incomplete
    def __init__(
        self, value: Incomplete | None = None, style: Incomplete | None = None, tag: Incomplete | None = None
    ) -> None: ...
    def count(self, s: str, start: int | None = None, end: int | None = None): ...
    def __getitem__(self, pos: int): ...
