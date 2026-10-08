from collections.abc import Callable, Sequence
from typing import Any, ClassVar, Final, Literal, NamedTuple, Protocol, TypeAlias, TypedDict, type_check_only
from typing_extensions import Self

from docutils.frontend import _OptionValidator
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

# Docutil's frontend options.
#
# The keywords are :const:`optparse.Option.ATTRS` and docutils'
# extensions "validator" and "overrides".
@type_check_only
class _OptionKwargs(TypedDict, total=False):
    action: str
    type: str
    dest: str
    default: object
    nargs: int
    const: object
    choices: Sequence[str]
    callback: Callable[..., object]
    callback_args: tuple[object, ...]
    callback_kwargs: dict[str, object]
    help: str
    metavar: str
    validator: _OptionValidator
    overrides: str

# Option tuple holding: (help text, option strings, keyword arguments).
_OptionTuple: TypeAlias = tuple[str, list[str], _OptionKwargs]
# A flat sequence of (group title, group description, options) tuples.
_SettingsSpecTuple: TypeAlias = tuple[str | Sequence[_OptionTuple] | None, ...]

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
