from _typeshed import Incomplete

class StackingContext:
    box: Incomplete
    page: Incomplete
    block_level_boxes: Incomplete
    float_contexts: Incomplete
    negative_z_contexts: Incomplete
    zero_z_contexts: Incomplete
    positive_z_contexts: Incomplete
    blocks_and_cells: Incomplete
    z_index: Incomplete
    def __init__(self, box, child_contexts, blocks, floats, blocks_and_cells, page) -> None: ...
    @classmethod
    def from_page(cls, page): ...
    @classmethod
    def from_box(cls, box, page, child_contexts=None): ...
