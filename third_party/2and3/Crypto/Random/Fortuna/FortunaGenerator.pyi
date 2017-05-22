from typing import Any

__revision__ = ...  # type: str

class AESGenerator:
    block_size = ...  # type: Any
    key_size = ...  # type: int
    max_blocks_per_request = ...  # type: Any
    counter = ...  # type: Any
    key = ...  # type: Any
    block_size_shift = ...  # type: Any
    blocks_per_key = ...  # type: Any
    max_bytes_per_request = ...  # type: Any
    def __init__(self) -> None: ...
    def reseed(self, seed): ...
    def pseudo_random_data(self, bytes): ...
