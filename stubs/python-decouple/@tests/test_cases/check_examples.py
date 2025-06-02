from __future__ import annotations

from typing import List, Optional
from typing_extensions import assert_type

from decouple import Choices, Csv, config

# Examples from the README
assert_type(config("EMAIL_HOST", default="localhost"), str)
assert_type(config("EMAIL_PORT", default=25, cast=int), int)
assert_type(config("EMAIL_HOST_PASSWORD", default=""), str)
assert_type(config("EMAIL_HOST_USER", default=""), str)
assert_type(config("EMAIL_USE_TLS", default=False, cast=bool), bool)
assert_type(config("ALLOWED_HOSTS", default="127.0.0.1", cast=Csv()), List[str])
assert_type(config("LIST_OF_INTEGERS", cast=Csv(int)), List[int])
assert_type(config("COMPLEX_STRING", cast=Csv(cast=lambda s: s.upper(), delimiter="\t", strip=" %*")), List[str])
assert_type(config("CONNECTION_TYPE", cast=Choices(["eth", "usb", "bluetooth"])), str)
assert_type(config("SOME_NUMBER", cast=Choices([7, 14, 42], cast=int)), int)

USB = "usb"
ETH = "eth"
BLUETOOTH = "bluetooth"
CONNECTION_OPTIONS = ((USB, "USB"), (ETH, "Ethernet"), (BLUETOOTH, "Bluetooth"))
assert_type(config("CONNECTION_TYPE", cast=Choices(choices=CONNECTION_OPTIONS)), str)
assert_type(config("CONNECTION_TYPE", cast=Choices(["eth", "usb", "bluetooth"])), str)


# Example from https://github.com/HBNetwork/python-decouple/issues/140
class Controller:
    def __init__(self, max_allowed_power: int):
        self._max_allowed_power = max_allowed_power


controller = Controller(config("MAX_ALLOWED_POWER", cast=int))


# Example from https://github.com/HBNetwork/python-decouple/issues/159
assert_type(config("MAX_RETRIES", cast=lambda v: int(v) if v else None, default=None), Optional[int])
