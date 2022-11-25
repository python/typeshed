from re import Pattern
from socket import socket

from Xlib._typing import Address, Unused

display_re: Pattern[str]

def get_display(display: str | None) -> tuple[str, None, str, int, int]: ...
def get_socket(dname: Address, protocol: Unused, host: Address, dno: int) -> socket: ...
def get_auth(sock: Unused, dname: Unused, host: Unused, dno: Unused) -> tuple[str, str]: ...
