from . import Extension
from ..inlinepatterns import HtmlInlineProcessor
from typing import Any

punctClass: str
endOfWordClass: str
closeClass: str
openingQuotesBase: str
substitutions: Any
singleQuoteStartRe: Any
doubleQuoteStartRe: Any
doubleQuoteSetsRe: str
singleQuoteSetsRe: str
decadeAbbrRe: str
openingDoubleQuotesRegex: Any
closingDoubleQuotesRegex: str
closingDoubleQuotesRegex2: Any
openingSingleQuotesRegex: Any
closingSingleQuotesRegex: Any
closingSingleQuotesRegex2: Any
remainingSingleQuotesRegex: str
remainingDoubleQuotesRegex: str
HTML_STRICT_RE: Any

class SubstituteTextPattern(HtmlInlineProcessor):
    replace: Any
    md: Any
    def __init__(self, pattern, replace, md) -> None: ...
    @property
    def markdown(self): ...
    def handleMatch(self, m, data): ...  # type: ignore

class SmartyExtension(Extension):
    config: Any
    substitutions: Any
    def __init__(self, **kwargs) -> None: ...
    def educateDashes(self, md) -> None: ...
    def educateEllipses(self, md) -> None: ...
    def educateAngledQuotes(self, md) -> None: ...
    def educateQuotes(self, md) -> None: ...
    inlinePatterns: Any
    def extendMarkdown(self, md) -> None: ...

def makeExtension(**kwargs): ...
