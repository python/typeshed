from typing import Literal

from .YoutubeDL import YoutubeDL

class Cache:
    def __init__(self, ydl: YoutubeDL) -> None: ...
    @property
    def enabled(self) -> bool: ...
    def store(self, section: str, key: str, data: object, dtype: Literal["json"] = "json") -> None: ...
    def load(
        self,
        section: str,
        key: str,
        dtype: Literal["json"] = "json",
        default: object | None = None,
        *,
        min_ver: str | None = None,
    ) -> object: ...
    def remove(self) -> None: ...
