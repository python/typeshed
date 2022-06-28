from types import NoneType
from typing_extensions import assert_type

a: type[None] = NoneType

assert_type(NoneType, type[None])
isinstance(None, NoneType)

