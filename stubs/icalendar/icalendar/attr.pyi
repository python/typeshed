rdates_property: property
exdates_property: property
rrules_property: property

def multi_language_text_property(main_prop: str, compatibility_prop: str, doc: str) -> property: ...
def single_int_property(prop: str, default: int, doc: str) -> property: ...
def single_utc_property(name: str, docs: str) -> property: ...
def single_string_property(name: str, docs: str, other_name: str | None = None) -> property: ...

color_property: property
sequence_property: property
categories_property: property

__all__ = [
    "single_utc_property",
    "color_property",
    "multi_language_text_property",
    "single_int_property",
    "sequence_property",
    "categories_property",
    "rdates_property",
    "exdates_property",
    "rrules_property",
]
