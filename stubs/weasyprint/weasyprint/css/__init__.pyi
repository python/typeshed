from _typeshed import Incomplete
from collections.abc import Generator
from typing import NamedTuple

PSEUDO_ELEMENTS: Incomplete

class PageSelectorType(NamedTuple):
    side: Incomplete
    blank: Incomplete
    first: Incomplete
    index: Incomplete
    name: Incomplete

class StyleFor:
    font_config: Incomplete
    def __init__(self, html, sheets, presentational_hints, font_config, target_collector) -> None: ...
    def __call__(self, element, pseudo_type=None): ...
    def set_computed_styles(self, element, parent, root=None, pseudo_type=None, base_url=None, target_collector=None) -> None: ...
    def add_page_declarations(self, page_type) -> None: ...
    def get_cascaded_styles(self): ...
    def get_computed_styles(self): ...

def get_child_text(element): ...
def text_decoration(key, value, parent_value, cascaded): ...
def find_stylesheets(
    wrapper_element, device_media_type, url_fetcher, base_url, font_config, counter_style, color_profiles, page_rules, layers
) -> Generator[Incomplete]: ...
def find_style_attributes(tree, presentational_hints: bool = False, base_url=None) -> Generator[Incomplete, None, Incomplete]: ...
def declaration_precedence(origin, importance): ...
def resolve_var(computed, token, parent_style, known_variables=None): ...
def resolve_math(token, computed=None, property_name=None, refer_to=None): ...

class InitialStyle(dict):
    parent_style: Incomplete
    specified: Incomplete
    cache: Incomplete
    font_config: Incomplete
    def __init__(self, font_config) -> None: ...
    def __missing__(self, key): ...

class AnonymousStyle(dict):
    parent_style: Incomplete
    is_root_element: bool
    specified: Incomplete
    cache: Incomplete
    font_config: Incomplete
    def __init__(self, parent_style) -> None: ...
    def copy(self): ...
    def __missing__(self, key): ...

class ComputedStyle(dict):
    specified: Incomplete
    parent_style: Incomplete
    cascaded: Incomplete
    is_root_element: Incomplete
    element: Incomplete
    pseudo_type: Incomplete
    root_style: Incomplete
    base_url: Incomplete
    font_config: Incomplete
    cache: Incomplete
    def __init__(self, parent_style, cascaded, element, pseudo_type, root_style, base_url, font_config) -> None: ...
    def copy(self): ...
    def __missing__(self, key): ...

class ColorProfile:
    src: Incomplete
    renderingintent: Incomplete
    components: Incomplete
    def __init__(self, file_object, descriptors) -> None: ...
    @property
    def name(self): ...
    @property
    def content(self): ...

def computed_from_cascaded(
    element, cascaded, parent_style, pseudo_type=None, root_style=None, base_url=None, target_collector=None
): ...
def parse_color_profile_name(prelude): ...
def parse_page_selectors(rule): ...
def preprocess_stylesheet(
    device_media_type,
    base_url,
    stylesheet_rules,
    url_fetcher,
    matcher,
    page_rules,
    layers,
    font_config,
    counter_style,
    color_profiles,
    ignore_imports: bool = False,
    layer=None,
): ...
def get_all_computed_styles(
    html,
    user_stylesheets=None,
    presentational_hints: bool = False,
    font_config=None,
    counter_style=None,
    color_profiles=None,
    page_rules=None,
    layers=None,
    target_collector=None,
    forms: bool = False,
): ...
