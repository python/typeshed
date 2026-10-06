from _typeshed import Unused
from datetime import datetime

class TimeStamp(datetime):
    def __deepcopy__(self, memo: Unused) -> TimeStamp: ...
