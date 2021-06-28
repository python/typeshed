from commonmark.main import Parser as Parser, dumpAST as dumpAST
from commonmark.render.html import HtmlRenderer as HtmlRenderer

class colors:
    HEADER: str
    OKBLUE: str
    OKGREEN: str
    WARNING: str
    FAIL: str
    ENDC: str

def trace_calls(frame, event, arg): ...
def main(): ...
