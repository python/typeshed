from jmespath import parser as parser
from jmespath.visitor import Options as Options
from typing import Any

python_ver: Any

def compile(expression): ...
def search(expression, data, options: Any | None = ...): ...
