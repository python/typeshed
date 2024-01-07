from collections.abc import Callable, Iterable, Mapping, Sequence
from typing import Any, ClassVar, Literal, NamedTuple
from typing_extensions import Self

from docutils.nodes import Node
from docutils.transforms import Transform

__docformat__: str
__version__: str
__version_details__: str

class _VersionInfo(NamedTuple):
    major: int
    minor: int
    micro: int
    releaselevel: str
    serial: int
    release: bool

class VersionInfo(_VersionInfo):
    def __new__(
        cls, major: int = 0, minor: int = 0, micro: int = 0, releaselevel: str = "final", serial: int = 0, release: bool = True
    ) -> Self: ...

__version_info__: VersionInfo

class ApplicationError(Exception): ...
class DataError(ApplicationError): ...

class SettingsSpec:
    settings_spec: ClassVar[tuple[Any, ...]]
    settings_defaults: ClassVar[Mapping[str, Any] | None]
    settings_default_overrides: ClassVar[Mapping[str, Any] | None]
    relative_path_settings: ClassVar[tuple[str, ...]]
    config_section: ClassVar[str | None]
    config_section_dependencies: ClassVar[tuple[str, ...] | None]

class TransformSpec:
    def get_transforms(self) -> Iterable[Transform]: ...
    # @deprecated("Use get_transforms() instead.")
    default_transforms: ClassVar[tuple[Transform, ...]]
    unknown_reference_resolvers: ClassVar[Sequence[Callable[[Node], bool]]]

class Component(SettingsSpec, TransformSpec):
    component_type: ClassVar[Literal['reader', 'parser', 'writer'] | None]
    supported: ClassVar[tuple[str, ...]]
    def supports(self, format: str) -> bool: ...
