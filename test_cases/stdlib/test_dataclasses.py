# pyright: reportUnnecessaryTypeIgnoreComment=true

import dataclasses
from typing import Any
from typing_extensions import assert_type


@dataclasses.dataclass
class D:
    ...


assert_type(dataclasses.astuple(D()), tuple[Any, ...])
assert_type(dataclasses.astuple(D(), tuple_factory=tuple), tuple[Any, ...])

assert_type(dataclasses.asdict(D()), dict[str, Any])
assert_type(dataclasses.asdict(D(), dict_factory=dict), dict[str, Any])
