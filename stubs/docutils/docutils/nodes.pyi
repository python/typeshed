from pathlib import Path
from typing import Any, Callable, Dict, Iterable, List, Optional, Tuple, Union, overload

__docformat__: str
unicode = str
basestring = str

class _traversal_list(list):
    done: bool = ...
    __add__: Any = ...
    __contains__: Any = ...
    __getitem__: Any = ...
    __reversed__: Any = ...
    __setitem__: Any = ...
    append: Any = ...
    count: Any = ...
    extend: Any = ...
    index: Any = ...
    insert: Any = ...
    pop: Any = ...
    reverse: Any = ...

class Node:
    parent: Optional[Node] = ...
    document: Optional[document] = ...
    source: Union[Path, str, None] = ...
    line: Optional[int] = ...
    def __bool__(self) -> bool: ...
    def asdom(self, dom: Optional[Any] = ...): ...
    def pformat(self, indent: str = ..., level: int = ...) -> None: ...
    def copy(self) -> Node: ...
    def deepcopy(self) -> Node: ...
    def astext(self) -> str: ...
    def setup_child(self, child: Node) -> None: ...
    def walk(self, visitor: NodeVisitor) -> bool: ...
    def walkabout(self, visitor: NodeVisitor) -> bool: ...
    def traverse(
        self,
        condition: Union[Callable[[Node], bool], Node, None] = ...,
        include_self: bool = ...,
        descend: bool = ...,
        siblings: bool = ...,
        ascend: bool = ...,
    ): ...
    def next_node(
        self,
        condition: Union[Callable[[Node], bool], Node, None] = ...,
        include_self: bool = ...,
        descend: bool = ...,
        siblings: bool = ...,
        ascend: bool = ...,
    ): ...

reprunicode = unicode

def ensure_str(s: unicode) -> str: ...
def unescape(text: str, restore_backslashes: bool = ..., respect_whitespace: bool = ...) -> str: ...

class Text(Node, reprunicode):
    tagname: str = ...
    children: Any = ...
    def __new__(cls, data: Any, rawsource: Optional[Any] = ...): ...
    rawsource: Any = ...
    def __init__(self, data: Any, rawsource: str = ...) -> None: ...
    def shortrepr(self, maxlen: int = ...): ...
    def astext(self): ...
    def copy(self): ...
    def deepcopy(self): ...
    def pformat(self, indent: str = ..., level: int = ...): ...
    def rstrip(self, chars: Optional[Any] = ...): ...
    def lstrip(self, chars: Optional[Any] = ...): ...

