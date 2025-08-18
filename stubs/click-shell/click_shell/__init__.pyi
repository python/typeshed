from typing import Final

from .core import Shell, make_click_shell
from .decorators import shell

__all__ = ["make_click_shell", "shell", "Shell", "__version__"]
__version__: Final[str]
