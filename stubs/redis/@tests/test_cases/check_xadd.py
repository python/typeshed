from typing import TypedDict

import redis


class RedisStreamData(TypedDict):
    foo: str
    bar: bytes


def check_xadd(r: redis.Redis[str]) -> None:
    # check that TypedDicts are accepted for the `fields` parameter of `xadd()`
    r.xadd("stream", fields=RedisStreamData({"foo": "bar", "bar": b"foo"}))
