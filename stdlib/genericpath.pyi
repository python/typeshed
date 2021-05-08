import sys
from os.path import (
    commonprefix as commonprefix,
    exists as exists,
    getatime as getatime,
    getctime as getctime,
    getmtime as getmtime,
    getsize as getsize,
    isdir as isdir,
    isfile as isfile,
)

if sys.version_info >= (3, 4):
    from os.path import samefile as samefile, sameopenfile as sameopenfile, samestat as samestat
