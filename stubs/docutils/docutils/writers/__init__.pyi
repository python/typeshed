from _typeshed import StrPath
from pathlib import Path
from typing import Final, Generic, TypedDict, TypeVar, type_check_only
from typing_extensions import NotRequired, Required

from docutils import Component, nodes
from docutils.frontend import Values
from docutils.io import Output
from docutils.languages import LanguageModule

_S = TypeVar("_S")

__docformat__: Final = "reStructuredText"

# It would probably be better to specialize writers for subclasses,
# but this gives us all possible Writer items without instance checks
# Parameters provided by any and all docutils :class:docutils.writers.`Writer`.
#
# See:
# <https://docutils.sourceforge.io/docs/api/publisher.html#parts-provided-by-all-writers>
# <https://docutils.sourceforge.io/docs/api/publisher.html#parts-provided-by-the-html-writers>
# <https://docutils.sourceforge.io/docs/api/publisher.html#html4-writer>
# <https://docutils.sourceforge.io/docs/api/publisher.html#html5-writer>
# <https://docutils.sourceforge.io/docs/api/publisher.html#pep-html-writer>
# <https://docutils.sourceforge.io/docs/api/publisher.html#s5-html-writer>
# <https://docutils.sourceforge.io/docs/api/publisher.html#parts-provided-by-the-xe-latex-writers>
@type_check_only
class _WriterParts(TypedDict, total=False):
    # Required/provided by all writers.
    whole: Required[str | bytes]
    # Required/provided by all writers.
    encoding: Required[str]
    # Required/provided by all writers.
    errors: Required[str]
    # Required/provided by all writers.
    version: Required[str]
    # Required/provided by HTML and (Xe)LaTeX writers.
    body: str
    # Required/provided by HTML writers.
    body_prefix: str
    # Required/provided by HTML and (Xe)LaTeX writers.
    body_pre_docinfo: str
    # Required/provided by HTML writers.
    body_suffix: str
    # Required/provided by HTML and (Xe)LaTeX writers.
    docinfo: str
    # Required/provided by HTML writers.
    footer: str
    # Required/provided by HTML writers.
    fragment: str
    # Required/provided by HTML writers.
    head: str
    # Required/provided by HTML and (Xe)LaTeX writers.
    head_prefix: str
    # Required/provided by HTML writers.
    header: str
    # Required/provided by HTML writers.
    html_body: str
    # Required/provided by HTML writers.
    html_head: str
    # Required/provided by HTML writers.
    html_prolog: str
    # Required/provided by HTML writers.
    html_subtitle: str
    # Required/provided by HTML writers.
    html_title: str
    # Required/provided by HTML writers.
    meta: str
    # Required/provided by HTML and (Xe)LaTeX writers.
    stylesheet: str
    # Required/provided by HTML and (Xe)LaTeX writers.
    subtitle: str
    # Required/provided by HTML and (Xe)LaTeX writers.
    title: str
    # Required/provided by PEP/HTML and S5/HTML writers.
    pepnum: str
    # Required/provided by (Xe)LaTeX writers.
    abstract: str
    # Required/provided by (Xe)LaTeX writers.
    dedication: str
    # Required/provided by (Xe)LaTeX writers.
    fallbacks: str
    # Required/provided by (Xe)LaTeX writers.
    latex_preamble: str
    # Required/provided by (Xe)LaTeX writers.
    pdfsetup: str
    # Required/provided by (Xe)LaTeX writers.
    requirements: str
    # Required/provided by (Xe)LaTeX writers.
    template: str
    # Required/provided by (Xe)LaTeX writers.
    titledata: str

# Parts returned by HTML writers (e.g. "html4css1", "html5_polyglot", "s5_html", "pep_html").
@type_check_only
class _HTMLWriterParts(TypedDict, total=True):  # noqa: Y049  # used by `core.publish_parts()`
    whole: str
    encoding: str
    errors: str
    version: str
    body: str
    body_prefix: str
    body_pre_docinfo: str
    body_suffix: str
    docinfo: str
    footer: str
    fragment: str
    head: str
    head_prefix: str
    header: str
    html_body: str
    html_head: str
    html_prolog: str
    html_subtitle: str
    html_title: str
    meta: str
    stylesheet: str
    subtitle: str
    title: str
    pepnum: NotRequired[str]  # only "pep_html"

# Parts returned by the (Xe)LaTeX writers ("latex2e", "xetex").
@type_check_only
class _LaTeXWriterParts(TypedDict, total=True):  # noqa: Y049  # used by `core.publish_parts()`
    whole: str
    encoding: str
    errors: str
    version: str
    abstract: str
    body: str
    body_pre_docinfo: str
    dedication: str
    docinfo: str
    fallbacks: str
    head_prefix: str
    latex_preamble: str
    pdfsetup: str
    requirements: str
    stylesheet: str
    subtitle: str
    template: str
    title: str
    titledata: str

class Writer(Component, Generic[_S]):
    parts: _WriterParts
    language: LanguageModule | None = None
    document: nodes.document | None = None
    destination: Output | None = None
    output: _S | None = None
    def __init__(self) -> None: ...
    def write(self, document: nodes.document, destination: Output) -> str | bytes | None: ...
    def translate(self) -> None: ...
    def assemble_parts(self) -> None: ...

class UnfilteredWriter(Writer[_S]): ...

class DoctreeTranslator(nodes.NodeVisitor):
    settings: Values
    def __init__(self, document: nodes.document) -> None: ...
    def uri2path(self, uri: str, output_path: StrPath | None = None) -> Path: ...

WRITER_ALIASES: Final[dict[str, str]]

def get_writer_class(writer_name: str) -> type[Writer[str | bytes]]: ...
