from typing import ClassVar

from docutils.parsers.rst import Directive

class Image(Directive):

    align_h_values: ClassVar[tuple[str, ...]]
    align_v_values: ClassVar[tuple[str, ...]]
    align_values: ClassVar[tuple[str, ...]]
    loading_values: ClassVar[tuple[str, ...]]

    def align(argument: str) -> str: ...
    def loading(argument: str) -> str: ...

class Figure(Image):
    def align(argument: str) -> str: ...
    def figwidth_value(argument: str) -> str: ...
