from _typeshed import Incomplete
from typing import NamedTuple

class EHABIBytecodeDecoder:
    mnemonic_array: Incomplete
    def __init__(self, bytecode_array) -> None: ...
    gpr_register_names: Incomplete

    class _DECODE_RECIPE_TYPE(NamedTuple):
        mask: Incomplete
        value: Incomplete
        handler: Incomplete
    ring: Incomplete

class MnemonicItem:
    bytecode: Incomplete
    mnemonic: Incomplete
    def __init__(self, bytecode, mnemonic) -> None: ...
