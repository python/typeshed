from click.core import Context
from typing import Optional


def get_current_context(silent: bool = False) -> Context:
    ...


def push_context(ctx: Context) -> None:
    ...


def pop_context() -> None:
    ...


def resolve_color_default(color: Optional[bool] = None) -> Optional[bool]:
    ...
