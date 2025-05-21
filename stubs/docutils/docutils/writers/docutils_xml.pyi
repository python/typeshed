import xml.sax
from _typeshed import Incomplete

import docutils
from docutils import nodes, writers

__docformat__: str

class RawXmlError(docutils.ApplicationError): ...

class Writer(writers.Writer):
    supported: Incomplete
    settings_spec: Incomplete
    settings_defaults: Incomplete
    config_section: str
    config_section_dependencies: Incomplete
    output: Incomplete
    translator_class: Incomplete
    def __init__(self) -> None: ...
    visitor: Incomplete
    def translate(self) -> None: ...

class XMLTranslator(nodes.GenericNodeVisitor):
    doctype: str
    generator: str
    xmlparser: Incomplete
    warn: Incomplete
    error: Incomplete
    settings: Incomplete
    indent: str
    newline: str
    level: int
    in_simple: int
    fixed_text: int
    output: Incomplete
    the_handle: Incomplete
    def __init__(self, document) -> None: ...
    simple_nodes: Incomplete
    def default_visit(self, node) -> None: ...
    def default_departure(self, node) -> None: ...
    def visit_Text(self, node) -> None: ...
    def depart_Text(self, node) -> None: ...
    def visit_raw(self, node) -> None: ...

class TestXml(xml.sax.handler.ContentHandler):
    locator: Incomplete
    def setDocumentLocator(self, locator) -> None: ...
