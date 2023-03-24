from collections.abc import Sequence
from re import Pattern
from typing_extensions import Final

from Xlib._typing import ErrorHandler
from Xlib.protocol import request, rq
from Xlib.xobject import resource

rgb_res: Final[list[Pattern[str]]]

class Colormap(resource.Resource):
    __colormap__ = resource.Resource.__resource__
    def free(self, onerror: ErrorHandler[object] | None = None) -> None: ...
    def copy_colormap_and_free(self, scr_cmap: int) -> Colormap: ...
    def install_colormap(self, onerror: ErrorHandler[object] | None = None) -> None: ...
    def uninstall_colormap(self, onerror: ErrorHandler[object] | None = None) -> None: ...
    def alloc_color(self, red: int, green: int, blue: int) -> request.AllocColor: ...
    def alloc_named_color(self, name: str) -> request.AllocColor | request.AllocNamedColor | None: ...
    def alloc_color_cells(self, contiguous: bool, colors: int, planes: int) -> request.AllocColorCells: ...
    def alloc_color_planes(self, contiguous: bool, colors: int, red: int, green: int, blue: int) -> request.AllocColorPlanes: ...
    def free_colors(self, pixels: Sequence[int], plane_mask: int, onerror: ErrorHandler[object] | None = None) -> None: ...
    def store_colors(self, items: dict[str, int], onerror: ErrorHandler[object] | None = None) -> None: ...
    def store_named_color(self, name: str, pixel: int, flags: int, onerror: ErrorHandler[object] | None = None) -> None: ...
    def query_colors(self, pixels: Sequence[int]) -> rq.Struct: ...
    def lookup_color(self, name: str) -> request.LookupColor: ...
