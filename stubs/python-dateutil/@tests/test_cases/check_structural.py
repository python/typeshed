from collections.abc import Sequence
from datetime import date, datetime, time, timedelta, tzinfo
from io import StringIO
from typing_extensions import assert_type

from dateutil import parser, utils
from dateutil.relativedelta import relativedelta
from dateutil.rrule import WEEKLY, rrule, rruleset
from dateutil.tz import UTC, tzoffset, tzstr


class CharacterStream:
    def __init__(self, text: str) -> None:
        self.stream = StringIO(text)

    def read(self, size: int, /) -> str:
        return self.stream.read(size)


class TimezoneLookup:
    def get(self, name: str, /) -> tzinfo | None:
        return UTC if name == "CSTM" else None

    def __contains__(self, name: object, /) -> bool:
        return name == "CSTM"


class Monday:
    weekday = 0
    n = None


class Offset:
    def total_seconds(self) -> float:
        return 5400


def check_parser(flag: bool) -> None:
    assert_type(parser.parse(CharacterStream("2024-01-01")), datetime)
    assert_type(parser.parse("2024-01-01", fuzzy_with_tokens=flag), datetime | tuple[datetime, tuple[str, ...]])
    assert_type(parser.parser().parse("2024-01-01", fuzzy_with_tokens=flag), datetime | tuple[datetime, tuple[str, ...]])
    parser.parse("2024-01-01 00:00 CSTM", tzinfos=TimezoneLookup())


def check_utilities() -> None:
    assert_type(utils.default_tzinfo(time(12), UTC), time)
    assert_type(utils.default_tzinfo(datetime(2024, 1, 1), None), datetime)
    utils.within_delta(3, 4, 1)
    utils.within_delta(date(2024, 1, 1), date(2024, 1, 2), timedelta(days=1))


def check_recurrence() -> None:
    rule = rrule(WEEKLY, dtstart=datetime(2024, 1, 1), byweekday=(day for day in (Monday(), 2)), count=3)
    assert_type(rule[0], datetime)
    assert_type(rule[:2], Sequence[datetime])
    rules = rruleset()
    rules.rrule(iter(rule))
    rules.exrule((datetime(2024, 1, 1),))
    assert_type(relativedelta(days=1.5, weekday=Monday()) * "2", relativedelta)


def check_offsets() -> None:
    assert_type(tzoffset("custom", Offset()).utcoffset(None), timedelta)
    assert_type(tzstr.instance("EST5"), tzstr)
