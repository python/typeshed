from collections.abc import Callable


class CheckpointOptions:
    experimental_io_device: None | str = None
    experimental_enable_async_checkpoint: bool = False
    experimental_write_callbacks: None | list[Callable] = None
    enable_async: bool = False
