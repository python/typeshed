from typing_extensions import assert_type

from affine import Affine
from rasterio.transform import TransformMethodsMixin, rowcol

transform = Affine.identity()

assert_type(rowcol(transform, 0.5, 0.5), tuple[int, int] | tuple[list[int], list[int]])
assert_type(rowcol(transform, 0.5, 0.5, op=lambda value: value), tuple[float, float] | tuple[list[float], list[float]])

mixin = TransformMethodsMixin()
assert_type(mixin.index(0.5, 0.5, op=lambda value: value), tuple[int, int] | tuple[list[int], list[int]])
