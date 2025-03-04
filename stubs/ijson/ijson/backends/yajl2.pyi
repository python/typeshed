from _typeshed import Incomplete
from collections.abc import Generator

yajl: Incomplete
YAJL_ALLOW_COMMENTS: int
YAJL_MULTIPLE_VALUES: int

def basic_parse_basecoro(
    target, allow_comments: bool = False, multiple_values: bool = False, use_float: bool = False
) -> Generator[None, Incomplete]: ...
