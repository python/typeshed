# Stubs for email (Python 3.4)

from typing import IO, Any

def message_from_string(s: str, *args, **kwargs): ...
def message_from_bytes(s: bytes, *args, **kwargs): ...
def message_from_file(fp: IO[str], *args, **kwargs): ...
def message_from_binary_file(fp: IO[bytes], *args, **kwargs): ...

# Names in __all__ with no definition:
#   base64mime
#   charset
#   encoders
#   errors
#   feedparser
#   generator
#   header
#   iterators
#   message
#   mime
#   parser
#   quoprimime
#   utils
