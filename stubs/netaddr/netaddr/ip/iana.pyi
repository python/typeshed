from _typeshed import Incomplete
from collections.abc import Callable, Mapping
from typing import TextIO
from typing_extensions import TypeAlias
from xml.sax import handler
from xml.sax.xmlreader import XMLReader

from netaddr.core import Publisher, Subscriber
from netaddr.ip import IPAddress, IPNetwork, IPRange

_IanaInfoKey: TypeAlias = IPAddress | IPNetwork | IPRange

IANA_INFO: dict[str, dict[_IanaInfoKey, dict[str, str]]]

class SaxRecordParser(handler.ContentHandler):
    def __init__(self, callback: Callable[[Mapping[str, object] | None], object] | None = ...) -> None: ...
    def startElement(self, name: str, attrs: Mapping[str, object]) -> None: ...
    def endElement(self, name: str) -> None: ...
    def characters(self, content: str) -> None: ...

class XMLRecordParser(Publisher):
    xmlparser: XMLReader
    fh: Incomplete
    def __init__(self, fh: Incomplete, **kwargs: object) -> None: ...
    def process_record(self, rec: Mapping[str, object]) -> dict[str, str] | None: ...
    def consume_record(self, rec: object) -> None: ...
    def parse(self) -> None: ...

class IPv4Parser(XMLRecordParser): ...
class IPv6Parser(XMLRecordParser): ...
class IPv6UnicastParser(XMLRecordParser): ...

class MulticastParser(XMLRecordParser):
    def normalise_addr(self, addr: str) -> str: ...

class DictUpdater(Subscriber):
    dct: dict[_IanaInfoKey, Incomplete]
    topic: str
    unique_key: str
    def __init__(self, dct: dict[_IanaInfoKey, Incomplete], topic: str, unique_key: str) -> None: ...
    def update(self, data: Incomplete) -> None: ...

def load_info() -> None: ...
def pprint_info(fh: TextIO | None = ...) -> None: ...
def query(ip_addr: IPAddress) -> dict[str, list[dict[str, str]]]: ...
