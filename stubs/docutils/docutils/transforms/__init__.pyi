from _typeshed import Incomplete
from collections.abc import Iterable, Mapping
from typing import Any, Final
from typing_extensions import TypeAlias

from docutils import ApplicationError, TransformSpec
from docutils.languages import LanguageImporter
from docutils.nodes import Node, document, pending

_TransformTuple: TypeAlias = tuple[str, type[Transform], Node | None, dict[str, Any]]

__docformat__: Final = "reStructuredText"

class TransformError(ApplicationError): ...

class Transform:
    default_priority: int | None
    document: document
    startnode: Node | None
    language: LanguageImporter
    def __init__(self, document: document, startnode: Node | None = None) -> None: ...
    def __getattr__(self, name: str, /) -> Incomplete: ...

class Transformer(TransformSpec):
    transforms: list[_TransformTuple]
    unknown_reference_resolvers: list[Incomplete]
    document: document
    applied: list[_TransformTuple]
    sorted: bool
    components: Mapping[str, TransformSpec]
    serialno: int
    def __init__(self, document: document): ...
    def add_transform(self, transform_class: type[Transform], priority: int | None = None, **kwargs) -> None: ...
    def add_transforms(self, transform_list: Iterable[type[Transform]]) -> None: ...
    def add_pending(self, pending: pending, priority: int | None = None) -> None: ...
    def get_priority_string(self, priority: int) -> str: ...
    def populate_from_components(self, components: Iterable[TransformSpec]) -> None: ...
    def apply_transforms(self) -> None: ...
