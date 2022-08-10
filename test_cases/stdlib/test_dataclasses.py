# pyright: reportUnnecessaryTypeIgnoreComment=true

import dataclasses
from typing import Any, Dict, Tuple
from typing_extensions import assert_type


@dataclasses.dataclass
class D:
    ...


assert_type(dataclasses.astuple(D()), Tuple[Any, ...])
assert_type(dataclasses.astuple(D(), tuple_factory=tuple), Tuple[Any, ...])

assert_type(dataclasses.asdict(D()), Dict[str, Any])
assert_type(dataclasses.asdict(D(), dict_factory=dict), Dict[str, Any])
