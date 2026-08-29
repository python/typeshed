from __future__ import annotations

from typing import List, Tuple
from typing_extensions import assert_type

import regex

# Regression test for #566: allcaptures()/allspans() were typed as fixed
# 1-tuples, which made a type checker refuse to unpack or index past the
# first element even though the runtime always returns one entry per group,
# a count that depends on the pattern rather than being fixed at one.
m = regex.match(r"(\w+) (\w+)", "hello world")
assert m is not None
assert_type(m.allcaptures(), Tuple[List[str], ...])
assert_type(m.allspans(), Tuple[List[Tuple[int, int]], ...])
