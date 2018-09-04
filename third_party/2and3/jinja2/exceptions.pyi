from typing import Any, Optional, Text

class TemplateError(Exception):
    def __init__(self, message: Optional[Text] = ...) -> None: ...
    @property
    def message(self): ...
    def __unicode__(self): ...

class TemplateNotFound(IOError, LookupError, TemplateError):
    message = ...  # type: Any
    name = ...  # type: Any
    templates = ...  # type: Any
    def __init__(self, name, message: Optional[Text] = ...) -> None: ...

class TemplatesNotFound(TemplateNotFound):
    templates = ...  # type: Any
    def __init__(self, names: Any = ..., message: Optional[Text] = ...) -> None: ...

class TemplateSyntaxError(TemplateError):
    lineno = ...  # type: int
    name = ...  # type: Text
    filename = ...  # type: Text
    source = ...  # type: Text
    translated = ...  # type: bool
    def __init__(self, message: Text, lineno: int, name: Optional[Text] = ..., filename: Optional[Text] = ...) -> None: ...

class TemplateAssertionError(TemplateSyntaxError): ...
class TemplateRuntimeError(TemplateError): ...
class UndefinedError(TemplateRuntimeError): ...
class SecurityError(TemplateRuntimeError): ...
class FilterArgumentError(TemplateRuntimeError): ...
