from _typeshed import Unused
from abc import abstractmethod
from typing import TypeAlias

from pyasn1.type.base import Asn1Type
from pyasn1.type.tag import Tag, TagSet

__all__ = ["Encoder", "encode"]

_EncodedValue: TypeAlias = tuple[bytes | tuple[int, ...], bool, bool]

class AbstractItemEncoder:
    supportIndefLenMode: bool
    eooIntegerSubstrate: tuple[int, int]
    eooOctetsSubstrate: bytes
    def encodeTag(self, singleTag: Tag, isConstructed: bool) -> tuple[int, ...]: ...
    def encodeLength(self, length: int, defMode: bool) -> tuple[int, ...]: ...
    @abstractmethod
    def encodeValue(self, value, asn1Spec, encodeFun, **options) -> _EncodedValue: ...
    def encode(self, value, asn1Spec=None, encodeFun=None, **options) -> bytes: ...

class EndOfOctetsEncoder(AbstractItemEncoder):
    def encodeValue(self, value, asn1Spec, encodeFun, **options) -> _EncodedValue: ...

class BooleanEncoder(AbstractItemEncoder):
    supportIndefLenMode: bool
    def encodeValue(self, value, asn1Spec, encodeFun, **options) -> _EncodedValue: ...

class IntegerEncoder(AbstractItemEncoder):
    supportIndefLenMode: bool
    supportCompactZero: bool
    def encodeValue(self, value, asn1Spec, encodeFun, **options) -> _EncodedValue: ...

class BitStringEncoder(AbstractItemEncoder):
    def encodeValue(self, value, asn1Spec, encodeFun, **options) -> _EncodedValue: ...

class OctetStringEncoder(AbstractItemEncoder):
    def encodeValue(self, value, asn1Spec, encodeFun, **options) -> _EncodedValue: ...

class NullEncoder(AbstractItemEncoder):
    supportIndefLenMode: bool
    def encodeValue(self, value, asn1Spec, encodeFun, **options) -> _EncodedValue: ...

class ObjectIdentifierEncoder(AbstractItemEncoder):
    supportIndefLenMode: bool
    def encodeValue(self, value, asn1Spec, encodeFun, **options) -> _EncodedValue: ...

class RelativeOIDEncoder(AbstractItemEncoder):
    supportIndefLenMode: bool
    def encodeValue(self, value, asn1Spec, encodeFun, **options) -> _EncodedValue: ...

class RealEncoder(AbstractItemEncoder):
    supportIndefLenMode: bool
    binEncBase: int
    def encodeValue(self, value, asn1Spec, encodeFun, **options) -> _EncodedValue: ...

class SequenceEncoder(AbstractItemEncoder):
    omitEmptyOptionals: bool
    def encodeValue(self, value, asn1Spec, encodeFun, **options) -> _EncodedValue: ...

class SequenceOfEncoder(AbstractItemEncoder):
    def encodeValue(self, value, asn1Spec, encodeFun, **options) -> _EncodedValue: ...

class ChoiceEncoder(AbstractItemEncoder):
    def encodeValue(self, value, asn1Spec, encodeFun, **options) -> _EncodedValue: ...

class AnyEncoder(OctetStringEncoder):
    def encodeValue(self, value, asn1Spec, encodeFun, **options) -> _EncodedValue: ...

TAG_MAP: dict[TagSet, AbstractItemEncoder]
TYPE_MAP: dict[int, AbstractItemEncoder]
# deprecated aliases
tagMap = TAG_MAP
typeMap = TYPE_MAP

class SingleItemEncoder:
    fixedDefLengthMode: bool | None
    fixedChunkSize: int | None
    TAG_MAP: dict[TagSet, AbstractItemEncoder]
    TYPE_MAP: dict[int, AbstractItemEncoder]

    def __init__(self, tagMap=..., typeMap=..., **ignored: Unused) -> None: ...
    def __call__(self, value, asn1Spec: Asn1Type | None = None, **options) -> bytes: ...

class Encoder:
    SINGLE_ITEM_ENCODER: type[SingleItemEncoder]
    def __init__(self, tagMap=..., typeMap=..., **options: Unused) -> None: ...
    def __call__(self, pyObject, asn1Spec: Asn1Type | None = None, **options) -> bytes: ...

encode: Encoder
