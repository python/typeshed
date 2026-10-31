from __future__ import annotations

import codecs
from typing_extensions import assert_type

assert_type(codecs.decode("x", "unicode-escape"), str)
assert_type(codecs.decode(b"x", "unicode-escape"), str)

assert_type(codecs.decode(b"x", "utf-8"), str)
assert_type(codecs.lookup("UTF-8").decode(b"potato", errors="replace"), tuple[str, int])
codecs.lookup("ascii").decode(b"potato", errors="replace")  # type: ignore
codecs.decode("x", "utf-8")  # type: ignore

assert_type(codecs.decode("ab", "hex"), bytes)
assert_type(codecs.decode(b"ab", "hex"), bytes)
