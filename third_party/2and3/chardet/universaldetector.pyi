from typing import Dict, Union, AnyStr, Pattern
from logging import Logger

class UniversalDetector:
    MINIMUM_THRESHOLD: float
    HIGH_BYTE_DETECTOR: Pattern[bytes]
    ESC_DETECTOR: Pattern[bytes]
    WIN_BYTE_DETECTOR: Pattern[bytes]
    ISO_WIN_MAP: Dict[str, str]

    result: Dict[str, Union[str, float]]
    done: bool
    lang_filter: int
    logger: Logger

    def __init__(self, lang_filter: int) -> None: ...
    def reset(self) -> None: ...
    def feed(self, byte_str: bytes) -> None: ...
    def close(self) -> Dict[str, Union[str, float]]: ...
