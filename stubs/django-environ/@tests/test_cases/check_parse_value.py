from __future__ import annotations

from typing import Union
from typing_extensions import TypedDict, assert_type

import environ

env = environ.Env()

assert_type(env.parse_value("just-a-value123", None), str)

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

# cast dict values
assert_type(env.parse_value("0=TRUE,99=FALSE", {}), dict[str, str])
assert_type(env.parse_value("0=TRUE,99=FALSE", {"cast": {}}), dict[str, Union[str, object]])
assert_type(env.parse_value("0=TRUE,99=FALSE", {"value": bool}), dict[str, bool])
assert_type(env.parse_value("0=TRUE,99=FALSE", {"value": bool, "cast": {}}), dict[str, Union[bool, object]])
assert_type(env.parse_value("0=TRUE,99=FALSE", {"key": int}), dict[int, str])
assert_type(env.parse_value("0=TRUE,99=FALSE", {"key": int, "cast": {}}), dict[int, Union[str, object]])
assert_type(env.parse_value("0=TRUE,99=FALSE", {"key": int, "value": bool}), dict[int, bool])
assert_type(env.parse_value("0=TRUE,99=FALSE", {"key": int, "value": bool, "cast": {}}), dict[int, Union[bool, object]])


# custom cast functions
def cast_float(x: str) -> float:
    return float(x)


assert_type(env.parse_value("20.5", cast_float), float)


class Person(TypedDict):
    first_name: str
    last_name: str
    age: int


def cast_person(v: str) -> Person:
    parts = v.split(",")
    return {"first_name": parts[0], "last_name": parts[1], "age": int(parts[2])}


assert_type(env.parse_value("Bob,Riveira,30", cast_person), Person)
