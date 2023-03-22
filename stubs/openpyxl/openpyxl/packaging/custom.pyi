from _typeshed import Incomplete
from openpyxl.descriptors import Bool, Strict
from openpyxl.descriptors.nested import NestedText
from openpyxl.descriptors.serialisable import Serialisable

class NestedBoolText(Bool, NestedText): ...

class _CustomDocumentProperty(Serialisable):
    tagname: str
    name: Incomplete
    lpwstr: Incomplete
    i4: Incomplete
    r8: Incomplete
    filetime: Incomplete
    bool: Incomplete
    linkTarget: Incomplete
    fmtid: Incomplete
    pid: Incomplete
    def __init__(
        self, name: Incomplete | None = ..., pid: int = ..., fmtid=..., linkTarget: Incomplete | None = ..., **kw
    ) -> None: ...
    @property
    def type(self): ...
    def to_tree(self, tagname: Incomplete | None = ..., idx: Incomplete | None = ..., namespace: Incomplete | None = ...): ...

class _CustomDocumentPropertyList(Serialisable):
    tagname: str
    property: Incomplete
    customProps: Incomplete
    def __init__(self, property=...) -> None: ...
    def __len__(self) -> int: ...
    def to_tree(self, tagname: Incomplete | None = ..., idx: Incomplete | None = ..., namespace: Incomplete | None = ...): ...

class _TypedProperty(Strict):
    name: Incomplete
    value: Incomplete
    def __init__(self, name, value) -> None: ...
    def __eq__(self, other): ...

class IntProperty(_TypedProperty):
    value: Incomplete

class FloatProperty(_TypedProperty):
    value: Incomplete

class StringProperty(_TypedProperty):
    value: Incomplete

class DateTimeProperty(_TypedProperty):
    value: Incomplete

class BoolProperty(_TypedProperty):
    value: Incomplete

class LinkProperty(_TypedProperty):
    value: Incomplete

CLASS_MAPPING: Incomplete
XML_MAPPING: Incomplete

class CustomPropertyList(Strict):
    props: Incomplete
    def __init__(self) -> None: ...
    @classmethod
    def from_tree(cls, tree): ...
    def append(self, prop) -> None: ...
    def to_tree(self): ...
    def __len__(self) -> int: ...
    @property
    def names(self): ...
    def __getitem__(self, name): ...
    def __delitem__(self, name) -> None: ...
    def __iter__(self): ...
