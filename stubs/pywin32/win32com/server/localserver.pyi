from collections.abc import Iterable

from _win32typing import PyIID

usage = """Invalid command line arguments

This program provides LocalServer COM support
for Python COM objects.

It is typically run automatically by COM, passing as arguments
The ProgID or CLSID of the Python Server(s) to be hosted
"""

def serve(clsids: Iterable[PyIID]) -> None: ...
def main() -> None: ...
