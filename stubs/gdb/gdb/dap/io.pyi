from typing import Any, BinaryIO

import gdb

from .server import _JSONValue
from .startup import DAPQueue

def read_json(stream: BinaryIO) -> Any: ...  # returns result of json.loads
def start_json_writer(stream: BinaryIO, queue: DAPQueue[_JSONValue]) -> gdb.Thread: ...
