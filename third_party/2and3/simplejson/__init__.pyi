import sys
from typing import Any, IO, Text, Union

from simplejson.scanner import JSONDecodeError as JSONDecodeError
from simplejson.decoder import JSONDecoder as JSONDecoder
from simplejson.encoder import JSONEncoder as JSONEncoder, JSONEncoderForHTML as JSONEncoderForHTML

if sys.version_info >= (3, 6):
    _LoadsString = Union[Text, bytes, bytearray]
else:
    _LoadsString = Text


def dumps(obj: Any, *args: Any, **kwds: Any) -> str: ...
def dump(obj: Any, fp: IO[str], *args: Any, **kwds: Any) -> None: ...
def loads(s: _LoadsString, **kwds: Any) -> Any: ...
def load(fp: IO[str], **kwds: Any) -> Any: ...
