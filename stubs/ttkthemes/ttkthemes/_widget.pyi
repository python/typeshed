from typing import Any

from ._utils import get_file_directory as get_file_directory

class ThemedWidget:
    pixmap_themes: Any
    PACKAGES: Any
    tk: Any
    png_support: Any
    def __init__(self, tk_interpreter, gif_override: bool = ...) -> None: ...
    def set_theme(self, theme_name) -> None: ...
    def get_themes(self): ...
    @property
    def themes(self): ...
    @property
    def current_theme(self): ...
    def set_theme_advanced(
        self,
        theme_name,
        brightness: float = ...,
        saturation: float = ...,
        hue: float = ...,
        preserve_transparency: bool = ...,
        output_dir: Any | None = ...,
        advanced_name: str = ...,
    ) -> None: ...
