from typing import Collection
from typing_extensions import assert_type

# See https://github.com/python/typeshed/pull/8977
assert_type(['a', {'b'}], list[Collection[str]])
