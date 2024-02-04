from collections.abc import Callable, Iterator
from contextlib import AbstractContextManager, contextmanager
from typing_extensions import Self

import tensorflow as tf

class SummaryWriter:
    def as_default(self, step: int | None = None) -> AbstractContextManager[Self]: ...

def scalar(name: str, data: float | tf.Tensor, step: int | tf.Tensor | None = None, description: str | None = None) -> bool: ...
def histogram(
    name: str, data: tf.Tensor, step: int | None = None, buckets: int | None = None, description: str | None = None
) -> bool: ...
def graph(graph_data: tf.Graph | tf.compat.v1.GraphDef) -> bool: ...
@contextmanager
def record_if(condition: bool | tf.Tensor | Callable[[], bool]) -> Iterator[None]: ...
def create_file_writer(
    logdir: str,
    max_queue: int | None = None,
    flush_millis: int | None = None,
    filename_suffix: str | None = None,
    name: str | None = None,
    experimental_trackable: bool = False,
) -> SummaryWriter: ...
