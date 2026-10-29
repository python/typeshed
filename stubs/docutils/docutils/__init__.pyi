from collections.abc import Callable, Sequence
from optparse import Option
from typing import (
    Any,
    ClassVar,
    Final,
    Literal,
    NamedTuple,
    Protocol,
    TypeAlias,
    TypedDict,
    type_check_only,
)
from typing_extensions import Self

from docutils.frontend import OptionParser, _OptionValidator
from docutils.nodes import Element
from docutils.transforms import Transform

__docformat__: Final = "reStructuredText"
__version__: Final[str]

_ReleaseLevels: TypeAlias = Literal["alpha", "beta", "candidate", "final"]

@type_check_only
class _VersionInfo(NamedTuple):
    major: int
    minor: int
    micro: int
    releaselevel: _ReleaseLevels
    serial: int
    release: bool

class VersionInfo(_VersionInfo):
    __slots__ = ()
    def __new__(
        cls,
        major: int = 0,
        minor: int = 0,
        micro: int = 0,
        releaselevel: _ReleaseLevels = "final",
        serial: int = 0,
        release: bool = True,
    ) -> Self: ...

__version_info__: Final[VersionInfo]
__version_details__: Final[str]

class ApplicationError(Exception): ...
class DataError(ApplicationError): ...

# The signature `optparse` calls a "callback" action's callback with, when the option
# does not specify  `callback_args` or `callback_kwargs`; those are passed on as
# further positional and keyword argumentss. A callback that expects them
# needs a type of its own.
#
# It is offered because `_OptionKwargs` is generic over its `callback`, whose
# default, `Callable[..., object]`, means "any parameter list" -- an `Any` that reaches
# every type mentioning the TypedDict. Naming a signature keeps it out.
@type_check_only
class _OptionCallback(Protocol):
    def __call__(self, option: Option, opt_str: str, value: str, parser: OptionParser, /) -> object: ...

# Docutil's frontend options.
#
# The keywords are :const:`optparse.Option.ATTRS` and docutils'
# extensions "validator" and "overrides".
#
# `_C` defaults to what `callback` was declared as before it became a type parameter
# so the unparameterised spelling means exactly what it did before. A `TypedDict` field
# is invariant, so a spec that names a callback type would need a cast where the
# a cast where the default spelling is expected, and the other way round.
@type_check_only
class _OptionKwargs[_C: Callable[..., object] = Callable[..., object]](TypedDict, total=False):
    action: str
    type: str
    dest: str
    default: object
    nargs: int
    const: object
    choices: Sequence[str]
    callback: _C
    callback_args: tuple[object, ...]
    callback_kwargs: dict[str, object]
    help: str
    metavar: str
    validator: _OptionValidator
    overrides: str

# Option tuple holding: (help text, option strings, keyword arguments).
type _OptionTuple[_C: Callable[..., object] = Callable[..., object]] = tuple[str, list[str], _OptionKwargs[_C]]
# A flat sequence of (group title, group description, options) tuples.
type _SettingsSpecTuple[_C: Callable[..., object] = Callable[..., object]] = tuple[
    str | Sequence[_OptionTuple[_C]] | None, ...
]

class SettingsSpec:
    settings_spec: ClassVar[_SettingsSpecTuple]
    # Setting values are heterogeneous, see:
    # <https://docutils.sourceforge.io/docs/user/config.html>.
    settings_defaults: ClassVar[dict[str, Any] | None]
    settings_default_overrides: ClassVar[dict[str, Any] | None]
    relative_path_settings: ClassVar[tuple[str, ...]]
    config_section: ClassVar[str | None]
    config_section_dependencies: ClassVar[tuple[str, ...] | None]

@type_check_only
class _UnknownReferenceResolver(Protocol):
    priority: int
    def __call__(self, node: Element, /) -> bool: ...

class TransformSpec:
    def get_transforms(self) -> list[type[Transform]]: ...
    # Deprecated, use/override `get_transforms()` instead.
    # This will be removed in Docutils 2.0.
    default_transforms: ClassVar[tuple[type[Transform], ...]]
    # Deprecated, will be removed in Docutils 1.0.
    unknown_reference_resolvers: Sequence[_UnknownReferenceResolver]

class Component(SettingsSpec, TransformSpec):
    component_type: ClassVar[Literal["reader", "parser", "writer", "input", "output"] | None]
    supported: ClassVar[tuple[str, ...]]
    def supports(self, format: str) -> bool: ...
