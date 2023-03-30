# TODO: Don't forget to re-enable before PR
# mypy: disable-error-code=assert-type
from __future__ import annotations

from typing import Any, List, Tuple, Union
from typing_extensions import Literal, assert_type

from openpyxl.descriptors.base import Descriptor, Length, NoneSet, Set, Typed
from openpyxl.descriptors.serialisable import Serialisable


class WithDescriptors(Serialisable):
    descriptor = Descriptor[str]()

    typed_default = Typed(expected_type=str)
    typed_not_none = Typed(expected_type=str, allow_none=False)
    typed_none = Typed(expected_type=str, allow_none=True)

    set_tuple = Set(values=("a", 1, 0.0))
    set_list = Set(values=["a", 1, 0.0])
    set_tuple_none = Set(values=("a", 1, 0.0, None))

    noneset_tuple = NoneSet(values=("a", 1, 0.0))
    noneset_list = NoneSet(values=["a", 1, 0.0])

    length_list = Length[List[str]](length=1)
    length_tuple = Length[Tuple[str, str]](length=1)  # Can't validate tuple length in a generic manner
    length_invalid = Length[object](length=1)  # type: ignore

    # Test inferred annotation
    assert_type(descriptor, Descriptor[str])

    assert_type(typed_default, Typed[str, Literal[False]])
    assert_type(typed_not_none, Typed[str, Literal[False]])
    assert_type(typed_none, Typed[str, Literal[True]])

    assert_type(set_tuple, Set[Union[Literal["a", 1], float]])
    assert_type(set_list, Set[Union[str, int, float]])  # Literals are [generified, *idk the right word] in non-tuples
    assert_type(set_tuple_none, Set[Union[Literal["a", 1, None], float]])

    assert_type(noneset_tuple, NoneSet[Union[Literal["a", 1], float]])
    assert_type(noneset_list, NoneSet[Union[str, float]])  # int and float are merged in generic unions

    assert_type(noneset_tuple, NoneSet[Union[Literal["a", 1], float]])

    assert_type(length_list, Length[list[str]])
    assert_type(length_tuple, Length[tuple[str, str]])


with_descriptors = WithDescriptors()


# Test with missing subclass
class NotSerialisable:
    descriptor = Descriptor[Any]()


NotSerialisable().descriptor = None  # type: ignore


# Test getters
assert_type(with_descriptors.descriptor, str)

assert_type(with_descriptors.typed_default, str)
assert_type(with_descriptors.typed_none, Union[str, None])

assert_type(with_descriptors.set_tuple, Union[Literal["a", 1], float])
assert_type(with_descriptors.set_tuple_none, Union[Literal["a", 1, None], float])
assert_type(with_descriptors.set_list, Union[str, int, float])  # Literals are [generified, *idk the right word] in non-tuples
assert_type(with_descriptors.set_tuple_none, Union[Literal["a", 1, None], float])

assert_type(with_descriptors.noneset_tuple, Union[Literal["a", 1], float, None])
assert_type(with_descriptors.noneset_list, Union[str, float, None])  # int and float are merged in generic unions

assert_type(with_descriptors.length_list, list[str])
assert_type(with_descriptors.length_tuple, tuple[str, str])


# Test setters (expected type, None, unexpected type)
with_descriptors.descriptor = ""
with_descriptors.descriptor = None  # type: ignore
with_descriptors.descriptor = 0  # type: ignore

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

# NOTE: Can't validate tuple length in a generic manner
with_descriptors.length_list = ["a", "a"]
with_descriptors.length_list = None  # type: ignore
with_descriptors.length_list = ("a", "a")  # type: ignore
with_descriptors.length_list = ""  # type: ignore
with_descriptors.length_tuple = ("a", "a")
with_descriptors.length_tuple = None  # type: ignore
with_descriptors.length_tuple = ["a", "a"]  # type: ignore
with_descriptors.length_tuple = ""  # type: ignore
