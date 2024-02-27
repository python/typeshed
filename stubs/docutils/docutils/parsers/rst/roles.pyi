from collections.abc import Callable
from typing import Any
from typing_extensions import TypeAlias

import docutils.parsers.rst.states
from docutils import nodes
from docutils.languages import _LanguageModule
from docutils.nodes import Node, TextElement
from docutils.parsers.rst.states import Inliner
from docutils.utils import Reporter, SystemMessage

DEFAULT_INTERPRETED_ROLE: str

_RoleFn: TypeAlias = Callable[
    [str, str, str, int, docutils.parsers.rst.states.Inliner, dict[str, Any], list[str]],
    tuple[list[nodes.reference], list[nodes.reference]],
]

def register_canonical_role(name: str, role_fn: _RoleFn) -> None: ...
def register_local_role(name: str, role_fn: _RoleFn) -> None: ...
def role(
    role_name: str, language_module: _LanguageModule, lineno: int, reporter: Reporter
) -> tuple[_RoleFn | None, list[SystemMessage]]: ...
def set_implicit_options(role_fn: _RoleFn) -> None: ...
def register_generic_role(canonical_name: str, node_class: Node) -> None: ...

class GenericRole:
    name: str
    node_class: Node
    def __init__(self, role_name: str, node_class: type[TextElement]) -> None: ...
    def __call__(
        self,
        role: str,
        rawtext: str,
        text: str,
        lineno: int,
        inliner: Inliner,
        options: dict[str, Any] | None = None,
        content: list[str] | None = None,
    ) -> tuple[list[Node], list[SystemMessage]]: ...

class CustomRole:
    name: str
    base_role: _RoleFn | CustomRole
    options: dict[str, Any]
    content: list[str]
    supplied_options: dict[str, Any]
    supplied_content: list[str]
    def __init__(
        self, role_name: str, base_role: _RoleFn | CustomRole, options: dict[str, Any] | None = None, content: list[str] | None = None
    ) -> None: ...
    def __call__(
        self,
        role: str,
        rawtext: str,
        text: str,
        lineno: int,
        inliner: Inliner,
        options: dict[str, Any] | None = None,
        content: list[str] | None = None,
    ) -> tuple[list[Node], list[SystemMessage]]: ...

def generic_custom_role(
    role: str, rawtext: str, text: str, lineno: int, inliner: Inliner, options: dict[str, Any] | None = None, content: list[str] | None = None
) -> tuple[list[Node], list[SystemMessage]]: ...
def pep_reference_role(
    role: str, rawtext: str, text: str, lineno: int, inliner: Inliner, options: dict[str, Any] | None = None, content: list[str] | None = None
) -> tuple[list[Node], list[SystemMessage]]: ...
def rfc_reference_role(
    role: str, rawtext: str, text: str, lineno: int, inliner: Inliner, options: dict[str, Any] | None = None, content: list[str] | None = None
) -> tuple[list[Node], list[SystemMessage]]: ...
def raw_role(
    role: str, rawtext: str, text: str, lineno: int, inliner: Inliner, options: dict[str, Any] | None = None, content: list[str] | None = None
) -> tuple[list[Node], list[SystemMessage]]: ...
def code_role(
    role: str, rawtext: str, text: str, lineno: int, inliner: Inliner, options: dict[str, Any] | None = None, content: list[str] | None = None
) -> tuple[list[Node], list[SystemMessage]]: ...
def math_role(
    role: str, rawtext: str, text: str, lineno: int, inliner: Inliner, options: dict[str, Any] | None = None, content: list[str] | None = None
) -> tuple[list[Node], list[SystemMessage]]: ...
def unimplemented_role(
    role: str, rawtext: str, text: str, lineno: int, inliner: Inliner, options: dict[str, Any] | None = None, content: list[str] | None = None
) -> tuple[list[Node], list[SystemMessage]]: ...
def set_classes(options: dict[str, str]) -> None: ...
def normalized_role_options(options: dict[str, Any] | None) -> dict[str, Any]:
