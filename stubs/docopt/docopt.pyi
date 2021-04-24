from typing import Any, Iterable, Optional

__version__: str

def docopt(
    doc: str,
    argv: Optional[Iterable[str]] = ...,
    help: bool = ...,
    version: Optional[Any] = ...,
    options_first: bool = ...,
) -> dict[str, Any]: ...  # Really should be dict[str, Union[str, bool]]
