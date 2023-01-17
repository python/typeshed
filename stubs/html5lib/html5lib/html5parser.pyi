from _typeshed import Incomplete
from _typeshed import SupportsRead
from typing import Any, overload
from typing_extensions import Literal
from xml.etree.ElementTree import Element

@overload
def parse(
    doc: str | bytes | SupportsRead[str] | SupportsRead[bytes],
    treebuilder: Literal["etree"] = ...,
    namespaceHTMLElements: bool = ...,
    **kwargs,
) -> Element: ...
@overload
def parse(
    doc: str | bytes | SupportsRead[str] | SupportsRead[bytes], treebuilder: str, namespaceHTMLElements: bool = ..., **kwargs
): ...
def parseFragment(doc, container: str = ..., treebuilder: str = ..., namespaceHTMLElements: bool = ..., **kwargs): ...
def method_decorator_metaclass(function): ...

class HTMLParser:
    strict: Any
    tree: Any
    errors: Any
    phases: Any
    def __init__(
        self, tree: Incomplete | None = ..., strict: bool = ..., namespaceHTMLElements: bool = ..., debug: bool = ...
    ) -> None: ...
    firstStartTag: bool
    log: Any
    compatMode: str
    innerHTML: Any
    phase: Any
    lastPhase: Any
    beforeRCDataPhase: Any
    framesetOK: bool
    def reset(self) -> None: ...
    @property
    def documentEncoding(self) -> str | None: ...
    def isHTMLIntegrationPoint(self, element) -> bool: ...
    def isMathMLTextIntegrationPoint(self, element) -> bool: ...
    def mainLoop(self) -> None: ...
    def parse(self, stream, scripting: bool = ..., **kwargs): ...
    def parseFragment(self, stream, *args, **kwargs): ...
    def parseError(self, errorcode: str = ..., datavars: Incomplete | None = ...) -> None: ...
    def adjustMathMLAttributes(self, token) -> None: ...
    def adjustSVGAttributes(self, token) -> None: ...
    def adjustForeignAttributes(self, token) -> None: ...
    def reparseTokenNormal(self, token) -> None: ...
    def resetInsertionMode(self) -> None: ...
    originalPhase: Any
    def parseRCDataRawtext(self, token, contentType) -> None: ...

def getPhases(debug): ...
def adjust_attributes(token, replacements) -> None: ...
def impliedTagToken(name, type: str = ..., attributes: Incomplete | None = ..., selfClosing: bool = ...): ...

class ParseError(Exception): ...