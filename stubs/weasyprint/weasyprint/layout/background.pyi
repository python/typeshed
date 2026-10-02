from _typeshed import Incomplete
from typing import NamedTuple

class Background(NamedTuple):
    color: Incomplete
    layers: Incomplete
    style: Incomplete

class BackgroundLayer(NamedTuple):
    image: Incomplete
    size: Incomplete
    position: Incomplete
    repeat: Incomplete
    unbounded: Incomplete
    painting_area: Incomplete
    positioning_area: Incomplete
    clipped_boxes: Incomplete

def box_rectangle(box, which_rectangle): ...
def layout_box_backgrounds(page, box, get_image_from_uri, layout_children: bool = True, style=None) -> None: ...
def layout_background_layer(box, page, resolution, image, size, clip, repeat, origin, position, attachment): ...
def layout_backgrounds(page, get_image_from_uri) -> None: ...
