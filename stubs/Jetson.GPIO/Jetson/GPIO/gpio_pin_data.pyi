from collections.abc import Sequence
from typing import Any, Final

CLARA_AGX_XAVIER: Final = "CLARA_AGX_XAVIER"
JETSON_NX: Final = "JETSON_NX"
JETSON_XAVIER: Final = "JETSON_XAVIER"
JETSON_TX2: Final = "JETSON_TX2"
JETSON_TX1: Final = "JETSON_TX1"
JETSON_NANO: Final = "JETSON_NANO"
JETSON_TX2_NX: Final = "JETSON_TX2_NX"
JETSON_ORIN: Final = "JETSON_ORIN"
JETSON_ORIN_NX: Final = "JETSON_ORIN_NX"
JETSON_ORIN_NANO: Final = "JETSON_ORIN_NANO"

JETSON_MODELS: list[str] = ...

JETSON_ORIN_NX_PIN_DEFS: list[tuple[int, str, str, int, int, str, str, str | None, int | None]] = ...
compats_jetson_orins_nx: Sequence[str] = ...
compats_jetson_orins_nano: Sequence[str] = ...

JETSON_ORIN_PIN_DEFS: list[tuple[int, str, str, int, int, str, str, str | None, int | None]] = ...
compats_jetson_orins: Sequence[str] = ...

CLARA_AGX_XAVIER_PIN_DEFS: list[tuple[int, str, str, int, int, str, str, str | None, int | None]] = ...
compats_clara_agx_xavier: Sequence[str] = ...

JETSON_NX_PIN_DEFS: list[tuple[int, str, str, int, int, str, str, str | None, int | None]] = ...
compats_nx: Sequence[str] = ...

JETSON_XAVIER_PIN_DEFS: list[tuple[int, str, str, int, int, str, str, str | None, int | None]] = ...
compats_xavier: Sequence[str] = ...

JETSON_TX2_NX_PIN_DEFS: list[tuple[int, str, str, int, int, str, str, str | None, int | None]] = ...
compats_tx2_nx: Sequence[str] = ...

JETSON_TX2_PIN_DEFS: list[tuple[int, str, str, int, int, str, str, str | None, int | None]] = ...
compats_tx2: Sequence[str] = ...

JETSON_TX1_PIN_DEFS: list[tuple[int, str, str, int, int, str, str, str | None, int | None]] = ...
compats_tx1: Sequence[str] = ...

JETSON_NANO_PIN_DEFS: list[tuple[int, str, str, int, int, str, str, str | None, int | None]] = ...
compats_nano: Sequence[str] = ...

jetson_gpio_data: dict[str, tuple[list[tuple[int, str, str, int, int, str, str, str | None, int | None]], dict[str, Any]]] = ...

class ChannelInfo:
    def __init__(
        self, channel: int, line_offset: int, gpio_name: str, gpio_chip: str, pwm_chip_dir: str, pwm_id: int
    ) -> None: ...

ids_warned: bool = ...

def find_pmgr_board(prefix: str) -> str | None: ...
def warn_if_not_carrier_board(*carrier_boards: str) -> None: ...
def get_compatibles(compatible_path: str) -> list[str]: ...
def get_model() -> str: ...
def get_data() -> tuple[str, Any, dict[str, dict[Any, ChannelInfo]]]: ...
