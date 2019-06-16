# Stubs for email.iterators (Python 3.4)

from email.message import Message
from typing import Iterator, Optional

def body_line_iterator(msg: Message, decode: bool = ...) -> Iterator[str]: ...
def typed_subpart_iterator(msg: Message, maintype: str = ...,
                           subtype: Optional[str] = ...) -> Iterator[str]: ...
