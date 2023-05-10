from typing import Any, ClassVar
from typing_extensions import Literal

from .ImageFile import ImageFile, PyDecoder

b_whitespace: bytes
MODES: Any

class PpmImageFile(ImageFile):
    format: ClassVar[Literal["PPM"]]
    format_description: ClassVar[str]

class PpmPlainDecoder(PyDecoder):
    def decode(self, buffer): ...

class PpmDecoder(PyDecoder):
    def decode(self, buffer): ...
