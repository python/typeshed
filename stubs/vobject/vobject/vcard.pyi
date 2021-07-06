from typing import Any

from . import behavior as behavior
from .base import (
    ContentLine as ContentLine,
    backslashEscape as backslashEscape,
    registerBehavior as registerBehavior,
    str_ as str_,
)
from .icalendar import stringToTextValues as stringToTextValues

basestring = basestring

class Name:
    family: Any
    given: Any
    additional: Any
    prefix: Any
    suffix: Any
    def __init__(
        self, family: str = ..., given: str = ..., additional: str = ..., prefix: str = ..., suffix: str = ...
    ) -> None: ...
    @staticmethod
    def toString(val): ...
    def __eq__(self, other): ...

class Address:
    box: Any
    extended: Any
    street: Any
    city: Any
    region: Any
    code: Any
    country: Any
    def __init__(
        self,
        street: str = ...,
        city: str = ...,
        region: str = ...,
        code: str = ...,
        country: str = ...,
        box: str = ...,
        extended: str = ...,
    ) -> None: ...
    @staticmethod
    def toString(val, join_char: str = ...): ...
    lines: Any
    one_line: Any
    def __eq__(self, other): ...

class VCardTextBehavior(behavior.Behavior):
    allowGroup: bool
    base64string: str
    @classmethod
    def decode(cls, line) -> None: ...
    @classmethod
    def encode(cls, line) -> None: ...

class VCardBehavior(behavior.Behavior):
    allowGroup: bool
    defaultBehavior: Any

class VCard3_0(VCardBehavior):
    name: str
    description: str
    versionString: str
    isComponent: bool
    sortFirst: Any
    knownChildren: Any
    @classmethod
    def generateImplicitParameters(cls, obj) -> None: ...

class FN(VCardTextBehavior):
    name: str
    description: str

class Label(VCardTextBehavior):
    name: str
    description: str

wacky_apple_photo_serialize: bool
REALLY_LARGE: float

class Photo(VCardTextBehavior):
    name: str
    description: str
    @classmethod
    def valueRepr(cls, line): ...
    @classmethod
    def serialize(cls, obj, buf, lineLength, validate) -> None: ...

def toListOrString(string): ...
def splitFields(string): ...
def toList(stringOrList): ...
def serializeFields(obj, order: Any | None = ...): ...

NAME_ORDER: Any
ADDRESS_ORDER: Any

class NameBehavior(VCardBehavior):
    hasNative: bool
    @staticmethod
    def transformToNative(obj): ...
    @staticmethod
    def transformFromNative(obj): ...

class AddressBehavior(VCardBehavior):
    hasNative: bool
    @staticmethod
    def transformToNative(obj): ...
    @staticmethod
    def transformFromNative(obj): ...

class OrgBehavior(VCardBehavior):
    hasNative: bool
    @staticmethod
    def transformToNative(obj): ...
    @staticmethod
    def transformFromNative(obj): ...
