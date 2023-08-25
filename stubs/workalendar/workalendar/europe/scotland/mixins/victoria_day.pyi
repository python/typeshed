class VictoriaDayMixin:
    include_victoria_day: bool
    victoria_day_label: str

class VictoriaDayFourthMondayMay(VictoriaDayMixin):
    def get_victoria_day(self, year): ...

class VictoriaDayLastMondayMay(VictoriaDayMixin):
    def get_victoria_day(self, year): ...

class VictoriaDayFirstMondayJune(VictoriaDayMixin):
    def get_victoria_day(self, year): ...
