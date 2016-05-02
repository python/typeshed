from typing import Any, Tuple

__all__ = None # type: list[str]
DEFAULTSECT = None # type: str
MAX_INTERPOLATION_DEPTH = None # type: int

class Error(Exception):
    def _get_message(self) -> None: ...

    def _set_message(self, value: str) -> None: ...

    message = None # type: Any

    def __init__(self, msg: str = ...) -> None: ...

    def __repr__(self) -> str: ...

    __str__ = __repr__


class NoSectionError(Error):
    section = ... # type: str
    args = ... # type: Tuple[str]
    def __init__(self, section: str) -> None: ...


class DuplicateSectionError(Error):
    section = ... # type: str
    args = ... # type: Tuple[str]
    def __init__(self, section: str) -> None: ...

class NoOptionError(Error):
    section = ... # type: str
    option = ... # type: str
    args = ... # type: Tuple[str,str]
    def __init__(self, option: str, section: str): -> None: ...

class InterpolationError(Error):
    section = ... # type: str
    option = ... # type: str
    msg = ... # type: str
    args = ... # type: Tuple[str,str,str]
    def __init__(self, option: str, section: str, msg: str) -> None: ...

class InterpolationMissingOptionError(InterpolationError):
    reference = ... # type: str
    args = ... # type: Tuple[str,str,str,str]
    def __init__(self, option: str, section: str, rawval: str, reference: str) -> None: ...

class InterpolationSyntaxError(InterpolationError): ...

class InterpolationDepthError(InterpolationError):
    def __init__(self, option: str, section: str, rawval: str) -> None: ...

class ParsingError(Error):
    filename = ... # type: str
    errors = ... # type: list[Tuple[Any,Any]]
    args = ... # type: Tuple[str]
    def __init__(self, filename: str): -> None: ...

    def append(self, lineno: Any, line: Any): -> None: ...

class MissingSectionHeaderError(ParsingError):
    lineno = ... # type: Any
    line = ... # type: Any
    args = ... # type: Tuple[str,Any,Any]
    def __init__(self, filename: str, lineno: Any, line: Any) -> None: ...


class RawConfigParser:
    _dict = ... # type: Any
    _sections = ... # type: dict
    _defaults = ... # type: dict
    _optcre = ... # type: Any
    def __init__(self, defaults: dict[Any,Any] = ..., dict_type: Any = ..., allow_no_value: bool = ...) -> None: ...

    def defaults(self) -> dict[Any,Any]: ...

    def sections(self) -> list[str]: ...

    def add_section(self, section: str) -> None: ...

    def has_section(self, section: str) -> bool: ...

    def options(self, section: str) -> list[str]: ...

    def read(self, filenames: str) -> list[str]: ...

    def readfp(self, fp: file, filename: str = ...) -> None: ...

    def get(self, section: str, option: str) -> str: ...

    def items(self, section: str) -> list[Tuple[Any,Any]]: ...

    def _get(self, section: str, conv: type, option: str) -> Any: ...

    def getint(self, section: str, option: str) -> int: ...

    def getfloat(self, section: str, option: str) -> float: ...

    _boolean_states = ... # type: dict[str,bool]

    def getboolean(self, section: str, option: str) -> bool: ...

    def optionxform(self, optionstr: str) -> str: ...

    def has_option(self, section: str, option: str) -> bool: ...

    def set(self, section: str, option: str, value: Any = ...) -> None: ...

    def write(self, fp: file) -> None: ...

    def remove_option(self, section: str, option: Any) -> bool: ...

    def remove_section(self, section: str) -> bool: ...

    SECTCRE = ... # type: Any
    OPTCRE = ... # type: Any
    OPTCRE_NV = ... # type: Any

    def _read(self, fp: file, fpname: str) -> None: ...

class ConfigParser(RawConfigParser):
    def get(self, section: str, option: str, raw: bool = ..., vars: dict = ...) -> Any: ...

    def items(self, section: str, raw: bool = ..., vars: dict = ...) -> list[Tuple[str,Any]]: ...

    def _interpolate(self, section: str, option: str, rawval: Any, vars: Any) -> str: ...

    _KEYCRE = ... # type: Any

    def _interpolation_replace(self, match: Any) -> str: ...


class SafeConfigParser(ConfigParser):
    def _interpolate(self, section: str, option: str, rawval: Any, vars: Any) -> str: ...

    _interpvar_re = ... # type: Any

    def _interpolate_some(self, option: str, accum: list, rest: str, section: str, map: dict, depth: int) -> None: ...
