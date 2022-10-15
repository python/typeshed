from typing import Any

class FPDFException(Exception): ...

class FPDFPageFormatException(FPDFException):
    argument: Any
    unknown: Any
    one: Any
    def __init__(self, argument, unknown: bool = ..., one: bool = ...) -> None: ...

class FPDFUnicodeEncodingException(FPDFException):
    def __init__(self, text_index, character, font_name) -> None: ...
