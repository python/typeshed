from typing import Final
from typing_extensions import LiteralString

from PyInstaller import compat as compat

__all__ = ("DEFAULT_DISTPATH", "DEFAULT_SPECPATH", "DEFAULT_WORKPATH", "HOMEPATH", "PLATFORM", "__version__")
__version__: Final[str]
HOMEPATH: Final[str]
DEFAULT_SPECPATH: Final[str]
DEFAULT_DISTPATH: Final[str]
DEFAULT_WORKPATH: Final[str]
PLATFORM: Final[LiteralString]
