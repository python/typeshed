from typing import IO, Any, Optional, Text as _Text, Union
from xml.sax.xmlreader import XMLReader

def parse(file: Union[str, IO[Any]], parser: Optional[XMLReader] = ..., bufsize: Optional[int] = ...): ...
def parseString(string: Union[bytes, _Text], parser: Optional[XMLReader] = ...): ...
def __getattr__(name: str) -> Any: ...  # incomplete
