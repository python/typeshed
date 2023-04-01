# TODO: Don't forget to re-enable before PR
# mypy: disable-error-code=assert-type
from __future__ import annotations

from _typeshed import ReadableBuffer
from datetime import date, datetime, time
from typing import Any, List, Tuple, Union
from typing_extensions import Literal, assert_type

from openpyxl.descriptors.base import Bool, Convertible, DateTime, Descriptor, Length, MatchPattern, MinMax, NoneSet, Set, Typed
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

    match_pattern_str_default = MatchPattern(pattern="")
    match_pattern_str = MatchPattern(pattern="", allow_none=False)
    match_pattern_str_none = MatchPattern(pattern="", allow_none=True)
    match_pattern_bytes_default = MatchPattern(pattern=b"")
    match_pattern_bytes = MatchPattern(pattern=b"", allow_none=False)
    match_pattern_bytes_none = MatchPattern(pattern=b"", allow_none=True)

    convertible_default = Convertible(expected_type=int)
    convertible_not_none = Convertible(expected_type=int, allow_none=False)
    convertible_none = Convertible(expected_type=int, allow_none=True)

    # NOTE: min and max params are independent of expected_type since int and floats can always be compared together
    minmax_default = MinMax(min=0, max=0)
    minmax_float = MinMax(min=0, max=0, expected_type=float, allow_none=False)
    minmax_float_none = MinMax(min=0, max=0, expected_type=float, allow_none=True)
    minmax_int = MinMax(min=0.0, max=0.0, expected_type=int, allow_none=False)
    minmax_int_none = MinMax(min=0.0, max=0.0, expected_type=int, allow_none=True)

    boolean_default = Bool()
    boolean_not_none = Bool(allow_none=False)
    boolean_none = Bool(allow_none=True)

    datetime_default = DateTime()
    datetime_not_none = DateTime(allow_none=False)
    datetime_none = DateTime(allow_none=True)

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

    assert_type(length_list, Length[list[str]])
    assert_type(length_tuple, Length[tuple[str, str]])

    assert_type(match_pattern_str_default, MatchPattern[str, Literal[False]])
    assert_type(match_pattern_str, MatchPattern[str, Literal[False]])
    assert_type(match_pattern_str_none, MatchPattern[str, Literal[True]])
    assert_type(match_pattern_bytes_default, MatchPattern[ReadableBuffer, Literal[False]])
    assert_type(match_pattern_bytes, MatchPattern[ReadableBuffer, Literal[False]])
    assert_type(match_pattern_bytes_none, MatchPattern[ReadableBuffer, Literal[True]])

    assert_type(convertible_default, Convertible[int, Literal[False]])
    assert_type(convertible_not_none, Convertible[int, Literal[False]])
    assert_type(convertible_none, Convertible[int, Literal[True]])

    assert_type(minmax_default, MinMax[float, Literal[False]])
    assert_type(minmax_float, MinMax[float, Literal[False]])
    assert_type(minmax_float_none, MinMax[float, Literal[True]])
    assert_type(minmax_int, MinMax[int, Literal[False]])
    assert_type(minmax_int_none, MinMax[int, Literal[True]])

    assert_type(boolean_default, Bool[Literal[False]])
    assert_type(boolean_not_none, Bool[Literal[False]])
    assert_type(boolean_none, Bool[Literal[True]])

    assert_type(datetime_default, DateTime[Literal[False]])
    assert_type(datetime_not_none, DateTime[Literal[False]])
    assert_type(datetime_none, DateTime[Literal[True]])


with_descriptors = WithDescriptors()


# Test with missing subclass
class NotSerialisable:
    descriptor = Descriptor[Any]()


NotSerialisable().descriptor = None  # type: ignore


# Test getters
assert_type(with_descriptors.descriptor, str)

assert_type(with_descriptors.typed_not_none, str)
assert_type(with_descriptors.typed_none, Union[str, None])

assert_type(with_descriptors.set_tuple, Union[Literal["a", 1], float])
assert_type(with_descriptors.set_tuple_none, Union[Literal["a", 1, None], float])
assert_type(with_descriptors.set_list, Union[str, int, float])  # Literals are [generified, *idk the right word] in non-tuples
assert_type(with_descriptors.set_tuple_none, Union[Literal["a", 1, None], float])

assert_type(with_descriptors.noneset_tuple, Union[Literal["a", 1], float, None])
assert_type(with_descriptors.noneset_list, Union[str, float, None])  # int and float are merged in generic unions

assert_type(with_descriptors.length_list, list[str])
assert_type(with_descriptors.length_tuple, tuple[str, str])

assert_type(with_descriptors.match_pattern_str, str)
assert_type(with_descriptors.match_pattern_str_none, Union[str, None])
assert_type(with_descriptors.match_pattern_bytes, ReadableBuffer)
assert_type(with_descriptors.match_pattern_bytes_none, Union[ReadableBuffer, None])

assert_type(with_descriptors.convertible_not_none, int)
assert_type(with_descriptors.convertible_none, Union[int, None])

