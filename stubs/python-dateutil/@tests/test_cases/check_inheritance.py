from datetime import date, datetime
from typing_extensions import assert_type

from dateutil.relativedelta import relativedelta


class MyDateTime(datetime):
    pass


d = MyDateTime.now()
x = d - relativedelta(days=1)
assert_type(x, MyDateTime)

d3 = datetime.today()
x3 = d3 - relativedelta(days=1)
assert_type(x3, datetime)

d2 = date.today()
x2 = d2 - relativedelta(days=1)
assert_type(x2, date)


class MyDate(date):
    pass


# A date subclass can be promoted to datetime when the delta includes time.
assert_type(MyDate(2024, 1, 1) + relativedelta(hours=1), date)
