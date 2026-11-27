from abc import ABCMeta, abstractmethod
from datetime import datetime

class BaseTrigger(metaclass=ABCMeta):
    @abstractmethod
    def get_next_fire_time(self, previous_fire_time: datetime | None, now: datetime) -> datetime | None: ...
