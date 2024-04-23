import abc
from _typeshed import Incomplete
from collections.abc import Callable, Iterator
from contextlib import AbstractContextManager, contextmanager
from typing import Literal
from typing_extensions import Self

import tensorflow as tf
from tensorflow._aliases import FloatArray, IntArray
from tensorflow.core.framework.graph_pb2 import GraphDef
from tensorflow.experimental.dtensor import Mesh

class SummaryWriter(metaclass=abc.ABCMeta):
    def as_default(self, step: int | None = None) -> AbstractContextManager[Self]: ...
    def close(self) -> None: ...
    def flush(self) -> None: ...
    def init(self) -> None: ...
    def set_as_default(self, step: int | None = None) -> None: ...

def audio(
    name: str,
    data: tf.Tensor,
    sample_rate: int | tf.Tensor,
    step: int | tf.Tensor | None = None,
    max_outputs: int | tf.Tensor | None = 3,
    encoding: Literal["wav"] | None = None,
    description: str | None = None,
) -> bool: ...
def create_file_writer(
    logdir: str,
    max_queue: int | None = None,
    flush_millis: int | None = None,
    filename_suffix: str | None = None,
    name: str | None = None,
    experimental_trackable: bool = False,
    experimental_mesh: Mesh | None = None,
) -> SummaryWriter: ...
def create_noop_writer() -> SummaryWriter: ...
def flush(writer: SummaryWriter | None = None, name: str | None = None) -> tf.Operation: ...
def graph(graph_data: tf.Graph | GraphDef) -> bool: ...
def histogram(
    name: str, data: tf.Tensor, step: int | None = None, buckets: int | None = None, description: str | None = None
) -> bool: ...
def image(
    name: str,
    data: tf.Tensor | FloatArray | IntArray,
    step: int | tf.Tensor | None = None,
    max_outputs: int | None = 3,
    description: str | None = None,
) -> bool: ...
@contextmanager
def record_if(condition: bool | tf.Tensor | Callable[[], bool]) -> Iterator[None]: ...
def scalar(name: str, data: float | tf.Tensor, step: int | tf.Tensor | None = None, description: str | None = None) -> bool: ...
def should_record_summaries() -> bool: ...
def text(name: str, data: str | tf.Tensor, step: int | tf.Tensor | None = None, description: str | None = None) -> bool: ...
def trace_export(name: str, step: int | tf.Tensor | None = None, profiler_outdir: str | None = None) -> None: ...
def trace_off() -> None: ...
def trace_on(graph: bool = True, profiler: bool = False, profiler_outdir: str | None = None) -> None: ...
def write(
    tag: str, tensor: tf.Tensor, step: int | tf.Tensor | None = None, metadata: Incomplete | None = None, name: str | None = None
) -> bool: ...
