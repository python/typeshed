import sys
from typing import Optional, Tuple

if sys.platform == "win32":

    _SequenceType = list[Tuple[str, Optional[str], int]]

    AdminExecuteSequence: _SequenceType
    AdminUISequence: _SequenceType
    AdvtExecuteSequence: _SequenceType
    InstallExecuteSequence: _SequenceType
    InstallUISequence: _SequenceType

    tables: list[str]
