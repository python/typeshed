from typing import List, MutableSequence, Text

def reset() -> None: ...
def listdir(path: Text) -> List[str]: ...

opendir = listdir

def annotate(head: Text, list: MutableSequence[str] | MutableSequence[Text] | MutableSequence[str | Text]) -> None: ...
