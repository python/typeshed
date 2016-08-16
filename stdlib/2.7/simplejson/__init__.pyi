from typing import Any, IO

def dumps(obj: Any) -> str: ...
def dump(obj: Any, fp: IO[str], *args: Any, **kwds: Any) -> None: ...
def loads(s: str, **kwds: Any) -> Any: ...
def load(fp: IO[str]) -> Any: ...

from simplejson.scanner import JSONDecodeError
from simplejson.decoder import JSONDecoder
from simplejson.encoder import JSONEncoder, JSONEncoderForHTML
