# TODO: Don't forget to re-enable before PR
# mypy: disable-error-code=assert-type
from __future__ import annotations

from typing import Any, Union
from typing_extensions import Literal, assert_type

from openpyxl.descriptors.base import Descriptor, NoneSet, Set, Typed
from openpyxl.descriptors.serialisable import Serialisable


class WithDescriptors(Serialisable):
    # Specifically testing infered type without non-runtime type hints
    descriptor = Descriptor()  # type: ignore[var-annotated]

    typed_default = Typed(expected_type=str)
    typed_not_none = Typed(expected_type=str, allow_none=False)
    typed_none = Typed(expected_type=str, allow_none=True)

    set_tuple = Set(values=("a", 1, 0.0))
    set_list = Set(values=["a", 1, 0.0])
    set_tuple_none = Set(values=("a", 1, 0.0, None))

    noneset_tuple = NoneSet(values=("a", 1, 0.0))
    noneset_list = NoneSet(values=["a", 1, 0.0])

    # Test inferred annotation
    assert_type(descriptor, Descriptor[Any])

    assert_type(typed_default, Typed[str, Literal[False]])
    assert_type(typed_not_none, Typed[str, Literal[False]])
    assert_type(typed_none, Typed[str, Literal[True]])

    assert_type(set_tuple, Set[Union[Literal["a", 1], float]])
    assert_type(set_list, Set[Union[str, int, float]])  # Literals are [generified, *idk the right word] in non-tuples
    assert_type(set_tuple_none, Set[Union[Literal["a", 1, None], float]])

    assert_type(noneset_tuple, NoneSet[Union[Literal["a", 1], float]])
    assert_type(noneset_list, NoneSet[Union[str, float]])  # int and float are merged in generic unions


with_descriptors = WithDescriptors()


# Test with missing subclass
class NotSerialisable:
    descriptor = Descriptor[Any]()


NotSerialisable().descriptor = None  # type: ignore

# Test getters
assert_type(with_descriptors.descriptor, Any)
assert_type(with_descriptors.typed_default, str)
assert_type(with_descriptors.typed_none, Union[str, None])
assert_type(with_descriptors.set_tuple, Union[Literal["a", 1], float])
assert_type(with_descriptors.set_tuple_none, Union[Literal["a", 1, None], float])
assert_type(with_descriptors.set_list, Union[str, int, float])  # Literals are [generified, *idk the right word] in non-tuples
assert_type(with_descriptors.set_tuple_none, Union[Literal["a", 1, None], float])
assert_type(with_descriptors.noneset_tuple, Union[Literal["a", 1], float, None])
assert_type(with_descriptors.noneset_list, Union[str, float, None])  # int and float are merged in generic unions

# Test setters (expected type, None, unexpected type)
with_descriptors.descriptor = object()
with_descriptors.descriptor = None
with_descriptors.descriptor = type

with_descriptors.typed_default = ""
with_descriptors.typed_default = None  # pyright: ignore[reportGeneralTypeIssues] # false negative in mypy
with_descriptors.typed_default = 0  # type: ignore

with_descriptors.typed_none = ""
with_descriptors.typed_not_none = None  # pyright: ignore[reportGeneralTypeIssues] # false negative in mypy
with_descriptors.typed_not_none = 0  # type: ignore

with_descriptors.typed_none = ""
with_descriptors.typed_none = None
with_descriptors.typed_none = 0  # type: ignore

# NOTE: Can't check Set for literal int wen used with a float because any int is a vlaid float
with_descriptors.set_tuple = "a"
with_descriptors.set_tuple = 0
with_descriptors.set_tuple = 0.0
with_descriptors.set_tuple = None  # pyright: ignore[reportGeneralTypeIssues] # false negative in mypy
with_descriptors.set_tuple = "none"  # pyright: ignore[reportGeneralTypeIssues] # false negative in mypy
with_descriptors.set_tuple = object()  # pyright: ignore[reportGeneralTypeIssues] # false negative in mypy

with_descriptors.set_list = "a"
with_descriptors.set_list = 0
with_descriptors.set_list = 0.0
with_descriptors.set_list = None  # pyright: ignore[reportGeneralTypeIssues] # false negative in mypy
with_descriptors.set_list = "none"  # can't check literals validity
with_descriptors.set_list = object()  # pyright: ignore[reportGeneralTypeIssues] # false negative in mypy

with_descriptors.set_tuple_none = "a"
with_descriptors.set_tuple_none = 0
with_descriptors.set_tuple_none = 0.0
with_descriptors.set_tuple_none = None
with_descriptors.set_tuple_none = "none"  # pyright: ignore[reportGeneralTypeIssues] # false negative in mypy
with_descriptors.set_tuple_none = object()  # pyright: ignore[reportGeneralTypeIssues] # false negative in mypy

with_descriptors.noneset_tuple = "a"
with_descriptors.noneset_tuple = 0
with_descriptors.noneset_tuple = 0.0
with_descriptors.noneset_tuple = None
with_descriptors.noneset_tuple = "none"
with_descriptors.noneset_tuple = object()  # pyright: ignore[reportGeneralTypeIssues] # false negative in mypy

with_descriptors.noneset_list = "a"
with_descriptors.noneset_list = 0
with_descriptors.noneset_list = 0.0
with_descriptors.noneset_list = None
with_descriptors.noneset_list = "none"
with_descriptors.noneset_list = object()  # pyright: ignore[reportGeneralTypeIssues] # false negative in mypy
