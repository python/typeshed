from __future__ import annotations

import json
from decimal import Decimal


# By default, json.dumps() will not accept any non JSON-serializable objects.
class CustomClass: ...


json.dumps(CustomClass())  # type: ignore
json.dumps(object())  # type: ignore
json.dumps(Decimal(1))  # type: ignore

# Serializable types are supported, included nested JSON.
json.dumps({"a": 34, "b": [1, 2, 3], "c": {"d": "hello", "e": False}})
json.dumps(
    {
        "numbers": [1, 2, 3, 4, 5],
        "strings": ["hello", "world"],
        "booleans": [True, False],
        "null": None,
        "nested": {"array": [[1, 2], [3, 4.34]], "object": {"x": 1, "y": 2}},
    }
)
json.dumps(1)
json.dumps(1.23)
json.dumps(True)
json.dumps(False)
json.dumps(None)
json.dumps("hello")

x: dict[str, float | int] = {"a": 1, "b": 2.0}
json.dumps(x)


# Custom types are supported when a custom encoder is provided.
def decimal_encoder(obj: Decimal) -> float:
    return float(obj)


json.dumps(Decimal(1), default=decimal_encoder)


# If the custom encoder doesn't return JSON, it will lead a typing error..
def custom_encoder(obj: Decimal) -> Decimal:
    return obj


json.dumps(Decimal(1), default=custom_encoder)  #  type: ignore
