from .fpdf import FPDF as FPDF, TitleStyle as TitleStyle
from .html import HTML2FPDF as HTML2FPDF, HTMLMixin as HTMLMixin
from .template import Template as Template
from pathlib import Path
from typing import Any

__license__: str
__version__: str
FPDF_VERSION: str
FPDF_FONT_DIR: Path
