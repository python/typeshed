from _typeshed import Incomplete
from collections.abc import Generator

__all__ = ["write_gexf", "read_gexf", "relabel_gexf_graph", "generate_gexf"]

def write_gexf(G, path, encoding: str = "utf-8", prettyprint: bool = True, version: str = "1.2draft") -> None: ...
def generate_gexf(
    G, encoding: str = "utf-8", prettyprint: bool = True, version: str = "1.2draft"
) -> Generator[Incomplete, Incomplete, None]: ...
def read_gexf(path, node_type: Incomplete | None = None, relabel: bool = False, version: str = "1.2draft"): ...

class GEXF:
    versions: Incomplete
    xml_type: Incomplete
    python_type: Incomplete
    def construct_types(self) -> None: ...
    convert_bool: Incomplete
    NS_GEXF: Incomplete
    NS_VIZ: Incomplete
    NS_XSI: Incomplete
    SCHEMALOCATION: Incomplete
    VERSION: Incomplete
    version: Incomplete
    def set_version(self, version) -> None: ...

class GEXFWriter(GEXF):
    prettyprint: Incomplete
    encoding: Incomplete
    xml: Incomplete
    edge_id: Incomplete
    attr_id: Incomplete
    all_edge_ids: Incomplete
    attr: Incomplete
    def __init__(
        self, graph: Incomplete | None = None, encoding: str = "utf-8", prettyprint: bool = True, version: str = "1.2draft"
    ) -> None: ...
    graph_element: Incomplete
    def add_graph(self, G) -> None: ...
    def add_nodes(self, G, graph_element) -> None: ...
    def add_edges(self, G, graph_element) -> None: ...
    def add_attributes(self, node_or_edge, xml_obj, data, default): ...
    def get_attr_id(self, title, attr_type, edge_or_node, default, mode): ...
    def add_viz(self, element, node_data): ...
    def add_parents(self, node_element, node_data): ...
    def add_slices(self, node_or_edge_element, node_or_edge_data): ...
    def add_spells(self, node_or_edge_element, node_or_edge_data): ...
    def alter_graph_mode_timeformat(self, start_or_end) -> None: ...
    def write(self, fh) -> None: ...
    def indent(self, elem, level: int = 0) -> None: ...

class GEXFReader(GEXF):
    node_type: Incomplete
    simple_graph: bool
    def __init__(self, node_type: Incomplete | None = None, version: str = "1.2draft") -> None: ...
    xml: Incomplete
    def __call__(self, stream): ...
    timeformat: Incomplete
    def make_graph(self, graph_xml): ...
    def add_node(self, G, node_xml, node_attr, node_pid: Incomplete | None = None) -> None: ...
    def add_start_end(self, data, xml): ...
    def add_viz(self, data, node_xml): ...
    def add_parents(self, data, node_xml): ...
    def add_slices(self, data, node_or_edge_xml): ...
    def add_spells(self, data, node_or_edge_xml): ...
    def add_edge(self, G, edge_element, edge_attr) -> None: ...
    def decode_attr_elements(self, gexf_keys, obj_xml): ...
    def find_gexf_attributes(self, attributes_element): ...

def relabel_gexf_graph(G): ...
