import sys

if sys.platform != "win32":
    from _gdbm import *
