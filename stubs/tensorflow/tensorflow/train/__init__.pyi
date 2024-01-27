from _typeshed import Incomplete
from collections.abc import Callable
from typing import Any, Self

import tensorflow as tf

class CheckpointOptions:
    experimental_io_device: None | str
    experimental_enable_async_checkpoint: bool
    experimental_write_callbacks: None | list[Callable[[str], Any] | Callable[[], Any]]
    enable_async: bool
    experimental_skip_slot_variables: bool
    experimental_sharding_callback: tf.train.experimental.ShardingCallback | None = None,

    def __init__(
        self,
        experimental_io_device: None | str = None,
        experimental_enable_async_checkpoint: bool = False,
        experimental_write_callbacks: None | list[Callable[[str], Any] | Callable[[], Any]] = None,
        enable_async: bool = False,
        experimental_skip_slot_variables: bool = False,
        experimental_sharding_callback: tf.train.experimental.ShardingCallback | None = None,
    ) -> None: ...
    def __copy__(self) -> Self: ...

def __getattr__(name: str) -> Incomplete: ...
