from _typeshed import Incomplete
from collections.abc import Generator

import qrcode.image.base

class PyPNGImage(qrcode.image.base.BaseImage):
    kind: str
    allowed_kinds: Incomplete
    needs_drawrect: bool
    def new_image(self, **kwargs): ...
    def drawrect(self, row, col) -> None: ...
    def save(self, stream, kind: Incomplete | None = None) -> None: ...
    def rows_iter(self) -> Generator[Incomplete, Incomplete, None]: ...
    def border_rows_iter(self) -> Generator[Incomplete, None, None]: ...

PymagingImage = PyPNGImage
