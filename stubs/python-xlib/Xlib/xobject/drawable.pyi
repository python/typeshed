# from builtins import map  # Explicit import for pytype https://github.com/google/pytype/issues/1324
from collections.abc import Iterable, Sequence

from PIL import Image
from Xlib._typing import ErrorHandler, SliceableBuffer
from Xlib.protocol import request, rq
from Xlib.xobject import colormap, cursor, fontable, resource

# Alias to _map. Otherwise mypy thinks map is Xlib.xobject.drawable.Window.map https://github.com/python/mypy/issues/14205
# _map = map
# Using map crashes pytype https://github.com/google/pytype/issues/1324
_map = list

class Drawable(resource.Resource):
    __drawable__ = resource.Resource.__resource__
    def get_geometry(self) -> request.GetGeometry: ...
    def create_pixmap(self, width: int, height: int, depth: int) -> Pixmap: ...
    def create_gc(self, **keys: object) -> fontable.GC: ...
    def copy_area(
        self,
        gc: int,
        src_drawable: int,
        src_x: int,
        src_y: int,
        width: int,
        height: int,
        dst_x: int,
        dst_y: int,
        onerror: ErrorHandler[object] | None = ...,
    ) -> None: ...
    def copy_plane(
        self,
        gc: int,
        src_drawable: int,
        src_x: int,
        src_y: int,
        width: int,
        height: int,
        dst_x: int,
        dst_y: int,
        bit_plane: int,
        onerror: ErrorHandler[object] | None = ...,
    ) -> None: ...
    def poly_point(
        self, gc: int, coord_mode: int, points: Sequence[tuple[int, int]], onerror: ErrorHandler[object] | None = ...
    ) -> None: ...
    def point(self, gc: int, x: int, y: int, onerror: ErrorHandler[object] | None = ...) -> None: ...
    def poly_line(
        self, gc: int, coord_mode: int, points: Sequence[tuple[int, int]], onerror: ErrorHandler[object] | None = ...
    ) -> None: ...
    def line(self, gc: int, x1: int, y1: int, x2: int, y2: int, onerror: ErrorHandler[object] | None = ...) -> None: ...
    def poly_segment(
        self, gc: int, segments: Sequence[tuple[int, int, int, int]], onerror: ErrorHandler[object] | None = ...
    ) -> None: ...
    def poly_rectangle(
        self, gc: int, rectangles: Sequence[tuple[int, int, int, int]], onerror: ErrorHandler[object] | None = ...
    ) -> None: ...
    def rectangle(self, gc: int, x: int, y: int, width: int, height: int, onerror: ErrorHandler[object] | None = ...) -> None: ...
    def poly_arc(
        self, gc: int, arcs: Sequence[tuple[int, int, int, int, int, int]], onerror: ErrorHandler[object] | None = ...
    ) -> None: ...
    def arc(
        self,
        gc: int,
        x: int,
        y: int,
        width: int,
        height: int,
        angle1: int,
        angle2: int,
        onerror: ErrorHandler[object] | None = ...,
    ) -> None: ...
    def fill_poly(
        self, gc: int, shape: int, coord_mode: int, points: Sequence[tuple[int, int]], onerror: ErrorHandler[object] | None = ...
    ) -> None: ...
    def poly_fill_rectangle(
        self, gc: int, rectangles: Sequence[tuple[int, int, int, int]], onerror: ErrorHandler[object] | None = ...
    ) -> None: ...
    def fill_rectangle(
        self, gc: int, x: int, y: int, width: int, height: int, onerror: ErrorHandler[object] | None = ...
    ) -> None: ...
    def poly_fill_arc(
        self, gc: int, arcs: Sequence[tuple[int, int, int, int, int, int]], onerror: ErrorHandler[object] | None = ...
    ) -> None: ...
    def fill_arc(
        self,
        gc: int,
        x: int,
        y: int,
        width: int,
        height: int,
        angle1: int,
        angle2: int,
        onerror: ErrorHandler[object] | None = ...,
    ) -> None: ...
    def put_image(
        self,
        gc: int,
        x: int,
        y: int,
        width: int,
        height: int,
        format: int,
        depth: int,
        left_pad: int,
        data: SliceableBuffer,
        onerror: ErrorHandler[object] | None = ...,
    ) -> None: ...
    def put_pil_image(self, gc: int, x: int, y: int, image: Image.Image, onerror: ErrorHandler[object] | None = ...) -> None: ...
    def get_image(self, x: int, y: int, width: int, height: int, format: int, plane_mask: int) -> request.GetImage: ...
    def draw_text(
        self, gc: int, x: int, y: int, text: dict[str, str | int], onerror: ErrorHandler[object] | None = ...
    ) -> None: ...
    def poly_text(
        self, gc: int, x: int, y: int, items: Sequence[dict[str, str | int]], onerror: ErrorHandler[object] | None = ...
    ) -> None: ...
    def poly_text_16(
        self, gc: int, x: int, y: int, items: Sequence[dict[str, str | int]], onerror: ErrorHandler[object] | None = ...
    ) -> None: ...
    def image_text(self, gc: int, x: int, y: int, string: str, onerror: ErrorHandler[object] | None = ...) -> None: ...
    def image_text_16(self, gc: int, x: int, y: int, string: str, onerror: ErrorHandler[object] | None = ...) -> None: ...
    def query_best_size(self, item_class: int, width: int, height: int) -> request.QueryBestSize: ...

