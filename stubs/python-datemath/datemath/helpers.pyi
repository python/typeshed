from typing import Any

import arrow

class DateMathException: ...

def parse(expression: str, now: arrow.Arrow | None, tz: str, type: str | None, roundDown: bool) -> arrow.Arrow: ...
def __getattr__(name: str) -> Any: ...  # incomplete
