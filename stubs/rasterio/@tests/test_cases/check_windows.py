"""Verify `rasterio.windows.Window` constructors and the from_bounds overload."""

from __future__ import annotations

from typing_extensions import assert_type

from rasterio.transform import from_origin
from rasterio.windows import Window, from_bounds

# Constructors.
w = Window(0, 0, 10, 10)
assert_type(w, Window)
assert_type(Window.from_slices(slice(0, 5), slice(0, 5)), Window)
assert_type(w.intersection(w), Window)
assert_type(w.todict(), dict[str, float])

# from_bounds — modern overload (no deprecated kwargs).
t = from_origin(0.0, 0.0, 1.0, 1.0)
assert_type(from_bounds(0, 0, 1, 1, t), Window)

# Negative widths are accepted at the type level; runtime validates.
assert_type(Window(0, 0, -1, -1), Window)
