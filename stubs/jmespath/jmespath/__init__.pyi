from typing import Any

from jmespath import parser as parser
from jmespath.visitor import Options as Options, TreeNode as TreeNode

def compile(expression: str) -> parser.ParsedResult: ...
def search(expression: str, data: Any, options: Options | None = ...) -> TreeNode: ...
