# from fontTools.misc.loggingTools
from collections.abc import Mapping
from logging import Logger
from typing import Protocol
from typing_extensions import TypeAlias

# from fonttools.ttLib.ttGlyphSet
class _TTGlyph(Protocol):
    def __init__(self, glyphSet: _TTGlyphSet, glyphName: str) -> None: ...
    def draw(self, pen) -> None: ...
    def drawPoints(self, pen) -> None: ...

_TTGlyphSet: TypeAlias = Mapping[str, _TTGlyph]  # Simplified for our needs

# from fontTools.misc.loggingTools

class LogMixin:
    @property
    def log(self) -> Logger: ...

# from fontTools.pens.basePen
class AbstractPen:
    def moveTo(self, pt: tuple[float, float]) -> None: ...
    def lineTo(self, pt: tuple[float, float]) -> None: ...
    def curveTo(self, *points: tuple[float, float]) -> None: ...
    def qCurveTo(self, *points: tuple[float, float]) -> None: ...
    def closePath(self) -> None: ...
    def endPath(self) -> None: ...
    def addComponent(self, glyphName: str, transformation: tuple[float, float, float, float, float, float]) -> None: ...

class LoggingPen(LogMixin, AbstractPen): ...

class DecomposingPen(LoggingPen):
    skipMissingComponents: bool
    glyphSet: _TTGlyphSet | None
    def __init__(self, glyphSet: _TTGlyphSet | None) -> None: ...
    def addComponent(self, glyphName: str, transformation: tuple[float, float, float, float, float, float]) -> None: ...

class BasePen(DecomposingPen):
    def __init__(self, glyphSet: _TTGlyphSet | None = ...) -> None: ...
    def closePath(self) -> None: ...
    def endPath(self) -> None: ...
    def moveTo(self, pt: tuple[float, float]) -> None: ...
    def lineTo(self, pt: tuple[float, float]) -> None: ...
    def curveTo(self, *points: tuple[float, float]) -> None: ...
    def qCurveTo(self, *points: tuple[float, float]) -> None: ...
