from __future__ import annotations

import enum
import sys
from typing_extensions import Literal, assert_type

if sys.version_info >= (3, 11):

    class Foo(enum.StrEnum):
        X = enum.auto()

    assert_type(Foo.X, Literal[Foo.X])
    assert_type(Foo.X.value, str)
