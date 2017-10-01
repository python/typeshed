from typing import Any, AnyStr

class TextWrapper(object):
    width: int = ...
    expand_tabs: bool = ...
    replace_whitespace: bool = ...
    drop_whitespace: bool = ...
    initial_indent: str = ...
    subsequent_indent: str = ...
    fix_sentence_endings: bool = ...
    break_long_words: bool = ...
    break_on_hyphens: bool = ...

    def __init__(
        self,
        width: int = ...,
        expand_tabs: bool = ...,
        replace_whitespace: bool = ...,
        drop_whitespace: bool = ...,
        initial_indent: str = ...,
        subsequent_indent: str = ...,
        fix_sentence_endings: bool = ...,
        break_long_words: bool = ...,
        break_on_hyphens: bool = ...,
    ) -> None:
        ...

    def wrap(self, text: AnyStr) -> List[AnyStr]:
        ...

    def fill(self, text: AnyStr) -> AnyStr:
        ...

def wrap(
        text: AnyStr, 
        width: int = ..., 
        expand_tabs: bool = ...,
        replace_whitespace: bool = ...,
        drop_whitespace: bool = ...,
        initial_indent: str = ...,
        subsequent_indent: str = ...,
        fix_sentence_endings: bool = ...,
        break_long_words: bool = ...,
        break_on_hyphens: bool = ...,
        ) -> AnyStr:
    ...

def fill(
        text: AnyStr,
        width: int =...,
        expand_tabs: bool = ...,
        replace_whitespace: bool = ...,
        drop_whitespace: bool = ...,
        initial_indent: str = ...,
        subsequent_indent: str = ...,
        fix_sentence_endings: bool = ...,
        break_long_words: bool = ...,
        break_on_hyphens: bool = ...,
        ) -> AnyStr:
    ...