class Element(Node):
    basic_attributes: Tuple[str, ...] = ...
    local_attributes: Tuple[str, ...] = ...
    list_attributes: Tuple[str, ...] = ...
    known_attributes: Tuple[str, ...] = ...
    tagname: Optional[str] = ...
    child_text_separator: str = ...
    rawsource: str = ...
    children: List[Node] = ...
    attributes: Dict[str, Any] = ...
    def __init__(self, rawsource: str = ..., *children: List[Node], **attributes: Dict[str, Any]) -> None: ...
    def shortrepr(self) -> str: ...
    def __unicode__(self) -> str: ...
    def starttag(self, quoteattr: Optional[str] = ...) -> str: ...
    def endtag(self) -> str: ...
    def emptytag(self) -> str: ...
    def __len__(self) -> int: ...
    @overload
    def __getitem__(self, key: basestring) -> Any: ...
    @overload
    def __getitem__(self, key: int) -> Node: ...
    @overload
    def __getitem__(self, key: slice) -> Iterable[Node]: ...
    @overload
    def __setitem__(self, key: basestring, item: Any) -> None: ...
    @overload
    def __setitem__(self, key: int, item: Node) -> None: ...
    @overload
    def __setitem__(self, key: slice, item: Iterable[Node]) -> None: ...
    def __delitem__(self, key: Union[basestring, int, slice]) -> None: ...
    def __add__(self, other: Union[Node, Iterable[Node]]): ...
    def __radd__(self, other: Union[Node, Iterable[Node]]): ...
    def __iadd__(self, other: Union[Node, Iterable[Node]]) -> "Element": ...
    def astext(self) -> str: ...
    def non_default_attributes(self) -> Dict[str, Any]: ...
    def attlist(self) -> list: ...
    def get(self, key: str, failobj: Optional[Any] = ...) -> Any: ...
    def hasattr(self, attr: str) -> bool: ...
    def delattr(self, attr: str) -> None: ...
    def setdefault(self, key: Any, failobj: Optional[Any] = ...) -> Any: ...
    has_key: Callable[[str], bool] = ...
    def __contains__(self, key: str) -> bool: ...
    def get_language_code(self, fallback: str = ...): ...
    def append(self, item: Any) -> None: ...
    def extend(self, item: Any) -> None: ...
    def insert(self, index: Any, item: Any) -> None: ...
    def pop(self, i: int = ...): ...
    def remove(self, item: Any) -> None: ...
    def index(self, item: Any): ...
    def is_not_default(self, key: Any): ...
    def update_basic_atts(self, dict_: Any) -> None: ...
    def append_attr_list(self, attr: Any, values: Any) -> None: ...
    def coerce_append_attr_list(self, attr: Any, value: Any) -> None: ...
    def replace_attr(self, attr: Any, value: Any, force: bool = ...) -> None: ...
    def copy_attr_convert(self, attr: Any, value: Any, replace: bool = ...) -> None: ...
    def copy_attr_coerce(self, attr: Any, value: Any, replace: Any) -> None: ...
    def copy_attr_concatenate(self, attr: Any, value: Any, replace: Any) -> None: ...
    def copy_attr_consistent(self, attr: Any, value: Any, replace: Any) -> None: ...
    def update_all_atts(self, dict_: Any, update_fun: Any = ..., replace: bool = ..., and_source: bool = ...) -> None: ...
    def update_all_atts_consistantly(self, dict_: Any, replace: bool = ..., and_source: bool = ...) -> None: ...
    def update_all_atts_concatenating(self, dict_: Any, replace: bool = ..., and_source: bool = ...) -> None: ...
    def update_all_atts_coercion(self, dict_: Any, replace: bool = ..., and_source: bool = ...) -> None: ...
    def update_all_atts_convert(self, dict_: Any, and_source: bool = ...) -> None: ...
    def clear(self) -> None: ...
    def replace(self, old: Any, new: Any) -> None: ...
    def replace_self(self, new: Any) -> None: ...
    def first_child_matching_class(self, childclass: Any, start: int = ..., end: Any = ...): ...
    def first_child_not_matching_class(self, childclass: Any, start: int = ..., end: Any = ...): ...
    def pformat(self, indent: str = ..., level: int = ...): ...
    def copy(self): ...
    def deepcopy(self): ...
    def set_class(self, name: Any) -> None: ...
    referenced: int = ...
    def note_referenced_by(self, name: Optional[Any] = ..., id: Optional[Any] = ...) -> None: ...
    @classmethod
    def is_not_list_attribute(cls, attr: Any): ...
    @classmethod
    def is_not_known_attribute(cls, attr: Any): ...

class TextElement(Element):
    child_text_separator: str = ...
    def __init__(self, rawsource: str = ..., text: str = ..., *children: Any, **attributes: Any) -> None: ...

class FixedTextElement(TextElement):
    def __init__(self, rawsource: str = ..., text: str = ..., *children: Any, **attributes: Any) -> None: ...

class Resolvable:
    resolved: int = ...

class BackLinkable:
    def add_backref(self, refid: Any) -> None: ...

class Root: ...
class Titular: ...
class PreBibliographic: ...
class Bibliographic: ...
class Decorative(PreBibliographic): ...
class Structural: ...
class Body: ...
class General(Body): ...
class Sequential(Body): ...
class Admonition(Body): ...
class Special(Body): ...
class Invisible(PreBibliographic): ...
class Part: ...
class Inline: ...
class Referential(Resolvable): ...

class Targetable(Resolvable):
    referenced: int = ...
    indirect_reference_name: Any = ...

class Labeled: ...

