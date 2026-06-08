# Stubs-only indirection for `affine` package types used in rasterio
# signatures. Until affine ships its own `py.typed` (planned for v3),
# `Affine` is exposed as `Any`. When affine v3 lands, replace the body
# of this module with `from affine import Affine as Affine`.
from typing import Any, TypeAlias

Affine: TypeAlias = Any
