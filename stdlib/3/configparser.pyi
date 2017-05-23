# Based on http://docs.python.org/3.5/library/configparser.html and on
# reading configparser.py.

from typing import (MutableMapping, Mapping, Dict, Sequence, List, Union,
                    Iterable, Iterator, Callable, Any, IO, overload, Optional, Pattern)
# Types only used in type comments only
from typing import Optional, Tuple  # noqa

# Internal type aliases
_section = Mapping[str, str]
_parser = MutableMapping[str, _section]
_converter = Callable[[str], Any]
_converters = Dict[str, _converter]

DEFAULTSECT: str
MAX_INTERPOLATION_DEPTH: int

class Interpolation:
    def before_get(self, parser: _parser,
                   section: str,
                   option: str,
                   value: str,
                   defaults: _section) -> str: ...

    def before_set(self, parser: _parser,
                   section: str,
                   option: str,
                   value: str) -> str: ...

    def before_read(self, parser: _parser,
                    section: str,
                    option: str,
                    value: str) -> str: ...

    def before_write(self, parser: _parser,
                     section: str,
                     option: str,
                     value: str) -> str: ...


class BasicInterpolation(Interpolation): ...
class ExtendedInterpolation(Interpolation): ...
class LegacyInterpolation(Interpolation): ...


class RawConfigParser(_parser):
    def __init__(self,
                 defaults: Optional[_section] = ...,
                 dict_type: Mapping[str, str] = ...,
                 allow_no_value: bool = ...,
                 *,
                 delimiters: Sequence[str] = ...,
                 comment_prefixes: Sequence[str] = ...,
                 inline_comment_prefixes: Optional[Sequence[str]] = ...,
                 strict: bool = ...,
                 empty_lines_in_values: bool = ...,
                 default_section: str = ...,
                 interpolation: Optional[Interpolation] = ...) -> None: ...

    def __len__(self) -> int: ...

    def __getitem__(self, section: str) -> _section: ...

    def __setitem__(self, section: str, options: _section) -> None: ...

    def __delitem__(self, section: str) -> None: ...

    def __iter__(self) -> Iterator[str]: ...

    def defaults(self) -> _section: ...

    def sections(self) -> List[str]: ...

    def add_section(self, section: str) -> None: ...

    def has_section(self, section: str) -> bool: ...

    def options(self, section: str) -> List[str]: ...

    def has_option(self, section: str, option: str) -> bool: ...

    def read(self, filenames: Union[str, Sequence[str]],
             encoding: str = None) -> List[str]: ...

    def read_file(self, f: Iterable[str], source: str = None) -> None: ...

    def read_string(self, string: str, source: str = ...) -> None: ...

    def read_dict(self, dictionary: Mapping[str, Mapping[str, Any]],
                  source: str = ...) -> None: ...

    def getint(self, section: str, option: str, *, raw: bool = ..., vars: _section = ..., fallback: int = ...) -> int: ...

    def getfloat(self, section: str, option: str, *, raw: bool = ..., vars: _section = ..., fallback: float = ...) -> float: ...

    def getboolean(self, section: str, option: str, *, raw: bool = ..., vars: _section = ..., fallback: bool = ...) -> bool: ...

    # This is incompatible with MutableMapping so we ignore the type
    def get(self, section: str, option: str, *, raw: bool = ..., vars: _section = ..., fallback: str = ...) -> str:  # type: ignore
        ...

    # This is incompatible with Mapping so we ignore the type.
    def items(self, section: str = ..., raw: bool = ..., vars: _section = ...) -> Iterable[Tuple[str, _section]]: ...  # type: ignore

    def set(self, section: str, option: str, value: str) -> None: ...

    def write(self,
              fileobject: IO[str],
              space_around_delimiters: bool = True) -> None: ...

    def remove_option(self, section: str, option: str) -> bool: ...

    def remove_section(self, section: str) -> bool: ...

    def optionxform(self, option: str) -> str: ...


class ConfigParser(RawConfigParser):
    def __init__(self,
                 defaults: _section = None,
                 dict_type: Mapping[str, str] = ...,
                 allow_no_value: bool = ...,
                 delimiters: Sequence[str] = ...,
                 comment_prefixes: Sequence[str] = ...,
                 inline_comment_prefixes: Sequence[str] = None,
                 strict: bool = ...,
                 empty_lines_in_values: bool = ...,
                 default_section: str = ...,
                 interpolation: Interpolation = None,
                 converters: _converters = ...) -> None: ...

class SafeConfigParser(ConfigParser): ...

class SectionProxy(MutableMapping[str, str]):
    def __init__(self, parser: RawConfigParser, name: str) -> None: ...
    def __getitem__(self, key: str) -> str: ...
    def __setitem__(self, key: str, value: str) -> None: ...
    def __delitem__(self, key: str) -> None: ...
    def __contains__(self, key: object) -> bool: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[str]: ...
    @property
    def parser(self) -> RawConfigParser: ...
    @property
    def name(self) -> str: ...
    def get(self, option: str, fallback: Optional[str] = ..., *, raw: bool = ...,  # type: ignore
            vars: Optional[_section] = ...,
            **kwargs: Any) -> str: ...
    # SectionProxy can have arbitrary attributes when custon converters are used
    def __getattr__(self, key: str) -> Callable[..., str]: ...

class ConverterMapping(MutableMapping[str, Optional[_converter]]):
    GETTERCRE: Pattern
    def __init__(self, parser: RawConfigParser) -> None: ...
    def __getitem__(self, key: str) -> _converter: ...
    def __setitem__(self, key: str, value: Optional[_converter]) -> None: ...
    def __delitem__(self, key: str) -> None: ...
    def __iter__(self) -> Iterator[str]: ...
    def __len__(self) -> int: ...


class Error(Exception):
    pass


class NoSectionError(Error):
    pass


class DuplicateSectionError(Error):
    section = ...  # type: str
    source = ...   # type: Optional[str]
    lineno = ...   # type: Optional[int]


class DuplicateOptionError(Error):
    section = ...  # type: str
    option = ...   # type: str
    source = ...   # type: Optional[str]
    lineno = ...   # type: Optional[int]


class NoOptionError(Error):
    section = ...  # type: str
    option = ...   # type: str


class InterpolationError(Error):
    section = ...  # type: str
    option = ...   # type: str


class InterpolationDepthError(InterpolationError):
    pass


class InterpolationMissingOptionError(InterpolationError):
    reference = ...  # type: str


class InterpolationSyntaxError(InterpolationError):
    pass


class ParsingError:
    source = ...  # type: str
    errors = ...  # type: Sequence[Tuple[int, str]]


class MissingSectionHeaderError(ParsingError):
    lineno = ...  # type: int
    line = ...    # type: str
