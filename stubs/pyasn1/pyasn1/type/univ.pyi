from _typeshed import Incomplete
from collections.abc import Generator

from pyasn1.type import base

NoValue: Incomplete
noValue: Incomplete

class Integer(base.SimpleAsn1Type):
    tagSet: Incomplete
    subtypeSpec: Incomplete
    namedValues: Incomplete
    typeId: Incomplete
    def __init__(self, value=..., **kwargs) -> None: ...
    def __and__(self, value): ...
    def __rand__(self, value): ...
    def __or__(self, value): ...
    def __ror__(self, value): ...
    def __xor__(self, value): ...
    def __rxor__(self, value): ...
    def __lshift__(self, value): ...
    def __rshift__(self, value): ...
    def __add__(self, value): ...
    def __radd__(self, value): ...
    def __sub__(self, value): ...
    def __rsub__(self, value): ...
    def __mul__(self, value): ...
    def __rmul__(self, value): ...
    def __mod__(self, value): ...
    def __rmod__(self, value): ...
    def __pow__(self, value, modulo: Incomplete | None = ...): ...
    def __rpow__(self, value): ...
    def __floordiv__(self, value): ...
    def __rfloordiv__(self, value): ...
    def __truediv__(self, value): ...
    def __rtruediv__(self, value): ...
    def __divmod__(self, value): ...
    def __rdivmod__(self, value): ...
    __hash__: Incomplete
    def __int__(self) -> int: ...
    def __float__(self) -> float: ...
    def __abs__(self): ...
    def __index__(self) -> int: ...
    def __pos__(self): ...
    def __neg__(self): ...
    def __invert__(self): ...
    def __round__(self, n: int = ...): ...
    def __floor__(self): ...
    def __ceil__(self): ...
    def __trunc__(self): ...
    def __lt__(self, value): ...
    def __le__(self, value): ...
    def __eq__(self, value): ...
    def __ne__(self, value): ...
    def __gt__(self, value): ...
    def __ge__(self, value): ...
    def prettyIn(self, value): ...
    def prettyOut(self, value): ...
    def getNamedValues(self): ...

class Boolean(Integer):
    tagSet: Incomplete
    subtypeSpec: Incomplete
    namedValues: Incomplete
    typeId: Incomplete

SizedIntegerBase = int

class SizedInteger(SizedIntegerBase):
    bitLength: Incomplete
    leadingZeroBits: Incomplete
    def setBitLength(self, bitLength): ...
    def __len__(self) -> int: ...

class BitString(base.SimpleAsn1Type):
    tagSet: Incomplete
    subtypeSpec: Incomplete
    namedValues: Incomplete
    typeId: Incomplete
    defaultBinValue: Incomplete
    defaultHexValue: Incomplete
    def __init__(self, value=..., **kwargs) -> None: ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
    def __lt__(self, other): ...
    def __le__(self, other): ...
    def __gt__(self, other): ...
    def __ge__(self, other): ...
    def __len__(self) -> int: ...
    def __getitem__(self, i): ...
    def __iter__(self): ...
    def __reversed__(self): ...
    def __add__(self, value): ...
    def __radd__(self, value): ...
    def __mul__(self, value): ...
    def __rmul__(self, value): ...
    def __lshift__(self, count): ...
    def __rshift__(self, count): ...
    def __int__(self) -> int: ...
    def __float__(self) -> float: ...
    def asNumbers(self): ...
    def asOctets(self): ...
    def asInteger(self): ...
    def asBinary(self): ...
    @classmethod
    def fromHexString(cls, value, internalFormat: bool = ..., prepend: Incomplete | None = ...): ...
    @classmethod
    def fromBinaryString(cls, value, internalFormat: bool = ..., prepend: Incomplete | None = ...): ...
    @classmethod
    def fromOctetString(cls, value, internalFormat: bool = ..., prepend: Incomplete | None = ..., padding: int = ...): ...
    def prettyIn(self, value): ...

class OctetString(base.SimpleAsn1Type):
    tagSet: Incomplete
    subtypeSpec: Incomplete
    typeId: Incomplete
    defaultBinValue: Incomplete
    defaultHexValue: Incomplete
    encoding: str
    def __init__(self, value=..., **kwargs) -> None: ...
    def prettyIn(self, value): ...
    def __bytes__(self) -> bytes: ...
    def asOctets(self): ...
    def asNumbers(self): ...
    def prettyOut(self, value): ...
    def prettyPrint(self, scope: int = ...): ...
    @staticmethod
    def fromBinaryString(value): ...
    @staticmethod
    def fromHexString(value): ...
    def __len__(self) -> int: ...
    def __getitem__(self, i): ...
    def __iter__(self): ...
    def __contains__(self, value) -> bool: ...
    def __add__(self, value): ...
    def __radd__(self, value): ...
    def __mul__(self, value): ...
    def __rmul__(self, value): ...
    def __int__(self) -> int: ...
    def __float__(self) -> float: ...
    def __reversed__(self): ...

