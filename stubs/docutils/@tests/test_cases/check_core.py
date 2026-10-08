from __future__ import annotations

from typing_extensions import assert_type

from docutils.core import publish_doctree, publish_parts

# `publish_parts()` returns writer-specific parts for the HTML and LaTeX writers.
# It should be possible to deduce key types with this knowledge.
html_parts = publish_parts("Hello", writer="html5")
assert_type(html_parts["body"], str)
assert_type(html_parts["whole"], str)
latex_parts = publish_parts("Hello", writer="latex")
assert_type(latex_parts["titledata"], str)
other_parts = publish_parts("Hello", writer="pseudoxml")
assert_type(other_parts["whole"], "str | bytes")
assert_type(other_parts.get("body"), "str | None")

# `settings_overrides` should accept any copyable mapping.
# This should include `dict`s of narrower value types.
overrides: dict[str, int] = {"report_level": 5, "halt_level": 5}
publish_doctree("x", settings_overrides=overrides)
publish_doctree("x", settings_overrides={"report_level": 5, "input_encoding": "utf-8"})


def not_a_mapping() -> None:
    publish_doctree("x", settings_overrides=[("report_level", 5)])  # type: ignore[arg-type]
