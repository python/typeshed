from _typeshed import SupportsRead, SupportsWrite
from collections.abc import Iterable, Iterator, MutableMapping
from pathlib import Path
from typing import Any, Callable, Dict, Protocol, Sequence, SupportsBytes, Tuple, Union
from typing_extensions import Literal

from ._imaging import (
    DEFAULT_STRATEGY as DEFAULT_STRATEGY,
    FILTERED as FILTERED,
    FIXED as FIXED,
    HUFFMAN_ONLY as HUFFMAN_ONLY,
    RLE as RLE,
)
from .ImageFilter import Filter
from .ImagePalette import ImagePalette

_Mode = Literal["1", "CMYK", "F", "HSV", "I", "L", "LAB", "P", "RGB", "RGBA", "RGBX", "YCbCr"]
_Resample = Literal[0, 1, 2, 3, 4, 5]
_Size = Tuple[int, int]
_Box = Tuple[int, int, int, int]

_ConversionMatrix = Union[
    Tuple[float, float, float, float], Tuple[float, float, float, float, float, float, float, float, float, float, float, float],
]
_Color = Union[float, Tuple[float, ...]]

class _Writeable(SupportsWrite[bytes], Protocol):
    def seek(self, __offset: int) -> Any: ...

# obsolete
NORMAL: Literal[0]
SEQUENCE: Literal[1]
CONTAINER: Literal[2]

class DecompressionBombWarning(RuntimeWarning): ...
class DecompressionBombError(Exception): ...

MAX_IMAGE_PIXELS: int

NONE: Literal[0]

FLIP_LEFT_RIGHT: Literal[0]
FLIP_TOP_BOTTOM: Literal[1]
ROTATE_90: Literal[2]
ROTATE_180: Literal[3]
ROTATE_270: Literal[4]
TRANSPOSE: Literal[5]
TRANSVERSE: Literal[6]

AFFINE: Literal[0]
EXTENT: Literal[1]
PERSPECTIVE: Literal[2]
QUAD: Literal[3]
MESH: Literal[4]

NEAREST: Literal[0]
BOX: Literal[4]
BILINEAR: Literal[2]
LINEAR: Literal[2]
HAMMING: Literal[5]
BICUBIC: Literal[3]
CUBIC: Literal[3]
LANCZOS: Literal[1]
ANTIALIAS: Literal[1]

ORDERED: Literal[1]
RASTERIZE: Literal[2]
FLOYDSTEINBERG: Literal[3]

WEB: Literal[0]
ADAPTIVE: Literal[1]

MEDIANCUT: Literal[0]
MAXCOVERAGE: Literal[1]
FASTOCTREE: Literal[2]
LIBIMAGEQUANT: Literal[3]

ID: list[str]
OPEN: dict[str, Any]
MIME: dict[str, str]
SAVE: dict[str, Any]
SAVE_ALL: dict[str, Any]
EXTENSION: dict[str, str]
DECODERS: dict[str, Any]
ENCODERS: dict[str, Any]

MODES: list[_Mode]

def getmodebase(mode: _Mode) -> Literal["L", "RGB"]: ...
def getmodetype(mode: _Mode) -> Literal["L", "I", "F"]: ...
def getmodebandnames(mode: _Mode) -> Tuple[str, ...]: ...
def getmodebands(mode: _Mode) -> int: ...
def preinit() -> None: ...
def init() -> None: ...
def coerce_e(value) -> _E: ...

class _E:
    def __init__(self, data) -> None: ...
    def __add__(self, other) -> _E: ...
    def __mul__(self, other) -> _E: ...

_ImageState = Tuple[Dict[str, Any], str, Tuple[int, int], Any, bytes]

