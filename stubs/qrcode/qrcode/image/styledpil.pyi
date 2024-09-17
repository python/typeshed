from _typeshed import StrOrBytesPath
from typing import IO, Any, Literal

from PIL import Image

from .._types import Ink
from . import base
from .styles.colormasks import QRColorMask
from .styles.moduledrawers import SquareModuleDrawer
from .styles.moduledrawers.base import QRModuleDrawer

class StyledPilImage(base.BaseImageWithDrawer):
    kind: Literal["PNG"]
    color_mask: QRColorMask
    default_drawer_class: type[SquareModuleDrawer]
    embeded_image: Image.Image
    embeded_image_resample: Image.Resampling
    paint_color: Ink
    def __init__(
        self,
        border: int,
        width: int,
        box_size: int,
        *args: Any,
        module_drawer: QRModuleDrawer | str | None = None,
        eye_drawer: QRModuleDrawer | str | None = None,
        color_mask: QRColorMask = ...,
        embeded_image_path: StrOrBytesPath | IO[bytes] | None = None,
        embeded_image: Image.Image | None = None,
        embeded_image_resample: Image.Resampling = ...,
        **kwargs: Any,
    ) -> None: ...
    def new_image(self, **kwargs: Any) -> Image.Image: ...
    def draw_embeded_image(self) -> None: ...
    def save(self, stream: IO[bytes], format: str | None = None, *, kind: str | None = None, **kwargs: Any) -> None: ...  # type: ignore[override]
    def __getattr__(self, name: str) -> Any: ...
