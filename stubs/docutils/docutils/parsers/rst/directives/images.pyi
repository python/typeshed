from _typeshed import Incomplete
from typing import Final

from docutils.parsers.rst import Directive

__docformat__: Final = "reStructuredText"

# TODO: add Image attr using Protocol
class PIL: ...

class Image(Directive):
    align_h_values: Incomplete
    align_v_values: Incomplete
    align_values: Incomplete
    loading_values: Incomplete
    def align(argument): ...
    def loading(argument): ...

class Figure(Image):
    def align(argument): ...
    def figwidth_value(argument): ...
