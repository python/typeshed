import json
from decimal import Decimal


# By default, json.dumps() will not accept any non-serializable objects.
class CustomClass: ...


json.dumps(CustomClass())  # Error
json.dumps(object())  # Error
json.dumps(Decimal(1))  # Error

# Serializable types are supported, included nested JSON.
json.dumps(
    {
        "a": 34,
        "b": [1, 2, 3],
        "c": {
            "d": "hello",
            "e": False,
        },
    }
)
json.dumps(
    {
        "numbers": [1, 2, 3, 4, 5],
        "strings": ["hello", "world"],
        "booleans": [True, False],
        "null": None,
        "nested": {"array": [[1, 2], [3, 4.34]], "object": {"x": 1, "y": 2}},
    }
)
json.dumps({"empty_array": [], "empty_object": {}, "float": 3.14, "scientific": 1.23e-4, "unicode": "Hello 世界"})
json.dumps(1)
json.dumps(1.23)
json.dumps(True)
json.dumps(False)
json.dumps(None)
json.dumps("hello")


# Custom types are supported when a custom encoder is provided.
def decimal_encoder(obj: Decimal) -> float:
    return float(obj)


json.dumps(Decimal(1), default=decimal_encoder)


# If the custom encoder doesn't return JSON, it will raise.
def custom_encoder(obj: Decimal) -> Decimal:
    return obj


json.dumps(Decimal(1), default=custom_encoder)  #  type: ignore
