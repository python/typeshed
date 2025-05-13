from typing import Any, Literal, Iterator, final

__all__ = ["Interpolation", "Template"]

@final
class Template:
    strings: tuple[str, ...]
    interpolations: tuple[Interpolation, ...]

    def __new__(cls, *args: str | Interpolation) -> Template: ...
    def __iter__(self) -> Iterator[str | Interpolation]: ...
    def __add__(self, other: Template | str) -> Template: ...
    @property
    def values(self) -> tuple[Any, ...]: ...

@final
class Interpolation:
    value: Any  # TODO: consider making `Interpolation` generic in runtime
    expression: str
    conversion: Literal["a", "r", "s"] | None
    format_spec: str

    __match_args__ = ("value", "expression", "conversion", "format_spec")

    def __new__(
        cls, value: Any, expression: str, conversion: Literal["a", "r", "s"] | None = None, format_spec: str = ""
    ) -> Interpolation: ...
