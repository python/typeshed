from _typeshed import SupportsDunderGT, SupportsDunderLT, SupportsGetItem
from collections.abc import Callable
from operator import itemgetter
from typing import Any, Tuple, TypeVar, Union

_T = TypeVar("_T")


# This should be equivalent to itemgetter.__call__
def standalone_call(obj: SupportsGetItem[int, _T]) -> _T: ...


# Regression tests for https://github.com/python/mypy/issues/14032

test_dict = min({"first": 1, "second": 2}, key=itemgetter(1))
test_items = min({"first": 1, "second": 2}.items(), key=itemgetter(1))
test_dict_standalone = min({"first": 1, "second": 2}, key=standalone_call)
test_items_standalone = min({"first": 1, "second": 2}.items(), key=standalone_call)

expected_type_form_min_param_1: Callable[[Tuple[str, int]], Union[SupportsDunderLT[Any], SupportsDunderGT[Any]]]
revealed_type_itemgetter_call: Callable[[SupportsGetItem[Any, _T]], _T]  # pyright: ignore[reportGeneralTypeIssues]

revealed_type_itemgetter_call = itemgetter(1)
expected_type_form_min_param_1 = itemgetter(1)

revealed_type_itemgetter_call = standalone_call
expected_type_form_min_param_1 = standalone_call
