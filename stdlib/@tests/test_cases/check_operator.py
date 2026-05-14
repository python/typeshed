from operator import methodcaller
from typing import Any
from typing_extensions import assert_type

m1 = methodcaller("foo")
assert_type(m1, methodcaller[[], Any])
m2 = methodcaller("foo", 42, bar="")
# assert_type(m2, methodcaller[[int, Arg(str, "bar")], Any])
m3: methodcaller[[], int] = methodcaller("foo")  # ok
m4: methodcaller[[int], Any] = methodcaller("foo", 1)  # ok
m5: methodcaller[[str], int] = methodcaller("foo", 1)  # type: ignore
