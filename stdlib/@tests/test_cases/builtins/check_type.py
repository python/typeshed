import sys
from typing_extensions import assert_type

if sys.version_info >= (3, 10):
    from types import UnionType

    # pyright has special-casing that causes this failure
    assert_type(int | int, UnionType | type[int])  # pyright: ignore[reportAssertTypeFailure]
