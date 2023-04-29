from _typeshed import Incomplete
from collections.abc import MutableMapping
from numbers import Rational
from types import TracebackType
from typing import Any, ClassVar
from typing_extensions import Literal

from ._imaging import _PixelAccessor
from .ImageFile import ImageFile

logger: Any
READ_LIBTIFF: bool
WRITE_LIBTIFF: bool
IFD_LEGACY_API: bool
II: bytes
MM: bytes
IMAGEWIDTH: int
IMAGELENGTH: int
BITSPERSAMPLE: int
COMPRESSION: int
PHOTOMETRIC_INTERPRETATION: int
FILLORDER: int
IMAGEDESCRIPTION: int
STRIPOFFSETS: int
SAMPLESPERPIXEL: int
ROWSPERSTRIP: int
STRIPBYTECOUNTS: int
X_RESOLUTION: int
Y_RESOLUTION: int
PLANAR_CONFIGURATION: int
RESOLUTION_UNIT: int
TRANSFERFUNCTION: int
SOFTWARE: int
DATE_TIME: int
ARTIST: int
PREDICTOR: int
COLORMAP: int
TILEOFFSETS: int
SUBIFD: int
EXTRASAMPLES: int
SAMPLEFORMAT: int
JPEGTABLES: int
REFERENCEBLACKWHITE: int
COPYRIGHT: int
IPTC_NAA_CHUNK: int
PHOTOSHOP_CHUNK: int
ICCPROFILE: int
EXIFIFD: int
XMP: int
JPEGQUALITY: int
IMAGEJ_META_DATA_BYTE_COUNTS: int
IMAGEJ_META_DATA: int
COMPRESSION_INFO: Any
COMPRESSION_INFO_REV: Any
OPEN_INFO: Any
PREFIXES: Any

class IFDRational(Rational):
    def __init__(self, value, denominator: int = 1) -> None: ...
    @property
    def numerator(a): ...
    @property
    def denominator(a): ...
    def limit_rational(self, max_denominator): ...
    def __hash__(self) -> int: ...
    def __eq__(self, other): ...
    __add__: Any
    __radd__: Any
    __sub__: Any
    __rsub__: Any
    __mul__: Any
    __rmul__: Any
    __truediv__: Any
    __rtruediv__: Any
    __floordiv__: Any
    __rfloordiv__: Any
    __mod__: Any
    __rmod__: Any
    __pow__: Any
    __rpow__: Any
    __pos__: Any
    __neg__: Any
    __abs__: Any
    __trunc__: Any
    __lt__: Any
    __gt__: Any
    __le__: Any
    __ge__: Any
    __bool__: Any
    __ceil__: Any
    __floor__: Any
    __round__: Any

class ImageFileDirectory_v2(MutableMapping[int, Any]):
    group: int | None
    tagtype: dict[int, int]
    def __init__(
        self, ifh: bytes = b"II*\x00\x00\x00\x00\x00", prefix: bytes | None = None, group: int | None = None
    ) -> None: ...
    @property
    def prefix(self) -> bytes: ...
    @property
    def offset(self) -> int | None: ...
    @property
    def legacy_api(self) -> bool: ...
    def reset(self) -> None: ...
    def named(self): ...
    def __len__(self) -> int: ...
    def __getitem__(self, tag): ...
    def __contains__(self, tag): ...
    def __setitem__(self, tag, value) -> None: ...
    def __delitem__(self, tag) -> None: ...
    def __iter__(self): ...
    def load_byte(self, data, legacy_api: bool = True): ...
    def write_byte(self, data): ...
    def load_string(self, data, legacy_api: bool = True): ...
    def write_string(self, value: int | str | bytes) -> bytes: ...
    def load_rational(self, data, legacy_api: bool = True): ...
    def write_rational(self, *values): ...
    def load_undefined(self, data, legacy_api: bool = True): ...
    def write_undefined(self, value): ...
    def load_signed_rational(self, data, legacy_api: bool = True): ...
    def write_signed_rational(self, *values): ...
    def load(self, fp) -> None: ...
    def tobytes(self, offset: int = 0): ...
    def save(self, fp): ...

class ImageFileDirectory_v1(ImageFileDirectory_v2):
    def __init__(self, *args, **kwargs) -> None: ...
    @property
    def tags(self): ...
    @property
    def tagdata(self): ...
    tagtype: dict[int, int]
    @classmethod
    def from_v2(cls, original): ...
    def to_v2(self): ...
    def __contains__(self, tag): ...
    def __len__(self) -> int: ...
    def __iter__(self): ...
    def __setitem__(self, tag, value) -> None: ...
    def __getitem__(self, tag): ...

ImageFileDirectory = ImageFileDirectory_v1

class TiffImageFile(ImageFile):
    format: ClassVar[Literal["TIFF", "MIC"]]
    format_description: ClassVar[str]
    tag_v2: Any
    tag: Any
    def __init__(self, fp: Incomplete | None = None, filename: Incomplete | None = None) -> None: ...
    @property
    def n_frames(self): ...
    im: Any
    def seek(self, frame) -> None: ...
    def tell(self): ...
    def load(self) -> _PixelAccessor: ...
    def load_end(self) -> None: ...

SAVE_INFO: Any

class AppendingTiffWriter:
    fieldSizes: Any
    Tags: Any
    f: Any
    close_fp: bool
    name: Any
    beginning: Any
    def __init__(self, fn, new: bool = False) -> None: ...
    whereToWriteNewIFDOffset: Any
    offsetOfNewPage: int
    IIMM: Any
    isFirst: bool
    def setup(self) -> None: ...
    def finalize(self) -> None: ...
    def newFrame(self) -> None: ...
    def __enter__(self): ...
    def __exit__(
        self, exc_type: type[BaseException] | None, exc_value: BaseException | None, traceback: TracebackType | None
    ) -> Literal[False]: ...
    def tell(self): ...
    def seek(self, offset, whence=0): ...
    def goToEnd(self) -> None: ...
    endian: Any
    longFmt: Any
    shortFmt: Any
    tagFormat: Any
    def setEndian(self, endian) -> None: ...
    def skipIFDs(self) -> None: ...
    def write(self, data): ...
    def readShort(self): ...
    def readLong(self): ...
    def rewriteLastShortToLong(self, value) -> None: ...
    def rewriteLastShort(self, value) -> None: ...
    def rewriteLastLong(self, value) -> None: ...
    def writeShort(self, value) -> None: ...
    def writeLong(self, value) -> None: ...
    def close(self) -> None: ...
    def fixIFD(self) -> None: ...
    def fixOffsets(self, count, isShort: bool = False, isLong: bool = False) -> None: ...