class Null(OctetString):
    tagSet: Incomplete
    subtypeSpec: Incomplete
    typeId: Incomplete
    def prettyIn(self, value): ...

class ObjectIdentifier(base.SimpleAsn1Type):
    tagSet: Incomplete
    subtypeSpec: Incomplete
    typeId: Incomplete
    def __add__(self, other): ...
    def __radd__(self, other): ...
    def asTuple(self): ...
    def __len__(self) -> int: ...
    def __getitem__(self, i): ...
    def __iter__(self): ...
    def __contains__(self, value) -> bool: ...
    def index(self, suboid): ...
    def isPrefixOf(self, other): ...
    def prettyIn(self, value): ...
    def prettyOut(self, value): ...

class Real(base.SimpleAsn1Type):
    binEncBase: Incomplete
    tagSet: Incomplete
    subtypeSpec: Incomplete
    typeId: Incomplete
    def prettyIn(self, value): ...
    def prettyPrint(self, scope: int = ...): ...
    @property
    def isPlusInf(self): ...
    @property
    def isMinusInf(self): ...
    @property
    def isInf(self): ...
    def __add__(self, value): ...
    def __radd__(self, value): ...
    def __mul__(self, value): ...
    def __rmul__(self, value): ...
    def __sub__(self, value): ...
    def __rsub__(self, value): ...
    def __mod__(self, value): ...
    def __rmod__(self, value): ...
    def __pow__(self, value, modulo: Incomplete | None = ...): ...
    def __rpow__(self, value): ...
    def __truediv__(self, value): ...
    def __rtruediv__(self, value): ...
    def __divmod__(self, value): ...
    def __rdivmod__(self, value): ...
    def __int__(self) -> int: ...
    def __float__(self) -> float: ...
    def __abs__(self): ...
    def __pos__(self): ...
    def __neg__(self): ...
    def __round__(self, n: int = ...): ...
    def __floor__(self): ...
    def __ceil__(self): ...
    def __trunc__(self): ...
    def __lt__(self, value): ...
    def __le__(self, value): ...
    def __eq__(self, value): ...
    def __ne__(self, value): ...
    def __gt__(self, value): ...
    def __ge__(self, value): ...
    def __bool__(self) -> bool: ...
    __hash__: Incomplete
    def __getitem__(self, idx): ...
    def isPlusInfinity(self): ...
    def isMinusInfinity(self): ...
    def isInfinity(self): ...

class Enumerated(Integer):
    tagSet: Incomplete
    subtypeSpec: Incomplete
    typeId: Incomplete
    namedValues: Incomplete

class SequenceOfAndSetOfBase(base.ConstructedAsn1Type):
    def __init__(self, *args, **kwargs) -> None: ...
    def __getitem__(self, idx): ...
    def __setitem__(self, idx, value) -> None: ...
    def append(self, value) -> None: ...
    def count(self, value): ...
    def extend(self, values) -> None: ...
    def index(self, value, start: int = ..., stop: Incomplete | None = ...): ...
    def reverse(self) -> None: ...
    def sort(self, key: Incomplete | None = ..., reverse: bool = ...) -> None: ...
    def __len__(self) -> int: ...
    def __iter__(self): ...
    def getComponentByPosition(self, idx, default=..., instantiate: bool = ...): ...
    def setComponentByPosition(
        self, idx, value=..., verifyConstraints: bool = ..., matchTags: bool = ..., matchConstraints: bool = ...
    ): ...
    @property
    def componentTagMap(self): ...
    @property
    def components(self): ...
    def clear(self): ...
    def reset(self): ...
    def prettyPrint(self, scope: int = ...): ...
    def prettyPrintType(self, scope: int = ...): ...
    @property
    def isValue(self): ...
    @property
    def isInconsistent(self): ...

class SequenceOf(SequenceOfAndSetOfBase):
    __doc__: Incomplete
    tagSet: Incomplete
    componentType: Incomplete
    subtypeSpec: Incomplete
    typeId: Incomplete

