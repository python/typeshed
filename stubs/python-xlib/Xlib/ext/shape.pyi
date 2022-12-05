from collections.abc import Sequence

from Xlib.display import Display
from Xlib.protocol import request, rq
from Xlib.protocol.structs import _Rectangle4IntSequence
from Xlib.xobject import drawable, resource

extname: str
OP = rq.Card8

class SO:
    Set: int
    Union: int
    Intersect: int
    Subtract: int
    Invert: int

class SK:
    Bounding: int
    Clip: int
    Input: int

class KIND(rq.Set):
    def __init__(self, name: str) -> None: ...

class NotifyEventData(rq.Event): ...
class QueryVersion(rq.ReplyRequest): ...
class Rectangles(rq.Request): ...
class Mask(rq.Request): ...
class Combine(rq.Request): ...
class Offset(rq.Request): ...
class QueryExtents(rq.ReplyRequest): ...
class SelectInput(rq.Request): ...
class InputSelected(rq.ReplyRequest): ...
class GetRectangles(rq.ReplyRequest): ...

class Event:
    Notify: int

def combine(
    self: drawable.Window, operation: int, destination_kind: int, source_kind: int, x_offset: int, y_offset: int
) -> None: ...
def get_rectangles(self: drawable.Window, source_kind: int) -> GetRectangles: ...
def input_selected(self: drawable.Window) -> InputSelected: ...
def mask(
    self: drawable.Window, operation: int, destination_kind: int, x_offset: int, y_offset: int, source_bitmap: int
) -> None: ...
def offset(self: drawable.Window, destination_kind: int, x_offset: int, y_offset: int) -> None: ...
def query_extents(self: drawable.Window) -> QueryExtents: ...
def query_version(self: Display | resource.Resource) -> QueryVersion: ...
def rectangles(
    self: drawable.Window,
    operation: int,
    destination_kind: int,
    ordering: int,
    x_offset: int,
    y_offset: int,
    rectangles: Sequence[_Rectangle4IntSequence],
) -> None: ...
def select_input(self: drawable.Window, enable: int) -> None: ...
def init(disp: Display, info: request.QueryExtension) -> None: ...
