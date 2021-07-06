from typing import Any

from . import base as base

class Behavior:
    name: str
    description: str
    versionString: str
    knownChildren: Any
    quotedPrintable: bool
    defaultBehavior: Any
    hasNative: bool
    isComponent: bool
    allowGroup: bool
    forceUTC: bool
    sortFirst: Any
    def __init__(self) -> None: ...
    @classmethod
    def validate(cls, obj, raiseException: bool = ..., complainUnrecognized: bool = ...): ...
    @classmethod
    def lineValidate(cls, line, raiseException, complainUnrecognized): ...
    @classmethod
    def decode(cls, line) -> None: ...
    @classmethod
    def encode(cls, line) -> None: ...
    @classmethod
    def transformToNative(cls, obj): ...
    @classmethod
    def transformFromNative(cls, obj) -> None: ...
    @classmethod
    def generateImplicitParameters(cls, obj) -> None: ...
    @classmethod
    def serialize(cls, obj, buf, lineLength, validate: bool = ...): ...
    @classmethod
    def valueRepr(cls, line): ...
