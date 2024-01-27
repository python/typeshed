from _typeshed import Incomplete
from collections.abc import Callable
from typing import Any, TypeVar, final
from typing_extensions import Self

import numpy as np
import tensorflow as tf
from google.protobuf.pyext.cpp_message import GeneratedProtocolMessageType
from tensorflow.python.trackable.base import Trackable

class CheckpointOptions:
    experimental_io_device: None | str
    experimental_enable_async_checkpoint: bool
    # experimental_write_callbacks: None | list[Callable[[str], Any] | Callable[[], Any]]
    enable_async: bool
    # experimental_skip_slot_variables: bool
    # experimental_sharding_callback: tf.train.experimental.ShardingCallback | None = None

    def __init__(
        self,
        experimental_io_device: None | str = None,
        experimental_enable_async_checkpoint: bool = False,
        # experimental_write_callbacks: None | list[Callable[[str], Any] | Callable[[], Any]] = None,
        enable_async: bool = False,
        # experimental_skip_slot_variables: bool = False,
        # experimental_sharding_callback: tf.train.experimental.ShardingCallback | None = None,
    ) -> None: ...
    # def __copy__(self) -> Self: ...

@final
class Example(GeneratedProtocolMessageType):
    features: Features

@final
class Features(GeneratedProtocolMessageType):
    feature: dict[str, Feature]

@final
class Feature(GeneratedProtocolMessageType):
    float_list: FloatList
    int64_list: Int64List
    bytes_list: BytesList

@final
class FloatList(GeneratedProtocolMessageType):
    value: list[float]

@final
class Int64List(GeneratedProtocolMessageType):
    value: list[int]

@final
class BytesList(GeneratedProtocolMessageType):
    value: list[bytes]

@final
class ServerDef(GeneratedProtocolMessageType): ...

@final
class ClusterDef(GeneratedProtocolMessageType): ...

_T = TypeVar("_T", bound=list[str] | tuple[str] | dict[int, str])

class ClusterSpec:
    def __init__(self, cluster: dict[str, _T] | ClusterDef | ClusterSpec) -> None: ...
    def as_dict(self) -> dict[str, list[str] | tuple[str] | dict[int, str]]: ...
    def num_tasks(self, job_name: str) -> int: ...

class _CheckpointLoadStatus:
    def assert_consumed(self) -> Self: ...
    def assert_existing_objects_matched(self) -> Self: ...
    def assert_nontrivial_match(self) -> Self: ...
    def expect_partial(self) -> Self: ...

class Checkpoint:
    def __init__(self, root: Trackable | None = None, **kwargs: Trackable) -> None: ...
    def read(self, save_path: str, options: CheckpointOptions | None = None) -> _CheckpointLoadStatus: ...
    def restore(self, save_path: str, options: CheckpointOptions | None = None) -> _CheckpointLoadStatus: ...
    def save(self, file_prefix: str, options: CheckpointOptions | None = None) -> str: ...
    # def sync(self) -> None: ...
    def write(self, file_prefix: str, options: CheckpointOptions | None = None) -> str: ...

class CheckpointManager:
    def __init__(
        self,
        checkpoint: Checkpoint,
        directory: str,
        max_to_keep: int,
        keep_checkpoint_every_n_hours: int | None = None,
        checkpoint_name: str = "ckpt",
        step_counter: tf.Variable | None = None,
        checkpoint_interval: int | None = None,
        init_fn: Callable[[], object] | None = None,
    ) -> None: ...
    def _sweep(self) -> None: ...

def latest_checkpoint(checkpoint_dir: str, latest_filename: str | None = None) -> str: ...
def load_variable(ckpt_dir_or_file: str, name: str) -> np.ndarray[Any, Any]: ...
def list_variables(ckpt_dir_or_file: str) -> list[tuple[str, list[int]]]: ...
def __getattr__(name: str) -> Incomplete: ...