assert_type(with_descriptors.minmax_float, float)
assert_type(with_descriptors.minmax_float_none, Union[float, None])
assert_type(with_descriptors.minmax_int, int)
assert_type(with_descriptors.minmax_int_none, Union[int, None])

assert_type(with_descriptors.boolean_not_none, bool)
assert_type(with_descriptors.boolean_none, Union[bool, None])

assert_type(with_descriptors.datetime_not_none, datetime)
assert_type(with_descriptors.datetime_none, Union[datetime, None])


# Test setters (expected type, None, unexpected type)
with_descriptors.descriptor = ""
with_descriptors.descriptor = None  # type: ignore
with_descriptors.descriptor = 0  # type: ignore


with_descriptors.typed_not_none = ""
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


with_descriptors.match_pattern_str = ""
with_descriptors.match_pattern_str = b""  # type: ignore
with_descriptors.match_pattern_str = None  # pyright: ignore[reportGeneralTypeIssues] # false negative in mypy
with_descriptors.match_pattern_str = 0  # type: ignore

with_descriptors.match_pattern_str_none = ""
with_descriptors.match_pattern_str_none = b""  # type: ignore
with_descriptors.match_pattern_str_none = None
with_descriptors.match_pattern_str_none = 0  # type: ignore

with_descriptors.match_pattern_bytes = ""  # type: ignore
with_descriptors.match_pattern_bytes = b""
with_descriptors.match_pattern_bytes = None  # pyright: ignore[reportGeneralTypeIssues] # false negative in mypy
with_descriptors.match_pattern_bytes = 0  # type: ignore

with_descriptors.match_pattern_bytes_none = ""  # type: ignore
with_descriptors.match_pattern_bytes_none = b""
with_descriptors.match_pattern_bytes_none = None
with_descriptors.match_pattern_bytes_none = 0  # type: ignore


with_descriptors.convertible_not_none = 0
with_descriptors.convertible_not_none = "0"
with_descriptors.convertible_not_none = None  # pyright: ignore[reportGeneralTypeIssues] # false negative in mypy
with_descriptors.convertible_not_none = object()  # pyright: ignore[reportGeneralTypeIssues] # false negative in mypy

with_descriptors.convertible_none = 0
with_descriptors.convertible_none = "0"
with_descriptors.convertible_none = None
with_descriptors.convertible_none = object()  # FIXME: False positive(?) in pyright and mypy


with_descriptors.minmax_float = 0
with_descriptors.minmax_float = "0"
with_descriptors.minmax_float = 0.0
with_descriptors.minmax_float = None  # pyright: ignore[reportGeneralTypeIssues] # false negative in mypy
with_descriptors.minmax_float = object()  # type: ignore

with_descriptors.minmax_float_none = 0
with_descriptors.minmax_float_none = "0"
with_descriptors.minmax_float_none = 0.0
with_descriptors.minmax_float_none = None
with_descriptors.minmax_float_none = object()  # type: ignore

with_descriptors.minmax_int = 0
with_descriptors.minmax_int = "0"
with_descriptors.minmax_int = 0.0
with_descriptors.minmax_int = None  # pyright: ignore[reportGeneralTypeIssues] # false negative in mypy
with_descriptors.minmax_int = object()  # type: ignore

with_descriptors.minmax_int_none = 0
with_descriptors.minmax_int_none = "0"
with_descriptors.minmax_int_none = 0.0
with_descriptors.minmax_int_none = None
with_descriptors.minmax_int_none = object()  # type: ignore


with_descriptors.boolean_not_none = False
with_descriptors.boolean_not_none = "0"
with_descriptors.boolean_not_none = 0
with_descriptors.boolean_not_none = None  # pyright: ignore[reportGeneralTypeIssues] # false negative in mypy
with_descriptors.boolean_not_none = 0.0  # type: ignore
with_descriptors.boolean_not_none = object()  # type: ignore

with_descriptors.boolean_none = False
with_descriptors.boolean_none = "0"
with_descriptors.boolean_none = 0
with_descriptors.boolean_none = None
with_descriptors.boolean_none = 0.0  # type: ignore
with_descriptors.boolean_none = object()  # type: ignore


with_descriptors.datetime_not_none = datetime(0, 0, 0)
with_descriptors.datetime_not_none = ""
with_descriptors.datetime_not_none = None  # pyright: ignore[reportGeneralTypeIssues] # false negative in mypy
with_descriptors.datetime_not_none = 0  # type: ignore
with_descriptors.datetime_not_none = date(0, 0, 0)  # type: ignore
with_descriptors.datetime_not_none = time()  # type: ignore

with_descriptors.datetime_none = datetime(0, 0, 0)
with_descriptors.datetime_none = ""
with_descriptors.datetime_none = None
with_descriptors.datetime_none = 0  # type: ignore
with_descriptors.datetime_none = date(0, 0, 0)  # type: ignore
with_descriptors.datetime_none = time()  # type: ignore
