from typing import IO, Any, Literal

from PIL import Image

from . import base

class PilImage(base.BaseImage):
    kind: Literal["PNG"]
    fill_color: str
    def new_image(self, *, back_color: str = "white", fill_color: str = "black", **kwargs: Any) -> Image.Image: ...
    def get_image(self, **kwargs: Any) -> Image.Image: ...
    def drawrect(self, row: int, col: int) -> None: ...
    def save(self, stream: IO[bytes], format: str | None = None, *, kind: str | None = None, **kwargs: Any) -> None: ...  # type: ignore[override]
    def __getattr__(self, name: str) -> Any: ...
