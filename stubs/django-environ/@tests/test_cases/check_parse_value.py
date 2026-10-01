from __future__ import annotations

from typing import Any
from typing_extensions import assert_type
from urllib.parse import ParseResult

import environ

env = environ.Env()

assert_type(env.parse_value("just-a-value123", None), str)

# helpers preserve default value types for missing environment variables
assert_type(env.str("NAME"), str)
assert_type(env.str("NAME", default=None), str | None)
assert_type(env.bool("DEBUG", default=None), bool | None)
assert_type(env.int("PORT", default=None), int | None)
assert_type(env.float("RATIO", default=None), float | None)
assert_type(env.url("URL"), ParseResult)
assert_type(env.url("URL", default=None), ParseResult | None)

# builtin types
assert_type(env.parse_value("string", str), str)
assert_type(env.parse_value("TRUE", bool), bool)
assert_type(env.parse_value("2000", int), int)
assert_type(env.parse_value("-500.01", float), float)
assert_type(env.parse_value("first,second,", list), list[str])
assert_type(env.parse_value("(first,second)", tuple), tuple[str, ...])
assert_type(env.parse_value("a=first,b=second", dict), dict[str, str])


# cast list values (first list element is used)
assert_type(env.parse_value("20.5,-0.2", [str]), list[str])
assert_type(env.parse_value("20.5,-0.2", [bool]), list[bool])
assert_type(env.parse_value("20.5,-0.2", [int]), list[int])
assert_type(env.parse_value("20.5,-0.2", [float]), list[float])

# cast tuple values (first tuple element is used)
assert_type(env.parse_value("(20.5,-0.2)", (str,)), tuple[str, ...])
assert_type(env.parse_value("(20.5,-0.2)", (bool,)), tuple[bool, ...])
assert_type(env.parse_value("(20.5,-0.2)", (int,)), tuple[int, ...])
assert_type(env.parse_value("(20.5,-0.2)", (float,)), tuple[float, ...])

# dict-valued casts split pairs with semicolons.
assert_type(env.parse_value("0=TRUE;99=FALSE", {}), dict[Any, Any])
assert_type(env.parse_value("0=TRUE;99=FALSE", {"key": int, "value": bool}), dict[Any, Any])
assert_type(env.parse_value("0=TRUE;99=FALSE", {"cast": {"0": bool}}), dict[Any, Any])


# custom cast functions
def cast_float(x: str) -> float:
    return float(x)


assert_type(env.parse_value("20.5", cast_float), float)
