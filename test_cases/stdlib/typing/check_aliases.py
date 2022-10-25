from typing import Collection
from typing_extensions import assert_type

assert_type(['a', {'b'}], list[Collection[str]])
