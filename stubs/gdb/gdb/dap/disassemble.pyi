from typing import TypedDict, type_check_only

@type_check_only
class _Instruction(TypedDict):
    address: str
    instruction: str
    instructionBytes: str

@type_check_only
class _DisassembleResult(TypedDict):
    instructions: _Instruction

def disassemble(
    *, memoryReference: str, offset: int = 0, instructionOffset: int = 0, instructionCount: int, **extra
) -> _DisassembleResult: ...  # extra argument is unused
