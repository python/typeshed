from __future__ import annotations

from typing import List
from typing_extensions import assert_type

from decouple import Csv

assert_type(Csv()(""), List[str])
assert_type(Csv(cast=int)(""), List[int])
# assert_type(type(Csv(post_process=set)("")), type(set)
# assert_type(Csv(int, ",", " ", tuple)(""), Tuple[Any, ...])
# assert_type(Csv(cast=int, post_process=tuple)(""), Tuple[Any, ...])
# assert_type(Csv(cast=int, delimiter=",", post_process=tuple)(""), Tuple[Any, ...])
