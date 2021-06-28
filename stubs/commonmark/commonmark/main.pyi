from commonmark.blocks import Parser as Parser
from commonmark.dump import dumpAST as dumpAST, dumpJSON as dumpJSON
from commonmark.render.html import HtmlRenderer as HtmlRenderer
from commonmark.render.rst import ReStructuredTextRenderer as ReStructuredTextRenderer

def commonmark(text, format: str = ...): ...
