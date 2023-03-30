from _typeshed import Incomplete
from typing_extensions import Literal, TypeAlias

from openpyxl.descriptors.base import NoneSet
from openpyxl.descriptors.serialisable import Serialisable

_WebPublishingTargetScreenSize: TypeAlias = Literal[
    "544x376",
    "640x480",
    "720x512",
    "800x600",
    "1024x768",
    "1152x882",
    "1152x900",
    "1280x1024",
    "1600x1200",
    "1800x1440",
    "1920x1200",
]

class WebPublishObject(Serialisable):
    tagname: str
    id: Incomplete
    divId: Incomplete
    sourceObject: Incomplete
    destinationFile: Incomplete
    title: Incomplete
    autoRepublish: Incomplete
    def __init__(
        self,
        id: Incomplete | None = None,
        divId: Incomplete | None = None,
        sourceObject: Incomplete | None = None,
        destinationFile: Incomplete | None = None,
        title: Incomplete | None = None,
        autoRepublish: Incomplete | None = None,
    ) -> None: ...

class WebPublishObjectList(Serialisable):
    tagname: str
    # Overwritten by property below
    # count: Integer
    webPublishObject: Incomplete
    __elements__: Incomplete
    def __init__(self, count: Incomplete | None = None, webPublishObject=()) -> None: ...
    @property
    def count(self): ...

class WebPublishing(Serialisable):
    tagname: str
    css: Incomplete
    thicket: Incomplete
    longFileNames: Incomplete
    vml: Incomplete
    allowPng: Incomplete
    targetScreenSize: NoneSet[_WebPublishingTargetScreenSize]
    dpi: Incomplete
    codePage: Incomplete
    characterSet: Incomplete
    def __init__(
        self,
        css: Incomplete | None = None,
        thicket: Incomplete | None = None,
        longFileNames: Incomplete | None = None,
        vml: Incomplete | None = None,
        allowPng: Incomplete | None = None,
        targetScreenSize: _WebPublishingTargetScreenSize | Literal["none"] | None = "800x600",
        dpi: Incomplete | None = None,
        codePage: Incomplete | None = None,
        characterSet: Incomplete | None = None,
    ) -> None: ...
