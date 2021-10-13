from typing import Tuple

class ModulusPack:
    pack: dict[int, list[tuple[int, int]]]
    discarded: list[tuple[int, str]]
    def __init__(self) -> None: ...
    def read_file(self, filename: str) -> None: ...
    def get_modulus(self, min: int, prefer: int, max: int) -> tuple[int, int]: ...
