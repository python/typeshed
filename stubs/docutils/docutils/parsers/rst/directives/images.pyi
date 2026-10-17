from collections.abc import Callable, Sequence
from typing import ClassVar, Final

from docutils import nodes
from docutils.parsers.rst import Directive

__docformat__: Final = "reStructuredText"

# The staticmethods are technically not "@staticmethod"s.
# They, are, however, implemented without a self parameter.
# This is because docutils still supports 3.9; staticmethods did
# not support __call__ until 3.10.

# When docutils 2 is released (and 3.9 support is dropped),
# these should become truly staticmethods upstream, and the test
# suppressions corresponding to these may be removed.

class Image(Directive):
    option_spec: ClassVar[dict[str, Callable[[str], object]]]
    align_h_values: ClassVar[tuple[str, ...]]
    align_v_values: ClassVar[tuple[str, ...]]
    align_values: ClassVar[tuple[str, ...]]
    loading_values: ClassVar[tuple[str, ...]]
    @staticmethod
    def align(argument: str) -> str: ...
    @staticmethod
    def loading(argument: str) -> str: ...
    def run(self) -> Sequence[nodes.Node]: ...

class Figure(Image):
    option_spec: ClassVar[dict[str, Callable[[str], object]]]
    @staticmethod
    def align(argument: str) -> str: ...
    @staticmethod
    def figwidth_value(argument: str) -> str: ...
    def run(self) -> Sequence[nodes.Node]: ...
