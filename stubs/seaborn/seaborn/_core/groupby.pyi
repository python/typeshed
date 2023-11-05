from _typeshed import Incomplete
from collections.abc import Callable, Hashable, Mapping
from typing import Any
from typing_extensions import Concatenate, ParamSpec, TypeAlias

from numpy import ufunc
from pandas import DataFrame
from pandas._typing import HashableT

# pandas._typing.AggFuncTypeFrame is partially Unknown: https://github.com/pandas-dev/pandas-stubs/issues/811
_AggFuncTypeBase: TypeAlias = Callable[..., Any] | str | ufunc
_AggFuncTypeDictFrame: TypeAlias = Mapping[HashableT, _AggFuncTypeBase | list[_AggFuncTypeBase]]
_AggFuncTypeFrame: TypeAlias = _AggFuncTypeBase | list[_AggFuncTypeBase] | _AggFuncTypeDictFrame[HashableT]

_P = ParamSpec("_P")

class GroupBy:
    order: dict[str, list[Incomplete] | None]
    def __init__(self, order: list[str] | dict[str, list[Incomplete] | None]) -> None: ...
    # Signature based on pandas.core.groupby.generic.DataFrameGroupBy.aggregate
    # args and kwargs possible values depend on func which itself can be
    # an attribute name, a mapping, a callable, or lead to a jitted numba function
    def agg(
        self,
        data: DataFrame,
        func: _AggFuncTypeFrame[Hashable] = ...,
        *args: Any,
        engine: str | None = None,
        engine_kwargs: dict[str, bool] | None = None,
        **kwargs: Any,
    ) -> DataFrame: ...
    def apply(
        self, data: DataFrame, func: Callable[Concatenate[DataFrame, _P], DataFrame], *args: _P.args, **kwargs: _P.kwargs
    ) -> DataFrame: ...
