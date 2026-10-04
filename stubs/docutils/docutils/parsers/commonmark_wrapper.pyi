from typing import Literal, TypeAlias

from docutils import parsers

_ParserName: TypeAlias = Literal["pycmark", "myst", "recommonmark"]

commonmark_parser_names: tuple[_ParserName, ...]
# If Parser is None or `parser_name` is an empty string, this module will fail to import.
Parser: type[parsers.Parser]
parser_name: _ParserName
# `name` is likely an unintentionally exposed variable.
# It is the loop induction variable `parser_name` is assigned from, and they should be equal.
name = parser_name
