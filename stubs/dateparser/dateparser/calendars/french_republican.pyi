from datetime import datetime

from dateparser.conf import Settings

from . import CalendarBase

class _french_republican_parser:
    @classmethod
    def _parse_with_parts(cls, datestring: str, settings: Settings) -> tuple[datetime, str | None, tuple[str, ...]]: ...

class FrenchRepublicanCalendar(CalendarBase):
    parser: type[_french_republican_parser]  # type: ignore[assignment]
