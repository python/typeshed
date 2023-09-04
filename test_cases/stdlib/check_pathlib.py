# pyright: strict
from pathlib import Path

if Path("asdf") == "asdf": ...  # type: ignore
