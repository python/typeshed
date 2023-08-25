class AutumHoliday:
    include_autumn_holiday: bool
    autumn_holiday_label: str

class AutumnHolidayLastMondaySeptember(AutumHoliday):
    def get_autumn_holiday(self, year): ...

class AutumnHolidayFirstMondayOctober(AutumHoliday):
    def get_autumn_holiday(self, year): ...

class AutumnHolidaySecondMondayOctober(AutumHoliday):
    def get_autumn_holiday(self, year): ...

class AutumnHolidayThirdMondayOctober(AutumHoliday):
    def get_autumn_holiday(self, year): ...
