import sys
from _stat import *
from typing import Final

# _stat.c defines FILE_ATTRIBUTE_* constants conditionally,
# making them available only at runtime on Windows.
# stat.py unconditionally redefines the same FILE_ATTRIBUTE_* constants
# on all platforms.
FILE_ATTRIBUTE_ARCHIVE: Final = 32  # type: ignore[misc]
FILE_ATTRIBUTE_COMPRESSED: Final = 2048  # type: ignore[misc]
FILE_ATTRIBUTE_DEVICE: Final = 64  # type: ignore[misc]
FILE_ATTRIBUTE_DIRECTORY: Final = 16  # type: ignore[misc]
FILE_ATTRIBUTE_ENCRYPTED: Final = 16384  # type: ignore[misc]
FILE_ATTRIBUTE_HIDDEN: Final = 2  # type: ignore[misc]
FILE_ATTRIBUTE_INTEGRITY_STREAM: Final = 32768  # type: ignore[misc]
FILE_ATTRIBUTE_NORMAL: Final = 128  # type: ignore[misc]
FILE_ATTRIBUTE_NOT_CONTENT_INDEXED: Final = 8192  # type: ignore[misc]
FILE_ATTRIBUTE_NO_SCRUB_DATA: Final = 131072  # type: ignore[misc]
FILE_ATTRIBUTE_OFFLINE: Final = 4096  # type: ignore[misc]
FILE_ATTRIBUTE_READONLY: Final = 1  # type: ignore[misc]
FILE_ATTRIBUTE_REPARSE_POINT: Final = 1024  # type: ignore[misc]
FILE_ATTRIBUTE_SPARSE_FILE: Final = 512  # type: ignore[misc]
FILE_ATTRIBUTE_SYSTEM: Final = 4  # type: ignore[misc]
FILE_ATTRIBUTE_TEMPORARY: Final = 256  # type: ignore[misc]
FILE_ATTRIBUTE_VIRTUAL: Final = 65536  # type: ignore[misc]

if sys.version_info >= (3, 13):
    # https://github.com/python/cpython/issues/114081#issuecomment-2119017790
    SF_RESTRICTED: Final = 0x00080000
