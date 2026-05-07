# At runtime, listing submodules in __all__ without them being imported is
# valid, and causes them to be included in a star import. See #6523
__all__ = ["dom", "parsers", "sax", "etree"]  # noqa: F822  # pyright: ignore[reportUnsupportedDunderAll]
import sys

if sys.version_info >= (3, 15):
    def is_valid_name(name: str) -> bool: ...
    def is_valid_text(data: str) -> bool: ...
