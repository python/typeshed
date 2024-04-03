from _typeshed import Incomplete

def format_datetime(value, datetime_format): ...

class Widget:
    def clean(self, value, row: Incomplete | None = None, **kwargs): ...
    def render(self, value, obj: Incomplete | None = None): ...

class NumberWidget(Widget):
    coerce_to_string: Incomplete
    def __init__(self, coerce_to_string: bool = False) -> None: ...
    def is_empty(self, value): ...
    def render(self, value, obj: Incomplete | None = None): ...

class FloatWidget(NumberWidget):
    def clean(self, value, row: Incomplete | None = None, **kwargs): ...

class IntegerWidget(NumberWidget):
    def clean(self, value, row: Incomplete | None = None, **kwargs): ...

class DecimalWidget(NumberWidget):
    def clean(self, value, row: Incomplete | None = None, **kwargs): ...

class CharWidget(Widget):
    coerce_to_string: Incomplete
    allow_blank: Incomplete
    def __init__(self, coerce_to_string: bool = False, allow_blank: bool = False) -> None: ...
    def clean(self, value, row: Incomplete | None = None, **kwargs): ...

class BooleanWidget(Widget):
    TRUE_VALUES: Incomplete
    FALSE_VALUES: Incomplete
    NULL_VALUES: Incomplete
    def render(self, value, obj: Incomplete | None = None): ...
    def clean(self, value, row: Incomplete | None = None, **kwargs): ...

class DateWidget(Widget):
    formats: Incomplete
    def __init__(self, format: Incomplete | None = None) -> None: ...
    def clean(self, value, row: Incomplete | None = None, **kwargs): ...
    def render(self, value, obj: Incomplete | None = None): ...

class DateTimeWidget(Widget):
    formats: Incomplete
    def __init__(self, format: Incomplete | None = None) -> None: ...
    def clean(self, value, row: Incomplete | None = None, **kwargs): ...
    def render(self, value, obj: Incomplete | None = None): ...

class TimeWidget(Widget):
    formats: Incomplete
    def __init__(self, format: Incomplete | None = None) -> None: ...
    def clean(self, value, row: Incomplete | None = None, **kwargs): ...
    def render(self, value, obj: Incomplete | None = None): ...

class DurationWidget(Widget):
    def clean(self, value, row: Incomplete | None = None, **kwargs): ...
    def render(self, value, obj: Incomplete | None = None): ...

class SimpleArrayWidget(Widget):
    separator: Incomplete
    def __init__(self, separator: Incomplete | None = None) -> None: ...
    def clean(self, value, row: Incomplete | None = None, **kwargs): ...
    def render(self, value, obj: Incomplete | None = None): ...

class JSONWidget(Widget):
    def clean(self, value, row: Incomplete | None = None, **kwargs): ...
    def render(self, value, obj: Incomplete | None = None): ...

class ForeignKeyWidget(Widget):
    model: Incomplete
    field: Incomplete
    use_natural_foreign_keys: Incomplete
    def __init__(self, model, field: str = "pk", use_natural_foreign_keys: bool = False, **kwargs) -> None: ...
    def get_queryset(self, value, row, *args, **kwargs): ...
    def clean(self, value, row: Incomplete | None = None, **kwargs): ...
    def render(self, value, obj: Incomplete | None = None): ...

class ManyToManyWidget(Widget):
    model: Incomplete
    separator: Incomplete
    field: Incomplete
    def __init__(self, model, separator: Incomplete | None = None, field: Incomplete | None = None, **kwargs) -> None: ...
    def clean(self, value, row: Incomplete | None = None, **kwargs): ...
    def render(self, value, obj: Incomplete | None = None): ...
