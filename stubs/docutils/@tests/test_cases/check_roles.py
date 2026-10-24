from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import Any
from typing_extensions import assert_type

from docutils import nodes
from docutils.parsers.rst import roles
from docutils.parsers.rst.states import Inliner

# Docutils calls Role functions with five positional arguments, so the names do not matter.
# `options` and `content` are passed as keyword-only by `CustomRole`, so they must have defaults.


def role_with_defaults(
    name: str,
    rawtext: str,
    text: str,
    lineno: int,
    inliner: Inliner,
    options: Mapping[str, Any] | None = None,
    content: Sequence[str] | None = None,
) -> tuple[list[nodes.Node], list[nodes.system_message]]:
    return [], []


def role_with_dict_defaults(
    typ: str, rawtext: str, text: str, lineno: int, inliner: Inliner, options: dict[str, Any] = {}, content: list[str] = []
) -> tuple[list[nodes.reference], list[nodes.system_message]]:
    return [], []


def role_without_defaults(
    name: str, rawtext: str, text: str, lineno: int, inliner: Inliner, options: dict[str, Any], content: list[str]
) -> tuple[list[nodes.Node], list[nodes.system_message]]:
    return [], []


roles.register_local_role("a", role_with_defaults)
roles.register_local_role("b", role_with_dict_defaults)
roles.register_local_role("c", role_without_defaults)  # type: ignore[arg-type]
roles.register_canonical_role("d", roles.GenericRole("d", nodes.emphasis))

# `normalize_options()` should preserve the value type of the options.
assert_type(roles.normalize_options({"class": ["a"]}), dict[str, list[str]])
