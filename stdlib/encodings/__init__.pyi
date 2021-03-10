from codecs import CodecInfo

class CodecRegistryError(LookupError, SystemError):
    pass

def normalize_encoding(encoding: str) -> str: ...
def search_function(encoding: str) -> CodecInfo: ...

