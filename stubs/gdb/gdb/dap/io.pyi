from typing import Any, BinaryIO

import gdb

from .startup import DAPQueue

def read_json(stream: BinaryIO) -> Any: ...  # returns result of json.loads

# objects from queue are passed to json.dumps
def start_json_writer(stream: BinaryIO, queue: DAPQueue[Any]) -> gdb.Thread: ...