class document(Root, Structural, Element):
    current_source: Any = ...
    current_line: Any = ...
    settings: Any = ...
    reporter: Any = ...
    indirect_targets: Any = ...
    substitution_defs: Any = ...
    substitution_names: Any = ...
    refnames: Any = ...
    refids: Any = ...
    nameids: Any = ...
    nametypes: Any = ...
    ids: Any = ...
    footnote_refs: Any = ...
    citation_refs: Any = ...
    autofootnotes: Any = ...
    autofootnote_refs: Any = ...
    symbol_footnotes: Any = ...
    symbol_footnote_refs: Any = ...
    footnotes: Any = ...
    citations: Any = ...
    autofootnote_start: int = ...
    symbol_footnote_start: int = ...
    id_counter: Any = ...
    parse_messages: Any = ...
    transform_messages: Any = ...
    transformer: Any = ...
    decoration: Any = ...
    document: Any = ...
    def __init__(self, settings: Any, reporter: Any, *args: Any, **kwargs: Any) -> None: ...
    def asdom(self, dom: Optional[Any] = ...): ...
    def set_id(self, node: Any, msgnode: Optional[Any] = ..., suggested_prefix: str = ...): ...
    def set_name_id_map(self, node: Any, id: Any, msgnode: Optional[Any] = ..., explicit: Optional[Any] = ...) -> None: ...
    def set_duplicate_name_id(self, node: Any, id: Any, name: Any, msgnode: Any, explicit: Any) -> None: ...
    def has_name(self, name: Any): ...
    def note_implicit_target(self, target: Any, msgnode: Optional[Any] = ...) -> None: ...
    def note_explicit_target(self, target: Any, msgnode: Optional[Any] = ...) -> None: ...
    def note_refname(self, node: Any) -> None: ...
    def note_refid(self, node: Any) -> None: ...
    def note_indirect_target(self, target: Any) -> None: ...
    def note_anonymous_target(self, target: Any) -> None: ...
    def note_autofootnote(self, footnote: Any) -> None: ...
    def note_autofootnote_ref(self, ref: Any) -> None: ...
    def note_symbol_footnote(self, footnote: Any) -> None: ...
    def note_symbol_footnote_ref(self, ref: Any) -> None: ...
    def note_footnote(self, footnote: Any) -> None: ...
    def note_footnote_ref(self, ref: Any) -> None: ...
    def note_citation(self, citation: Any) -> None: ...
    def note_citation_ref(self, ref: Any) -> None: ...
    def note_substitution_def(self, subdef: Any, def_name: Any, msgnode: Optional[Any] = ...) -> None: ...
    def note_substitution_ref(self, subref: Any, refname: Any) -> None: ...
    def note_pending(self, pending: Any, priority: Optional[Any] = ...) -> None: ...
    def note_parse_message(self, message: Any) -> None: ...
    def note_transform_message(self, message: Any) -> None: ...
    def note_source(self, source: Any, offset: Any) -> None: ...
    def copy(self): ...
    def get_decoration(self): ...

class title(Titular, PreBibliographic, TextElement): ...
class subtitle(Titular, PreBibliographic, TextElement): ...
class rubric(Titular, TextElement): ...
class docinfo(Bibliographic, Element): ...
class author(Bibliographic, TextElement): ...
class authors(Bibliographic, Element): ...
class organization(Bibliographic, TextElement): ...
class address(Bibliographic, FixedTextElement): ...
class contact(Bibliographic, TextElement): ...
class version(Bibliographic, TextElement): ...
class revision(Bibliographic, TextElement): ...
class status(Bibliographic, TextElement): ...
class date(Bibliographic, TextElement): ...
class copyright(Bibliographic, TextElement): ...

class decoration(Decorative, Element):
    def get_header(self): ...
    def get_footer(self): ...

class header(Decorative, Element): ...
class footer(Decorative, Element): ...
class section(Structural, Element): ...
class topic(Structural, Element): ...
class sidebar(Structural, Element): ...
class transition(Structural, Element): ...
class paragraph(General, TextElement): ...
class compound(General, Element): ...
class container(General, Element): ...
class bullet_list(Sequential, Element): ...
class enumerated_list(Sequential, Element): ...
class list_item(Part, Element): ...
class definition_list(Sequential, Element): ...
class definition_list_item(Part, Element): ...
class term(Part, TextElement): ...
class classifier(Part, TextElement): ...
class definition(Part, Element): ...
class field_list(Sequential, Element): ...
class field(Part, Element): ...
class field_name(Part, TextElement): ...
class field_body(Part, Element): ...

class option(Part, Element):
    child_text_separator: str = ...

class option_argument(Part, TextElement):
    def astext(self): ...

class option_group(Part, Element):
    child_text_separator: str = ...

class option_list(Sequential, Element): ...

class option_list_item(Part, Element):
    child_text_separator: str = ...

