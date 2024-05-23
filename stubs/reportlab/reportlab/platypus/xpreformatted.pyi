from _typeshed import Incomplete

from reportlab.platypus.paragraph import Paragraph

class XPreformatted(Paragraph):
    caseSensitive: Incomplete
    def __init__(
        self,
        text,
        style,
        bulletText: Incomplete | None = None,
        frags: Incomplete | None = None,
        caseSensitive: int = 1,
        dedent: int = 0,
    ) -> None: ...
    height: int
    width: Incomplete
    def breakLines(self, width): ...
    breakLinesCJK = breakLines  # pyright: ignore[reportAssignmentType]

class PythonPreformatted(XPreformatted):
    formats: Incomplete
    def __init__(
        self, text, style, bulletText: Incomplete | None = None, dedent: int = 0, frags: Incomplete | None = None
    ) -> None: ...
    def escapeHtml(self, text): ...
    def fontify(self, code): ...
