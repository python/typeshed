from _typeshed import Incomplete

ANGLE_TO_RADIANS: Incomplete
LENGTHS_TO_PIXELS: Incomplete
RESOLUTION_TO_DPPX: Incomplete
FONT_UNITS: Incomplete
ABSOLUTE_UNITS: Incomplete
LENGTH_UNITS = ABSOLUTE_UNITS | FONT_UNITS
ANGLE_UNITS: Incomplete

def to_pixels(value, style, property_name, font_size=None): ...
def to_radians(value): ...
