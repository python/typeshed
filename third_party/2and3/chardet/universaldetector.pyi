from typing import Dict, Union, AnyStr, Pattern, Optional
from logging import Logger

if sys.version_info >= (3, 8):
    from typing import TypedDict

    class FinalResultType(TypedDict):
        encoding: str
        confidence: float
        language: str

    class IntermediateResultType(TypedDict):
        encoding: Optional[str]
        confidence: float
        language: Optional[str]

class UniversalDetector(object):
    MINIMUM_THRESHOLD: float
    HIGH_BYTE_DETECTOR: Pattern[bytes]
    ESC_DETECTOR: Pattern[bytes]
    WIN_BYTE_DETECTOR: Pattern[bytes]
    ISO_WIN_MAP: Dict[str, str]

    if sys.version_info >= (3, 8):
        result: IntermediateResultType
    else:
        result: Dict[str, Union[str, float]]
    done: bool
    lang_filter: int
    logger: Logger

    def __init__(self, lang_filter: int) -> None: ...
    def reset(self) -> None: ...
    def feed(self, byte_str: bytes) -> None: ...

    if sys.version_info >= (3, 8):
        def close(self) -> FinalResultType: ...
    else:
        def close(self) -> Dict[str, Union[str, float]]: ...
