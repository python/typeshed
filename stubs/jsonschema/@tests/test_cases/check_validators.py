from __future__ import annotations

from collections.abc import Iterator
from typing import Any
from typing_extensions import assert_type

from jsonschema import Draft202012Validator
from jsonschema.exceptions import ValidationError
from jsonschema.protocols import Validator
from jsonschema.validators import _Validator, create, extend


def pattern(validator: Validator, value: str, instance: str, schema: Any) -> Iterator[ValidationError]:
    yield from ()


def properties(
    validator: Validator, value: dict[str, Any], instance: dict[str, Any], schema: dict[str, Any]
) -> Iterator[ValidationError]:
    yield from ()


def not_a_keyword_callback(instance: object) -> Iterator[ValidationError]:
    yield from ()


def extend_any(validator_class: type[Validator]) -> None:
    # Any validator class satisfying the protocol, not only those built by create().
    assert_type(extend(validator_class), type[_Validator])


# Keyword callbacks narrow their parameters; a dict literal mixing them must still match.
assert_type(extend(Draft202012Validator, {"pattern": pattern, "properties": properties}), type[_Validator])
assert_type(extend(Draft202012Validator, [("pattern", pattern), ("properties", properties)]), type[_Validator])
assert_type(extend(Draft202012Validator), type[_Validator])
extend(Draft202012Validator, {"pattern": not_a_keyword_callback})  # type: ignore
extend(Draft202012Validator, [("pattern", not_a_keyword_callback)])  # type: ignore

assert_type(create({}, {"pattern": pattern, "properties": properties}), type[_Validator])
assert_type(create({}, [("pattern", pattern)]), type[_Validator])
assert_type(create({}), type[_Validator])
