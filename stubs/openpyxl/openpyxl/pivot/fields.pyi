from _typeshed import Incomplete
from typing_extensions import Literal

from openpyxl.descriptors.base import Typed
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
    u: Incomplete
    f: Incomplete
    c: Incomplete
    cp: Incomplete
    bc: Incomplete
    fc: Incomplete
    i: Incomplete
    un: Incomplete
    st: Incomplete
    b: Incomplete
    __elements__: Incomplete
    def __init__(
        self,
        tpls=(),
        x=(),
        u: Incomplete | None = None,
        f: Incomplete | None = None,
        c: Incomplete | None = None,
        cp: Incomplete | None = None,
        _in: Incomplete | None = None,
        bc: Incomplete | None = None,
        fc: Incomplete | None = None,
        i: Incomplete | None = None,
        un: Incomplete | None = None,
        st: Incomplete | None = None,
        b: Incomplete | None = None,
    ) -> None: ...

class Number(Serialisable):
    tagname: str
    tpls: Incomplete
    x: Incomplete
    v: Incomplete
    u: Incomplete
    f: Incomplete
    c: Incomplete
    cp: Incomplete
    bc: Incomplete
    fc: Incomplete
    i: Incomplete
    un: Incomplete
    st: Incomplete
    b: Incomplete
    __elements__: Incomplete
    def __init__(
        self,
        tpls=(),
        x=(),
        v: Incomplete | None = None,
        u: Incomplete | None = None,
        f: Incomplete | None = None,
        c: Incomplete | None = None,
        cp: Incomplete | None = None,
        _in: Incomplete | None = None,
        bc: Incomplete | None = None,
        fc: Incomplete | None = None,
        i: Incomplete | None = None,
        un: Incomplete | None = None,
        st: Incomplete | None = None,
        b: Incomplete | None = None,
    ) -> None: ...

class Error(Serialisable):
    tagname: str
    tpls: Typed[TupleList, Literal[True]]
    x: Incomplete
    v: Incomplete
    u: Incomplete
    f: Incomplete
    c: Incomplete
    cp: Incomplete
    bc: Incomplete
    fc: Incomplete
    i: Incomplete
    un: Incomplete
    st: Incomplete
    b: Incomplete
    __elements__: Incomplete
    def __init__(
        self,
        tpls: TupleList | None = None,
        x=(),
        v: Incomplete | None = None,
        u: Incomplete | None = None,
        f: Incomplete | None = None,
        c: Incomplete | None = None,
        cp: Incomplete | None = None,
        _in: Incomplete | None = None,
        bc: Incomplete | None = None,
        fc: Incomplete | None = None,
        i: Incomplete | None = None,
        un: Incomplete | None = None,
        st: Incomplete | None = None,
        b: Incomplete | None = None,
    ) -> None: ...

class Boolean(Serialisable):
    tagname: str
    x: Incomplete
    v: Incomplete
    u: Incomplete
    f: Incomplete
    c: Incomplete
    cp: Incomplete
    __elements__: Incomplete
    def __init__(
        self,
        x=(),
        v: Incomplete | None = None,
        u: Incomplete | None = None,
        f: Incomplete | None = None,
        c: Incomplete | None = None,
        cp: Incomplete | None = None,
    ) -> None: ...

class Text(Serialisable):
    tagname: str
    tpls: Incomplete
    x: Incomplete
    v: Incomplete
    u: Incomplete
    f: Incomplete
    c: Incomplete
    cp: Incomplete
    bc: Incomplete
    fc: Incomplete
    i: Incomplete
    un: Incomplete
    st: Incomplete
    b: Incomplete
    __elements__: Incomplete
    def __init__(
        self,
        tpls=(),
        x=(),
        v: Incomplete | None = None,
        u: Incomplete | None = None,
        f: Incomplete | None = None,
        c: Incomplete | None = None,
        cp: Incomplete | None = None,
        _in: Incomplete | None = None,
        bc: Incomplete | None = None,
        fc: Incomplete | None = None,
        i: Incomplete | None = None,
        un: Incomplete | None = None,
        st: Incomplete | None = None,
        b: Incomplete | None = None,
    ) -> None: ...

class DateTimeField(Serialisable):
    tagname: str
    x: Incomplete
    v: Incomplete
    u: Incomplete
    f: Incomplete
    c: Incomplete
    cp: Incomplete
    __elements__: Incomplete
    def __init__(
        self,
        x=(),
        v: Incomplete | None = None,
        u: Incomplete | None = None,
        f: Incomplete | None = None,
        c: Incomplete | None = None,
        cp: Incomplete | None = None,
    ) -> None: ...