class option_string(Part, TextElement): ...
class description(Part, Element): ...
class literal_block(General, FixedTextElement): ...
class doctest_block(General, FixedTextElement): ...
class math_block(General, FixedTextElement): ...
class line_block(General, Element): ...

class line(Part, TextElement):
    indent: Any = ...

class block_quote(General, Element): ...
class attribution(Part, TextElement): ...
class attention(Admonition, Element): ...
class caution(Admonition, Element): ...
class danger(Admonition, Element): ...
class error(Admonition, Element): ...
class important(Admonition, Element): ...
class note(Admonition, Element): ...
class tip(Admonition, Element): ...
class hint(Admonition, Element): ...
class warning(Admonition, Element): ...
class admonition(Admonition, Element): ...
class comment(Special, Invisible, FixedTextElement): ...
class substitution_definition(Special, Invisible, TextElement): ...
class target(Special, Invisible, Inline, TextElement, Targetable): ...
class footnote(General, BackLinkable, Element, Labeled, Targetable): ...
class citation(General, BackLinkable, Element, Labeled, Targetable): ...
class label(Part, TextElement): ...
class figure(General, Element): ...
class caption(Part, TextElement): ...
class legend(Part, Element): ...
class table(General, Element): ...
class tgroup(Part, Element): ...
class colspec(Part, Element): ...
class thead(Part, Element): ...
class tbody(Part, Element): ...
class row(Part, Element): ...
class entry(Part, Element): ...

class system_message(Special, BackLinkable, PreBibliographic, Element):
    def __init__(self, message: Optional[Any] = ..., *children: Any, **attributes: Any) -> None: ...
    def astext(self): ...

class pending(Special, Invisible, Element):
    transform: Any = ...
    details: Any = ...
    def __init__(
        self, transform: Any, details: Optional[Any] = ..., rawsource: str = ..., *children: Any, **attributes: Any
    ) -> None: ...
    def pformat(self, indent: str = ..., level: int = ...): ...
    def copy(self): ...

class raw(Special, Inline, PreBibliographic, FixedTextElement): ...
class emphasis(Inline, TextElement): ...
class strong(Inline, TextElement): ...
class literal(Inline, TextElement): ...
class reference(General, Inline, Referential, TextElement): ...
class footnote_reference(Inline, Referential, TextElement): ...
class citation_reference(Inline, Referential, TextElement): ...
class substitution_reference(Inline, TextElement): ...
class title_reference(Inline, TextElement): ...
class abbreviation(Inline, TextElement): ...
class acronym(Inline, TextElement): ...
class superscript(Inline, TextElement): ...
class subscript(Inline, TextElement): ...
class math(Inline, TextElement): ...

class image(General, Inline, Element):
    def astext(self): ...

class inline(Inline, TextElement): ...
class problematic(Inline, TextElement): ...
class generated(Inline, TextElement): ...

node_class_names: Any

class NodeVisitor:
    optional: Any = ...
    document: Any = ...
    def __init__(self, document: Any) -> None: ...
    def dispatch_visit(self, node: Any): ...
    def dispatch_departure(self, node: Any): ...
    def unknown_visit(self, node: Any) -> None: ...
    def unknown_departure(self, node: Any) -> None: ...

class SparseNodeVisitor(NodeVisitor): ...

class GenericNodeVisitor(NodeVisitor):
    def default_visit(self, node: Any) -> None: ...
    def default_departure(self, node: Any) -> None: ...

class TreeCopyVisitor(GenericNodeVisitor):
    parent_stack: Any = ...
    parent: Any = ...
    def __init__(self, document: Any) -> None: ...
    def get_tree_copy(self): ...
    def default_visit(self, node: Any) -> None: ...
    def default_departure(self, node: Any) -> None: ...

class TreePruningException(Exception): ...
class SkipChildren(TreePruningException): ...
class SkipSiblings(TreePruningException): ...
class SkipNode(TreePruningException): ...
class SkipDeparture(TreePruningException): ...
class NodeFound(TreePruningException): ...
class StopTraversal(TreePruningException): ...

def make_id(string: Any): ...
def dupname(node: Any, name: Any) -> None: ...
def fully_normalize_name(name: Any): ...
def whitespace_normalize_name(name: Any): ...
def serial_escape(value: Any): ...
def pseudo_quoteattr(value: Any): ...
