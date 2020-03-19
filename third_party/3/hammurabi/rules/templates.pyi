from hammurabi.rules.common import SinglePathRule as SinglePathRule
from pathlib import Path
from typing import Any, Dict, Optional

class TemplateRendered(SinglePathRule):
    destination: Any = ...
    context: Any = ...
    def __init__(
        self,
        name: str,
        template: Optional[Path] = ...,
        destination: Optional[Path] = ...,
        context: Optional[Dict[str, Any]] = ...,
        **kwargs: Any
    ) -> None: ...
    def post_task_hook(self) -> None: ...
    def task(self) -> Path: ...
