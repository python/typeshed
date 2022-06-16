import datetime
from collections.abc import Iterable
from decimal import Decimal
from typing_extensions import Literal, NotRequired, TypedDict

from .feedback import _Feedback
from .matching import _Match
from .time_estimates import _CrackTimesDisplay, _CrackTimeSeconds

class _Result(TypedDict):
    password: str
    guesses: Decimal
    guesses_log10: float
    sequence: list[_Match]
    calc_time: NotRequired[datetime.timedelta]
    crack_times_seconds: NotRequired[_CrackTimeSeconds]
    crack_times_display: NotRequired[_CrackTimesDisplay]
    score: Literal[0, 1, 2, 3, 4]
    feedback: _Feedback

def zxcvbn(password: str, user_inputs: Iterable[object] | None = ...) -> _Result: ...
