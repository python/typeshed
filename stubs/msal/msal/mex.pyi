from _typeshed import Incomplete
from logging import Logger
from xml.etree.ElementTree import Element

logger: Logger

def send_request(mex_endpoint: str, http_client, **kwargs) -> dict[str, Incomplete] | None: ...

class Mex:
    NS: dict[str, str]
    ACTION_13: str
    ACTION_2005: str
    dom: Element
    def __init__(self, mex_document: str) -> None: ...
    def get_wstrust_username_password_endpoint(self) -> dict[str, Incomplete] | None: ...
