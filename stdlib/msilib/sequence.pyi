import sys
from typing import List,  Tuple

if sys.platform == "win32":

    _SequenceType = List[Tuple[str, str | None, int]]

    AdminExecuteSequence: _SequenceType
    AdminUISequence: _SequenceType
    AdvtExecuteSequence: _SequenceType
    InstallExecuteSequence: _SequenceType
    InstallUISequence: _SequenceType

    tables: list[str]
