
import sys

from typing import AnyStr, Union

# Is this correct? It seems to be for windows
if sys.version_info < (3, 7):
    def url2pathname(pathname: AnyStr) -> AnyStr: ...
    def pathname2url(pathname: AnyStr) -> AnyStr: ...
    def _pncomp2url(component: Union[str, bytes]) -> str: ...  # undocumented
