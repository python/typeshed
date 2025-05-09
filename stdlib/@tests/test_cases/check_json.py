from __future__ import annotations

import json
from decimal import Decimal
from typing import Any, TypedDict


class _File:
    def write(self, s: str) -> int: ...


fp = _File()


# By default, json.dumps() will not accept any non JSON-serializable objects.
class CustomClass: ...


json.dumps(CustomClass())  # type: ignore
json.dump(CustomClass(), fp)  # type: ignore
json.dumps(object())  # type: ignore
json.dump(object(), fp)  # type: ignore
json.dumps(Decimal(1))  # type: ignore
json.dump(Decimal(1), fp)  # type: ignore

# Serializable types are supported, included nested JSON.
json.dumps({"a": 34, "b": [1, 2, 3], "c": {"d": "hello", "e": False}})
json.dump({"a": 34, "b": [1, 2, 3], "c": {"d": "hello", "e": False}}, fp)
json.dumps(
    {
        "numbers": [1, 2, 3, 4, 5],
        "strings": ["hello", "world"],
        "booleans": [True, False],
        "null": None,
        "nested": {"array": [[1, 2], [3, 4.34]], "object": {"x": 1, "y": 2}},
    }
)
json.dump(
    {
        "numbers": [1, 2, 3, 4, 5],
        "strings": ["hello", "world"],
        "booleans": [True, False],
        "null": None,
        "nested": {"array": [[1, 2], [3, 4.34]], "object": {"x": 1, "y": 2}},
    },
    fp,
)
json.dumps(1)
json.dump(1, fp)
json.dumps(1.23)
json.dump(1.23, fp)
json.dumps(True)
json.dump(True, fp)

# Test explicit nested types that might cause variance issues.
x: dict[str, float | int] = {"a": 1, "b": 2.0}
json.dumps(x)
json.dump(x, fp)

z: dict[str, dict[str, dict[str, list[int]]]] = {"a": {"b": {"c": [1, 2, 3]}}}
json.dumps(z)
json.dump(z, fp)


# Custom types are supported when a custom encoder is provided.
def decimal_encoder(obj: Decimal) -> float:
    return float(obj)


json.dumps(Decimal(1), default=decimal_encoder)
json.dump(Decimal(1), fp, default=decimal_encoder)


# If the custom encoder doesn't return JSON, it will lead a typing error..
def custom_encoder(obj: Decimal) -> Decimal:
    return obj


json.dumps(Decimal(1), default=custom_encoder)  #  type: ignore
json.dump(Decimal(1), fp, default=custom_encoder)  #  type: ignore


class MyTypedDict(TypedDict):
    a: str
    b: str


json.dumps(MyTypedDict(a="hello", b="world"))


# We should allow anything for subclasses of json.JSONEncoder.
# Type-checking custom encoders is not practical without generics.
class MyJSONEncoder(json.JSONEncoder): ...


json.dumps(Decimal(1), cls=MyJSONEncoder)
json.dump(Decimal(1), fp, cls=MyJSONEncoder)
