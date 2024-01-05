from typing import Final

from Xlib._typing import Unused
from Xlib.display import Display
from Xlib.protocol import request, rq
from Xlib.xobject import drawable, resource

extname: Final = "XFIXES"
XFixesSelectionNotify: Final = 0
XFixesCursorNotify: Final = 1
XFixesSetSelectionOwnerNotifyMask: Final = 0x1
XFixesSelectionWindowDestroyNotifyMask: Final = 0x2
XFixesSelectionClientCloseNotifyMask: Final = 0x4
XFixesDisplayCursorNotifyMask: Final = 0x1
XFixesSetSelectionOwnerNotify: Final = 0
XFixesSelectionWindowDestroyNotify: Final = 1
XFixesSelectionClientCloseNotify: Final = 2
XFixesDisplayCursorNotify: Final = 0

class QueryVersion(rq.ReplyRequest): ...

def query_version(self: Display | resource.Resource) -> QueryVersion: ...

class HideCursor(rq.Request): ...

def hide_cursor(self: drawable.Window) -> None: ...

class ShowCursor(rq.Request): ...

def show_cursor(self: drawable.Window) -> None: ...

class SelectSelectionInput(rq.Request): ...

def select_selection_input(self: Display | resource.Resource, window: int, selection: int, mask: int) -> SelectSelectionInput: ...

class SelectionNotify(rq.Event): ...
class SetSelectionOwnerNotify(SelectionNotify): ...
class SelectionWindowDestroyNotify(SelectionNotify): ...
class SelectionClientCloseNotify(SelectionNotify): ...
class SelectCursorInput(rq.Request): ...

def select_cursor_input(self: Display | resource.Resource, window: int, mask: int) -> SelectCursorInput: ...

class GetCursorImage(rq.ReplyRequest): ...

def get_cursor_image(self: Display | resource.Resource, window: Unused) -> GetCursorImage: ...

class DisplayCursorNotify(rq.Event): ...

def init(disp: Display, info: request.QueryExtension) -> None: ...
