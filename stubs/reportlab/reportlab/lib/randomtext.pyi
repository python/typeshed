from collections.abc import Sequence
from typing import Final

__version__: Final[str]
STARTUP: Final[Sequence[str]]
COMPUTERS: Final[Sequence[str]]
BLAH: Final[Sequence[str]]
BUZZWORD: Final[Sequence[str]]
STARTREK: Final[Sequence[str]]
PRINTING: Final[Sequence[str]]
PYTHON: Final[Sequence[str]]
leadins: Final[Sequence[str]]
subjects: Final[Sequence[str]]
verbs: Final[Sequence[str]]
objects: Final[Sequence[str]]

def format_wisdom(text: str, line_length: int = 72) -> str: ...
def chomsky(times: int = 1) -> str: ...
def randomText(
    theme: str | Sequence[str] = [
        "strategic",
        "direction",
        "proactive",
        "venture capital",
        "reengineering",
        "forecast",
        "resources",
        "SWOT analysis",
        "forward-thinking",
        "profit",
        "growth",
        "doubletalk",
        "B2B",
        "B2C",
        "venture capital",
        "IPO",
        "NASDAQ meltdown - we're all doomed!",
    ],
    sentences: int = 5,
) -> str: ...
