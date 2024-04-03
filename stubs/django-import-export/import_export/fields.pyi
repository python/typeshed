from _typeshed import Incomplete

class Field:
    empty_values: Incomplete
    attribute: Incomplete
    default: Incomplete
    column_name: Incomplete
    widget: Incomplete
    readonly: Incomplete
    saves_null_values: Incomplete
    dehydrate_method: Incomplete
    m2m_add: Incomplete
    def __init__(
        self,
        attribute: Incomplete | None = None,
        column_name: Incomplete | None = None,
        widget: Incomplete | None = None,
        default=...,
        readonly: bool = False,
        saves_null_values: bool = True,
        dehydrate_method: Incomplete | None = None,
        m2m_add: bool = False,
    ) -> None: ...
    def clean(self, data, **kwargs): ...
    def get_value(self, obj): ...
    def save(self, obj, data, is_m2m: bool = False, **kwargs) -> None: ...
    def export(self, obj): ...
    def get_dehydrate_method(self, field_name: Incomplete | None = None): ...
