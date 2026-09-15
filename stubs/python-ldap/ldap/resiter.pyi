from typing import Any
from collections.abc import Generator

from ldap.pkginfo import __version__ as __version__

class ResultProcessor:
    def allresults(
        self, msgid, timeout: int = -1, add_ctrls: int = 0
    ) -> Generator[Any, None, None]: ...  # TODO: Precise type for Generator yield
