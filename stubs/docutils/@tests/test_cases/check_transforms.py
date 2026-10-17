from __future__ import annotations

from typing import Any

from docutils.transforms import Transform

# `apply()` overrides should be accepted with and without kwargs,
# True keyword arguments (and positional) should error.


class DocutilsStyle(Transform):
    def apply(self) -> None: ...


class SphinxStyle(Transform):
    def apply(self, **kwargs: Any) -> None: ...


class RequiredKeyword(Transform):
    def apply(self, *, level: int) -> None: ...  # type: ignore[override]


def apply(transform: Transform) -> None:
    transform.apply()
    transform.apply(level=1)  # type: ignore[call-arg]
