import sys
from typing import Tuple

if sys.platform == "win32":

    ActionText: list[tuple[str, str, str | None]]
    UIText: list[tuple[str, str | None]]

    tables: list[str]
