from pathlib import Path

from .enums import Align as Align, TextMode as TextMode, XPos as XPos, YPos as YPos
from .fonts import FontFace as FontFace, TextStyle as TextStyle
from .fpdf import FPDF as FPDF, FPDFException as FPDFException, TitleStyle as TitleStyle
from .html import HTML2FPDF as HTML2FPDF, HTMLMixin as HTMLMixin
from .prefs import ViewerPreferences as ViewerPreferences
from .template import FlexTemplate as FlexTemplate, Template as Template

__license__: str
__version__: str
FPDF_VERSION: str
FPDF_FONT_DIR: Path

__all__ = [
    "FPDF",
    "FPDF_FONT_DIR",
    "FPDF_VERSION",
    "HTML2FPDF",
    "Align",
    "FPDFException",
    "FlexTemplate",
    "FontFace",
    "HTMLMixin",
    "Template",
    "TextMode",
    "TextStyle",
    "TitleStyle",
    "ViewerPreferences",
    "XPos",
    "YPos",
    "__license__",
    "__version__",
]
