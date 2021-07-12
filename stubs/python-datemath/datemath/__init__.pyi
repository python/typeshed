from datetime import datetime

import arrow

from .helpers import DateMathException as DateMathException, parse as parse

def dm(expression: str, now: arrow.Arrow | None, tz: str, type: str | None, roundDown: bool) -> arrow.Arrow: ...
def datemath(expression: str, now: arrow.Arrow | None, tz: str, type: str | None, roundDown: bool) -> datetime: ...
