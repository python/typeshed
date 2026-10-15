from _typeshed import Incomplete

class Font:
    hb_font: Incomplete
    hb_face: Incomplete
    file_content: Incomplete
    index: Incomplete
    font_size: Incomplete
    style: Incomplete
    family: Incomplete
    variations: Incomplete
    weight: Incomplete
    hash: Incomplete
    name: Incomplete
    ascent: Incomplete
    descent: Incomplete
    tables: Incomplete
    bitmap: bool
    italic_angle: int
    upem: Incomplete
    png: Incomplete
    svg: Incomplete
    glyph_count: Incomplete
    stemv: int
    stemh: int
    widths: Incomplete
    to_unicode: Incomplete
    missing: Incomplete
    used_in_forms: bool
    flags: Incomplete
    def __init__(self, pango_font, description, font_size) -> None: ...
    def get_unused_glyph_id(self, codepoint): ...
    def clean(self, to_unicode, hinting) -> None: ...
    @property
    def type(self): ...
    def subset(self, to_unicode, hinting) -> None: ...

def build_fonts_dictionary(pdf, fonts, compress, subset, options): ...
