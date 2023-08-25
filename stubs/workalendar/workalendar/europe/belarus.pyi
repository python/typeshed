from _typeshed import Incomplete

from ..core import OrthodoxCalendar

class Belarus(OrthodoxCalendar):
    include_labour_day: bool
    include_christmas: bool
    christmas_day_label: str
    orthodox_christmas_day_label: str
    FIXED_HOLIDAYS: Incomplete
    def get_radonitsa(self, year): ...
    def get_variable_days(self, year): ...
