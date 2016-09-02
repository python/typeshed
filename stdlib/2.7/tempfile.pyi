# Stubs for tempfile
# Ron Murawski <ron@horizonchess.com>

# based on http://docs.python.org/3.3/library/tempfile.html
# Adapted for Python 2.7 by Michal Pokorny

# TODO: Don't use basestring. Use Union[str, bytes] or AnyStr for arguments.
#       Avoid using Union[str, bytes] for return values, as it implies that
#       an isinstance() check will often be required, which is inconvenient.

from typing import Tuple, IO, Union, AnyStr, Any, overload

tempdir = ...  # type: str
template = ...  # type: str

# TODO text files

def TemporaryFile(
        mode: Union[bytes, unicode] = ...,
        bufsize: int = ...,
        suffix: Union[bytes, unicode] = ...,
        prefix: Union[bytes, unicode] = ...,
        dir: Union[bytes, unicode] = ...) -> IO[str]: ...
def NamedTemporaryFile(
        mode: Union[bytes, unicode] = ...,
        bufsize: int = ...,
        suffix: Union[bytes, unicode] = ...,
        prefix: Union[bytes, unicode] = ...,
        dir: Union[bytes, unicode] = ...,
        delete: bool = ...
        ) -> IO[str]: ...
def SpooledTemporaryFile(
        max_size: int = ...,
        mode: Union[bytes, unicode] = ...,
        buffering: int = ...,
        suffix: Union[bytes, unicode] = ...,
        prefix: Union[bytes, unicode] = ...,
        dir: Union[bytes, unicode] = ...) -> IO[str]:
    ...

class TemporaryDirectory:
    name = ...  # type: Any  # Can be str or unicode
    def __init__(self,
                 suffix: Union[bytes, unicode] = ...,
                 prefix: Union[bytes, unicode] = ...,
                 dir: Union[bytes, unicode] = ...) -> None: ...
    def cleanup(self) -> None: ...
    def __enter__(self) -> Any: ...  # Can be str or unicode
    def __exit__(self, type, value, traceback) -> bool: ...

@overload
def mkstemp() -> Tuple[int, str]: ...
@overload
def mkstemp(suffix: AnyStr = ..., prefix: AnyStr = ..., dir: AnyStr = ...,
            text: bool = ...) -> Tuple[int, AnyStr]: ...
@overload
def mkdtemp() -> str: ...
@overload
def mkdtemp(suffix: AnyStr = ..., prefix: AnyStr = ..., dir: AnyStr = ...) -> AnyStr: ...
@overload
def mktemp() -> str: ...
@overload
def mktemp(suffix: AnyStr = ..., prefix: AnyStr = ..., dir: AnyStr = ...) -> AnyStr: ...
def gettempdir() -> str: ...
def gettempprefix() -> str: ...
