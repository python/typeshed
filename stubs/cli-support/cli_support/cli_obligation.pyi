from _typeshed import Incomplete

from .xml_base import XmlBase

class CliObligation(XmlBase):
    TOPIC_TAG: str
    TEXT_TAG: str
    LICENSES_TAG: str
    LICENSE_TAG: str
    text: str
    topic: str
    licenses: Incomplete
    def __init__(self) -> None: ...
