from __future__ import annotations

from pathlib import Path

# make sure this causes mypy to emit a --strict-equality error,
# and pyright to report a reportUnnecessaryComparison error
if Path("asdf") == "asdf":  # type: ignore
    ...
