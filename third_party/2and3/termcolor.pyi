# Stub for termcolor: https://pypi.python.org/pypi/termcolor
from typing import Any, Iterable, Optional, Text

def colored(
    text: Text, color: Optional[Text] = ..., on_color: Optional[Text] = ..., attrs: Optional[Iterable[Text]] = ...,
) -> Text: ...
def cprint(
    text: Text, color: Optional[Text] = ..., on_color: Optional[Text] = ..., attrs: Optional[Iterable[Text]] = ..., **kwargs: Any,
) -> None: ...
