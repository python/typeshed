from typing import cast
from typing_extensions import assert_type

from serial.serialutil import SerialBase

serial_base = cast(SerialBase, None)
assert_type(serial_base.read_all(), bytes)
