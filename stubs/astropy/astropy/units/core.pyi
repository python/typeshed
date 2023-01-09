from _typeshed import Incomplete
from numbers import Real
from typing import Any

from astropy.utils.exceptions import AstropyWarning

class _UnitRegistry:  # undocumented
    def __init__(self, init=..., equivalencies=..., aliases=...) -> None: ...
    @property
    def registry(self): ...
    @property
    def all_units(self): ...
    @property
    def non_prefix_units(self): ...
    def set_enabled_units(self, units): ...
    def add_enabled_units(self, units) -> None: ...
    def get_units_with_physical_type(self, unit): ...
    @property
    def equivalencies(self): ...
    def set_enabled_equivalencies(self, equivalencies): ...
    def add_enabled_equivalencies(self, equivalencies) -> None: ...
    @property
    def aliases(self): ...
    def set_enabled_aliases(self, aliases) -> None: ...
    def add_enabled_aliases(self, aliases) -> None: ...

class _UnitContext:  # undocumented
    def __init__(self, init=..., equivalencies=...) -> None: ...
    def __enter__(self) -> None: ...
    def __exit__(self, type, value, tb) -> None: ...

def get_current_unit_registry(): ...
def set_enabled_units(units) -> _UnitContext: ...
def add_enabled_units(units) -> _UnitContext: ...
def set_enabled_equivalencies(equivalencies) -> _UnitContext: ...
def add_enabled_equivalencies(equivalencies) -> _UnitContext: ...
def set_enabled_aliases(aliases) -> _UnitContext: ...
def add_enabled_aliases(aliases) -> _UnitContext: ...

class UnitsError(Exception): ...
class UnitScaleError(UnitsError, ValueError): ...
class UnitConversionError(UnitsError, ValueError): ...
class UnitTypeError(UnitsError, TypeError): ...
class UnitsWarning(AstropyWarning): ...

class UnitBase:
    __array_priority__: int
    def __deepcopy__(self, memo: Any) -> UnitBase: ...
    def __bytes__(self) -> bytes: ...
    @property
    def names(self) -> None: ...
    @property
    def name(self) -> None: ...
    @property
    def aliases(self) -> None: ...
    @property
    def scale(self) -> Real: ...
    @property
    def bases(self) -> list[UnitBase]: ...
    @property
    def powers(self) -> list[Real]: ...
    def to_string(self, format=...): ...
    def __format__(self, format_spec) -> str: ...
    def __pow__(self, p: Real) -> CompositeUnit: ...
    def __truediv__(self, m): ...
    def __rtruediv__(self, m): ...
    def __mul__(self, m): ...
    def __rmul__(self, m): ...
    def __rlshift__(self, m): ...
    def __rrshift__(self, m): ...
    def __hash__(self): ...
    def __eq__(self, other) -> bool: ...
    def __ne__(self, other) -> bool: ...
    def __le__(self, other) -> bool: ...
    def __ge__(self, other) -> bool: ...
    def __lt__(self, other) -> bool: ...
    def __gt__(self, other) -> bool: ...
    def __neg__(self): ...
    def is_equivalent(self, other, equivalencies=...): ...
    def to(self, other, value=..., equivalencies=...): ...
    def in_units(self, other, value: float = ..., equivalencies=...): ...
    def decompose(self, bases=...) -> None: ...
    def compose(
        self,
        equivalencies=...,
        units: Incomplete | None = ...,
        max_depth: int = ...,
        include_prefix_units: Incomplete | None = ...,
    ): ...
    def to_system(self, system): ...
    @property
    def si(self): ...
    @property
    def cgs(self): ...
    @property
    def physical_type(self): ...

    class EquivalentUnitsList(list[UnitBase]):
        HEADING_NAMES: Incomplete
        ROW_LEN: int
        NO_EQUIV_UNITS_MSG: str
    def find_equivalent_units(self, equivalencies=..., units: Incomplete | None = ..., include_prefix_units: bool = ...): ...
    def is_unity(self): ...

class NamedUnit(UnitBase):
    __doc__: Incomplete
    def __init__(
        self, st, doc: Incomplete | None = ..., format: Incomplete | None = ..., namespace: Incomplete | None = ...
    ) -> None: ...
    def get_format_name(self, format): ...
    @property
    def names(self): ...
    @property
    def name(self): ...
    @property
    def aliases(self): ...
    @property
    def short_names(self): ...
    @property
    def long_names(self): ...

class IrreducibleUnit(NamedUnit):
    def __reduce__(self): ...
    @property
    def represents(self): ...
    def decompose(self, bases=...): ...

class UnrecognizedUnit(IrreducibleUnit):
    __reduce__: Incomplete
    def __bytes__(self) -> bytes: ...
    def to_string(self, format: Incomplete | None = ...): ...
    __pow__: Incomplete
    __truediv__: Incomplete
    __rtruediv__: Incomplete
    __mul__: Incomplete
    __rmul__: Incomplete
    __lt__: Incomplete
    __gt__: Incomplete
    __le__: Incomplete
    __ge__: Incomplete
    __neg__: Incomplete
    def __eq__(self, other): ...
    def __ne__(self, other): ...
    def is_equivalent(self, other, equivalencies: Incomplete | None = ...): ...
    def get_format_name(self, format): ...
    def is_unity(self): ...

class _UnitMetaClass(type):
    def __call__(
        self,
        s: str = ...,
        represents: Incomplete | None = ...,
        format: Incomplete | None = ...,
        namespace: Incomplete | None = ...,
        doc: Incomplete | None = ...,
        parse_strict: str = ...,
    ): ...

class Unit(NamedUnit, metaclass=_UnitMetaClass):
    def __init__(
        self,
        st,
        represents: Incomplete | None = ...,
        doc: Incomplete | None = ...,
        format: Incomplete | None = ...,
        namespace: Incomplete | None = ...,
    ) -> None: ...
    @property
    def represents(self): ...
    def decompose(self, bases=...): ...
    def is_unity(self): ...
    def __hash__(self): ...

class PrefixUnit(Unit): ...

class CompositeUnit(UnitBase):
    def __init__(self, scale, bases, powers, decompose: bool = ..., decompose_bases=..., _error_check: bool = ...) -> None: ...
    @property
    def scale(self): ...
    @property
    def bases(self): ...
    @property
    def powers(self): ...
    def __copy__(self): ...
    def decompose(self, bases=...): ...
    def is_unity(self): ...

def def_unit(
    s,
    represents: Incomplete | None = ...,
    doc: Incomplete | None = ...,
    format: Incomplete | None = ...,
    prefixes: bool = ...,
    exclude_prefixes=...,
    namespace: Incomplete | None = ...,
): ...

dimensionless_unscaled: Incomplete
one = dimensionless_unscaled
