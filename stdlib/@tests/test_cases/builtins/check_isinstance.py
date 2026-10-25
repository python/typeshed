from typing import Any, cast
from typing_extensions import TypeIs, assert_type

o = cast(Any, "")
assert_type(isinstance(o, int), TypeIs[int])
assert_type(isinstance(o, object), TypeIs[object])
assert_type(isinstance(o, str), TypeIs[str])
assert_type(isinstance(o, (bytes, memoryview)), TypeIs[bytes | memoryview[int]])
assert_type(isinstance(o, (set, type[dict])), TypeIs[set[Any] | type[dict[Any, Any]]])
