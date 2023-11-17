from markdown.core import Markdown

from . import util

def build_preprocessors(md: Markdown, **kwargs) -> util.Registry[Preprocessor]: ...

class Preprocessor(util.Processor):
    def run(self, lines: list[str]) -> list[str]: ...

class NormalizeWhitespace(Preprocessor): ...
class HtmlBlockPreprocessor(Preprocessor): ...
