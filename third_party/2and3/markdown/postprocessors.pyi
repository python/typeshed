from . import util
from typing import Any

def build_postprocessors(md: Any, **kwargs: Any): ...

class Postprocessor(util.Processor):
    def run(self, text: Any) -> None: ...

class RawHtmlPostprocessor(Postprocessor):
    def run(self, text: Any): ...
    def isblocklevel(self, html: Any): ...

class AndSubstitutePostprocessor(Postprocessor):
    def run(self, text: Any): ...

class UnescapePostprocessor(Postprocessor):
    RE: Any = ...
    def unescape(self, m: Any): ...
    def run(self, text: Any): ...
