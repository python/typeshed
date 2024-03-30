from collections.abc import Callable
from typing import Any, Final
from typing_extensions import TypeAlias

from Xlib._typing import ErrorHandler, Unused
from Xlib.display import Display
from Xlib.protocol import rq
from Xlib.xobject import drawable, resource

_Update: TypeAlias = Callable[[rq.DictWrapper | dict[str, Any]], object]

extname: Final = "Composite"
RedirectAutomatic: Final = 0
RedirectManual: Final = 1

class QueryVersion(rq.ReplyRequest): ...

def query_version(self: Display | resource.Resource) -> QueryVersion: ...

class RedirectWindow(rq.Request): ...

def redirect_window(self: drawable.Window, update: _Update, onerror: ErrorHandler[object] | None = None) -> None: ...

class RedirectSubwindows(rq.Request): ...

def redirect_subwindows(self: drawable.Window, update: _Update, onerror: ErrorHandler[object] | None = None) -> None: ...

class UnredirectWindow(rq.Request): ...

def unredirect_window(self: drawable.Window, update: _Update, onerror: ErrorHandler[object] | None = None) -> None: ...

class UnredirectSubindows(rq.Request): ...

def unredirect_subwindows(self: drawable.Window, update: _Update, onerror: ErrorHandler[object] | None = None) -> None: ...

class CreateRegionFromBorderClip(rq.Request): ...

def create_region_from_border_clip(self: drawable.Window, onerror: ErrorHandler[object] | None = None) -> int: ...

class NameWindowPixmap(rq.Request): ...

def name_window_pixmap(self: Display | resource.Resource, onerror: ErrorHandler[object] | None = None) -> drawable.Pixmap: ...

class GetOverlayWindow(rq.ReplyRequest): ...

def get_overlay_window(self: Display) -> GetOverlayWindow: ...
def init(disp: Display, info: Unused) -> None: ...
