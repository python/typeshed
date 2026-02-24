import codecs
import sys
from codecs import CodecInfo

import aliases
import utf_8
import utf_8_sig

class CodecRegistryError(LookupError, SystemError): ...

def normalize_encoding(encoding: str | bytes) -> str: ...
def search_function(encoding: str) -> CodecInfo | None: ...

if sys.version_info >= (3, 14) and sys.platform == "win32":
    def win32_code_page_search_function(encoding: str) -> CodecInfo | None: ...

# Needed for submodules
def __getattr__(name: str): ...  # incomplete module
