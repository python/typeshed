from __future__ import annotations

from typing_extensions import assert_type

# Both import methods work, see the comment in grpc/__init__.py.
from grpc import aio

assert_type(aio.Server(), aio.Server)  # type: ignore[abstract]
