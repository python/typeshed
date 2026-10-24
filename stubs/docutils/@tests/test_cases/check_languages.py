from __future__ import annotations

from typing import TYPE_CHECKING
from typing_extensions import assert_type

from docutils.languages import LanguageImporter, get_language
from docutils.parsers.rst.languages import get_language as get_rst_language

if TYPE_CHECKING:
    from docutils.languages import LanguageModule
    from docutils.parsers.rst.languages import RSTLanguageModule


assert_type(get_language("de"), "LanguageModule")

# The rST importer has should have no fallback language.
assert_type(get_rst_language("de"), "RSTLanguageModule | None")

# The module type should default to `LanguageModule`.
assert_type(LanguageImporter()("de"), "LanguageModule")
