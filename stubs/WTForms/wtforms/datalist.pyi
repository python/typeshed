from dataclasses import dataclass
from enum import EnumMeta
from typing import Any, Protocol, type_check_only

from markupsafe import Markup
from wtforms.fields import Field

@type_check_only
class _DataListWidget(Protocol):
    def __call__(self, datalist: DataList, /, *, field: Field | None = None, **kwargs: Any) -> Markup: ...

__all__ = ("DataList", "DataListChoice", "enum_datalist")

@dataclass
class DataListChoice:
    value: str
    label: str | None = ...
    render_kw: dict[str, Any] = ...
    def __post_init__(self) -> None: ...
    def __iter__(self): ...
    @classmethod
    def from_input(cls, input): ...

def enum_datalist(enum_cls: EnumMeta, *, by: str = "value", label: str | None = None) -> DataList: ...

class DataList:
    widget: _DataListWidget
    render_kw: dict[str, Any]
    id: str | None
    def __init__(
        self, choices=None, *, render_kw: dict[str, Any] | None = None, widget: _DataListWidget | None = None
    ) -> None: ...
    def iter_choices(self, field: Field | None = None) -> list[DataListChoice]: ...
    def __call__(self, field: Field | None = None, **kwargs: Any) -> Markup: ...
