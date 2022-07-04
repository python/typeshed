from _typeshed import Incomplete

from dask.callbacks import Callback  # type: ignore

class TqdmCallback(Callback):
    tqdm_class: Incomplete
    def __init__(
        self, start: Incomplete | None = ..., pretask: Incomplete | None = ..., tqdm_class=..., **tqdm_kwargs
    ) -> None: ...
    def display(self) -> None: ...
