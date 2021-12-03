from typing import Any

def translate_underscores(name): ...
def to_flag(name): ...
def sort_candidate(arg): ...
def flag_key(x): ...

class ParserContext:
    args: Any
    positional_args: Any
    flags: Any
    inverse_flags: Any
    name: Any
    aliases: Any
    def __init__(self, name=..., aliases=..., args=...) -> None: ...
    def add_arg(self, *args, **kwargs) -> None: ...
    @property
    def missing_positional_args(self): ...
    @property
    def as_kwargs(self): ...
    def names_for(self, flag): ...
    def help_for(self, flag): ...
    def help_tuples(self): ...
    def flag_names(self): ...