class Image:
    format: Any
    format_description: Any
    im: Any
    mode: str
    palette: Any
    info: dict[Any, Any]
    readonly: int
    pyaccess: Any
    @property
    def width(self) -> int: ...
    @property
    def height(self) -> int: ...
    @property
    def size(self) -> tuple[int, int]: ...
    def __enter__(self) -> Image: ...
    def __exit__(self, *args: Any) -> None: ...
    def close(self) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    def __array__(self) -> Any: ...  # returns numpy.array()
    def __getstate__(self) -> _ImageState: ...
    def __setstate__(self, state: _ImageState) -> None: ...
    def tobytes(self, encoder_name: str = ..., *args) -> bytes: ...
    def tobitmap(self, name: str = ...) -> bytes: ...
    def frombytes(self, data: bytes, decoder_name: str = ..., *args) -> None: ...
    def load(self) -> None: ...
    def verify(self) -> None: ...
    def convert(
        self,
        mode: str | None = ...,
        matrix: _ConversionMatrix | None = ...,
        dither: int | None = ...,
        palette: Literal[0, 1] = ...,
        colors: int = ...,
    ) -> Image: ...
    def quantize(
        self,
        colors: int = ...,
        method: Literal[0, 1, 2, 3] | None = ...,
        kmeans: int = ...,
        palette: Image | None = ...,
        dither: int = ...,
    ) -> Image: ...
    def copy(self) -> Image: ...
    __copy__ = copy
    def crop(self, box: _Box | None = ...) -> Image: ...
    def draft(self, mode: str, size: _Size) -> None: ...
    def filter(self, filter: Filter | Callable[[], Filter]) -> Image: ...
    def getbands(self) -> Tuple[str, ...]: ...
    def getbbox(self) -> tuple[int, int, int, int] | None: ...
    def getcolors(self, maxcolors: int = ...) -> list[tuple[int, int]]: ...
    def getdata(self, band: int | None = ...): ...
    def getextrema(self): ...
    def getexif(self) -> Exif: ...
    def getim(self): ...
    def getpalette(self) -> list[int] | None: ...
    def getpixel(self, xy: tuple[int, int]): ...
    def getprojection(self) -> tuple[list[int], list[int]]: ...
    def histogram(self, mask: Image | None = ..., extrema: tuple[int, int] | tuple[float, float] | None = ...) -> list[int]: ...
    def entropy(self, mask: Image | None = ..., extrema: tuple[int, int] | tuple[float, float] | None = ...) -> float: ...
    def paste(self, im: Image, box: tuple[float, float] | _Box | None = ..., mask: Image | None = ...) -> None: ...
    def alpha_composite(self, im: Image, dest: tuple[int, int] = ..., source: tuple[int, int] = ...) -> None: ...
    def point(self, lut, mode: str | None = ...) -> Image: ...
    def putalpha(self, alpha: Image | int) -> None: ...
    def putdata(self, data: Sequence[int], scale: float = ..., offset: float = ...) -> None: ...
    def putpalette(self, data: ImagePalette | bytes | Iterable[int] | SupportsBytes, rawmode: str | None = ...) -> None: ...
    def putpixel(self, xy: tuple[int, int], value: _Color | list[float]) -> None: ...
    def remap_palette(self, dest_map: Iterable[int], source_palette: Sequence[int] | None = ...) -> Image: ...
    def resize(
        self,
        size: tuple[int, int],
        resample: _Resample | None = ...,
        box: tuple[float, float, float, float] | None = ...,
        reducing_gap: float | None = ...,
    ) -> Image: ...
    def reduce(self, factor: int | tuple[int, int] | list[int], box: _Box | None = ...) -> None: ...
    def rotate(
        self,
        angle: float,
        resample: _Resample = ...,
        expand: bool = ...,
        center: tuple[float, float] | None = ...,
        translate: tuple[float, float] | None = ...,
        fillcolor: _Color | None = ...,
    ) -> Image: ...
    def save(
        self,
        fp: str | bytes | Path | _Writeable,
        format: str | None = ...,
        *,
        save_all: bool = ...,
        bitmap_format: Literal["bmp", "png"] = ...,  # for ICO files
        **params: Any,
    ) -> None: ...
    def seek(self, frame: int) -> None: ...
    def show(self, title: str | None = ..., command: str | None = ...) -> None: ...
    def split(self) -> Tuple[Image, ...]: ...
    def getchannel(self, channel: int | str) -> Image: ...
    def tell(self) -> int: ...
    def thumbnail(self, size: tuple[int, int], resample: _Resample = ..., reducing_gap: float = ...) -> None: ...
    def transform(
        self,
        size: _Size,
        method: Literal[0, 1, 2, 3, 4],
        data=...,
        resample: _Resample = ...,
        fill: int = ...,
        fillcolor: _Color | int | None = ...,
    ) -> None: ...
    def transpose(self, method: Literal[0, 1, 2, 3, 4, 5, 6]) -> Image: ...
    def effect_spread(self, distance: int) -> Image: ...
    def toqimage(self): ...
    def toqpixmap(self): ...

class ImagePointHandler: ...
class ImageTransformHandler: ...

def new(mode: _Mode, size: tuple[int, int], color: float | Tuple[float, ...] = ...) -> Image: ...
def frombytes(mode: _Mode, size: tuple[int, int], data, decoder_name: str = ..., *args) -> Image: ...
def frombuffer(mode: _Mode, size: tuple[int, int], data, decoder_name: str = ..., *args) -> Image: ...
def fromarray(obj, mode: _Mode | None = ...) -> Image: ...
def fromqimage(im) -> Image: ...
def fromqpixmap(im) -> Image: ...
def open(
    fp: str | bytes | Path | SupportsRead[bytes], mode: Literal["r"] = ..., formats: list[str] | tuple[str] | None = ...
) -> Image: ...
def alpha_composite(im1: Image, im2: Image) -> Image: ...
def blend(im1: Image, im2: Image, alpha: float) -> Image: ...
def composite(image1: Image, image2: Image, mask: Image) -> Image: ...
def eval(image: Image, *args) -> Image: ...
def merge(mode: str, bands: Sequence[Image]) -> Image: ...
def register_open(id: str, factory, accept=...) -> None: ...
def register_mime(id: str, mimetype: str) -> None: ...
def register_save(id: str, driver) -> None: ...
def register_save_all(id: str, driver) -> None: ...
def register_extension(id: str, extension: str) -> None: ...
def register_extensions(id: str, extensions: Iterable[str]) -> None: ...
def registered_extensions() -> dict[str, str]: ...
def register_decoder(name: str, decoder) -> None: ...
def register_encoder(name: str, encoder) -> None: ...
def effect_mandelbrot(size: tuple[int, int], extent: tuple[float, float, float, float], quality: int) -> Image: ...
def effect_noise(size: tuple[int, int], sigma: float) -> Image: ...
def linear_gradient(mode: str) -> Image: ...
def radial_gradient(mode: str) -> Image: ...

class Exif(MutableMapping[int, Any]):
    def load(self, data: bytes) -> None: ...
    def tobytes(self, offset: int = ...) -> bytes: ...
    def get_ifd(self, tag: int): ...
    def __len__(self) -> int: ...
    def __getitem__(self, tag: int) -> Any: ...
    def __contains__(self, tag: object) -> bool: ...
    def __setitem__(self, tag: int, value: Any) -> None: ...
    def __delitem__(self, tag: int) -> None: ...
    def __iter__(self) -> Iterator[int]: ...
