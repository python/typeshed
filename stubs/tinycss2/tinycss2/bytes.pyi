from webencodings import Encoding

from .ast import Node

def decode_stylesheet_bytes(
    css_bytes: bytes, protocol_encoding: str | None = ..., environment_encoding: Encoding | None = ...
) -> tuple[str, Encoding]: ...
def parse_stylesheet_bytes(
    css_bytes: bytes,
    protocol_encoding: str | None = ...,
    environment_encoding: Encoding | None = ...,
    skip_comments: bool = ...,
    skip_whitespace: bool = ...,
) -> tuple[list[Node], Encoding]: ...
