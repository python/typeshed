from collections.abc import Sequence
from typing import overload
from typing_extensions import TypeAlias

from cv2 import Mat
from cv2.cv2 import (
    GCompileArg,
    GMat,
    _NumericScalar,
    gapi_wip_draw_Circle,
    gapi_wip_draw_Image,
    gapi_wip_draw_Line,
    gapi_wip_draw_Mosaic,
    gapi_wip_draw_Poly,
    gapi_wip_draw_Rect,
    gapi_wip_draw_Text,
)
from cv2.gapi import GArray

_Prim: TypeAlias = Text | Rect | Circle | Line | Mosaic | Image | Poly

Circle = gapi_wip_draw_Circle
Image = gapi_wip_draw_Image
Line = gapi_wip_draw_Line
Mosaic = gapi_wip_draw_Mosaic
Poly = gapi_wip_draw_Poly
Rect = gapi_wip_draw_Rect
Text = gapi_wip_draw_Text

@overload
def render(bgr: Mat | _NumericScalar, prims: Sequence[_Prim], args: Sequence[GCompileArg] = ...) -> None: ...
@overload
def render(
    y_plane: Mat | _NumericScalar, uv_plane: Mat | _NumericScalar, prims: Sequence[_Prim], args: Sequence[GCompileArg] = ...
) -> None: ...
def render3ch(src: GMat, prims: GArray.Prim) -> GMat: ...
def renderNV12(y: GMat, uv: GMat, prims: GArray.Prim) -> tuple[GMat, GMat]: ...
