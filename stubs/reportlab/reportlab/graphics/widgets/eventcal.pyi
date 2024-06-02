from _typeshed import Incomplete
from typing import Final

from reportlab.graphics.widgetbase import Widget

__version__: Final[str]

class EventCalendar(Widget):
    x: int
    y: int
    width: int
    height: int
    timeColWidth: Incomplete
    trackRowHeight: int
    data: Incomplete
    trackNames: Incomplete
    startTime: Incomplete
    endTime: Incomplete
    day: int
    def __init__(self) -> None: ...
    def computeSize(self) -> None: ...
    def computeStartAndEndTimes(self) -> None: ...
    def getAllTracks(self): ...
    def getRelevantTalks(self, talkList): ...
    def scaleTime(self, theTime): ...
    def getTalkRect(self, startTime, duration, trackId, text): ...
    def draw(self): ...

def test() -> None: ...
