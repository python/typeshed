from collections.abc import Callable, Mapping, Sequence
from typing import Any, Final, Protocol, TypeAlias, TypeVar, type_check_only
from typing_extensions import deprecated

from docutils.nodes import Node, system_message
from docutils.parsers.rst.languages import RSTLanguageModule
from docutils.parsers.rst.states import Inliner
from docutils.utils import Reporter

__docformat__: Final = "reStructuredText"
DEFAULT_INTERPRETED_ROLE: Final = "title-reference"

_T = TypeVar("_T")
_T_co = TypeVar("_T_co", covariant=True)

@type_check_only
class _SupportsCopy(Protocol[_T_co]):
    def copy(self) -> _T_co: ...

# Role functions are called by the `Inliner` with five positional arguments that differ between implementations.
# `CustomRole` additionally passes `options` and `content` as keyword arguments, so role functions must provide defaults for them.
@type_check_only
class _RoleFn(Protocol):
    def __call__(
        self,
        name: str,
        rawtext: str,
        text: str,
        lineno: int,
        inliner: Inliner,
        /,
        options: dict[str, Any] = ...,
        content: list[str] = ...,
    ) -> tuple[Sequence[Node], Sequence[system_message]]: ...

# The (optional) `options` function attribute of role functions is a mapping of option names to option conversion functions.
_RoleOptionSpec: TypeAlias = dict[str, Callable[[str], object]]

def role(
    role_name: str, language_module: RSTLanguageModule | None, lineno: int, reporter: Reporter
) -> tuple[_RoleFn | None, list[system_message]]: ...
def register_canonical_role(name: str, role_fn: _RoleFn) -> None: ...
def register_local_role(name: str, role_fn: _RoleFn) -> None: ...
def set_implicit_options(role_fn: _RoleFn) -> None: ...
def register_generic_role(canonical_name: str, node_class: type[Node]) -> None: ...

class GenericRole:
    name: str
    node_class: type[Node]
    def __init__(self, role_name: str, node_class: type[Node]) -> None: ...
    def __call__(
        self,
        role: str,
        rawtext: str,
        text: str,
        lineno: int,
        inliner: Inliner,
        options: Mapping[str, object] | None = None,
        content: Sequence[str] | None = None,
    ) -> tuple[list[Node], list[system_message]]: ...

class CustomRole:
    name: str
    base_role: _RoleFn
    options: _RoleOptionSpec | None
    content: bool | None
    supplied_options: Mapping[str, object] | None
    supplied_content: Sequence[str] | None
    def __init__(
        self,
        role_name: str,
        base_role: _RoleFn,
        options: Mapping[str, object] | None = None,
        content: Sequence[str] | None = None,
    ) -> None: ...
    def __call__(
        self,
        role: str,
        rawtext: str,
        text: str,
        lineno: int,
        inliner: Inliner,
        options: Mapping[str, object] | None = None,
        content: Sequence[str] | None = None,
    ) -> tuple[Sequence[Node], Sequence[system_message]]: ...

def generic_custom_role(
    role: str,
    rawtext: str,
    text: str,
    lineno: int,
    inliner: Inliner,
    options: Mapping[str, object] | None = None,
    content: Sequence[str] | None = None,
) -> tuple[list[Node], list[system_message]]: ...
def pep_reference_role(
    role: str,
    rawtext: str,
    text: str,
    lineno: int,
    inliner: Inliner,
    options: Mapping[str, object] | None = None,
    content: Sequence[str] | None = None,
) -> tuple[list[Node], list[system_message]]: ...
def rfc_reference_role(
    role: str,
    rawtext: str,
    text: str,
    lineno: int,
    inliner: Inliner,
    options: Mapping[str, object] | None = None,
    content: Sequence[str] | None = None,
) -> tuple[list[Node], list[system_message]]: ...
def raw_role(
    role: str,
    rawtext: str,
    text: str,
    lineno: int,
    inliner: Inliner,
    options: Mapping[str, object] | None = None,
    content: Sequence[str] | None = None,
) -> tuple[list[Node], list[system_message]]: ...
def code_role(
    role_name: str,
    rawtext: str,
    text: str,
    lineno: int,
    inliner: Inliner,
    options: Mapping[str, object] | None = None,
    content: Sequence[str] | None = None,
) -> tuple[list[Node], list[system_message]]: ...
def math_role(
    role: str,
    rawtext: str,
    text: str,
    lineno: int,
    inliner: Inliner,
    options: Mapping[str, object] | None = None,
    content: Sequence[str] | None = None,
) -> tuple[list[Node], list[system_message]]: ...
def unimplemented_role(
    role: str,
    rawtext: str,
    text: str,
    lineno: int,
    inliner: Inliner,
    options: Mapping[str, object] | None = None,
    content: Sequence[str] | None = None,
) -> tuple[list[Node], list[system_message]]: ...
@deprecated("Deprecated and will be removed in Docutils 2.0, Use `roles.normalize_options()` instead.")
def set_classes(options: dict[str, Any]) -> None: ...
@deprecated("Deprecated and will be removed in Docutils 2.0, Use `roles.normalize_options()` instead.")
def normalized_role_options(options: _SupportsCopy[dict[str, _T]] | None) -> dict[str, _T]: ...

# This returns a copy of `options` (e.g. a `dict`) with the "class" key renamed to "classes".
def normalize_options(options: _SupportsCopy[dict[str, _T]] | None) -> dict[str, _T]: ...
