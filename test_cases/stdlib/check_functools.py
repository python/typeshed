import sys

if sys.version_info >= (3, 8):
    from typing import cast
    from typing_extensions import assert_type
    from functools import cached_property

    class A:
        def __init__(self, x: int):
            self.x = x
            
        @cached_property
        def x(self) -> int:
            return 0

    assert_type(A(x=1).x, int)

    class B:
        @cached_property
        def x(self) -> int:
            return 0

    b = B()
    assert_type(b.x, int)
    b.x = cast(int, 4)
    assert_type(b.x, int)
