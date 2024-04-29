from __future__ import annotations

from datetime import date, datetime, time, timedelta, timezone, tzinfo
from typing import Union, cast
from typing_extensions import Never, assert_type

UTC: timezone = timezone.utc

dt_none = cast(datetime[None], None)
dt_tz = cast(datetime[tzinfo], None)
dt_both = cast(datetime[Union[tzinfo, None]], None)

# Constructors

assert_type(datetime(2000, 1, 1), datetime[None])
assert_type(datetime(2000, 1, 1, tzinfo=None), datetime[None])
assert_type(datetime(2000, 1, 1, tzinfo=UTC), datetime[tzinfo])

assert_type(datetime.fromtimestamp(0), datetime[None])
assert_type(datetime.fromtimestamp(0, None), datetime[None])
assert_type(datetime.fromtimestamp(0, UTC), datetime[tzinfo])
assert_type(datetime.utcfromtimestamp(0), datetime[None])  # pyright: ignore[reportDeprecated]

assert_type(datetime.now(), datetime[None])
assert_type(datetime.now(None), datetime[None])
assert_type(datetime.now(UTC), datetime[tzinfo])
assert_type(datetime.utcnow(), datetime[None])  # pyright: ignore[reportDeprecated]

assert_type(datetime.fromisoformat("2000-01-01"), datetime[Union[tzinfo, None]])

# Comparisons

assert_type(dt_none < dt_none, bool)
assert_type(dt_tz < dt_tz, bool)
assert_type(dt_both < dt_both, bool)

assert_type(dt_none < dt_tz, Never)
assert_type(dt_tz < dt_none, Never)
assert_type(dt_both < dt_none, bool)
assert_type(dt_both < dt_tz, bool)
assert_type(dt_none < dt_both, bool)

# Sub

assert_type(dt_none - dt_none, timedelta)
assert_type(dt_tz - dt_tz, timedelta)
assert_type(dt_both - dt_both, timedelta)

assert_type(dt_none - dt_tz, Never)
assert_type(dt_tz - dt_none, Never)
assert_type(dt_both - dt_none, timedelta)
assert_type(dt_both - dt_tz, timedelta)
assert_type(dt_none - dt_both, timedelta)
assert_type(dt_tz - dt_both, timedelta)

# Combine

assert_type(datetime.combine(date(2000, 1, 1), time(12, 0)), datetime[None])
assert_type(datetime.combine(date(2000, 1, 1), time(12, 0), tzinfo=None), datetime[None])
assert_type(datetime.combine(date(2000, 1, 1), time(12, 0), tzinfo=UTC), datetime[tzinfo])

# Replace

assert_type(dt_none.replace(year=2001), datetime[None])
assert_type(dt_none.replace(year=2001, tzinfo=None), datetime[None])
assert_type(dt_none.replace(year=2001, tzinfo=UTC), datetime[tzinfo])
assert_type(dt_tz.replace(year=2001), datetime[tzinfo])
assert_type(dt_tz.replace(year=2001, tzinfo=None), datetime[None])
assert_type(dt_tz.replace(year=2001, tzinfo=UTC), datetime[tzinfo])
assert_type(dt_both.replace(year=2001), datetime[Union[tzinfo, None]])
assert_type(dt_both.replace(year=2001, tzinfo=None), datetime[None])
assert_type(dt_both.replace(year=2001, tzinfo=UTC), datetime[tzinfo])

# Attributes

assert_type(dt_none.tzinfo, None)
assert_type(dt_tz.tzinfo, tzinfo)
assert_type(dt_both.tzinfo, Union[tzinfo, None])
