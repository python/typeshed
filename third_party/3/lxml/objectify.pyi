# Hand-written stub, incomplete

from typing import AnyStr

from lxml.etree import ElementBase, XMLParser

class ObjectifiedElement(ElementBase):
    pass

def fromstring(text: AnyStr,
               parser: XMLParser = ...,
               *,
               base_url: AnyStr = ...) -> ObjectifiedElement: ...