class Window(Drawable):
    __window__ = resource.Resource.__resource__
    def create_window(
        self,
        x: int,
        y: int,
        width: int,
        height: int,
        border_width: int,
        depth: int,
        window_class: int = ...,
        visual: int = ...,
        onerror: ErrorHandler[object] | None = ...,
        **keys: object,
    ) -> Window: ...
    def change_attributes(self, onerror: ErrorHandler[object] | None = ..., **keys: object) -> None: ...
    def get_attributes(self) -> request.GetWindowAttributes: ...
    def destroy(self, onerror: ErrorHandler[object] | None = ...) -> None: ...
    def destroy_sub_windows(self, onerror: ErrorHandler[object] | None = ...) -> None: ...
    def change_save_set(self, mode: int, onerror: ErrorHandler[object] | None = ...) -> None: ...
    def reparent(self, parent: int, x: int, y: int, onerror: ErrorHandler[object] | None = ...) -> None: ...
    def map(self, onerror: ErrorHandler[object] | None = ...) -> None: ...
    def map_sub_windows(self, onerror: ErrorHandler[object] | None = ...) -> None: ...
    def unmap(self, onerror: ErrorHandler[object] | None = ...) -> None: ...
    def unmap_sub_windows(self, onerror: ErrorHandler[object] | None = ...) -> None: ...
    def configure(self, onerror: ErrorHandler[object] | None = ..., **keys: object) -> None: ...
    def circulate(self, direction: int, onerror: ErrorHandler[object] | None = ...) -> None: ...
    def raise_window(self, onerror: ErrorHandler[object] | None = ...) -> None: ...
    def query_tree(self) -> request.QueryTree: ...
    def change_property(
        self,
        property: int,
        property_type: int,
        format: int,
        data: Sequence[float] | Sequence[str],
        mode: int = ...,
        onerror: ErrorHandler[object] | None = ...,
    ) -> None: ...
    def change_text_property(
        self, property: int, property_type: int, data: bytes | str, mode: int = ..., onerror: ErrorHandler[object] | None = ...
    ) -> None: ...
    def delete_property(self, property: int, onerror: ErrorHandler[object] | None = ...) -> None: ...
    def get_property(
        self, property: int, property_type: int, offset: int, length: int, delete: bool = ...
    ) -> request.GetProperty | None: ...
    def get_full_property(self, property: int, property_type: int, sizehint: int = ...) -> request.GetProperty | None: ...
    def get_full_text_property(self, property: int, property_type: int = ..., sizehint: int = ...) -> str | None: ...
    def list_properties(self) -> list[int]: ...
    def set_selection_owner(self, selection: int, time: int, onerror: ErrorHandler[object] | None = ...) -> None: ...
    def convert_selection(
        self, selection: int, target: int, property: int, time: int, onerror: ErrorHandler[object] | None = ...
    ) -> None: ...
    def send_event(
        self, event: rq.Event, event_mask: int = ..., propagate: bool = ..., onerror: ErrorHandler[object] | None = ...
    ) -> None: ...
    def grab_pointer(
        self, owner_events: bool, event_mask: int, pointer_mode: int, keyboard_mode: int, confine_to: int, cursor: int, time: int
    ) -> int: ...
    def grab_button(
        self,
        button: int,
        modifiers: int,
        owner_events: bool,
        event_mask: int,
        pointer_mode: int,
        keyboard_mode: int,
        confine_to: int,
        cursor: int,
        onerror: ErrorHandler[object] | None = ...,
    ) -> None: ...
    def ungrab_button(self, button: int, modifiers: int, onerror: ErrorHandler[object] | None = ...) -> None: ...
    def grab_keyboard(self, owner_events: bool, pointer_mode: int, keyboard_mode: int, time: int) -> int: ...
    def grab_key(
        self,
        key: int,
        modifiers: int,
        owner_events: bool,
        pointer_mode: int,
        keyboard_mode: int,
        onerror: ErrorHandler[object] | None = ...,
    ) -> None: ...
    def ungrab_key(self, key: int, modifiers: int, onerror: ErrorHandler[object] | None = ...) -> None: ...
    def query_pointer(self) -> request.QueryPointer: ...
    def get_motion_events(self, start: int, stop: int) -> rq.Struct: ...
    def translate_coords(self, src_window: int, src_x: int, src_y: int) -> request.TranslateCoords: ...
    def warp_pointer(
        self,
        x: int,
        y: int,
        src_window: int = ...,
        src_x: int = ...,
        src_y: int = ...,
        src_width: int = ...,
        src_height: int = ...,
        onerror: ErrorHandler[object] | None = ...,
    ) -> None: ...
    def set_input_focus(self, revert_to: int, time: int, onerror: ErrorHandler[object] | None = ...) -> None: ...
    def clear_area(
        self,
        x: int = ...,
        y: int = ...,
        width: int = ...,
        height: int = ...,
        exposures: bool = ...,
        onerror: ErrorHandler[object] | None = ...,
    ) -> None: ...
    def create_colormap(self, visual: int, alloc: int) -> colormap.Colormap: ...
    def list_installed_colormaps(self) -> list[colormap.Colormap]: ...
    def rotate_properties(self, properties: Sequence[int], delta: int, onerror: ErrorHandler[object] | None = ...) -> None: ...
    def set_wm_name(self, name: bytes | str, onerror: ErrorHandler[object] | None = ...) -> None: ...
    def get_wm_name(self) -> str | None: ...
    def set_wm_icon_name(self, name: bytes | str, onerror: ErrorHandler[object] | None = ...) -> None: ...
    def get_wm_icon_name(self) -> str | None: ...
    def set_wm_class(self, inst: str, cls: str, onerror: ErrorHandler[object] | None = ...) -> None: ...
    def get_wm_class(self) -> tuple[str, str] | None: ...
    def set_wm_transient_for(self, window: Window, onerror: ErrorHandler[object] | None = ...) -> None: ...
    def get_wm_transient_for(self) -> Window | None: ...
    def set_wm_protocols(self, protocols: Iterable[int], onerror: ErrorHandler[object] | None = ...) -> None: ...
    def get_wm_protocols(self) -> list[int]: ...
    def set_wm_colormap_windows(self, windows: Iterable[Window], onerror: ErrorHandler[object] | None = ...) -> None: ...
    def get_wm_colormap_windows(self) -> list[Window] | _map[Window]: ...
    def set_wm_client_machine(self, name: bytes | str, onerror: ErrorHandler[object] | None = ...) -> None: ...
    def get_wm_client_machine(self) -> str | None: ...
    def set_wm_normal_hints(
        self, hints: rq.DictWrapper | dict[str, object] = ..., onerror: ErrorHandler[object] | None = ..., **keys: object
    ) -> None: ...
    def get_wm_normal_hints(self) -> rq.DictWrapper | None: ...
    def set_wm_hints(
        self, hints: rq.DictWrapper | dict[str, object] = ..., onerror: ErrorHandler[object] | None = ..., **keys: object
    ) -> None: ...
    def get_wm_hints(self) -> rq.DictWrapper | None: ...
    def set_wm_state(
        self, hints: rq.DictWrapper | dict[str, object] = ..., onerror: ErrorHandler[object] | None = ..., **keys: object
    ) -> None: ...
    def get_wm_state(self) -> rq.DictWrapper | None: ...
    def set_wm_icon_size(
        self, hints: rq.DictWrapper | dict[str, object] = ..., onerror: ErrorHandler[object] | None = ..., **keys: object
    ) -> None: ...
    def get_wm_icon_size(self) -> rq.DictWrapper | None: ...

class Pixmap(Drawable):
    __pixmap__ = resource.Resource.__resource__
    def free(self, onerror: ErrorHandler[object] | None = ...) -> None: ...
    def create_cursor(
        self, mask: int, foreground: tuple[int, int, int], background: tuple[int, int, int], x: int, y: int
    ) -> cursor.Cursor: ...

def roundup(value: int, unit: int) -> int: ...
