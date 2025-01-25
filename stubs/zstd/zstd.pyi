from _typeshed import ReadableBuffer

class Error(Exception): ...

def ZSTD_compress(data: ReadableBuffer, level: int = ..., threads: int = ..., /) -> bytes: ...

compress = ZSTD_compress
dumps = ZSTD_compress

def ZSTD_check(data: bytes | str) -> int: ...

check = ZSTD_check

def ZSTD_uncompress(data: ReadableBuffer, /) -> bytes: ...

decompress = ZSTD_uncompress
uncompress = ZSTD_uncompress
loads = ZSTD_uncompress
decode = ZSTD_uncompress

def ZSTD_version() -> str: ...
def ZSTD_version_number() -> int: ...
def ZSTD_threads_count() -> int: ...
def ZSTD_max_threads_count() -> int: ...
def ZSTD_external() -> int: ...
def ZSTD_with_asm() -> int: ...
def ZSTD_with_threads() -> int: ...
def version() -> str: ...
