from __future__ import annotations

import platform
import sys
from typing_extensions import assert_type

# platform.uname_result emulates a 6 field named tuple, but on 3.9+ the processor
# field is lazily evaluated, which results in it being a little funky.
uname = platform.uname()
if sys.version_info >= (3, 9):
    myuname = platform.uname_result("Darwin", "local", "22.5.0", "Darwin Kernel Version 22.5.0", "arm64")
else:
    myuname = platform.uname_result("Darwin", "local", "22.5.0", "Darwin Kernel Version 22.5.0", "arm64", "arm")

assert_type(uname, platform.uname_result)
assert_type(myuname, platform.uname_result)

assert_type(uname[5], str)
assert_type(myuname[5], str)
