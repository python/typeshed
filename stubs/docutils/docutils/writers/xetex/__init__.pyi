from _typeshed import Incomplete

from docutils.writers import latex2e

__docformat__: str

class Writer(latex2e.Writer):
    supported: Incomplete
    default_template: str
    default_preamble: str
    config_section: str
    config_section_dependencies: Incomplete
    settings_spec: Incomplete
    translator_class: Incomplete
    def __init__(self) -> None: ...

class Babel(latex2e.Babel):
    language_codes: Incomplete
    language_code: Incomplete
    reporter: Incomplete
    language: Incomplete
    otherlanguages: Incomplete
    warn_msg: str
    quote_index: int
    quotes: Incomplete
    literal_double_quote: str
    def __init__(self, language_code, reporter) -> None: ...
    def __call__(self): ...

class XeLaTeXTranslator(latex2e.LaTeXTranslator):
    is_xetex: bool
    def __init__(self, document) -> None: ...
