import ast
from collections.abc import Iterable
from types import FrameType

def getline(frame: FrameType) -> str: ...
def getargnodes(frame: FrameType) -> Iterable[tuple[ast.expr, str]]: ...