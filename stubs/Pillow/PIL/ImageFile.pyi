from typing import Any

from .Image import Image

class ImageFile(Image):
    def __getattr__(self, __item: str) -> Any: ...  # incomplete

def __getattr__(__name: str) -> Any: ...  # incomplete
