from _typeshed import Incomplete

from ruamel.yaml.error import MarkedYAMLError
from ruamel.yaml.events import *
from ruamel.yaml.tag import Tag
from ruamel.yaml.tokens import *

__all__ = ["Parser", "RoundTripParser", "ParserError"]

class ParserError(MarkedYAMLError): ...

class Parser:
    DEFAULT_TAGS: Incomplete
    loader: Incomplete
    def __init__(self, loader) -> None: ...
    current_event: Incomplete
    tag_handles: Incomplete
    states: Incomplete
    marks: Incomplete
    state: Incomplete
    def reset_parser(self) -> None: ...
    def dispose(self) -> None: ...
    @property
    def scanner(self): ...
    @property
    def resolver(self): ...
    def check_event(self, *choices) -> bool: ...
    def peek_event(self): ...
    last_event: Incomplete
    def get_event(self): ...
    def parse_stream_start(self): ...
    def parse_implicit_document_start(self): ...
    def parse_document_start(self): ...
    def parse_document_end(self): ...
    def parse_document_content(self): ...
    def process_directives(self): ...
    def parse_block_node(self): ...
    def parse_flow_node(self): ...
    def parse_block_node_or_indentless_sequence(self): ...
    def select_tag_transform(self, tag: Tag) -> None: ...
    def parse_node(self, block: bool = False, indentless_sequence: bool = False): ...
    def parse_block_sequence_first_entry(self): ...
    def parse_block_sequence_entry(self): ...
    def parse_indentless_sequence_entry(self): ...
    def parse_block_mapping_first_key(self): ...
    def parse_block_mapping_key(self): ...
    def parse_block_mapping_value(self): ...
    def parse_flow_sequence_first_entry(self): ...
    def parse_flow_sequence_entry(self, first: bool = False): ...
    def parse_flow_sequence_entry_mapping_key(self): ...
    def parse_flow_sequence_entry_mapping_value(self): ...
    def parse_flow_sequence_entry_mapping_end(self): ...
    def parse_flow_mapping_first_key(self): ...
    def parse_flow_mapping_key(self, first: bool = False): ...
    def parse_flow_mapping_value(self): ...
    def parse_flow_mapping_empty_value(self): ...
    def process_empty_scalar(self, mark, comment: Incomplete | None = None): ...
    def move_token_comment(self, token, nt: Incomplete = None, empty: bool | None = False): ...

class RoundTripParser(Parser):
    def select_tag_transform(self, tag: Tag) -> None: ...
    def move_token_comment(self, token, nt: Incomplete = None, empty: bool | None = False): ...

class RoundTripParserSC(RoundTripParser):
    def move_token_comment(self, token, nt: Incomplete | None = None, empty: bool | None = False) -> None: ...
    def distribute_comment(self, comment, line): ...
