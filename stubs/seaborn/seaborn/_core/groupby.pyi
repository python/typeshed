from _typeshed import Incomplete
from collections.abc import Callable
from typing import Any
from typing_extensions import Concatenate, ParamSpec

from pandas import DataFrame
from pandas._typing import (
    AggFuncTypeFrame,  # pyright: ignore[reportUnknownVariableType]  # This is for pandas-stubs to improve https://github.com/pandas-dev/pandas-stubs/issues/811
)

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
        func: AggFuncTypeFrame = ...,  # pyright: ignore[reportUnknownParameterType]  # This is for pandas-stubs to improve https://github.com/pandas-dev/pandas-stubs/issues/811
        *args: Any,
        engine: str | None = None,
        engine_kwargs: dict[str, bool] | None = None,
        **kwargs: Any,
    ) -> DataFrame: ...
    def apply(
        self, data: DataFrame, func: Callable[Concatenate[DataFrame, _P], DataFrame], *args: _P.args, **kwargs: _P.kwargs
    ) -> DataFrame: ...
