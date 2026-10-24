from __future__ import annotations

from collections.abc import Callable, Sequence
from typing import ClassVar

from docutils import nodes
from docutils.parsers.rst import Directive, directives
from docutils.parsers.rst.directives.body import Rubric, Topic
from docutils.parsers.rst.directives.images import Figure
from docutils.parsers.rst.directives.tables import CSVTable


# `option_spec` should accept any mapping.
# This should include `dict` subclasses with narrower converters.
class DummyOptionSpec(dict[str, Callable[[str], str]]):
    def __bool__(self) -> bool:
        return True


class AnyOptions(Directive):
    option_spec = DummyOptionSpec()


# Concrete directives have a `dict` option spec that should be extendable.
class Exercise(Topic):
    option_spec: ClassVar[dict[str, Callable[[str], object]]] = {**Topic.option_spec, "difficulty": directives.nonnegative_int}


class MyFigure(Figure):
    option_spec: ClassVar[dict[str, Callable[[str], object]]] = Figure.option_spec.copy()
    option_spec["caption"] = directives.unchanged

    # Overrides should be able to return a (narrower) sequence of nodes.
    def run(self) -> Sequence[nodes.Node]:
        return super().run()


class MyRubric(Rubric):
    def run(self) -> list[nodes.rubric | nodes.system_message]:
        return []


class MyCSVTable(CSVTable):
    def run(self) -> Sequence[nodes.table | nodes.system_message]:
        return super().run()


# A directive's own `option_spec` literal should be acceptable.
class MyDirective(Directive):
    option_spec = {"class": directives.class_option, "flag": directives.flag, "count": directives.nonnegative_int}

    def run(self) -> list[nodes.Node]:
        return []
