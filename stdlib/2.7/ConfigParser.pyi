from typing import Any, Tuple

__all__ = None # type: list[str]
DEFAULTSECT = None # type: str
MAX_INTERPOLATION_DEPTH = None # type: int

class Error(Exception):
    def _get_message(self): # type: () -> None
        pass

    def _set_message(self, value): # type: (str) -> None
        pass

    message = None # type: Any

    def __init__(self, msg=''): # type (str) -> None
        pass

    def __repr__(self): # type () -> str
        return ""

    __str__ = __repr__


class NoSectionError(Error):
    def __init__(self, section): # type: (str) -> None
        self.section = None # type: str
        self.args = None # type: Tuple[str]

class DuplicateSectionError(Error):
    def __init__(self, section): # type: (str) -> None
        self.section = None # type: str
        self.args = None # type: Tuple[str]

class NoOptionError(Error):
    def __init__(self, option, section): # type: (str,str) -> None
        self.option = None # type: str
        self.section = None # type: str
        self.args = None # type: Tuple[str,str]

class InterpolationError(Error):
    def __init__(self, option, section, msg): # type: (str,str,str) -> None
        self.option = None # type: str
        self.section = None # type: str
        self.args = None # type: Tuple[str,str,str]

class InterpolationMissingOptionError(InterpolationError):
    def __init__(self, option, section, rawval, reference): # type: (str,str,str,str) -> None
        msg = None # type: str
        self.reference = None # type: str
        self.args = None # type: Tuple[str,str,str,str]

class InterpolationSyntaxError(InterpolationError):
    pass

class InterpolationDepthError(InterpolationError):
    def __init__(self, option, section, rawval): # type: (str,str,str) -> None
        msg = None # type: str
        self.args = None # type: Tuple[str,str,str]

class ParsingError(Error):
    def __init__(self, filename):  # type: (str) -> None
        self.filename = None # type: str
        self.errors = None # type: list[Tuple[Any,Any]]
        self.args = None # type: Tuple[str]

    def append(self, lineno, line): # type: (Any,Any) -> None
        pass

class MissingSectionHeaderError(ParsingError):
    def __init__(self, filename, lineno, line): # type: (str,Any,Any) -> None
        self.filename = None # type: str
        self.lineno = None # type: Any
        self.line = None # type: Any
        self.args = None # type: Tuple[str,Any,Any]


class RawConfigParser:
    def __init__(self, defaults=None, dict_type=None, allow_no_value=False): # type: (dict[Any,Any],Any,bool) -> None
        self._dict = dict_type
        self._sections = self._dict() # type: dict
        self._defaults = self._dict() # type: dict
        self._optcre = None # type: Any

    def defaults(self): # type: () -> dict[Any,Any]
        return None

    def sections(self): # type: () -> list[str]
        return None

    def add_section(self, section): # type: (str) -> None
        pass

    def has_section(self, section): # type: (str) -> bool
        return False

    def options(self, section): # type: (str) -> list[str]
        return None

    def read(self, filenames): # type: (str) -> list[str]
        return None

    def readfp(self, fp, filename=None): # type: (file, str) -> None
        pass

    def get(self, section, option):   # type: (str,str) -> str
        pass

    def items(self, section): # type: (str) -> list[Tuple[Any,Any]]
        return None

    def _get(self, section, conv, option): # type: (str,type,str) -> Any
        return None

    def getint(self, section, option): # type: (str,str) -> int
        pass

    def getfloat(self, section, option): # type: (str,str) -> float
        return None

    _boolean_states = None # type: dict[str,bool]

    def getboolean(self, section, option): # type: (str,str) -> bool
        return None

    def optionxform(self, optionstr): # type: (str) -> str
        return None

    def has_option(self, section, option): # type: (str,str) -> bool
        return None

    def set(self, section, option, value=None): # type: (str,str,Any) -> None
        pass

    def write(self, fp): # type: (file) -> None
        pass

    def remove_option(self, section, option): # type: (str,Any) -> bool
        return None

    def remove_section(self, section): # type: (str) -> bool
        return None

    SECTCRE = None # type: Any
    OPTCRE = None # type: Any
    OPTCRE_NV = None # type: Any

    def _read(self, fp, fpname): # type: (file,str) -> None
        pass

class ConfigParser(RawConfigParser):
    def get(self, section, option, raw=False, vars=None): # type: (str,str,bool,dict) -> Any
        return None

    def items(self, section, raw=False, vars=None): # type: (str,bool,dict) -> list[Tuple[str,Any]]
        return None

    def _interpolate(self, section, option, rawval, vars): # type: (str,str,Any,Any) -> str
        return None

    _KEYCRE = None # type: Any

    def _interpolation_replace(self, match): # type: (Any) -> str
        return None


class SafeConfigParser(ConfigParser):

    def _interpolate(self, section, option, rawval, vars): # type: (str,str,Any,Any) -> str
        return None

    _interpvar_re = None # type: Any

    def _interpolate_some(self, option, accum, rest, section, map, depth): # type: (str,list,str,str,dict,int) -> None
        pass

    def set(self, section, option, value=None): # type: (str,str,Any) -> None
        pass
