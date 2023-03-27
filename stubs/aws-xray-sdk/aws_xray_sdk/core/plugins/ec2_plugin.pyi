from _typeshed import Incomplete
from typing import Any

log: Any
SERVICE_NAME: str
ORIGIN: str
IMDS_URL: str

def initialize() -> None: ...
def get_token(): ...
def get_metadata(token: Incomplete | None = None): ...
def parse_metadata_json(json_str): ...
def do_request(url, headers: Incomplete | None = None, method: str = 'GET'): ...
