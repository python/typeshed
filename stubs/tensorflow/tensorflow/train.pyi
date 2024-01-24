from collections.abc import Callable
from typing import Any

class CheckpointOptions:
    experimental_io_device: None | str = None
    experimental_enable_async_checkpoint: bool = False
    experimental_write_callbacks: None | list[Callable[[str], Any] | Callable[[], Any]] = None
    enable_async: bool = False
