import sys
from genericpath import *
from os.path import (
    abspath as abspath,
    altsep as altsep,
    basename as basename,
    commonpath as commonpath,
    curdir as curdir,
    defpath as defpath,
    devnull as devnull,
    dirname as dirname,
    expanduser as expanduser,
    expandvars as expandvars,
    extsep as extsep,
    isabs as isabs,
    islink as islink,
    ismount as ismount,
    join as join,
    lexists as lexists,
    normcase as normcase,
    normpath as normpath,
    pardir as pardir,
    pathsep as pathsep,
    realpath as realpath,
    relpath as relpath,
    sep as sep,
    split as split,
    splitdrive as splitdrive,
    splitext as splitext,
    supports_unicode_filenames as supports_unicode_filenames,
)

if sys.version_info < (3, 7) and sys.platform == "win32":
    from os.path import splitunc as splitunc
