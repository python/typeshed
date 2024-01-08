from _typeshed import Incomplete

from .core import AdaptationError, Adapter
from .lib.py3compat import decodebytes as decodebytes

class BitIntegerError(AdaptationError): ...
class MappingError(AdaptationError): ...
class ConstError(AdaptationError): ...
class ValidationError(AdaptationError): ...
class PaddingError(AdaptationError): ...

class BitIntegerAdapter(Adapter):
    width: Incomplete
    swapped: Incomplete
    signed: Incomplete
    bytesize: Incomplete
    def __init__(self, subcon, width, swapped: bool = False, signed: bool = False, bytesize: int = 8) -> None: ...

class MappingAdapter(Adapter):
    decoding: Incomplete
    encoding: Incomplete
    decdefault: Incomplete
    encdefault: Incomplete
    def __init__(self, subcon, decoding, encoding, decdefault=..., encdefault=...) -> None: ...

class FlagsAdapter(Adapter):
    flags: Incomplete
    def __init__(self, subcon, flags) -> None: ...

class StringAdapter(Adapter):
    encoding: Incomplete
    def __init__(self, subcon, encoding: Incomplete | None = None) -> None: ...

class PaddedStringAdapter(Adapter):
    padchar: Incomplete
    paddir: Incomplete
    trimdir: Incomplete
    def __init__(self, subcon, padchar: bytes = b"\x00", paddir: str = "right", trimdir: str = "right") -> None: ...

class LengthValueAdapter(Adapter): ...

class CStringAdapter(StringAdapter):
    terminators: Incomplete
    def __init__(self, subcon, terminators: bytes = b"\x00", encoding: Incomplete | None = None) -> None: ...

class TunnelAdapter(Adapter):
    inner_subcon: Incomplete
    def __init__(self, subcon, inner_subcon) -> None: ...

class ExprAdapter(Adapter):
    def __init__(self, subcon, encoder, decoder) -> None: ...

class HexDumpAdapter(Adapter):
    linesize: Incomplete
    def __init__(self, subcon, linesize: int = 16) -> None: ...

class ConstAdapter(Adapter):
    value: Incomplete
    def __init__(self, subcon, value) -> None: ...

class SlicingAdapter(Adapter):
    start: Incomplete
    stop: Incomplete
    def __init__(self, subcon, start, stop: Incomplete | None = None) -> None: ...

class IndexingAdapter(Adapter):
    index: Incomplete
    def __init__(self, subcon, index) -> None: ...

class PaddingAdapter(Adapter):
    pattern: Incomplete
    strict: Incomplete
    def __init__(self, subcon, pattern: bytes = b"\x00", strict: bool = False) -> None: ...

class Validator(Adapter): ...

class OneOf(Validator):
    valids: Incomplete
    def __init__(self, subcon, valids) -> None: ...

class NoneOf(Validator):
    invalids: Incomplete
    def __init__(self, subcon, invalids) -> None: ...