class SetOf(SequenceOfAndSetOfBase):
    __doc__: Incomplete
    tagSet: Incomplete
    componentType: Incomplete
    subtypeSpec: Incomplete
    typeId: Incomplete

class SequenceAndSetBase(base.ConstructedAsn1Type):
    componentType: Incomplete

    class DynamicNames:
        def __init__(self) -> None: ...
        def __len__(self) -> int: ...
        def __contains__(self, item) -> bool: ...
        def __iter__(self): ...
        def __getitem__(self, item): ...
        def getNameByPosition(self, idx): ...
        def getPositionByName(self, name): ...
        def addField(self, idx) -> None: ...

    def __init__(self, **kwargs) -> None: ...
    def __getitem__(self, idx): ...
    def __setitem__(self, idx, value) -> None: ...
    def __contains__(self, key) -> bool: ...
    def __len__(self) -> int: ...
    def __iter__(self): ...
    def values(self) -> Generator[Incomplete, None, None]: ...
    def keys(self): ...
    def items(self) -> Generator[Incomplete, None, None]: ...
    def update(self, *iterValue, **mappingValue) -> None: ...
    def clear(self): ...
    def reset(self): ...
    @property
    def components(self): ...
    def getComponentByName(self, name, default=..., instantiate: bool = ...): ...
    def setComponentByName(
        self, name, value=..., verifyConstraints: bool = ..., matchTags: bool = ..., matchConstraints: bool = ...
    ): ...
    def getComponentByPosition(self, idx, default=..., instantiate: bool = ...): ...
    def setComponentByPosition(
        self, idx, value=..., verifyConstraints: bool = ..., matchTags: bool = ..., matchConstraints: bool = ...
    ): ...
    @property
    def isValue(self): ...
    @property
    def isInconsistent(self): ...
    def prettyPrint(self, scope: int = ...): ...
    def prettyPrintType(self, scope: int = ...): ...
    def setDefaultComponents(self): ...
    def getComponentType(self): ...
    def getNameByPosition(self, idx): ...

class Sequence(SequenceAndSetBase):
    __doc__: Incomplete
    tagSet: Incomplete
    subtypeSpec: Incomplete
    componentType: Incomplete
    typeId: Incomplete
    def getComponentTagMapNearPosition(self, idx): ...
    def getComponentPositionNearType(self, tagSet, idx): ...

class Set(SequenceAndSetBase):
    __doc__: Incomplete
    tagSet: Incomplete
    componentType: Incomplete
    subtypeSpec: Incomplete
    typeId: Incomplete
    def getComponent(self, innerFlag: bool = ...): ...
    def getComponentByType(self, tagSet, default=..., instantiate: bool = ..., innerFlag: bool = ...): ...
    def setComponentByType(
        self,
        tagSet,
        value=...,
        verifyConstraints: bool = ...,
        matchTags: bool = ...,
        matchConstraints: bool = ...,
        innerFlag: bool = ...,
    ): ...
    @property
    def componentTagMap(self): ...

class Choice(Set):
    tagSet: Incomplete
    componentType: Incomplete
    subtypeSpec: Incomplete
    typeId: Incomplete
    def __eq__(self, other): ...
    def __ne__(self, other): ...
    def __lt__(self, other): ...
    def __le__(self, other): ...
    def __gt__(self, other): ...
    def __ge__(self, other): ...
    def __bool__(self) -> bool: ...
    def __len__(self) -> int: ...
    def __contains__(self, key) -> bool: ...
    def __iter__(self): ...
    def values(self) -> Generator[Incomplete, None, None]: ...
    def keys(self) -> Generator[Incomplete, None, None]: ...
    def items(self) -> Generator[Incomplete, None, None]: ...
    def checkConsistency(self) -> None: ...
    def getComponentByPosition(self, idx, default=..., instantiate: bool = ...): ...
    def setComponentByPosition(
        self, idx, value=..., verifyConstraints: bool = ..., matchTags: bool = ..., matchConstraints: bool = ...
    ): ...
    @property
    def effectiveTagSet(self): ...
    @property
    def tagMap(self): ...
    def getComponent(self, innerFlag: bool = ...): ...
    def getName(self, innerFlag: bool = ...): ...
    @property
    def isValue(self): ...
    def clear(self): ...
    def getMinTagSet(self): ...

class Any(OctetString):
    tagSet: Incomplete
    subtypeSpec: Incomplete
    typeId: Incomplete
    @property
    def tagMap(self): ...
