from .xml_base import XmlBase

class CliExternalId(XmlBase):
    KEY_TAG: str
    VALUE_TAG: str
    key: str
    value: str
    def __init__(self) -> None: ...
