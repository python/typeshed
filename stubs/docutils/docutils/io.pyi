from _typeshed import (
    OpenBinaryModeReading,
    OpenBinaryModeWriting,
    OpenTextModeReading,
    OpenTextModeWriting,
    StrPath,
    SupportsWrite,
    Unused,
)
from re import Pattern
from typing import IO, ClassVar, Final, Generic, Literal, TextIO, TypeVar, overload
from typing_extensions import deprecated

from docutils import TransformSpec, nodes

__docformat__: Final = "reStructuredText"

class InputError(OSError): ...
class OutputError(OSError): ...

def check_encoding(stream: TextIO, encoding: str) -> bool | None: ...
def error_string(err: BaseException) -> str: ...

_S = TypeVar("_S")
_R = TypeVar("_R", default=str)

class Input(TransformSpec, Generic[_S, _R]):
    component_type: ClassVar[str]
    default_source_path: ClassVar[str | None]
    encoding: str | None
    error_handler: str
    source: _S | None
    source_path: str | None
    successful_encoding: str | None = None
    def __init__(
        self,
        source: _S | None = None,
        source_path: str | None = None,
        encoding: str | None = "utf-8",
        error_handler: str = "strict",
    ) -> None: ...
    def read(self) -> _R: ...
    def decode(self, data: str | bytes | bytearray) -> str: ...
    coding_slug: ClassVar[Pattern[bytes]]
    byte_order_marks: ClassVar[tuple[tuple[bytes, str], ...]]

    @deprecated("Deprecated and will be removed in Docutils 1.0.")
    def determine_encoding_from_data(self, data: str | bytes | bytearray) -> str | None: ...
    def isatty(self) -> bool: ...

class Output(TransformSpec):
    component_type: ClassVar[str]
    default_destination_path: ClassVar[str | None]
    encoding: str | None
    error_handler: str
    # A file-like object (`FileOutput`), the output data (`StringOutput`), or `None`.
    destination: IO[str] | IO[bytes] | str | bytes | None
    destination_path: StrPath | None
    def __init__(
        self,
        destination: IO[str] | IO[bytes] | str | bytes | None = None,
        destination_path: StrPath | None = None,
        encoding: str | None = None,
        error_handler: str | None = "strict",
    ) -> None: ...
    def write(self, data: str | bytes) -> str | bytes | None: ...

    # `str` is encoded to `bytes` unless the output encoding is "unicode".
    @overload
    def encode(self, data: bytes) -> bytes: ...
    @overload
    def encode(self, data: str) -> str | bytes: ...

class ErrorOutput:
    destination: SupportsWrite[str] | SupportsWrite[bytes] | Literal[False]
    encoding: str
    encoding_errors: str
    decoding_errors: str
    def __init__(
        self,
        destination: str | SupportsWrite[str] | SupportsWrite[bytes] | Literal[False] | None = None,
        encoding: str | None = None,
        encoding_errors: str = "backslashreplace",
        decoding_errors: str = "replace",
    ) -> None: ...
    def write(self, data: str | bytes | Exception) -> None: ...
    def close(self) -> None: ...
    def isatty(self) -> bool: ...

class FileInput(Input[IO[str]]):
    autoclose: bool
    def __init__(
        self,
        source: IO[str] | None = None,
        source_path: StrPath | None = None,
        encoding: str | None = "utf-8",
        error_handler: str | None = "strict",
        autoclose: bool = True,
        mode: OpenTextModeReading | OpenBinaryModeReading = "r",
    ) -> None: ...
    def read(self) -> str: ...
    def readlines(self) -> list[str]: ...
    def close(self) -> None: ...

class FileOutput(Output):
    default_destination_path: ClassVar[str]
    mode: ClassVar[OpenTextModeWriting | OpenBinaryModeWriting]
    opened: bool
    autoclose: bool
    destination: IO[str] | IO[bytes] | None
    def __init__(
        self,
        destination: IO[str] | IO[bytes] | None = None,
        destination_path: StrPath | None = None,
        encoding: str | None = None,
        error_handler: str | None = "strict",
        autoclose: bool = True,
        handle_io_errors: None = None,
        mode: OpenTextModeWriting | OpenBinaryModeWriting | None = None,
    ) -> None: ...
    def open(self) -> None: ...
    def write(self, data: str | bytes) -> str | bytes: ...
    def close(self) -> None: ...

class BinaryFileOutput(FileOutput):
    @deprecated("The `BinaryFileOutput` is deprecated by `FileOutput` and will be removed in Docutils 0.24.")
    def __init__(
        self,
        destination: IO[str] | IO[bytes] | None = None,
        destination_path: StrPath | None = None,
        encoding: str | None = None,
        error_handler: str | None = "strict",
        autoclose: bool = True,
        handle_io_errors: None = None,
        mode: OpenTextModeWriting | OpenBinaryModeWriting | None = None,
    ) -> None: ...

class StringInput(Input[str]):
    default_source_path: ClassVar[str]
    def read(self) -> str: ...

class StringOutput(Output):
    default_destination_path: ClassVar[str]
    # Only defined after a call to write().
    destination: str | bytes
    def write(self, data: str | bytes) -> str | bytes: ...

class NullInput(Input[None, str]):
    default_source_path: ClassVar[str]
    def read(self) -> str: ...

class NullOutput(Output):
    default_destination_path: ClassVar[str]
    destination: None
    def write(self, data: Unused) -> None: ...

class DocTreeInput(Input[nodes.document, nodes.document]):
    default_source_path: ClassVar[str]
    def read(self) -> nodes.document: ...
