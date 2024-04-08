from _typeshed import Incomplete

from icalendar.caselessdict import CaselessDict

class ComponentFactory(CaselessDict):
    def __init__(self, *args, **kwargs) -> None: ...

INLINE: Incomplete

class Component(CaselessDict):
    name: Incomplete
    required: Incomplete
    singletons: Incomplete
    multiple: Incomplete
    exclusive: Incomplete
    inclusive: Incomplete
    ignore_exceptions: bool
    subcomponents: Incomplete
    errors: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...
    def __bool__(self) -> bool: ...
    __nonzero__ = __bool__
    def is_empty(self): ...
    @property
    def is_broken(self): ...
    def add(self, name, value, parameters: Incomplete | None = None, encode: int = 1) -> None: ...
    def decoded(self, name, default=[]): ...
    def get_inline(self, name, decode: int = 1): ...
    def set_inline(self, name, values, encode: int = 1) -> None: ...
    def add_component(self, component) -> None: ...
    def walk(self, name: Incomplete | None = None): ...
    def property_items(self, recursive: bool = True, sorted: bool = True): ...
    @classmethod
    def from_ical(cls, st, multiple: bool = False): ...
    def content_line(self, name, value, sorted: bool = True): ...
    def content_lines(self, sorted: bool = True): ...
    def to_ical(self, sorted: bool = True): ...
    def __eq__(self, other): ...

class Event(Component):
    name: str
    canonical_order: Incomplete
    required: Incomplete
    singletons: Incomplete
    exclusive: Incomplete
    multiple: Incomplete
    ignore_exceptions: bool

class Todo(Component):
    name: str
    required: Incomplete
    singletons: Incomplete
    exclusive: Incomplete
    multiple: Incomplete

class Journal(Component):
    name: str
    required: Incomplete
    singletons: Incomplete
    multiple: Incomplete

class FreeBusy(Component):
    name: str
    required: Incomplete
    singletons: Incomplete
    multiple: Incomplete

class Timezone(Component):
    name: str
    canonical_order: Incomplete
    required: Incomplete
    singletons: Incomplete
    def to_tz(self): ...

class TimezoneStandard(Component):
    name: str
    required: Incomplete
    singletons: Incomplete
    multiple: Incomplete

class TimezoneDaylight(Component):
    name: str
    required: Incomplete
    singletons: Incomplete
    multiple: Incomplete

class Alarm(Component):
    name: str
    required: Incomplete
    singletons: Incomplete
    inclusive: Incomplete
    multiple: Incomplete

class Calendar(Component):
    name: str
    canonical_order: Incomplete
    required: Incomplete
    singletons: Incomplete

types_factory: Incomplete
component_factory: Incomplete
