import dataclasses as dc
from typing import Any, Dict, Tuple, Type
from typing_extensions import assert_type


@dc.dataclass
class Foo:
    attr: str


assert_type(dc.fields(Foo), Tuple[dc.Field[Any], ...])
dc.asdict(Foo)  # type: ignore
dc.astuple(Foo)  # type: ignore
dc.replace(Foo)  # type: ignore

if dc.is_dataclass(Foo):
    # The inferred type doesn't change
    # if it's already known to be a subtype of type[_DataclassInstance]
    assert_type(Foo, Type[Foo])

f = Foo(attr="attr")

assert_type(dc.fields(f), Tuple[dc.Field[Any], ...])
assert_type(dc.asdict(f), Dict[str, Any])
assert_type(dc.astuple(f), Tuple[Any, ...])
assert_type(dc.replace(f, attr="new"), Foo)

if dc.is_dataclass(f):
    # The inferred type doesn't change
    # if it's already known to be a subtype of _DataclassInstance
    assert_type(f, Foo)


def test_other_isdataclass_overloads(x: type, y: object) -> None:
    dc.fields(x)  # TODO: why does this pass mypy? It should fail, ideally...
    dc.fields(y)  # type: ignore

    dc.asdict(x)  # type: ignore
    dc.asdict(y)  # type: ignore

    dc.astuple(x)  # type: ignore
    dc.astuple(y)  # type: ignore

    dc.replace(x)  # type: ignore
    dc.replace(y)  # type: ignore

    if dc.is_dataclass(x):
        assert_type(dc.fields(x), Tuple[dc.Field[Any], ...])
        # These should fail due to the fact it's a dataclass class, not an instance
        dc.asdict(x)  # type: ignore
        dc.astuple(x)  # type: ignore
        dc.replace(x)  # type: ignore

    if dc.is_dataclass(y):
        assert_type(dc.fields(y), Tuple[dc.Field[Any], ...])
        # These should fail due to the fact we don't know
        # whether it's a dataclass class or a dataclass instance
        dc.asdict(y)  # type: ignore
        dc.astuple(y)  # type: ignore
        dc.replace(y)  # type: ignore

    if dc.is_dataclass(y) and not isinstance(y, type):
        assert_type(dc.fields(y), Tuple[dc.Field[Any], ...])
        assert_type(dc.asdict(y), Dict[str, Any])
        assert_type(dc.astuple(y), Tuple[Any, ...])
        dc.replace(y)
