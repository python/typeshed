from __future__ import annotations

from typing import Any
from typing_extensions import assert_type

from docutils import nodes


# Well-known attributes with stable types have `Literal`-keyed overloads.
# So, it should be able to deduce the types of certain keys.
def attributes(node: nodes.Element) -> None:
    assert_type(node["classes"], list[str])
    assert_type(node.get("classes"), list[str])
    assert_type(node.get("backrefs"), "list[str] | None")
    assert_type(node["refuri"], str)
    assert_type(node.get("refuri"), "str | None")
    assert_type(node.get("refuri", ""), str)

    # Arbitrary attributes are `Any`.
    assert_type(node.get("highlight_args", {}), Any)


# Visitor methods should be overridable with any return type.
class Visitor(nodes.SparseNodeVisitor):
    def visit_paragraph(self, node: nodes.paragraph) -> None:
        raise nodes.SkipNode

    def visit_section(self, node: nodes.Element) -> bool:
        return True


# A node's parent may be `None`; the root document never has one.
def parents(document: nodes.document, paragraph: nodes.paragraph) -> None:
    assert_type(document.parent, None)
    assert_type(paragraph.parent, "nodes.Element | None")
    if paragraph.parent is not None:
        paragraph.parent.remove(paragraph)


# Visit/depart methods do not exist on the base `NodeVisitor` at runtime.
# The methods only exist when a subclass defines them.
class DirectVisitor(nodes.NodeVisitor):
    def visit_paragraph(self, node: nodes.paragraph) -> None:
        # Pyright correctly flags this as not existing NodeVisitor.
        super().visit_paragraph(node)  # pyright: ignore[reportGeneralTypeIssues]


class SparseVisitor(nodes.SparseNodeVisitor):
    # Pyright correctly allows this because it is concretely defined
    # in SparseNodeVisitor.
    def visit_paragraph(self, node: nodes.paragraph) -> None:
        super().visit_paragraph(node)
