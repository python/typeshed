import abc
from typing import Any

from ...._types import Box
from ....main import ActiveWithNeighbors
from ...base import BaseImage

class QRModuleDrawer(abc.ABC, metaclass=abc.ABCMeta):
    needs_neighbors: bool = False
    def __init__(self, **kwargs: Any) -> None: ...
    img: BaseImage
    def initialize(self, img: BaseImage) -> None: ...
    @abc.abstractmethod
    def drawrect(self, box: Box, is_active: bool | ActiveWithNeighbors) -> None: ...
