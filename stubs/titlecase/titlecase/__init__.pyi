import logging
import re
from typing import Final, Protocol, TypeAlias, overload
from typing_extensions import LiteralString

import regex

Pattern: TypeAlias = re.Pattern[str] | regex.Pattern[str]

__all__ = ["titlecase"]
__version__: Final[str]
logger: Final[logging.Logger]

REGEX_AVAILABLE: Final[bool]

SMALL: Final[str]
PUNCT: Final[str]

SMALL_WORDS: Pattern
SMALL_FIRST: Pattern
SMALL_LAST: Pattern
SUBPHRASE: Pattern

MAC_MC: Final[Pattern]
MR_MRS_MS_DR: Final[Pattern]
INLINE_PERIOD: Final[Pattern]
UC_ELSEWHERE: Final[Pattern]
CAPFIRST: Final[Pattern]
APOS_SECOND: Final[Pattern]
UC_INITIALS: Final[Pattern]

class CallbackProtocol(Protocol):
    def __call__(self, word: str, /, *, all_caps: bool) -> str | None: ...

class Immutable: ...
class ImmutableString(str, Immutable): ...
class ImmutableBytes(bytes, Immutable): ...

@overload
def set_small_word_list() -> None: ...
@overload
def set_small_word_list(small: str) -> None: ...

def titlecase(
    text: str, callback: CallbackProtocol | None = None, small_first_last: bool = True, preserve_blank_lines: bool = False
) -> LiteralString: ...
def create_wordlist_filter_from_file(file_path: str | None) -> CallbackProtocol: ...
def cmd() -> None: ...
