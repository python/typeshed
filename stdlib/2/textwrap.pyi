from typing import Any, AnyStr

class _unicode: ...

class TextWrapper:
    whitespace_trans = ...  # type: Any
    unicode_whitespace_trans = ...  # type: Any
    uspace = ...  # type: Any
    wordsep_re = ...  # type: Any
    wordsep_simple_re = ...  # type: Any
    sentence_end_re = ...  # type: Any
    width = ...  # type: Any
    initial_indent = ...  # type: Any
    subsequent_indent = ...  # type: Any
    expand_tabs = ...  # type: Any
    replace_whitespace = ...  # type: Any
    fix_sentence_endings = ...  # type: Any
    break_long_words = ...  # type: Any
    drop_whitespace = ...  # type: Any
    break_on_hyphens = ...  # type: Any
    wordsep_re_uni = ...  # type: Any
    wordsep_simple_re_uni = ...  # type: Any
    def __init__(self, width=..., initial_indent=..., subsequent_indent=..., expand_tabs=..., replace_whitespace=..., fix_sentence_endings=..., break_long_words=..., drop_whitespace=..., break_on_hyphens=...) -> None: ...
    def wrap(self, text): ...
    def fill(self, text): ...

def wrap(text, width=..., **kwargs): ...
def fill(text, width=..., **kwargs): ...
def dedent(text: AnyStr) -> AnyStr: ...
