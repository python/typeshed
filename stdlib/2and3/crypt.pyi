import sys
from typing import List, NamedTuple, Optional


if sys.version_info >= (3, 3):
    class _Method: ...

    METHOD_CRYPT: _Method
    METHOD_MD5: _Method
    METHOD_SHA256: _Method
    METHOD_SHA512: _Method

    methods: List[_Method]

    def mksalt(method: Optional[_Method] = ...) -> str: ...
    def crypt(word: str, salt: Optional[str] = ...) -> str: ...
else:
    def crypt(word: str, salt: str) -> str: ...
