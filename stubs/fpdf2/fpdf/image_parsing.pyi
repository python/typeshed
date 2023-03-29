from _typeshed import Incomplete, Unused
from logging import Logger
from typing import Any
from typing_extensions import Literal, TypeAlias

from PIL import Image

_ImageFilter: TypeAlias = Literal["AUTO", "FlateDecode", "DCTDecode", "JPXDecode"]

RESAMPLE: Image.Resampling
LOGGER: Logger
SUPPORTED_IMAGE_FILTERS: tuple[_ImageFilter, ...]
TIFFBitRevTable: list[int]

def load_image(filename): ...
def is_iccp_valid(iccp, filename) -> bool: ...

# Returned dict could be typed as a TypedDict.
def get_img_info(
    filename, img: Incomplete | None = None, image_filter: _ImageFilter = "AUTO", dims: Incomplete | None = None
) -> dict[str, Any]: ...

class temp_attr:
    obj: Any
    field: str
    value: Any
    exists: bool  # defined after __enter__ is called
    def __init__(self, obj: Any, field: str, value: Any) -> None: ...
    def __enter__(self) -> None: ...
    def __exit__(self, exctype: Unused, excinst: Unused, exctb: Unused) -> None: ...

def ccitt_payload_location_from_pil(img: Image.Image) -> tuple[int, int]: ...
def transcode_monochrome(img: Image.Image): ...
