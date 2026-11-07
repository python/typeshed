from __future__ import annotations

from typing_extensions import assert_type
from xml.dom.minidom import Document
from xml.etree.ElementTree import Comment, ElementTree, ProcessingInstruction

document = Document()

assert_type(document.toxml(), str)
assert_type(document.toxml(encoding=None), str)
assert_type(document.toxml(encoding="UTF8"), bytes)
assert_type(document.toxml("UTF8"), bytes)
assert_type(document.toxml(standalone=True), str)
assert_type(document.toxml("UTF8", True), bytes)
assert_type(document.toxml(encoding="UTF8", standalone=True), bytes)


# Because toprettyxml can mix positional and keyword variants of the "encoding" argument, which
# determines the return type, the proper stub typing isn't immediately obvious. This is a basic
# brute-force sanity check.
# Test cases like toxml
assert_type(document.toprettyxml(), str)
assert_type(document.toprettyxml(encoding=None), str)
assert_type(document.toprettyxml(encoding="UTF8"), bytes)
assert_type(document.toprettyxml(standalone=True), str)
assert_type(document.toprettyxml(encoding="UTF8", standalone=True), bytes)
# Test cases unique to toprettyxml
assert_type(document.toprettyxml("  "), str)
assert_type(document.toprettyxml("  ", "\r\n"), str)
assert_type(document.toprettyxml("  ", "\r\n", "UTF8"), bytes)
assert_type(document.toprettyxml("  ", "\r\n", "UTF8", True), bytes)
assert_type(document.toprettyxml("  ", "\r\n", standalone=True), str)


# Regression for #14671: ET.Comment/ProcessingInstruction are valid
# element tags at runtime (insert_comments=True), so a plain Element's
# tag must be comparable with them.
def check_comment_tag(doc: ElementTree) -> None:
    for el in doc.findall("*"):
        _ = el.tag is Comment
        _ = el.tag is ProcessingInstruction


def check_comment_element() -> None:
    c = Comment("a comment")
    assert c.tag is Comment
    assert c.tag is not ProcessingInstruction
