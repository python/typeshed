from typing import Any

esc: str
codes: Any
dark_colors: Any
light_colors: Any
x: int

def reset_color(): ...
def colorize(color_key, text): ...
def ansiformat(attr, text): ...
