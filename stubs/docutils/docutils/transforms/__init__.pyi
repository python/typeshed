from collections.abc import Iterable, Mapping
from typing import Any, ClassVar, Final, TypeAlias

from docutils import ApplicationError, TransformSpec, nodes
from docutils.languages import LanguageModule

_TransformTuple: TypeAlias = tuple[str, type[Transform], nodes.Node | None, dict[str, Any]]

__docformat__: Final = "reStructuredText"

class TransformError(ApplicationError): ...

class Transform:
    default_priority: ClassVar[int | None]
    document: nodes.document
    startnode: nodes.Node | None
    language: LanguageModule
    def __init__(self, document: nodes.document, startnode: nodes.Node | None = None) -> None: ...
    # The base method accepts (and ignores) `**kwargs` at runtime, so that `Transformer`
    # can pass on the keyword arguments given to `add_transform()`. These are never used
    # in practice, and docutils' own transforms don't accept any, so the stub declares the
    # call that all transforms support; subclasses may still accept optional keywords.
    def apply(self) -> None: ...

class Transformer(TransformSpec):
    transforms: list[_TransformTuple]
    document: nodes.document
    applied: list[_TransformTuple]
    sorted: bool
    components: Mapping[str, TransformSpec]
    serialno: int
    def __init__(self, document: nodes.document) -> None: ...
    def add_transform(self, transform_class: type[Transform], priority: int | None = None, **kwargs: object) -> None: ...
    def add_transforms(self, transform_list: Iterable[type[Transform]]) -> None: ...
    def add_pending(self, pending: nodes.pending, priority: int | None = None) -> None: ...
    def get_priority_string(self, priority: int) -> str: ...
    def populate_from_components(self, components: Iterable[TransformSpec]) -> None: ...
    def apply_transforms(self) -> None: ...
