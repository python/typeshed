from _typeshed import SupportsItems
from collections.abc import Iterable, Iterator, Mapping, Sequence
from typing import Any, ClassVar

from wtforms.fields.core import Field, UnboundField
from wtforms.meta import DefaultMeta, _MultiDictLike

class BaseForm:
    meta: DefaultMeta
    form_errors: list[str]
    # we document this, because it's the only efficient way to introspect
    # the field names of the form, it also seems to be stable API-wise
    _fields: dict[str, Field]
    def __init__(
        self,
        fields: SupportsItems[str, UnboundField[Any]] | Iterable[tuple[str, UnboundField[Any]]],
        prefix: str = "",
        meta: DefaultMeta = ...,
    ) -> None: ...
    def __iter__(self) -> Iterator[Field]: ...
    def __contains__(self, name: str) -> bool: ...
    def __getitem__(self, name: str) -> Field: ...
    def __setitem__(self, name: str, value: UnboundField[Any]) -> None: ...
    def __delitem__(self, name: str) -> None: ...
    def populate_obj(self, obj: object) -> None: ...
    # while we would like to be more strict on extra_filters, we can't easily do that
    # without it being annoying in most situations
    def process(
        self,
        formdata: _MultiDictLike | None = None,
        obj: object | None = None,
        data: Mapping[str, Any] | None = None,
        extra_filters: Mapping[str, Sequence[Any]] | None = None,
        **kwargs: object,
    ) -> None: ...
    # same thing here with extra_validators
    def validate(self, extra_validators: Mapping[str, Sequence[Any]] | None = None) -> bool: ...
    @property
    def data(self) -> dict[str, Any]: ...
    @property
    def errors(self) -> dict[str | None, Sequence[str]]: ...

class FormMeta(type):
    def __init__(cls, name: str, bases: Sequence[type[object]], attrs: Mapping[str, Any]) -> None: ...
    def __call__(cls, *args: Any, **kwargs: Any) -> Any: ...
    def __setattr__(cls, name: str, value: object) -> None: ...
    def __delattr__(cls, name: str) -> None: ...

class Form(BaseForm, metaclass=FormMeta):
    # due to the metaclass this should always be a subclass of DefaultMeta
    # but if we annotate this as such, then subclasses cannot use it in the
    # intended way
    Meta: ClassVar[type[Any]]
    # this attribute is documented, so we annotate it
    _unbound_fields: ClassVar[list[tuple[str, UnboundField[Any]]]]
    def __init__(
        self,
        formdata: _MultiDictLike | None = None,
        obj: object | None = None,
        prefix: str = "",
        data: Mapping[str, Any] | None = None,
        meta: Mapping[str, Any] | None = None,
        *,
        # same issue as with process
        extra_filters: Mapping[str, Sequence[Any]] | None = None,
        **kwargs: object,
    ) -> None: ...
    # this should emit a type_error, since it's not allowed to be called
    def __setitem__(self, name: str, value: None) -> None: ...  # type: ignore[override]
    def __delitem__(self, name: str) -> None: ...
    def __delattr__(self, name: str) -> None: ...
