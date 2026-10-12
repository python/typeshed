import _operator
import operator
from typing_extensions import assert_type


class Index:
    def __index__(self) -> int:
        return 3


assert_type(operator.length_hint(object(), Index()), int)
assert_type(_operator.length_hint(object(), Index()), int)
operator.length_hint(object(), 1.5)  # type: ignore[arg-type]
