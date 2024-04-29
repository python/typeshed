from datetime import date, datetime, time, tzinfo, UTC
from typing import assert_type

dt_wo: datetime[None]
dt_tz: datetime[tzinfo]
dt_any: datetime[tzinfo | None]


# Constructors

assert_type(datetime(2000, 1, 1), datetime[None])
assert_type(datetime(2000, 1, 1, tzinfo=None), datetime[None])
assert_type(datetime(2000, 1, 1, tzinfo=UTC), datetime[tzinfo])

assert_type(datetime.fromtimestamp(0), datetime[None])
assert_type(datetime.fromtimestamp(0, None), datetime[None])
assert_type(datetime.fromtimestamp(0, UTC), datetime[tzinfo])
assert_type(datetime.utcfromtimestamp(0), datetime[None])

assert_type(datetime.now(), datetime[None])
assert_type(datetime.now(None), datetime[None])
assert_type(datetime.now(UTC), datetime[tzinfo])
assert_type(datetime.utcnow(), datetime[None])

assert_type(datetime.fromisoformat("2000-01-01"), datetime[tzinfo | None])

# Combine

assert_type(datetime.combine(date(2000, 1, 1), time(12, 0)), datetime[None])
assert_type(datetime.combine(date(2000, 1, 1), time(12, 0), tzinfo=None), datetime[None])
assert_type(datetime.combine(date(2000, 1, 1), time(12, 0), tzinfo=UTC), datetime[tzinfo])

# Replace

assert_type(dt_wo.replace(year=2001), datetime[None])
assert_type(dt_wo.replace(year=2001, tzinfo=None), datetime[None])
assert_type(dt_wo.replace(year=2001, tzinfo=UTC), datetime[tzinfo])
assert_type(dt_tz.replace(year=2001), datetime[tzinfo])
assert_type(dt_tz.replace(year=2001, tzinfo=None), datetime[None])
assert_type(dt_tz.replace(year=2001, tzinfo=UTC), datetime[tzinfo])
assert_type(dt_any.replace(year=2001), datetime[tzinfo | None])
assert_type(dt_any.replace(year=2001, tzinfo=None), datetime[None])
assert_type(dt_any.replace(year=2001, tzinfo=UTC), datetime[tzinfo])

# Attributes

assert_type(dt_wo.tzinfo, None)
assert_type(dt_tz.tzinfo, tzinfo)
assert_type(dt_any.tzinfo, tzinfo | None)
