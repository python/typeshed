from typing import Any

from passlib.utils.compat import irange as irange

def varlist(name, count): ...
def indent_block(block, padding): ...

BFSTR: Any

def render_encipher(write, indent: int = ...) -> None: ...
def write_encipher_function(write, indent: int = ...) -> None: ...
def write_expand_function(write, indent: int = ...) -> None: ...
def main() -> None: ...
