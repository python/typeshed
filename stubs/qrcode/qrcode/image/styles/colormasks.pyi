from _typeshed import Incomplete, StrOrBytesPath
from typing import IO, Any

from PIL import Image

from ..._types import Ink
from ..styledpil import StyledPilImage

class QRColorMask:
    back_color: Ink
    has_transparency: bool
    paint_color: Ink
    def initialize(self, styledPilImage: StyledPilImage, image: Any) -> None: ...
    def apply_mask(self, image: Image.Image) -> None: ...
    def get_fg_pixel(self, image: Image.Image, x: int, y: int) -> Ink: ...
    def get_bg_pixel(self, image: Image.Image, x: int, y: int) -> Ink: ...
    def interp_num(self, n1: int, n2: int, norm: float) -> int: ...
    def interp_color(self, col1: Ink, col2: Ink, norm: float) -> Ink: ...
    def extrap_num(self, n1: int, n2: int, interped_num: int) -> float | None: ...
    def extrap_color(self, col1: Ink, col2: Ink, interped_color: Ink) -> float | None: ...

class SolidFillColorMask(QRColorMask):
    front_color: Ink
    def __init__(self, back_color: Ink = (255, 255, 255), front_color: Ink = (0, 0, 0)) -> None: ...

class RadialGradiantColorMask(QRColorMask):
    center_color: Ink
    edge_color: Ink
    def __init__(
        self, back_color: Ink = (255, 255, 255), center_color: Ink = (0, 0, 0), edge_color: Ink = (0, 0, 255)
    ) -> None: ...

class SquareGradiantColorMask(QRColorMask):
    center_color: Ink
    edge_color: Ink
    def __init__(
        self, back_color: Ink = (255, 255, 255), center_color: Ink = (0, 0, 0), edge_color: Ink = (0, 0, 255)
    ) -> None: ...

class HorizontalGradiantColorMask(QRColorMask):
    left_color: Ink
    right_color: Ink
    def __init__(
        self, back_color: Ink = (255, 255, 255), left_color: Ink = (0, 0, 0), right_color: Ink = (0, 0, 255)
    ) -> None: ...

class VerticalGradiantColorMask(QRColorMask):
    top_color: Incomplete
    bottom_color: Incomplete
    def __init__(
        self, back_color: Ink = (255, 255, 255), top_color: Ink = (0, 0, 0), bottom_color: Ink = (0, 0, 255)
    ) -> None: ...

class ImageColorMask(QRColorMask):
    color_img: Incomplete
    def __init__(
        self,
        back_color: Ink = (255, 255, 255),
        color_mask_path: StrOrBytesPath | IO[bytes] | None = None,
        color_mask_image: Image.Image | None = None,
    ) -> None: ...
    paint_color: Ink
