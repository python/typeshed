from _typeshed import Incomplete

__version__: str

def getStdMonthNames(): ...
def getStdShortMonthNames(): ...
def getStdDayNames(): ...
def getStdShortDayNames(): ...
def isLeapYear(year): ...

class NormalDateException(Exception): ...

class NormalDate:
    def __init__(self, normalDate: Incomplete | None = None) -> None: ...
    def add(self, days) -> None: ...
    def __add__(self, days): ...
    def __radd__(self, days): ...
    def clone(self): ...
    def __lt__(self, other): ...
    def __le__(self, other): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
    def __ge__(self, other): ...
    def __gt__(self, other): ...
    def day(self): ...
    def dayOfWeek(self): ...
    @property
    def __day_of_week_name__(self): ...
    def dayOfWeekAbbrev(self): ...
    def dayOfWeekName(self): ...
    def dayOfYear(self): ...
    def daysBetweenDates(self, normalDate): ...
    def equals(self, target): ...
    def endOfMonth(self): ...
    def firstDayOfMonth(self): ...
    def formatUS(self): ...
    def formatUSCentury(self): ...
    def formatMS(self, fmt): ...
    def __hash__(self): ...
    def __int__(self) -> int: ...
    def isLeapYear(self): ...
    def lastDayOfMonth(self): ...
    def localeFormat(self): ...
    def month(self): ...
    @property
    def __month_name__(self): ...
    def monthAbbrev(self): ...
    def monthName(self): ...
    def normalize(self, scalar) -> None: ...
    def range(self, days): ...
    def scalar(self): ...
    def setDay(self, day) -> None: ...
    def setMonth(self, month) -> None: ...
    normalDate: Incomplete
    def setNormalDate(self, normalDate) -> None: ...
    def setYear(self, year) -> None: ...
    def __sub__(self, v): ...
    def __rsub__(self, v): ...
    def toTuple(self): ...
    def year(self): ...

def bigBang(): ...
def bigCrunch(): ...
def dayOfWeek(y, m, d): ...
def firstDayOfYear(year): ...
def FND(d): ...

Epoch: Incomplete
ND = NormalDate
BDEpoch: Incomplete
BDEpochScalar: int

class BusinessDate(NormalDate):
    def add(self, days) -> None: ...
    def __add__(self, days): ...
    def __sub__(self, v): ...
    def asNormalDate(self): ...
    def daysBetweenDates(self, normalDate): ...
    def normalize(self, i) -> None: ...
    def scalar(self): ...
    def setNormalDate(self, normalDate) -> None: ...
