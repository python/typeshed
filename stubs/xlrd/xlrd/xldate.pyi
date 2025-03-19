import datetime
from typing import Literal

_JDN_delta: tuple[int, int]
epoch_1904: datetime.datetime
epoch_1900: datetime.datetime
epoch_1900_minus_1: datetime.datetime
_XLDAYS_TOO_LARGE: tuple[int, int]
_days_in_month: tuple[None, int, int, int, int, int, int, int, int, int, int, int, int]

class XLDateError(ValueError): ...
class XLDateNegative(XLDateError): ...
class XLDateAmbiguous(XLDateError): ...
class XLDateTooLarge(XLDateError): ...
class XLDateBadDatemode(XLDateError): ...
class XLDateBadTuple(XLDateError): ...

# 0: 1900-based, 1: 1904-based.
def xldate_as_tuple(xldate: float, datemode: Literal[0, 1]) -> tuple[int, int, int, int, int, int]: ...
def xldate_as_datetime(xldate: float, datemode: Literal[0, 1]) -> datetime.datetime: ...
def _leap(y: int) -> Literal[0, 1]: ...
def xldate_from_date_tuple(date_tuple: tuple[int, int, int], datemode: Literal[0, 1]) -> float: ...
def xldate_from_time_tuple(time_tuple: tuple[int, int, int]) -> float: ...
def xldate_from_datetime_tuple(datetime_tuple: tuple[int, int, int, int, int, int], datemode: Literal[0, 1]) -> float: ...
