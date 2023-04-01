from _typeshed import Incomplete
from typing_extensions import Literal

from openpyxl.descriptors.base import Bool, Integer, Typed, _ConvertibleToBool
from openpyxl.descriptors.serialisable import Serialisable

class Index(Serialisable):
    tagname: str
    v: Incomplete
    def __init__(self, v: int = 0) -> None: ...

class Tuple(Serialisable):
    fld: Incomplete
    hier: Incomplete
    item: Incomplete
    def __init__(self, fld: Incomplete | None = None, hier: Incomplete | None = None, item: Incomplete | None = None) -> None: ...

class TupleList(Serialisable):
    c: Incomplete
    tpl: Typed[Tuple, Literal[False]]
    __elements__: Incomplete
    def __init__(self, c: Incomplete | None, tpl: Tuple) -> None: ...

class Missing(Serialisable):
    tagname: str
    tpls: Incomplete
    x: Incomplete
    u: Bool[Literal[True]]
    f: Bool[Literal[True]]
    c: Incomplete
    cp: Incomplete
    _in: Integer  # Not private. Avoids name clash
    bc: Incomplete
    fc: Incomplete
    i: Bool[Literal[True]]
    un: Bool[Literal[True]]
    st: Bool[Literal[True]]
    b: Bool[Literal[True]]
    __elements__: Incomplete
    def __init__(
        self,
        tpls=(),
        x=(),
        u: _ConvertibleToBool | None = None,
        f: _ConvertibleToBool | None = None,
        c: Incomplete | None = None,
        cp: Incomplete | None = None,
        _in: Incomplete | None = None,
        bc: Incomplete | None = None,
        fc: Incomplete | None = None,
        i: _ConvertibleToBool | None = None,
        un: _ConvertibleToBool | None = None,
        st: _ConvertibleToBool | None = None,
        b: _ConvertibleToBool | None = None,
    ) -> None: ...

class Number(Serialisable):
    tagname: str
    tpls: Incomplete
    x: Incomplete
    v: Incomplete
    u: Bool[Literal[True]]
    f: Bool[Literal[True]]
    c: Incomplete
    cp: Incomplete
    _in: Integer  # Not private. Avoids name clash
    bc: Incomplete
    fc: Incomplete
    i: Bool[Literal[True]]
    un: Bool[Literal[True]]
    st: Bool[Literal[True]]
    b: Bool[Literal[True]]
    __elements__: Incomplete
    def __init__(
        self,
        tpls=(),
        x=(),
        v: Incomplete | None = None,
        u: _ConvertibleToBool | None = None,
        f: _ConvertibleToBool | None = None,
        c: Incomplete | None = None,
        cp: Incomplete | None = None,
        _in: Incomplete | None = None,
        bc: Incomplete | None = None,
        fc: Incomplete | None = None,
        i: _ConvertibleToBool | None = None,
        un: _ConvertibleToBool | None = None,
        st: _ConvertibleToBool | None = None,
        b: _ConvertibleToBool | None = None,
    ) -> None: ...

class Error(Serialisable):
    tagname: str
    tpls: Typed[TupleList, Literal[True]]
    x: Incomplete
    v: Incomplete
    u: Bool[Literal[True]]
    f: Bool[Literal[True]]
    c: Incomplete
    cp: Incomplete
    _in: Integer  # Not private. Avoids name clash
    bc: Incomplete
    fc: Incomplete
    i: Bool[Literal[True]]
    un: Bool[Literal[True]]
    st: Bool[Literal[True]]
    b: Bool[Literal[True]]
    __elements__: Incomplete
    def __init__(
        self,
        tpls: TupleList | None = None,
        x=(),
        v: Incomplete | None = None,
        u: _ConvertibleToBool | None = None,
        f: _ConvertibleToBool | None = None,
        c: Incomplete | None = None,
        cp: Incomplete | None = None,
        _in: Incomplete | None = None,
        bc: Incomplete | None = None,
        fc: Incomplete | None = None,
        i: _ConvertibleToBool | None = None,
        un: _ConvertibleToBool | None = None,
        st: _ConvertibleToBool | None = None,
        b: _ConvertibleToBool | None = None,
    ) -> None: ...

class Boolean(Serialisable):
    tagname: str
    x: Incomplete
    v: Bool[Literal[False]]
    u: Bool[Literal[True]]
    f: Bool[Literal[True]]
    c: Incomplete
    cp: Incomplete
    __elements__: Incomplete
    def __init__(
        self,
        x,
        v: _ConvertibleToBool,
        u: _ConvertibleToBool | None = None,
        f: _ConvertibleToBool | None = None,
        c: Incomplete | None = None,
        cp: Incomplete | None = None,
    ) -> None: ...

class Text(Serialisable):
    tagname: str
    tpls: Incomplete
    x: Incomplete
    v: Incomplete
    u: Bool[Literal[True]]
    f: Bool[Literal[True]]
    c: Incomplete
    cp: Incomplete
    _in: Integer  # Not private. Avoids name clash
    bc: Incomplete
    fc: Incomplete
    i: Bool[Literal[True]]
    un: Bool[Literal[True]]
    st: Bool[Literal[True]]
    b: Bool[Literal[True]]
    __elements__: Incomplete
    def __init__(
        self,
        tpls=(),
        x=(),
        v: Incomplete | None = None,
        u: _ConvertibleToBool | None = None,
        f: _ConvertibleToBool | None = None,
        c: Incomplete | None = None,
        cp: Incomplete | None = None,
        _in: Incomplete | None = None,
        bc: Incomplete | None = None,
        fc: Incomplete | None = None,
        i: _ConvertibleToBool | None = None,
        un: _ConvertibleToBool | None = None,
        st: _ConvertibleToBool | None = None,
        b: _ConvertibleToBool | None = None,
    ) -> None: ...

class DateTimeField(Serialisable):
    tagname: str
    x: Incomplete
    v: Incomplete
    u: Bool[Literal[True]]
    f: Bool[Literal[True]]
    c: Incomplete
    cp: Incomplete
    __elements__: Incomplete
    def __init__(
        self,
        x=(),
        v: Incomplete | None = None,
        u: _ConvertibleToBool | None = None,
        f: _ConvertibleToBool | None = None,
        c: Incomplete | None = None,
        cp: Incomplete | None = None,
    ) -> None: ...
