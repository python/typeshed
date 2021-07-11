from bs4.dammit import EntitySubstitution as EntitySubstitution
from typing import Any

class Formatter(EntitySubstitution):
    XML_FORMATTERS: Any
    HTML_FORMATTERS: Any
    HTML: str
    XML: str
    HTML_DEFAULTS: Any
    language: Any
    entity_substitution: Any
    void_element_close_prefix: Any
    cdata_containing_tags: Any
    def __init__(self, language: Any | None = ..., entity_substitution: Any | None = ..., void_element_close_prefix: str = ..., cdata_containing_tags: Any | None = ...) -> None: ...
    def substitute(self, ns): ...
    def attribute_value(self, value): ...
    def attributes(self, tag): ...

class HTMLFormatter(Formatter):
    REGISTRY: Any
    def __init__(self, *args, **kwargs): ...

class XMLFormatter(Formatter):
    REGISTRY: Any
    def __init__(self, *args, **kwargs): ...
