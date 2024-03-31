from xml.dom.minidom import Document

from braintree.util.datetime_parser import parse_datetime as parse_datetime

binary_type = bytes

class Parser:
    doc: Document
    def __init__(self, xml) -> None: ...
    def parse(self): ...
