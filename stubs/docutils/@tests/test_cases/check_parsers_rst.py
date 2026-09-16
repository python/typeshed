from typing import Any
from typing_extensions import TypedDict, assert_type

from docutils import nodes
from docutils.parsers.rst import Directive


class Options(TypedDict):
    language: str
    count: int


class CustomDirective(Directive[Options]):
    def run(self) -> list[nodes.Node]:
        assert_type(self.options, Options)
        assert_type(self.options["language"], str)
        assert_type(self.options["count"], int)
        return []


class DefaultDirective(Directive):
    def run(self) -> list[nodes.Node]:
        assert_type(self.options, dict[str, Any])
        return []
