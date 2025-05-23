from typing import Any

from cachetools import LRUCache, cached

cache: LRUCache[str, Any] = LRUCache(maxsize=128)


@cached(cache)
def example_function(x: int) -> str:
    return str(x)


original_function = example_function.__wrapped__
result = original_function(42)
