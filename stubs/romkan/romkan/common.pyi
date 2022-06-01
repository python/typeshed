import re
from collections.abc import Generator, Iterable
from typing import Any, Match, Pattern

KUNREITAB: str
KUNREITAB_H: str
HEPBURNTAB: str
HEPBURNTAB_H: str

# list[N] -> Generator[N, None, None] .forall N
def pairs(arr: list[Any], size: int = ...) -> Generator[Any, None, None]: ...

KANROM: dict[str, str]
ROMKAN: dict[str, str]
kana: str
roma: str
ROMPAT: re.Pattern
KANPAT: re.Pattern
KUNREI: list[str]
HEPBURN: list[str]
KUNPAT: re.Pattern
HEPPAT: re.Pattern
TO_HEPBURN: dict[str, str]
TO_KUNREI: dict[str, str]
KANROM_H: dict[str, str]
ROMKAN_H: dict[str, str]
ROMPAT_H: re.Pattern
KANPAT_H: re.Pattern
KUNREI_H: list[str]
HEPBURN_H: list[str]
KUNPAT_H: re.Pattern
HEPPAT_H: re.Pattern
TO_HEPBURN_H: dict[str, str]
TO_KUNREI_H: dict[str, str]

def normalize_double_n(str: str) -> str: ...
def to_katakana(str: str) -> str: ...
def to_hiragana(str: str) -> str: ...
def to_kana(str) -> str: ...
def to_hepburn(str) -> str: ...
def to_kunrei(str) -> str: ...
def to_roma(str) -> str: ...
def is_consonant(str) -> re.Match: ...
def is_vowel(str) -> re.Match: ...
def expand_consonant(str) -> Iterable[str]: ...
