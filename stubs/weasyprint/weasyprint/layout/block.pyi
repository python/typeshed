from .min_max import handle_min_max_width

def block_level_layout(
    context,
    box,
    bottom_space,
    skip_stack,
    containing_block,
    page_is_empty: bool = True,
    absolute_boxes=None,
    fixed_boxes=None,
    adjoining_margins=None,
    first_letter_style=None,
    first_line_style=None,
    discard: bool = False,
    max_lines=None,
): ...
def block_level_layout_switch(
    context,
    box,
    bottom_space,
    skip_stack,
    containing_block,
    page_is_empty,
    absolute_boxes,
    fixed_boxes,
    adjoining_margins,
    first_letter_style,
    first_line_style,
    discard,
    max_lines,
): ...
def block_box_layout(
    context,
    box,
    bottom_space,
    skip_stack,
    containing_block,
    page_is_empty,
    absolute_boxes,
    fixed_boxes,
    adjoining_margins,
    first_letter_style,
    first_line_style,
    discard,
    max_lines,
): ...
@handle_min_max_width
def block_level_width(box, containing_block) -> None: ...
def relative_positioning(box, containing_block) -> None: ...
def block_container_layout(
    context,
    box,
    bottom_space,
    skip_stack,
    page_is_empty,
    absolute_boxes,
    fixed_boxes,
    adjoining_margins,
    first_letter_style,
    first_line_style,
    discard,
    max_lines,
): ...
def collapse_margin(adjoining_margins): ...
def block_level_page_break(sibling_before, sibling_after): ...
def block_level_page_name(sibling_before, sibling_after): ...
def find_earlier_page_break(context, children, absolute_boxes, fixed_boxes): ...
def find_last_in_flow_child(children): ...
def reversed_enumerate(seq): ...
def remove_placeholders(context, box_list, absolute_boxes, fixed_boxes) -> None: ...
def avoid_page_break(page_break, context): ...
def force_page_break(page_break, context): ...
