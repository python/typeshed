from _typeshed import Incomplete
from typing import type_check_only
from typing_extensions import final

from pyasn1.type import constraint, namedtype
from pyasn1.type.tag import TagSet

class Asn1Item:
    @classmethod
    def getTypeId(cls, increment: int = ...): ...

class Asn1Type(Asn1Item):
    tagSet: TagSet
    subtypeSpec: constraint.ConstraintsIntersection
    typeId: int | None
    def __init__(self, **kwargs) -> None: ...
    def __setattr__(self, name, value) -> None: ...
    @property
    def readOnly(self): ...
    @property
    def effectiveTagSet(self): ...
    @property
    def tagMap(self): ...
    def isSameTypeWith(self, other, matchTags: bool = ..., matchConstraints: bool = ...): ...
    def isSuperTypeOf(self, other, matchTags: bool = ..., matchConstraints: bool = ...): ...
    @staticmethod
    def isNoValue(*values): ...
    def prettyPrint(self, scope: int = ...) -> None: ...
    def getTagSet(self): ...
    def getEffectiveTagSet(self): ...
    def getTagMap(self): ...
    def getSubtypeSpec(self): ...
    def hasValue(self): ...

Asn1ItemBase = Asn1Type

@final
class NoValue:
    skipMethods: set[str]
    def __new__(cls): ...
    def __getattr__(self, attr) -> None: ...
    # def __new__.<locals>.getPlug.<locals>.plug
    @type_check_only
    def plug(self, *args: object, **kw: object): ...
    # Magic methods assigned dynamically, priority from right to left: plug < str < int < list < dict
    __abs__ = int.__abs__
    __add__ = list.__add__
    __and__ = int.__and__
    __bool__ = int.__bool__
    __ceil__ = int.__ceil__
    __class_getitem__ = plug
    __contains__ = dict.__contains__
    __delitem__ = dict.__delitem__
    __dir__ = plug
    __divmod__ = int.__divmod__
    __float__ = int.__float__
    __floor__ = int.__floor__
    __floordiv__ = int.__floordiv__
    __ge__ = list.__ge__
    __getitem__ = dict.__getitem__
    __gt__ = list.__gt__
    __iadd__ = list.__iadd__
    __imul__ = list.__imul__
    __index__ = int.__index__
    # self instead of cls
    __init_subclass__ = plug  # pyright: ignore[reportGeneralTypeIssues]
    __int__ = int.__int__
    __invert__ = int.__invert__
    __ior__ = plug
    __iter__ = dict.__iter__
    __le__ = list.__le__
    __len__ = dict.__len__
    __lshift__ = int.__lshift__
    __lt__ = list.__lt__
    __mod__ = int.__mod__
    __mul__ = list.__mul__
    __neg__ = int.__neg__
    __or__ = int.__or__
    __pos__ = int.__pos__
    __pow__ = int.__pow__
    __radd__ = int.__radd__
    __rand__ = int.__rand__
    __rdivmod__ = int.__rdivmod__
    __reversed__ = list.__reversed__
    __rfloordiv__ = int.__rfloordiv__
    __rlshift__ = int.__rlshift__
    __rmod__ = int.__rmod__
    __rmul__ = list.__rmul__
    __ror__ = int.__ror__
    __round__ = int.__round__
    __rpow__ = int.__rpow__
    __rrshift__ = int.__rrshift__
    __rshift__ = int.__rshift__
    __rsub__ = int.__rsub__
    __rtruediv__ = int.__rtruediv__
    __rxor__ = int.__rxor__
    __setitem__ = list.__setitem__
    __str__ = plug
    __sub__ = int.__sub__
    __truediv__ = int.__truediv__
    __trunc__ = int.__trunc__
    __xor__ = int.__xor__

class SimpleAsn1Type(Asn1Type):
    defaultValue: Incomplete | NoValue
    def __init__(self, value=..., **kwargs) -> None: ...
    def __lt__(self, other): ...
    def __le__(self, other): ...
    def __gt__(self, other): ...
    def __ge__(self, other): ...
    def __bool__(self) -> bool: ...
    def __hash__(self): ...
    @property
    def isValue(self): ...
    def clone(self, value=..., **kwargs): ...
    def subtype(self, value=..., **kwargs): ...
    def prettyIn(self, value): ...
    def prettyOut(self, value): ...
    def prettyPrint(self, scope: int = ...): ...
    def prettyPrintType(self, scope: int = ...): ...

AbstractSimpleAsn1Item = SimpleAsn1Type

class ConstructedAsn1Type(Asn1Type):
    strictConstraints: bool
    componentType: namedtype.NamedTypes | None
    sizeSpec: constraint.ConstraintsIntersection
    def __init__(self, **kwargs) -> None: ...
    def __lt__(self, other): ...
    def __le__(self, other): ...
    def __gt__(self, other): ...
    def __ge__(self, other): ...
    def __bool__(self) -> bool: ...
    @property
    def components(self) -> None: ...
    def clone(self, **kwargs): ...
    def subtype(self, **kwargs): ...
    def getComponentByPosition(self, idx) -> None: ...
    def setComponentByPosition(self, idx, value, verifyConstraints: bool = ...) -> None: ...
    def setComponents(self, *args, **kwargs): ...
    def setDefaultComponents(self) -> None: ...
    def getComponentType(self): ...
    def verifySizeSpec(self) -> None: ...

AbstractConstructedAsn1Item = ConstructedAsn1Type
