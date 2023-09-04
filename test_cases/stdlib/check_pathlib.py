# pyright: strict
from __future__ import annotations

from pathlib import Path

if Path("asdf") == "asdf":  # type: ignore
    ...
