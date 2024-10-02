import sys
from _stat import *
from typing import Final

if sys.version_info >= (3, 13):
    # https://github.com/python/cpython/issues/114081#issuecomment-2119017790
    SF_RESTRICTED: Final = 0x00080000

if sys.platform != "win32":
    # Available in stat but not in _stat
    # Locking behind platform check to avoid redefinitions
    FILE_ATTRIBUTE_ARCHIVE: Final = 32
    FILE_ATTRIBUTE_COMPRESSED: Final = 2048
    FILE_ATTRIBUTE_DEVICE: Final = 64
    FILE_ATTRIBUTE_DIRECTORY: Final = 16
    FILE_ATTRIBUTE_ENCRYPTED: Final = 16384
    FILE_ATTRIBUTE_HIDDEN: Final = 2
    FILE_ATTRIBUTE_INTEGRITY_STREAM: Final = 32768
    FILE_ATTRIBUTE_NORMAL: Final = 128
    FILE_ATTRIBUTE_NOT_CONTENT_INDEXED: Final = 8192
    FILE_ATTRIBUTE_NO_SCRUB_DATA: Final = 131072
    FILE_ATTRIBUTE_OFFLINE: Final = 4096
    FILE_ATTRIBUTE_READONLY: Final = 1
    FILE_ATTRIBUTE_REPARSE_POINT: Final = 1024
    FILE_ATTRIBUTE_SPARSE_FILE: Final = 512
    FILE_ATTRIBUTE_SYSTEM: Final = 4
    FILE_ATTRIBUTE_TEMPORARY: Final = 256
    FILE_ATTRIBUTE_VIRTUAL: Final = 65536
