from _typeshed import Incomplete

ANGLE_TO_RADIANS: Incomplete
LENGTHS_TO_PIXELS: Incomplete
RESOLUTION_TO_DPPX: Incomplete
ABSOLUTE_UNITS: Incomplete
FONT_UNITS: Incomplete
VIEWPORT_UNITS: Incomplete
RELATIVE_UNITS = FONT_UNITS | VIEWPORT_UNITS
LENGTH_UNITS = ABSOLUTE_UNITS | RELATIVE_UNITS
ANGLE_UNITS: Incomplete

def to_pixels(value, style, property_name, font_size=None): ...
def to_radians(value): ...
