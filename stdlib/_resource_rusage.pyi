# This module does not exist at runtime. It's meant to reduce the number of
# import cycles and fix a mypy crash.
# See https://github.com/python/typeshed/issues/11220 for details.

import sys
from _typeshed import structseq
from typing import Final, final

if sys.platform != "win32":
    @final
    class struct_rusage(
        structseq[float], tuple[float, float, int, int, int, int, int, int, int, int, int, int, int, int, int, int]
    ):
        if sys.version_info >= (3, 10):
            __match_args__: Final = (
                "ru_utime",
                "ru_stime",
                "ru_maxrss",
                "ru_ixrss",
                "ru_idrss",
                "ru_isrss",
                "ru_minflt",
                "ru_majflt",
                "ru_nswap",
                "ru_inblock",
                "ru_oublock",
                "ru_msgsnd",
                "ru_msgrcv",
                "ru_nsignals",
                "ru_nvcsw",
                "ru_nivcsw",
            )
        @property
        def ru_utime(self) -> float: ...
        @property
        def ru_stime(self) -> float: ...
        @property
        def ru_maxrss(self) -> int: ...
        @property
        def ru_ixrss(self) -> int: ...
        @property
        def ru_idrss(self) -> int: ...
        @property
        def ru_isrss(self) -> int: ...
        @property
        def ru_minflt(self) -> int: ...
        @property
        def ru_majflt(self) -> int: ...
        @property
        def ru_nswap(self) -> int: ...
        @property
        def ru_inblock(self) -> int: ...
        @property
        def ru_oublock(self) -> int: ...
        @property
        def ru_msgsnd(self) -> int: ...
        @property
        def ru_msgrcv(self) -> int: ...
        @property
        def ru_nsignals(self) -> int: ...
        @property
        def ru_nvcsw(self) -> int: ...
        @property
        def ru_nivcsw(self) -> int: ...
