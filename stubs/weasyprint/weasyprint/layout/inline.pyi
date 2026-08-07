from _typeshed import Incomplete
from collections.abc import Generator

from .min_max import handle_min_max_width

def iter_line_boxes(
    context,
    box,
    position_y,
    bottom_space,
    skip_stack,
    containing_block,
    absolute_boxes,
    fixed_boxes,
    first_letter_style,
    first_line_style,
) -> Generator[Incomplete]: ...
def get_next_linebox(
    context,
    linebox,
    position_y,
    bottom_space,
    skip_stack,
    containing_block,
    absolute_boxes,
    fixed_boxes,
    first_letter_style,
    first_line_style,
): ...
def skip_first_whitespace(box, skip_stack): ...
def remove_last_whitespace(context, line) -> None: ...
def first_letter_to_box(box, skip_stack, first_letter_style): ...
def atomic_box(context, box, position_x, skip_stack, containing_block, absolute_boxes, fixed_boxes): ...
def inline_block_box_layout(context, box, position_x, skip_stack, containing_block, absolute_boxes, fixed_boxes): ...
def inline_block_baseline(box): ...
@handle_min_max_width
def inline_block_width(box, context, containing_block) -> None: ...
def split_inline_level(
    context,
    box,
    position_x,
    max_x,
    bottom_space,
    skip_stack,
    containing_block,
    absolute_boxes,
    fixed_boxes,
    line_placeholders,
    waiting_floats,
    line_children,
    first_letter_style,
    first_line_style,
): ...
def split_inline_box(
    context,
    box,
    position_x,
    max_x,
    bottom_space,
    skip_stack,
    containing_block,
    absolute_boxes,
    fixed_boxes,
    line_placeholders,
    waiting_floats,
    line_children,
    first_letter_style,
    first_line_style,
): ...
def split_text_box(context, box, available_width, skip, is_line_start: bool = True): ...
def line_box_verticality(box): ...
def translate_subtree(box, dy) -> None: ...
def aligned_subtree_verticality(box, top_bottom_subtrees, baseline_y): ...
def inline_box_verticality(box, top_bottom_subtrees, baseline_y): ...
def text_align(context, line, available_width, last): ...
def justify_line(context, line, extra_width) -> None: ...
def count_expandable_spaces(box): ...
def add_word_spacing(context, box, justification_spacing, x_advance): ...
def is_phantom_linebox(linebox): ...
def can_break_inside(box): ...
