from _typeshed import Incomplete
from typing import Any
from typing_extensions import TypeAlias

Callback: TypeAlias = Any  # Actually dask.callbacks.Callback
class TqdmCallback(Callback):
    tqdm_class: Incomplete
    def __init__(
        self, start: Incomplete | None = ..., pretask: Incomplete | None = ..., tqdm_class=..., **tqdm_kwargs
    ) -> None: ...
    def display(self) -> None: ...
