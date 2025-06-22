from collections.abc import Buffer, Callable, Iterable, Iterator, Mapping
from contextlib import contextmanager
from types import TracebackType
from typing import Any, Final, NamedTuple, NewType, cast, type_check_only

from typing_extensions import Self

@type_check_only
class _IntFlag(int):
    def __or__(self, other: object) -> Self: ...
    def __and__(self, other: object) -> Self: ...
    def __xor__(self, other: object) -> Self: ...
    def __invert__(self) -> Self: ...

Condition = NewType("Condition", int)
NONE: Final[Condition]
ALWAYS: Final[Condition]
ONCE: Final[Condition]
FIRST_USE_EVER: Final[Condition]
APPEARING: Final[Condition]

StyleVar = NewType("StyleVar", int)
STYLE_ALPHA: Final[StyleVar]
STYLE_WINDOW_PADDING: Final[StyleVar]
STYLE_WINDOW_ROUNDING: Final[StyleVar]
STYLE_WINDOW_BORDERSIZE: Final[StyleVar]
STYLE_WINDOW_MIN_SIZE: Final[StyleVar]
STYLE_WINDOW_TITLE_ALIGN: Final[StyleVar]
STYLE_CHILD_ROUNDING: Final[StyleVar]
STYLE_CHILD_BORDERSIZE: Final[StyleVar]
STYLE_POPUP_ROUNDING: Final[StyleVar]
STYLE_POPUP_BORDERSIZE: Final[StyleVar]
STYLE_FRAME_PADDING: Final[StyleVar]
STYLE_FRAME_ROUNDING: Final[StyleVar]
STYLE_FRAME_BORDERSIZE: Final[StyleVar]
STYLE_ITEM_SPACING: Final[StyleVar]
STYLE_ITEM_INNER_SPACING: Final[StyleVar]
STYLE_INDENT_SPACING: Final[StyleVar]
STYLE_CELL_PADDING: Final[StyleVar]
STYLE_SCROLLBAR_SIZE: Final[StyleVar]
STYLE_SCROLLBAR_ROUNDING: Final[StyleVar]
STYLE_GRAB_MIN_SIZE: Final[StyleVar]
STYLE_GRAB_ROUNDING: Final[StyleVar]
STYLE_TAB_ROUNDING: Final[StyleVar]
STYLE_BUTTON_TEXT_ALIGN: Final[StyleVar]
STYLE_SELECTABLE_TEXT_ALIGN: Final[StyleVar]

ButtonFlags = NewType("ButtonFlags", _IntFlag)
BUTTON_NONE: Final[ButtonFlags]
BUTTON_MOUSE_BUTTON_LEFT: Final[ButtonFlags]
BUTTON_MOUSE_BUTTON_RIGHT: Final[ButtonFlags]
BUTTON_MOUSE_BUTTON_MIDDLE: Final[ButtonFlags]

Key = NewType("Key", int)
KEY_TAB: Final[Key]
KEY_LEFT_ARROW: Final[Key]
KEY_RIGHT_ARROW: Final[Key]
KEY_UP_ARROW: Final[Key]
KEY_DOWN_ARROW: Final[Key]
KEY_PAGE_UP: Final[Key]
KEY_PAGE_DOWN: Final[Key]
KEY_HOME: Final[Key]
KEY_END: Final[Key]
KEY_INSERT: Final[Key]
KEY_DELETE: Final[Key]
KEY_BACKSPACE: Final[Key]
KEY_SPACE: Final[Key]
KEY_ENTER: Final[Key]
KEY_ESCAPE: Final[Key]
KEY_PAD_ENTER: Final[Key]
KEY_A: Final[Key]
KEY_C: Final[Key]
KEY_V: Final[Key]
KEY_X: Final[Key]
KEY_Y: Final[Key]
KEY_Z: Final[Key]

KEY_MOD_NONE: Final[int]
KEY_MOD_CTRL: Final[int]
KEY_MOD_SHIFT: Final[int]
KEY_MOD_ALT: Final[int]
KEY_MOD_SUPER: Final[int]

NAV_INPUT_ACTIVATE: Final[int]
NAV_INPUT_CANCEL: Final[int]
NAV_INPUT_INPUT: Final[int]
NAV_INPUT_MENU: Final[int]
NAV_INPUT_DPAD_LEFT: Final[int]
NAV_INPUT_DPAD_RIGHT: Final[int]
NAV_INPUT_DPAD_UP: Final[int]
NAV_INPUT_DPAD_DOWN: Final[int]
NAV_INPUT_L_STICK_LEFT: Final[int]
NAV_INPUT_L_STICK_RIGHT: Final[int]
NAV_INPUT_L_STICK_UP: Final[int]
NAV_INPUT_L_STICK_DOWN: Final[int]
NAV_INPUT_FOCUS_PREV: Final[int]
NAV_INPUT_FOCUS_NEXT: Final[int]
NAV_INPUT_TWEAK_SLOW: Final[int]
NAV_INPUT_TWEAK_FAST: Final[int]
NAV_INPUT_COUNT: Final[int]

WindowFlags = NewType("WindowFlags", _IntFlag)
WINDOW_NONE: Final[WindowFlags]
WINDOW_NO_TITLE_BAR: Final[WindowFlags]
WINDOW_NO_RESIZE: Final[WindowFlags]
WINDOW_NO_MOVE: Final[WindowFlags]
WINDOW_NO_SCROLLBAR: Final[WindowFlags]
WINDOW_NO_SCROLL_WITH_MOUSE: Final[WindowFlags]
WINDOW_NO_COLLAPSE: Final[WindowFlags]
WINDOW_ALWAYS_AUTO_RESIZE: Final[WindowFlags]
WINDOW_NO_BACKGROUND: Final[WindowFlags]
WINDOW_NO_SAVED_SETTINGS: Final[WindowFlags]
WINDOW_NO_MOUSE_INPUTS: Final[WindowFlags]
WINDOW_MENU_BAR: Final[WindowFlags]
WINDOW_HORIZONTAL_SCROLLING_BAR: Final[WindowFlags]
WINDOW_NO_FOCUS_ON_APPEARING: Final[WindowFlags]
WINDOW_NO_BRING_TO_FRONT_ON_FOCUS: Final[WindowFlags]
WINDOW_ALWAYS_VERTICAL_SCROLLBAR: Final[WindowFlags]
WINDOW_ALWAYS_HORIZONTAL_SCROLLBAR: Final[WindowFlags]
WINDOW_ALWAYS_USE_WINDOW_PADDING: Final[WindowFlags]
WINDOW_NO_NAV_INPUTS: Final[WindowFlags]
WINDOW_NO_NAV_FOCUS: Final[WindowFlags]
WINDOW_UNSAVED_DOCUMENT: Final[WindowFlags]
WINDOW_NO_NAV: Final[WindowFlags]
WINDOW_NO_DECORATION: Final[WindowFlags]
WINDOW_NO_INPUTS: Final[WindowFlags]

ColorEditFlags = NewType("ColorEditFlags", _IntFlag)
COLOR_EDIT_NONE: Final[ColorEditFlags]
COLOR_EDIT_NO_ALPHA: Final[ColorEditFlags]
COLOR_EDIT_NO_PICKER: Final[ColorEditFlags]
COLOR_EDIT_NO_OPTIONS: Final[ColorEditFlags]
COLOR_EDIT_NO_SMALL_PREVIEW: Final[ColorEditFlags]
COLOR_EDIT_NO_INPUTS: Final[ColorEditFlags]
COLOR_EDIT_NO_TOOLTIP: Final[ColorEditFlags]
COLOR_EDIT_NO_LABEL: Final[ColorEditFlags]
COLOR_EDIT_NO_SIDE_PREVIEW: Final[ColorEditFlags]
COLOR_EDIT_NO_DRAG_DROP: Final[ColorEditFlags]
COLOR_EDIT_NO_BORDER: Final[ColorEditFlags]
COLOR_EDIT_ALPHA_BAR: Final[ColorEditFlags]
COLOR_EDIT_ALPHA_PREVIEW: Final[ColorEditFlags]
COLOR_EDIT_ALPHA_PREVIEW_HALF: Final[ColorEditFlags]
COLOR_EDIT_HDR: Final[ColorEditFlags]
COLOR_EDIT_DISPLAY_RGB: Final[ColorEditFlags]
COLOR_EDIT_DISPLAY_HSV: Final[ColorEditFlags]
COLOR_EDIT_DISPLAY_HEX: Final[ColorEditFlags]
COLOR_EDIT_UINT8: Final[ColorEditFlags]
COLOR_EDIT_FLOAT: Final[ColorEditFlags]
COLOR_EDIT_PICKER_HUE_BAR: Final[ColorEditFlags]
COLOR_EDIT_PICKER_HUE_WHEEL: Final[ColorEditFlags]
COLOR_EDIT_INPUT_RGB: Final[ColorEditFlags]
COLOR_EDIT_INPUT_HSV: Final[ColorEditFlags]
COLOR_EDIT_DEFAULT_OPTIONS: Final[ColorEditFlags]

TreeNodeFlags = NewType("TreeNodeFlags", _IntFlag)
TREE_NODE_NONE: Final[TreeNodeFlags]
TREE_NODE_SELECTED: Final[TreeNodeFlags]
TREE_NODE_FRAMED: Final[TreeNodeFlags]
TREE_NODE_ALLOW_ITEM_OVERLAP: Final[TreeNodeFlags]
TREE_NODE_NO_TREE_PUSH_ON_OPEN: Final[TreeNodeFlags]
TREE_NODE_NO_AUTO_OPEN_ON_LOG: Final[TreeNodeFlags]
TREE_NODE_DEFAULT_OPEN: Final[TreeNodeFlags]
TREE_NODE_OPEN_ON_DOUBLE_CLICK: Final[TreeNodeFlags]
TREE_NODE_OPEN_ON_ARROW: Final[TreeNodeFlags]
TREE_NODE_LEAF: Final[TreeNodeFlags]
TREE_NODE_BULLET: Final[TreeNodeFlags]
TREE_NODE_FRAME_PADDING: Final[TreeNodeFlags]
TREE_NODE_SPAN_AVAILABLE_WIDTH: Final[TreeNodeFlags]
TREE_NODE_SPAN_FULL_WIDTH: Final[TreeNodeFlags]
TREE_NODE_NAV_LEFT_JUPS_BACK_HERE: Final[TreeNodeFlags]
TREE_NODE_COLLAPSING_HEADER: Final[TreeNodeFlags]

PopupFlags = NewType("PopupFlags", _IntFlag)
POPUP_NONE: Final[PopupFlags]
POPUP_MOUSE_BUTTON_LEFT: Final[PopupFlags]
POPUP_MOUSE_BUTTON_RIGHT: Final[PopupFlags]
POPUP_MOUSE_BUTTON_MIDDLE: Final[PopupFlags]
POPUP_MOUSE_BUTTON_MASK: Final[PopupFlags]
POPUP_MOUSE_BUTTON_DEFAULT: Final[PopupFlags]
POPUP_NO_OPEN_OVER_EXISTING_POPUP: Final[PopupFlags]
POPUP_NO_OPEN_OVER_ITEMS: Final[PopupFlags]
POPUP_ANY_POPUP_ID: Final[PopupFlags]
POPUP_ANY_POPUP_LEVEL: Final[PopupFlags]
POPUP_ANY_POPUP: Final[PopupFlags]

SelectableFlags = NewType("SelectableFlags", _IntFlag)
SELECTABLE_NONE: Final[SelectableFlags]
SELECTABLE_DONT_CLOSE_POPUPS: Final[SelectableFlags]
SELECTABLE_SPAN_ALL_COLUMNS: Final[SelectableFlags]
SELECTABLE_ALLOW_DOUBLE_CLICK: Final[SelectableFlags]
SELECTABLE_DISABLED: Final[SelectableFlags]
SELECTABLE_ALLOW_ITEM_OVERLAP: Final[SelectableFlags]

ComboFlags = NewType("ComboFlags", _IntFlag)
COMBO_NONE: Final[ComboFlags]
COMBO_POPUP_ALIGN_LEFT: Final[ComboFlags]
COMBO_HEIGHT_SMALL: Final[ComboFlags]
COMBO_HEIGHT_REGULAR: Final[ComboFlags]
COMBO_HEIGHT_LARGE: Final[ComboFlags]
COMBO_HEIGHT_LARGEST: Final[ComboFlags]
COMBO_NO_ARROW_BUTTON: Final[ComboFlags]
COMBO_NO_PREVIEW: Final[ComboFlags]
COMBO_HEIGHT_MASK: Final[ComboFlags]

TabBarFlags = NewType("TabBarFlags", _IntFlag)
TAB_BAR_NONE: Final[TabBarFlags]
TAB_BAR_REORDERABLE: Final[TabBarFlags]
TAB_BAR_AUTO_SELECT_NEW_TABS: Final[TabBarFlags]
TAB_BAR_TAB_LIST_POPUP_BUTTON: Final[TabBarFlags]
TAB_BAR_NO_CLOSE_WITH_MIDDLE_MOUSE_BUTTON: Final[TabBarFlags]
TAB_BAR_NO_TAB_LIST_SCROLLING_BUTTONS: Final[TabBarFlags]
TAB_BAR_NO_TOOLTIP: Final[TabBarFlags]
TAB_BAR_FITTING_POLICY_RESIZE_DOWN: Final[TabBarFlags]
TAB_BAR_FITTING_POLICY_SCROLL: Final[TabBarFlags]
TAB_BAR_FITTING_POLICY_MASK: Final[TabBarFlags]
TAB_BAR_FITTING_POLICY_DEFAULT: Final[TabBarFlags]

TabItemFlags = NewType("TabItemFlags", _IntFlag)
TAB_ITEM_NONE: Final[TabItemFlags]
TAB_ITEM_UNSAVED_DOCUMENT: Final[TabItemFlags]
TAB_ITEM_SET_SELECTED: Final[TabItemFlags]
TAB_ITEM_NO_CLOSE_WITH_MIDDLE_MOUSE_BUTTON: Final[TabItemFlags]
TAB_ITEM_NO_PUSH_ID: Final[TabItemFlags]
TAB_ITEM_NO_TOOLTIP: Final[TabItemFlags]
TAB_ITEM_NO_REORDER: Final[TabItemFlags]
TAB_ITEM_LEADING: Final[TabItemFlags]
TAB_ITEM_TRAILING: Final[TabItemFlags]

TableFlags = NewType("TableFlags", _IntFlag)
TABLE_NONE: Final[TableFlags]
TABLE_RESIZABLE: Final[TableFlags]
TABLE_REORDERABLE: Final[TableFlags]
TABLE_HIDEABLE: Final[TableFlags]
TABLE_SORTABLE: Final[TableFlags]
TABLE_NO_SAVED_SETTINGS: Final[TableFlags]
TABLE_CONTEXT_MENU_IN_BODY: Final[TableFlags]
TABLE_ROW_BACKGROUND: Final[TableFlags]
TABLE_BORDERS_INNER_HORIZONTAL: Final[TableFlags]
TABLE_BORDERS_OUTER_HORIZONTAL: Final[TableFlags]
TABLE_BORDERS_INNER_VERTICAL: Final[TableFlags]
TABLE_BORDERS_OUTER_VERTICAL: Final[TableFlags]
TABLE_BORDERS_HORIZONTAL: Final[TableFlags]
TABLE_BORDERS_VERTICAL: Final[TableFlags]
TABLE_BORDERS_INNER: Final[TableFlags]
TABLE_BORDERS_OUTER: Final[TableFlags]
TABLE_BORDERS: Final[TableFlags]
TABLE_NO_BORDERS_IN_BODY: Final[TableFlags]
TABLE_NO_BORDERS_IN_BODY_UTIL_RESIZE: Final[TableFlags]
TABLE_SIZING_FIXED_FIT: Final[TableFlags]
TABLE_SIZING_FIXED_SAME: Final[TableFlags]
TABLE_SIZING_STRETCH_PROP: Final[TableFlags]
TABLE_SIZING_STRETCH_SAME: Final[TableFlags]
TABLE_NO_HOST_EXTEND_X: Final[TableFlags]
TABLE_NO_HOST_EXTEND_Y: Final[TableFlags]
TABLE_NO_KEEP_COLUMNS_VISIBLE: Final[TableFlags]
TABLE_PRECISE_WIDTHS: Final[TableFlags]
TABLE_NO_CLIP: Final[TableFlags]
TABLE_PAD_OUTER_X: Final[TableFlags]
TABLE_NO_PAD_OUTER_X: Final[TableFlags]
TABLE_NO_PAD_INNER_X: Final[TableFlags]
TABLE_SCROLL_X: Final[TableFlags]
TABLE_SCROLL_Y: Final[TableFlags]
TABLE_SORT_MULTI: Final[TableFlags]
TABLE_SORT_TRISTATE: Final[TableFlags]

TableColumnFlags = NewType("TableColumnFlags", _IntFlag)
TABLE_COLUMN_NONE: Final[TableColumnFlags]
TABLE_COLUMN_DEFAULT_HIDE: Final[TableColumnFlags]
TABLE_COLUMN_DEFAULT_SORT: Final[TableColumnFlags]
TABLE_COLUMN_WIDTH_STRETCH: Final[TableColumnFlags]
TABLE_COLUMN_WIDTH_FIXED: Final[TableColumnFlags]
TABLE_COLUMN_NO_RESIZE: Final[TableColumnFlags]
TABLE_COLUMN_NO_REORDER: Final[TableColumnFlags]
TABLE_COLUMN_NO_HIDE: Final[TableColumnFlags]
TABLE_COLUMN_NO_CLIP: Final[TableColumnFlags]
TABLE_COLUMN_NO_SORT: Final[TableColumnFlags]
TABLE_COLUMN_NO_SORT_ASCENDING: Final[TableColumnFlags]
TABLE_COLUMN_NO_SORT_DESCENDING: Final[TableColumnFlags]
TABLE_COLUMN_NO_HEADER_WIDTH: Final[TableColumnFlags]
TABLE_COLUMN_PREFER_SORT_ASCENDING: Final[TableColumnFlags]
TABLE_COLUMN_PREFER_SORT_DESCENDING: Final[TableColumnFlags]
TABLE_COLUMN_INDENT_ENABLE: Final[TableColumnFlags]
TABLE_COLUMN_INDENT_DISABLE: Final[TableColumnFlags]
TABLE_COLUMN_IS_ENABLED: Final[TableColumnFlags]
TABLE_COLUMN_IS_VISIBLE: Final[TableColumnFlags]
TABLE_COLUMN_IS_SORTED: Final[TableColumnFlags]
TABLE_COLUMN_IS_HOVERED: Final[TableColumnFlags]

TableRowFlags = NewType("TableRowFlags", _IntFlag)
TABLE_ROW_NONE: Final[TableRowFlags]
TABLE_ROW_HEADERS: Final[TableRowFlags]

TableBackgroundTarget = NewType("TableBackgroundTarget", int)
TABLE_BACKGROUND_TARGET_NONE: Final[TableBackgroundTarget]
TABLE_BACKGROUND_TARGET_ROW_BG0: Final[TableBackgroundTarget]
TABLE_BACKGROUND_TARGET_ROW_BG1: Final[TableBackgroundTarget]
TABLE_BACKGROUND_TARGET_CELL_BG: Final[TableBackgroundTarget]

FocusFlags = NewType("FocusFlags", _IntFlag)
FOCUS_NONE: Final[FocusFlags]
FOCUS_CHILD_WINDOWS: Final[FocusFlags]
FOCUS_ROOT_WINDOW: Final[FocusFlags]
FOCUS_ANY_WINDOW: Final[FocusFlags]
FOCUS_ROOT_AND_CHILD_WINDOWS: Final[FocusFlags]

HoverFlags = NewType("HoverFlags", _IntFlag)
HOVERED_NONE: Final[HoverFlags]
HOVERED_CHILD_WINDOWS: Final[HoverFlags]
HOVERED_ROOT_WINDOW: Final[HoverFlags]
HOVERED_ANY_WINDOW: Final[HoverFlags]
HOVERED_ALLOW_WHEN_BLOCKED_BY_POPUP: Final[HoverFlags]
HOVERED_ALLOW_WHEN_BLOCKED_BY_ACTIVE_ITEM: Final[HoverFlags]
HOVERED_ALLOW_WHEN_OVERLAPPED: Final[HoverFlags]
HOVERED_ALLOW_WHEN_DISABLED: Final[HoverFlags]
HOVERED_RECT_ONLY: Final[HoverFlags]
HOVERED_ROOT_AND_CHILD_WINDOWS: Final[HoverFlags]

DragDropFlags = NewType("DragDropFlags", _IntFlag)
DRAG_DROP_NONE: Final[DragDropFlags]
DRAG_DROP_SOURCE_NO_PREVIEW_TOOLTIP: Final[DragDropFlags]
DRAG_DROP_SOURCE_NO_DISABLE_HOVER: Final[DragDropFlags]
DRAG_DROP_SOURCE_NO_HOLD_TO_OPEN_OTHERS: Final[DragDropFlags]
DRAG_DROP_SOURCE_ALLOW_NULL_ID: Final[DragDropFlags]
DRAG_DROP_SOURCE_EXTERN: Final[DragDropFlags]
DRAG_DROP_SOURCE_AUTO_EXPIRE_PAYLOAD: Final[DragDropFlags]

DragDropAcceptFlags = NewType("DragDropAcceptFlags", _IntFlag)
DRAG_DROP_ACCEPT_BEFORE_DELIVERY: Final[DragDropAcceptFlags]
DRAG_DROP_ACCEPT_NO_DRAW_DEFAULT_RECT: Final[DragDropAcceptFlags]
DRAG_DROP_ACCEPT_NO_PREVIEW_TOOLTIP: Final[DragDropAcceptFlags]
DRAG_DROP_ACCEPT_PEEK_ONLY: Final[DragDropAcceptFlags]

Direction = NewType("Direction", int)
DIRECTION_NONE: Final[Direction]
DIRECTION_LEFT: Final[Direction]
DIRECTION_RIGHT: Final[Direction]
DIRECTION_UP: Final[Direction]
DIRECTION_DOWN: Final[Direction]

SortDirection = NewType("SortDirection", int)
SORT_DIRECTION_NONE: Final[SortDirection]
SORT_DIRECTION_ASCENDING: Final[SortDirection]
SORT_DIRECTION_DESCENDING: Final[SortDirection]

MouseCursor = NewType("MouseCursor", int)
MOUSE_CURSOR_NONE: Final[MouseCursor]
MOUSE_CURSOR_ARROW: Final[MouseCursor]
MOUSE_CURSOR_TEXT_INPUT: Final[MouseCursor]
MOUSE_CURSOR_RESIZE_ALL: Final[MouseCursor]
MOUSE_CURSOR_RESIZE_NS: Final[MouseCursor]
MOUSE_CURSOR_RESIZE_EW: Final[MouseCursor]
MOUSE_CURSOR_RESIZE_NESW: Final[MouseCursor]
MOUSE_CURSOR_RESIZE_NWSE: Final[MouseCursor]
MOUSE_CURSOR_HAND: Final[MouseCursor]
MOUSE_CURSOR_NOT_ALLOWED: Final[MouseCursor]

Color = NewType("Color", int)
COLOR_TEXT: Final[Color]
COLOR_TEXT_DISABLED: Final[Color]
COLOR_WINDOW_BACKGROUND: Final[Color]
COLOR_CHILD_BACKGROUND: Final[Color]
COLOR_POPUP_BACKGROUND: Final[Color]
COLOR_BORDER: Final[Color]
COLOR_BORDER_SHADOW: Final[Color]
COLOR_FRAME_BACKGROUND: Final[Color]
COLOR_FRAME_BACKGROUND_HOVERED: Final[Color]
COLOR_FRAME_BACKGROUND_ACTIVE: Final[Color]
COLOR_TITLE_BACKGROUND: Final[Color]
COLOR_TITLE_BACKGROUND_ACTIVE: Final[Color]
COLOR_TITLE_BACKGROUND_COLLAPSED: Final[Color]
COLOR_MENUBAR_BACKGROUND: Final[Color]
COLOR_SCROLLBAR_BACKGROUND: Final[Color]
COLOR_SCROLLBAR_GRAB: Final[Color]
COLOR_SCROLLBAR_GRAB_HOVERED: Final[Color]
COLOR_SCROLLBAR_GRAB_ACTIVE: Final[Color]
COLOR_CHECK_MARK: Final[Color]
COLOR_SLIDER_GRAB: Final[Color]
COLOR_SLIDER_GRAB_ACTIVE: Final[Color]
COLOR_BUTTON: Final[Color]
COLOR_BUTTON_HOVERED: Final[Color]
COLOR_BUTTON_ACTIVE: Final[Color]
COLOR_HEADER: Final[Color]
COLOR_HEADER_HOVERED: Final[Color]
COLOR_HEADER_ACTIVE: Final[Color]
COLOR_SEPARATOR: Final[Color]
COLOR_SEPARATOR_HOVERED: Final[Color]
COLOR_SEPARATOR_ACTIVE: Final[Color]
COLOR_RESIZE_GRIP: Final[Color]
COLOR_RESIZE_GRIP_HOVERED: Final[Color]
COLOR_RESIZE_GRIP_ACTIVE: Final[Color]
COLOR_TAB: Final[Color]
COLOR_TAB_HOVERED: Final[Color]
COLOR_TAB_ACTIVE: Final[Color]
COLOR_TAB_UNFOCUSED: Final[Color]
COLOR_TAB_UNFOCUSED_ACTIVE: Final[Color]
COLOR_PLOT_LINES: Final[Color]
COLOR_PLOT_LINES_HOVERED: Final[Color]
COLOR_PLOT_HISTOGRAM: Final[Color]
COLOR_PLOT_HISTOGRAM_HOVERED: Final[Color]
COLOR_TABLE_HEADER_BACKGROUND: Final[Color]
COLOR_TABLE_BORDER_STRONG: Final[Color]
COLOR_TABLE_BORDER_LIGHT: Final[Color]
COLOR_TABLE_ROW_BACKGROUND: Final[Color]
COLOR_TABLE_ROW_BACKGROUND_ALT: Final[Color]
COLOR_TEXT_SELECTED_BACKGROUND: Final[Color]
COLOR_DRAG_DROP_TARGET: Final[Color]
COLOR_NAV_HIGHLIGHT: Final[Color]
COLOR_NAV_WINDOWING_HIGHLIGHT: Final[Color]
COLOR_NAV_WINDOWING_DIM_BACKGROUND: Final[Color]
COLOR_MODAL_WINDOW_DIM_BACKGROUND: Final[Color]
COLOR_COUNT: Final[Color]

DataType = NewType("DataType", int)
DATA_TYPE_S8: Final[DataType]
DATA_TYPE_U8: Final[DataType]
DATA_TYPE_S16: Final[DataType]
DATA_TYPE_U16: Final[DataType]
DATA_TYPE_S32: Final[DataType]
DATA_TYPE_U32: Final[DataType]
DATA_TYPE_S64: Final[DataType]
DATA_TYPE_U64: Final[DataType]
DATA_TYPE_FLOAT: Final[DataType]
DATA_TYPE_DOUBLE: Final[DataType]

TextInputFlags = NewType("TextInputFlags", _IntFlag)
INPUT_TEXT_NONE: Final[TextInputFlags]
INPUT_TEXT_CHARS_DECIMAL: Final[TextInputFlags]
INPUT_TEXT_CHARS_HEXADECIMAL: Final[TextInputFlags]
INPUT_TEXT_CHARS_UPPERCASE: Final[TextInputFlags]
INPUT_TEXT_CHARS_NO_BLANK: Final[TextInputFlags]
INPUT_TEXT_AUTO_SELECT_ALL: Final[TextInputFlags]
INPUT_TEXT_ENTER_RETURNS_TRUE: Final[TextInputFlags]
INPUT_TEXT_CALLBACK_COMPLETION: Final[TextInputFlags]
INPUT_TEXT_CALLBACK_HISTORY: Final[TextInputFlags]
INPUT_TEXT_CALLBACK_ALWAYS: Final[TextInputFlags]
INPUT_TEXT_CALLBACK_CHAR_FILTER: Final[TextInputFlags]
INPUT_TEXT_ALLOW_TAB_INPUT: Final[TextInputFlags]
INPUT_TEXT_CTRL_ENTER_FOR_NEW_LINE: Final[TextInputFlags]
INPUT_TEXT_NO_HORIZONTAL_SCROLL: Final[TextInputFlags]
INPUT_TEXT_ALWAYS_OVERWRITE: Final[TextInputFlags]
INPUT_TEXT_ALWAYS_INSERT_MODE: Final[TextInputFlags]
INPUT_TEXT_READ_ONLY: Final[TextInputFlags]
INPUT_TEXT_PASSWORD: Final[TextInputFlags]
INPUT_TEXT_NO_UNDO_REDO: Final[TextInputFlags]
INPUT_TEXT_CHARS_SCIENTIFIC: Final[TextInputFlags]
INPUT_TEXT_CALLBACK_RESIZE: Final[TextInputFlags]
INPUT_TEXT_CALLBACK_EDIT: Final[TextInputFlags]

DrawCornerFlags = NewType("DrawCornerFlags", _IntFlag)
DRAW_CORNER_NONE: Final[DrawCornerFlags]
DRAW_CORNER_TOP_LEFT: Final[DrawCornerFlags]
DRAW_CORNER_TOP_RIGHT: Final[DrawCornerFlags]
DRAW_CORNER_BOTTOM_LEFT: Final[DrawCornerFlags]
DRAW_CORNER_BOTTOM_RIGHT: Final[DrawCornerFlags]
DRAW_CORNER_TOP: Final[DrawCornerFlags]
DRAW_CORNER_BOTTOM: Final[DrawCornerFlags]
DRAW_CORNER_LEFT: Final[DrawCornerFlags]
DRAW_CORNER_RIGHT: Final[DrawCornerFlags]
DRAW_CORNER_ALL: Final[DrawCornerFlags]

DrawFlags = NewType("DrawFlags", _IntFlag)
DRAW_NONE: Final[DrawFlags]
DRAW_CLOSED: Final[DrawFlags]
DRAW_ROUND_CORNERS_TOP_LEFT: Final[DrawFlags]
DRAW_ROUND_CORNERS_TOP_RIGHT: Final[DrawFlags]
DRAW_ROUND_CORNERS_BOTTOM_LEFT: Final[DrawFlags]
DRAW_ROUND_CORNERS_BOTTOM_RIGHT: Final[DrawFlags]
DRAW_ROUND_CORNERS_NONE: Final[DrawFlags]
DRAW_ROUND_CORNERS_TOP: Final[DrawFlags]
DRAW_ROUND_CORNERS_BOTTOM: Final[DrawFlags]
DRAW_ROUND_CORNERS_LEFT: Final[DrawFlags]
DRAW_ROUND_CORNERS_RIGHT: Final[DrawFlags]
DRAW_ROUND_CORNERS_ALL: Final[DrawFlags]

DrawListFlags = NewType("DrawListFlags", _IntFlag)
DRAW_LIST_NONE: Final[DrawListFlags]
DRAW_LIST_ANTI_ALIASED_LINES: Final[DrawListFlags]
DRAW_LIST_ANTI_ALIASED_LINES_USE_TEX: Final[DrawListFlags]
DRAW_LIST_ANTI_ALIASED_FILL: Final[DrawListFlags]
DRAW_LIST_ALLOW_VTX_OFFSET: Final[DrawListFlags]

FontAtlasFlags = NewType("FontAtlasFlags", _IntFlag)
FONT_ATLAS_NONE: Final[FontAtlasFlags]
FONT_ATLAS_NO_POWER_OF_TWO_HEIGHT: Final[FontAtlasFlags]
FONT_ATLAS_NO_MOUSE_CURSOR: Final[FontAtlasFlags]
FONT_ATLAS_NO_BAKED_LINES: Final[FontAtlasFlags]

ConfigFlags = NewType("ConfigFlags", _IntFlag)
CONFIG_NONE: Final[ConfigFlags]
CONFIG_NAV_ENABLE_KEYBOARD: Final[ConfigFlags]
CONFIG_NAV_ENABLE_GAMEPAD: Final[ConfigFlags]
CONFIG_NAV_ENABLE_SET_MOUSE_POS: Final[ConfigFlags]
CONFIG_NAV_NO_CAPTURE_KEYBOARD: Final[ConfigFlags]
CONFIG_NO_MOUSE: Final[ConfigFlags]
CONFIG_NO_MOUSE_CURSOR_CHANGE: Final[ConfigFlags]
CONFIG_IS_RGB: Final[ConfigFlags]
CONFIG_IS_TOUCH_SCREEN: Final[ConfigFlags]

BackendFlags = NewType("BackendFlags", _IntFlag)
BACKEND_NONE: Final[BackendFlags]
BACKEND_HAS_GAMEPAD: Final[BackendFlags]
BACKEND_HAS_MOUSE_CURSORS: Final[BackendFlags]
BACKEND_HAS_SET_MOUSE_POS: Final[BackendFlags]
BACKEND_RENDERER_HAS_VTX_OFFSET: Final[BackendFlags]

SliderFlags = NewType("SliderFlags", _IntFlag)
SLIDER_FLAGS_NONE: Final[SliderFlags]
SLIDER_FLAGS_ALWAYS_CLAMP: Final[SliderFlags]
SLIDER_FLAGS_LOGARITHMIC: Final[SliderFlags]
SLIDER_FLAGS_NO_ROUND_TO_FORMAT: Final[SliderFlags]
SLIDER_FLAGS_NO_INPUT: Final[SliderFlags]

MouseButton = NewType("MouseButton", int)
MOUSE_BUTTON_LEFT: Final[MouseButton]
MOUSE_BUTTON_RIGHT: Final[MouseButton]
MOUSE_BUTTON_MIDDLE: Final[MouseButton]

ViewportFlags = NewType("ViewportFlags", _IntFlag)
VIEWPORT_FLAGS_NONE: Final[ViewportFlags]
VIEWPORT_FLAGS_IS_PLATFORM_WINDOW: Final[ViewportFlags]
VIEWPORT_FLAGS_IS_PLATFORM_MONITOR: Final[ViewportFlags]
VIEWPORT_FLAGS_OWNED_BY_APP: Final[ViewportFlags]

class Vec2(NamedTuple):
    x: float
    y: float

class Vec4(NamedTuple):
    x: float
    y: float
    z: float
    w: float

class _ImGuiContext:
    _keepalive_cache: list[int]

    def __eq__(self, other: object) -> bool: ...

class _DrawCmd:
    @property
    def clip_rect(self) -> Vec4: ...
    @property
    def texture_id(self) -> int: ...
    @property
    def elem_count(self) -> int: ...

class _DrawList:
    flags: int

    @property
    def cmd_buffer_size(self) -> int: ...
    @property
    def cmd_buffer_data(self) -> int: ...
    @property
    def vtx_buffer_size(self) -> int: ...
    @property
    def vtx_buffer_data(self) -> int: ...
    @property
    def idx_buffer_size(self) -> int: ...
    @property
    def idx_buffer_data(self) -> int: ...
    def push_clip_rect(
        self,
        clip_rect_min_x: float,
        clip_rect_min_y: float,
        clip_rect_max_x: float,
        clip_rect_max_y: float,
        intersect_with_current_clip_rect: bool = False,
    ) -> None: ...
    def push_clip_rect_full_screen(self) -> None: ...
    def pop_clip_rect(self) -> None: ...
    def push_texture_id(self, texture_id: int) -> None: ...
    def pop_texture_id(self) -> None: ...
    def get_clip_rect_min(self) -> Vec2: ...
    def get_clip_rect_max(self) -> Vec2: ...
    def add_line(self, start_x: float, start_y: float, end_x: float, end_y: float, col: int, thickness: float = 1.0) -> None: ...
    def add_rect(
        self,
        upper_left_x: float,
        upper_left_y: float,
        lower_right_x: float,
        lower_right_y: float,
        col: int,
        rounding: float = 0.0,
        flags: int = 0,
        thickness: float = 1.0,
    ) -> None: ...
    def add_rect_filled(
        self,
        upper_left_x: float,
        upper_left_y: float,
        lower_right_x: float,
        lower_right_y: float,
        col: int,
        rounding: float = 0.0,
        flags: int = 0,
    ) -> None: ...
    def add_rect_filled_multicolor(
        self,
        upper_left_x: float,
        upper_left_y: float,
        lower_right_x: float,
        lower_right_y: float,
        col_upr_left: int,
        col_upr_right: int,
        col_bot_right: int,
        col_bot_left: int,
    ) -> None: ...
    def add_quad(
        self,
        point1_x: float,
        point1_y: float,
        point2_x: float,
        point2_y: float,
        point3_x: float,
        point3_y: float,
        point4_x: float,
        point4_y: float,
        col: int,
        thickness: float = 1.0,
    ) -> None: ...
    def add_quad_filled(
        self,
        point1_x: float,
        point1_y: float,
        point2_x: float,
        point2_y: float,
        point3_x: float,
        point3_y: float,
        point4_x: float,
        point4_y: float,
        col: int,
    ) -> None: ...
    def add_triangle(
        self,
        point1_x: float,
        point1_y: float,
        point2_x: float,
        point2_y: float,
        point3_x: float,
        point3_y: float,
        col: int,
        thickness: float = 1.0,
    ) -> None: ...
    def add_triangle_filled(
        self, point1_x: float, point1_y: float, point2_x: float, point2_y: float, point3_x: float, point3_y: float, col: int
    ) -> None: ...
    def add_bezier_cubic(
        self,
        point1_x: float,
        point1_y: float,
        point2_x: float,
        point2_y: float,
        point3_x: float,
        point3_y: float,
        point4_x: float,
        point4_y: float,
        col: int,
        thickness: float,
        num_segments: int = 0,
    ) -> None: ...
    def add_bezier_quadratic(
        self,
        point1_x: float,
        point1_y: float,
        point2_x: float,
        point2_y: float,
        point3_x: float,
        point3_y: float,
        col: int,
        thickness: float,
        num_segments: int = 0,
    ) -> None: ...
    def add_circle(
        self, centre_x: float, centre_y: float, radius: float, col: int, num_segments: int = 0, thickness: float = 1.0
    ) -> None: ...
    def add_ngon_filled(self, centre_x: float, centre_y: float, radius: float, col: int, num_segments: int) -> None: ...
    def add_text(self, pos_x: float, pos_y: float, col: int, text: str) -> None: ...
    def add_image(
        self,
        texture_id: int,
        a: tuple[int, int],
        b: tuple[int, int],
        uv_a: tuple[int, int] = (0, 0),
        uv_b: tuple[int, int] = (1, 1),
        col: int = 0xFFFFFFFF,
    ) -> None: ...
    def add_image_rounded(
        self,
        texture_id: int,
        a: tuple[int, int],
        b: tuple[int, int],
        uv_a: tuple[int, int] = (0, 0),
        uv_b: tuple[int, int] = (1, 1),
        col: int = 0xFFFFFFFF,
        rounding: float = 0.0,
        flags: int = 0,
    ) -> None: ...
    def add_polyline(self, points: list[tuple[float, float]], col: int, flags: int = 0, thickness: float = 1.0) -> None: ...
    def path_clear(self) -> None: ...
    def path_line_to(self, x: float, y: float) -> None: ...
    def path_arc_to(
        self, center_x: float, center_y: float, radius: float, a_min: float, a_max: float, num_segments: int = 0
    ) -> None: ...
    def path_arc_to_fast(
        self, center_x: float, center_y: float, radius: float, a_min_of_12: float, a_max_of_12: float
    ) -> None: ...
    def path_rect(
        self, point1_x: float, point1_y: float, point2_x: float, point2_y: float, rounding: float = 0.0, flags: int = 0
    ) -> None: ...
    def path_fill_convex(self, col: int) -> None: ...
    def path_stroke(self, col: int, flags: int = 0, thickness: float = 1.0) -> None: ...
    def channels_split(self, channels_count: int) -> None: ...
    def channels_set_current(self, idx: int) -> None: ...
    def channels_merge(self) -> None: ...
    def prim_reserve(self, idx_count: int, vtx_count: int) -> None: ...
    def prim_unreserve(self, idx_count: int, vtx_count: int) -> None: ...
    def prim_rect(self, a_x: float, a_y: float, b_x: float, b_y: float, color: int = 0xFFFFFFFF) -> None: ...
    def prim_rect_UV(
        self,
        a_x: float,
        a_y: float,
        b_x: float,
        b_y: float,
        uv_a_u: float,
        uv_a_v: float,
        uv_b_u: float,
        uv_b_v: float,
        color: int = 0xFFFFFFFF,
    ) -> None: ...
    def prim_quad_UV(
        self,
        a_x: float,
        a_y: float,
        b_x: float,
        b_y: float,
        c_x: float,
        c_y: float,
        d_x: float,
        d_y: float,
        uv_a_u: float,
        uv_a_v: float,
        uv_b_u: float,
        uv_b_v: float,
        uv_c_u: float,
        uv_c_v: float,
        uv_d_u: float,
        uv_d_v: float,
        color: int = 0xFFFFFFFF,
    ) -> None: ...
    def prim_write_vtx(self, pos_x: float, pos_y: float, u: float, v: float, color: int = 0xFFFFFFFF) -> None: ...
    def prim_write_idx(self, idx: int) -> None: ...
    def prim_vtx(self, pos_x: float, pos_y: float, u: float, v: float, color: int = 0xFFFFFFFF) -> None: ...
    @property
    def commands(self) -> list[_DrawCmd]: ...

class _Colors:
    def __init__(self, gui_style: GuiStyle) -> None: ...
    def __getitem__(self, variable: int) -> Vec4: ...
    def __setitem__(self, variable: int, value: Vec4) -> None: ...

class GuiStyle:
    alpha: float
    window_padding: Vec2
    window_min_size: Vec2
    window_rounding: float
    window_border_size: float
    child_rounding: float
    child_border_size: float
    popup_rounding: float
    popup_border_size: float
    window_title_align: Vec2
    window_menu_button_position: int
    frame_padding: Vec2
    frame_rounding: float
    frame_border_size: float
    item_spacing: Vec2
    item_inner_spacing: Vec2
    cell_padding: Vec2
    touch_extra_padding: Vec2
    indent_spacing: float
    columns_min_spacing: float
    scrollbar_size: float
    scrollbar_rounding: float
    grab_min_size: float
    grab_rounding: float
    log_slider_deadzone: float
    tab_rounding: float
    tab_border_size: float
    tab_min_width_for_close_button: float
    color_button_position: int
    button_text_align: Vec2
    selectable_text_align: Vec2
    display_window_padding: Vec2
    display_safe_area_padding: Vec2
    mouse_cursor_scale: float
    anti_aliased_lines: bool
    anti_aliased_line_use_tex: bool
    anti_aliased_fill: bool
    curve_tessellation_tolerance: float
    circle_segment_max_error: float
    circle_tessellation_max_error: float

    @staticmethod
    def create() -> GuiStyle: ...
    def color(self, variable: int) -> Vec4: ...
    @property
    def colors(self) -> _Colors: ...
    def __eq__(self, other: object) -> bool: ...

class _ImGuiTableColumnSortSpecs:
    column_user_id: int
    column_index: int
    sort_order: int
    sort_direction: SortDirection

    def __init__(self) -> None: ...
    def _require_pointer(self) -> None: ...

class _ImGuiTableColumnSortSpecs_array:
    def __init__(self) -> None: ...
    def __getitem__(self, idx: int) -> _ImGuiTableColumnSortSpecs: ...
    def __iter__(self) -> Self: ...
    def __next__(self) -> _ImGuiTableColumnSortSpecs: ...
    def _require_pointer(self) -> None: ...

class _ImGuiTableSortSpecs:
    specs_dirty: bool

    def __init__(self) -> None: ...
    @property
    def specs(self) -> _ImGuiTableColumnSortSpecs_array: ...
    @property
    def specs_count(self) -> int: ...
    def _require_pointer(self) -> None: ...

class _ImGuiViewport:
    def __init__(self) -> None: ...
    def get_center(self) -> Vec2: ...
    def get_work_center(self) -> Vec2: ...
    @property
    def flags(self) -> int: ...
    @property
    def pos(self) -> Vec2: ...
    @property
    def size(self) -> Vec2: ...
    @property
    def work_pos(self) -> Vec2: ...
    @property
    def work_size(self) -> Vec2: ...
    def _require_pointer(self) -> None: ...

class _DrawData:
    def __init__(self) -> None: ...
    def deindex_all_buffers(self) -> None: ...
    def scale_clip_rects(self, width: float, height: float) -> None: ...
    @property
    def valid(self) -> bool: ...
    @property
    def cmd_count(self) -> int: ...
    @property
    def total_vtx_count(self) -> int: ...
    @property
    def display_pos(self) -> Vec2: ...
    @property
    def display_size(self) -> Vec2: ...
    @property
    def frame_buffer_scale(self) -> Vec2: ...
    @property
    def total_idx_count(self) -> int: ...
    @property
    def command_lists(self) -> list[_DrawList]: ...
    def _require_pointer(self) -> None: ...

class _StaticGlyphRanges: ...

class GlyphRanges:
    def __init__(self, glyph_ranges: Iterable[int]) -> None: ...

class FontConfig:
    def __init__(
        self,
        font_no: int | None = None,
        size_pixels: float | None = None,
        oversample_h: int | None = None,
        oversample_v: int | None = None,
        pixel_snap_h: bool | None = None,
        glyph_extra_spacing_x: float | None = None,
        glyph_extra_spacing_y: float | None = None,
        glyph_offset_x: float | None = None,
        glyph_offset_y: float | None = None,
        glyph_min_advance_x: float | None = None,
        glyph_max_advance_x: float | None = None,
        merge_mode: bool | None = None,
        font_builder_flags: int | None = None,
        rasterizer_multiply: float | None = None,
        ellipsis_char: str | None = None,
    ) -> None: ...

class _Font: ...

class _FontAtlas:
    texture_id: int
    texture_desired_width: int

    def __init__(self) -> None: ...
    def add_font_default(self) -> _Font: ...
    def add_font_from_file_ttf(
        self,
        filename: str,
        size_pixels: float,
        font_config: FontConfig | None = None,
        glyph_ranges: GlyphRanges | _StaticGlyphRanges | None = None,
    ) -> _Font: ...
    def clear_tex_data(self) -> None: ...
    def clear_input_data(self) -> None: ...
    def clear_fonts(self) -> None: ...
    def clear(self) -> None: ...
    def get_glyph_ranges_chinese(self) -> _StaticGlyphRanges: ...
    def get_glyph_ranges_chinese_full(self) -> _StaticGlyphRanges: ...
    def get_glyph_ranges_cyrillic(self) -> _StaticGlyphRanges: ...
    def get_glyph_ranges_default(self) -> _StaticGlyphRanges: ...
    def get_glyph_ranges_japanese(self) -> _StaticGlyphRanges: ...
    def get_glyph_ranges_korean(self) -> _StaticGlyphRanges: ...
    def get_glyph_ranges_latin(self) -> _StaticGlyphRanges: ...
    def get_glyph_ranges_thai(self) -> _StaticGlyphRanges: ...
    def get_glyph_ranges_vietnamese(self) -> _StaticGlyphRanges: ...
    def get_tex_data_as_alpha8(self) -> tuple[int, int, bytes]: ...
    def get_tex_data_as_rgba32(self) -> tuple[int, int, bytes]: ...
    @property
    def texture_width(self) -> int: ...
    @property
    def texture_height(self) -> int: ...
    def _require_pointer(self) -> None: ...

class _IO:
    config_flags: int
    backend_flags: int
    display_size: Vec2
    delta_time: float
    ini_saving_rate: float
    log_file_name: str
    ini_file_name: str
    mouse_double_click_time: float
    mouse_double_click_max_distance: float
    mouse_drag_threshold: float
    key_repeat_delay: float
    key_repeat_rate: float
    font_global_scale: float
    font_allow_user_scaling: bool
    display_fb_scale: Vec2
    config_mac_osx_behaviors: bool
    config_cursor_blink: bool
    config_drag_click_to_input_text: bool
    config_windows_resize_from_edges: bool
    config_windows_move_from_title_bar_only: bool
    config_memory_compact_timer: float
    get_clipboard_text_fn: Callable[[], str | None] | None
    set_clipboard_text_fn: Callable[[str], None] | None
    mouse_pos: Vec2
    mouse_wheel: float
    mouse_wheel_horizontal: float
    mouse_draw_cursor: bool
    key_ctrl: bool
    key_shift: bool
    key_alt: bool
    key_super: bool

    def __init__(self) -> None: ...
    @property
    def key_map(self) -> Mapping[int, int]: ...  # Real return type would be `cython.view.array`
    @property
    def fonts(self) -> _FontAtlas: ...
    @property
    def mouse_down(self) -> Mapping[int, int]: ...  # Real return type would be `cython.view.array`
    @property
    def keys_down(self) -> Mapping[int, int]: ...  # Real return type would be `cython.view.array`
    @property
    def nav_inputs(self) -> Mapping[int, float]: ...  # Real return type would be `cython.view.array`
    @property
    def want_capture_mouse(self) -> bool: ...
    @property
    def want_capture_keyboard(self) -> bool: ...
    @property
    def want_text_input(self) -> bool: ...
    @property
    def want_set_mouse_pos(self) -> bool: ...
    @property
    def want_save_ini_settings(self) -> bool: ...
    @property
    def nav_active(self) -> bool: ...
    @property
    def nav_visible(self) -> bool: ...
    @property
    def framerate(self) -> float: ...
    @property
    def metrics_render_vertices(self) -> int: ...
    @property
    def metrics_render_indices(self) -> int: ...
    @property
    def metrics_render_windows(self) -> int: ...
    @property
    def metrics_active_windows(self) -> int: ...
    @property
    def metrics_active_allocations(self) -> int: ...
    @property
    def mouse_delta(self) -> Vec2: ...
    def add_input_character(self, c: int) -> None: ...
    def add_input_character_utf16(self, chars: str) -> None: ...
    def add_input_character_utf8(self, chars: str) -> None: ...
    def clear_input_characters(self) -> None: ...

class _InputTextSharedBuffer: ...

class _ImGuiInputTextCallbackData:
    event_char: str
    buffer: str
    buffer_dirty: bool
    cursor_pos: int
    selection_start: int
    selection_end: int

    def __init__(self) -> None: ...
    def delete_chars(self, pos: int, bytes_count: int) -> None: ...
    def insert_chars(self, pos: int, text: str) -> None: ...
    def select_all(self) -> None: ...
    def clear_selection(self) -> None: ...
    def has_selection(self) -> bool: ...
    @property
    def event_flag(self) -> int: ...
    @property
    def flags(self) -> int: ...
    @property
    def user_data(self) -> Any: ...  # User-provided callback data
    @property
    def event_key(self) -> int: ...
    @property
    def buffer_text_length(self) -> int: ...
    @property
    def buffer_size(self) -> int: ...
    def _require_pointer(self) -> None: ...

class _ImGuiSizeCallbackData:
    desired_size: Vec2

    def __init__(self): ...
    @property
    def user_data(self) -> Any: ...  # User-provided callback data
    @property
    def pos(self) -> Vec2: ...
    @property
    def current_size(self) -> Vec2: ...
    def _require_pointer(self) -> None: ...

class _callback_user_info:
    def __init__(self) -> None: ...
    def populate(
        self,
        callback_fn: Callable[[_ImGuiInputTextCallbackData | _ImGuiSizeCallbackData], int | None],
        user_data: Any,  # User-provided callback data
    ) -> None: ...

class _BeginEndGroup:
    def __enter__(self) -> Self: ...
    def __exit__(
        self, exc_type: type[BaseException] | None, exc_val: BaseException | None, exc_tb: TracebackType | None
    ) -> None: ...
    def __eq__(self, other: object) -> bool: ...

class _BeginEndDragDropSource:
    @property
    def dragging(self) -> bool: ...
    def __enter__(self) -> Self: ...
    def __exit__(
        self, exc_type: type[BaseException] | None, exc_val: BaseException | None, exc_tb: TracebackType | None
    ) -> None: ...
    def __bool__(self) -> bool: ...
    def __eq__(self, other: object) -> bool: ...

class _BeginEndDragDropTarget:
    @property
    def hovered(self) -> bool: ...
    def __enter__(self) -> Self: ...
    def __exit__(
        self, exc_type: type[BaseException] | None, exc_val: BaseException | None, exc_tb: TracebackType | None
    ) -> None: ...
    def __bool__(self) -> bool: ...
    def __eq__(self, other: object) -> bool: ...

class _BeginEndTabItem:
    @property
    def opened(self) -> bool: ...
    @property
    def selected(self) -> bool: ...
    def __enter__(self) -> Self: ...
    def __exit__(
        self, exc_type: type[BaseException] | None, exc_val: BaseException | None, exc_tb: TracebackType | None
    ) -> None: ...
    def __getitem__(self, item: int) -> bool: ...
    def __iter__(self) -> Iterator[bool]: ...
    def __eq__(self, other: object) -> bool: ...

class _BeginEndTabBar:
    @property
    def opened(self) -> bool: ...
    def __enter__(self) -> Self: ...
    def __exit__(
        self, exc_type: type[BaseException] | None, exc_val: BaseException | None, exc_tb: TracebackType | None
    ) -> None: ...
    def __getitem__(self, item: int) -> bool: ...
    def __eq__(self, other: object) -> bool: ...

class _BeginEnd:
    @property
    def expanded(self) -> bool: ...
    @property
    def opened(self) -> bool: ...
    def __enter__(self) -> Self: ...
    def __exit__(
        self, exc_type: type[BaseException] | None, exc_val: BaseException | None, exc_tb: TracebackType | None
    ) -> None: ...
    def __getitem__(self, item: int) -> bool: ...
    def __eq__(self, other: object) -> bool: ...

class _BeginEndChild:
    @property
    def visible(self) -> bool: ...
    def __enter__(self) -> Self: ...
    def __exit__(
        self, exc_type: type[BaseException] | None, exc_val: BaseException | None, exc_tb: TracebackType | None
    ) -> None: ...
    def __bool__(self) -> bool: ...
    def __eq__(self, other: object) -> bool: ...

class _BeginEndListBox:
    @property
    def opened(self) -> bool: ...
    def __enter__(self) -> Self: ...
    def __exit__(
        self, exc_type: type[BaseException] | None, exc_val: BaseException | None, exc_tb: TracebackType | None
    ) -> None: ...
    def __bool__(self) -> bool: ...
    def __eq__(self, other: object) -> bool: ...

class _BeginEndTooltip:
    def __enter__(self) -> Self: ...
    def __exit__(
        self, exc_type: type[BaseException] | None, exc_val: BaseException | None, exc_tb: TracebackType | None
    ) -> None: ...

class _BeginEndMainMenuBar:
    @property
    def opened(self) -> bool: ...
    def __enter__(self) -> Self: ...
    def __exit__(
        self, exc_type: type[BaseException] | None, exc_val: BaseException | None, exc_tb: TracebackType | None
    ) -> None: ...
    def __bool__(self) -> bool: ...
    def __eq__(self, other: object) -> bool: ...

class _BeginEndMenuBar:
    @property
    def opened(self) -> bool: ...
    def __enter__(self) -> Self: ...
    def __exit__(
        self, exc_type: type[BaseException] | None, exc_val: BaseException | None, exc_tb: TracebackType | None
    ) -> None: ...
    def __bool__(self) -> bool: ...
    def __eq__(self, other: object) -> bool: ...

class _BeginEndMenu:
    @property
    def opened(self) -> bool: ...
    def __enter__(self) -> Self: ...
    def __exit__(
        self, exc_type: type[BaseException] | None, exc_val: BaseException | None, exc_tb: TracebackType | None
    ) -> None: ...
    def __bool__(self) -> bool: ...
    def __eq__(self, other: object) -> bool: ...

class _BeginEndPopup:
    @property
    def opened(self) -> bool: ...
    def __enter__(self) -> Self: ...
    def __exit__(
        self, exc_type: type[BaseException] | None, exc_val: BaseException | None, exc_tb: TracebackType | None
    ) -> None: ...
    def __bool__(self) -> bool: ...
    def __eq__(self, other: object) -> bool: ...

class _BeginEndPopupModal:
    @property
    def opened(self) -> bool: ...
    @property
    def visible(self) -> bool: ...
    def __enter__(self) -> Self: ...
    def __exit__(
        self, exc_type: type[BaseException] | None, exc_val: BaseException | None, exc_tb: TracebackType | None
    ) -> None: ...
    def __getitem__(self, item: int) -> bool: ...
    def __iter__(self) -> Iterator[bool]: ...
    def __eq__(self, other: object) -> bool: ...

class _BeginEndTable:
    @property
    def opened(self) -> bool: ...
    def __enter__(self) -> Self: ...
    def __exit__(
        self, exc_type: type[BaseException] | None, exc_val: BaseException | None, exc_tb: TracebackType | None
    ) -> None: ...
    def __bool__(self) -> bool: ...
    def __eq__(self, other: object) -> bool: ...

class _BeginEndCombo:
    @property
    def opened(self) -> bool: ...
    def __enter__(self) -> Self: ...
    def __exit__(
        self, exc_type: type[BaseException] | None, exc_val: BaseException | None, exc_tb: TracebackType | None
    ) -> None: ...
    def __bool__(self) -> bool: ...
    def __eq__(self, other: object) -> bool: ...

def get_io() -> _IO: ...
def get_style() -> GuiStyle: ...
def new_frame() -> None: ...
def end_frame() -> None: ...
def render() -> None: ...
def show_user_guide() -> None: ...
def get_version() -> str: ...
def style_colors_dark(dst: GuiStyle | None = None) -> None: ...
def style_colors_classic(dst: GuiStyle | None = None) -> None: ...
def style_colors_light(dst: GuiStyle | None = None) -> None: ...
def show_style_editor(style: GuiStyle | None = None) -> None: ...
def show_demo_window(closable: bool = False) -> bool: ...
def show_about_window(closable: bool = False) -> bool: ...
def show_test_window() -> None: ...
def show_metrics_window(closable: bool = False) -> bool: ...
def show_style_selector(label: str) -> bool: ...
def show_font_selector(label: str) -> None: ...
def begin(label: str, closable: bool = False, flags: WindowFlags = WINDOW_NONE) -> _BeginEnd: ...
def get_draw_data() -> _DrawData: ...
def end() -> None: ...
def begin_child(
    label: str | int, width: float = 0.0, height: float = 0.0, border: bool = False, flags: WindowFlags = WINDOW_NONE
) -> _BeginEndChild: ...
def end_child() -> None: ...
def get_content_region_max() -> Vec2: ...
def get_content_region_available() -> Vec2: ...
def get_content_region_available_width() -> float: ...
def get_window_content_region_min() -> Vec2: ...
def get_window_content_region_max() -> Vec2: ...
def get_window_content_region_width() -> float: ...
def set_window_focus() -> None: ...
def set_window_focus_labeled(label: str) -> None: ...
def set_window_size(width: float, height: float, condition: Condition = ONCE) -> None: ...
def set_window_size_named(label: str, width: float, height: float, condition: Condition = ONCE) -> None: ...
def get_scroll_x() -> int: ...
def get_scroll_y() -> int: ...
def get_scroll_max_x() -> int: ...
def get_scroll_max_y() -> int: ...
def set_scroll_x(scroll_x: float) -> None: ...
def set_scroll_y(scroll_y: float) -> None: ...
def set_window_font_scale(scale: float) -> None: ...
def set_next_window_collapsed(collapsed: bool, condition: Condition = ALWAYS) -> None: ...
def set_next_window_focus() -> None: ...
def set_next_window_bg_alpha(alpha: float) -> None: ...
def get_window_draw_list() -> _DrawList: ...
def get_overlay_draw_list() -> _DrawList: ...
def get_window_position() -> Vec2: ...
def get_window_size() -> Vec2: ...
def get_window_width() -> float: ...
def get_window_height() -> float: ...
def set_next_window_position(
    x: float, y: float, condition: Condition = ALWAYS, pivot_x: float = 0.0, pivot_y: float = 0.0
) -> None: ...
def set_next_window_size(width: float, height: float, condition: Condition = ALWAYS) -> None: ...
def set_next_window_size_constraints(
    size_min: tuple[float, float],
    size_max: tuple[float, float],
    callback: Callable[[_ImGuiSizeCallbackData], None] | None = None,
    user_data: Any = None,  # User-provided callback data
) -> None: ...
def set_next_window_content_size(width: float, height: float) -> None: ...
def set_window_position(x: float, y: float, condition: Condition = ALWAYS) -> None: ...
def set_window_position_labeled(label: str, x: float, y: float, condition: Condition = ALWAYS) -> None: ...
def set_window_collapsed(collapsed: bool, condition: Condition = ALWAYS) -> None: ...
def set_window_collapsed_labeled(label: str, collapsed: bool, condition: Condition = ALWAYS) -> None: ...
def is_window_collapsed() -> bool: ...
def tree_node(text: str, flags: TreeNodeFlags = TREE_NODE_NONE) -> bool: ...
def tree_pop() -> None: ...
def get_tree_node_to_label_spacing() -> float: ...
def collapsing_header(text: str, visible: bool | None = None, flags: TreeNodeFlags = TREE_NODE_NONE) -> bool: ...
def set_next_item_open(is_open: bool, condition: Condition = NONE) -> None: ...
def selectable(
    label: str, selected: bool = False, flags: SelectableFlags = SELECTABLE_NONE, width: float = 0.0, height: float = 0.0
) -> bool: ...
def listbox(label: str, current: int, items: Iterable[str], height_in_items: int = -1) -> tuple[bool, int]: ...
def begin_list_box(label: str, width: float = 0.0, height: float = 0.0) -> _BeginEndListBox: ...
def listbox_header(label: str, width: float = 0.0, height: float = 0.0) -> bool: ...
def end_list_box() -> None: ...
def listbox_footer() -> None: ...
def set_tooltip(text: str) -> None: ...
def begin_tooltip() -> _BeginEndTooltip: ...
def end_tooltip() -> None: ...
def begin_main_menu_bar() -> _BeginEndMainMenuBar: ...
def end_main_menu_bar() -> None: ...
def begin_menu_bar() -> _BeginEndMenuBar: ...
def end_menu_bar() -> None: ...
def begin_menu(label: str, enabled: bool = True) -> _BeginEndMenu: ...
def end_menu() -> None: ...
def menu_item(label: str, shortcut: str | None = None, selected: bool = False, enabled: bool = True) -> tuple[bool, bool]: ...
def open_popup(label: str, flags: PopupFlags = POPUP_NONE) -> None: ...
def open_popup_on_item_click(label: str | None = None, popup_flags: PopupFlags = POPUP_MOUSE_BUTTON_RIGHT) -> None: ...
def begin_popup(label: str, flags: WindowFlags = WINDOW_NONE) -> _BeginEndPopup: ...
def begin_popup_modal(title: str, visible: bool | None = None, flags: WindowFlags = WINDOW_NONE) -> _BeginEndPopupModal: ...
def begin_popup_context_item(label: str | None = None, mouse_button: PopupFlags = POPUP_MOUSE_BUTTON_RIGHT) -> _BeginEndPopup: ...
def begin_popup_context_window(
    label: str | None = None, popup_flags: PopupFlags = POPUP_MOUSE_BUTTON_RIGHT, also_over_items: bool = True
) -> _BeginEndPopup: ...
def begin_popup_context_void(label: str | None = None, popup_flags: PopupFlags = POPUP_MOUSE_BUTTON_RIGHT) -> _BeginEndPopup: ...
def is_popup_open(label: str, flags: PopupFlags = POPUP_NONE) -> bool: ...
def end_popup() -> None: ...
def close_current_popup() -> None: ...
def begin_table(
    label: str,
    column: int,
    flags: TableFlags = TABLE_NONE,
    outer_size_width: float = 0.0,
    outer_size_height: float = 0.0,
    inner_width: float = 0.0,
) -> _BeginEndTable: ...
def end_table() -> None: ...
def table_next_row(row_flags: TableRowFlags = TABLE_ROW_NONE, min_row_height: float = 0.0) -> None: ...
def table_next_column() -> bool: ...
def table_set_column_index(column_n: int) -> bool: ...
def table_setup_column(
    label: str, flags: TableColumnFlags = TABLE_COLUMN_NONE, init_width_or_weight: float = 0.0, user_id: int = 0
) -> None: ...
def table_setup_scroll_freeze(cols: int, rows: int) -> None: ...
def table_headers_row() -> None: ...
def table_header(label: str) -> None: ...
def table_get_sort_specs() -> _ImGuiTableSortSpecs: ...
def table_get_column_count() -> int: ...
def table_get_column_index() -> int: ...
def table_get_row_index() -> int: ...
def table_get_column_name(column_n: int = -1) -> str: ...
def table_get_column_flags(column_n: int = -1) -> TableColumnFlags: ...
def table_set_background_color(target: int, color: int, column_n: int = -1) -> None: ...
def text(text: str) -> None: ...
def text_colored(text: str, r: float, g: float, b: float, a: float = 1.0) -> None: ...
def text_disabled(text: str) -> None: ...
def text_wrapped(text: str) -> None: ...
def label_text(label: str, text: str) -> None: ...
def text_unformatted(text: str) -> None: ...
def bullet() -> None: ...
def bullet_text(text: str) -> None: ...
def button(label: str, width: int = 0, height: int = 0) -> bool: ...
def small_button(label: str) -> bool: ...
def arrow_button(label: str, direction: int = DIRECTION_NONE) -> bool: ...
def invisible_button(identifier: str, width: float, height: float, flags: ButtonFlags = BUTTON_NONE) -> bool: ...
def color_button(desc_id: str, r: float, g: float, b: float, a: float = 1.0, width: float = 0.0, height: float = 0.0) -> bool: ...
def image_button(
    texture_id: int,
    width: float,
    height: float,
    uv0: tuple[float, float] = (0.0, 0.0),
    uv1: tuple[float, float] = (1.0, 1.0),
    tint_color: tuple[float, float, float, float] = (1.0, 1.0, 1.0, 1.0),
    border_color: tuple[float, float, float, float] = (0.0, 0.0, 0.0, 0.0),
    frame_padding: int = -1,
) -> bool: ...
def image(
    texture_id: int,
    width: float,
    height: float,
    uv0: tuple[float, float] = (0.0, 0.0),
    uv1: tuple[float, float] = (1.0, 1.0),
    tint_color: tuple[float, float, float, float] = (1.0, 1.0, 1.0, 1.0),
    border_color: tuple[float, float, float, float] = (0.0, 0.0, 0.0, 0.0),
) -> None: ...
def checkbox(label: str, state: bool) -> tuple[bool, bool]: ...
def checkbox_flags(label: str, flags: int, flags_value: int) -> tuple[bool, int]: ...
def radio_button(label: str, active: bool) -> bool: ...
def begin_combo(label: str, preview_value: str, flags: ComboFlags = COMBO_NONE) -> _BeginEndCombo: ...
def end_combo() -> None: ...
def combo(label: str, current: int, items: list[str], height_in_items: int = -1) -> tuple[bool, int]: ...
def color_edit3(
    label: str, r: float, g: float, b: float, flags: ColorEditFlags = COLOR_EDIT_NONE
) -> tuple[bool, tuple[float, float, float]]: ...
def color_edit4(
    label: str, r: float, g: float, b: float, a: float, flags: ColorEditFlags = COLOR_EDIT_NONE
) -> tuple[bool, tuple[float, float, float, float]]: ...
def drag_float(
    label: str,
    value: float,
    change_speed: float = 1.0,
    min_value: float = 0.0,
    max_value: float = 0.0,
    format: str = "%.3f",
    flags: SliderFlags = SLIDER_FLAGS_NONE,
    power: float = 1.0,
) -> tuple[bool, float]: ...
def drag_float2(
    label: str,
    value0: float,
    value1: float,
    change_speed: float = 1.0,
    min_value: float = 0.0,
    max_value: float = 0.0,
    format: str = "%.3f",
    flags: SliderFlags = SLIDER_FLAGS_NONE,
    power: float = 1.0,
) -> tuple[bool, tuple[float, float]]: ...
def drag_float3(
    label: str,
    value0: float,
    value1: float,
    value2: float,
    change_speed: float = 1.0,
    min_value: float = 0.0,
    max_value: float = 0.0,
    format: str = "%.3f",
    flags: SliderFlags = SLIDER_FLAGS_NONE,
    power: float = 1.0,
) -> tuple[bool, tuple[float, float, float]]: ...
def drag_float4(
    label: str,
    value0: float,
    value1: float,
    value2: float,
    value3: float,
    change_speed: float = 1.0,
    min_value: float = 0.0,
    max_value: float = 0.0,
    format: str = "%.3f",
    flags: SliderFlags = SLIDER_FLAGS_NONE,
    power: float = 1.0,
) -> tuple[bool, tuple[float, float, float, float]]: ...
def drag_float_range2(
    label: str,
    current_min: float,
    current_max: float,
    speed: float = 1.0,
    min_value: float = 0.0,
    max_value: float = 0.0,
    format: str = "%.3f",
    format_max: str | None = None,
    flags: SliderFlags = SLIDER_FLAGS_NONE,
) -> tuple[bool, float, float]: ...
def drag_int(
    label: str,
    value: int,
    change_speed: float = 1.0,
    min_value: int = 0,
    max_value: int = 0,
    format: str = "%d",
    flags: SliderFlags = SLIDER_FLAGS_NONE,
) -> tuple[bool, int]: ...
def drag_int2(
    label: str,
    value0: int,
    value1: int,
    change_speed: float = 1.0,
    min_value: int = 0,
    max_value: int = 0,
    format: str = "%d",
    flags: SliderFlags = SLIDER_FLAGS_NONE,
) -> tuple[bool, tuple[int, int]]: ...
def drag_int3(
    label: str,
    value0: int,
    value1: int,
    value2: int,
    change_speed: float = 1.0,
    min_value: int = 0,
    max_value: int = 0,
    format: str = "%d",
    flags: SliderFlags = SLIDER_FLAGS_NONE,
) -> tuple[bool, tuple[int, int, int]]: ...
def drag_int4(
    label: str,
    value0: int,
    value1: int,
    value2: int,
    value3: int,
    change_speed: float = 1.0,
    min_value: int = 0,
    max_value: int = 0,
    format: str = "%d",
    flags: SliderFlags = SLIDER_FLAGS_NONE,
) -> tuple[bool, tuple[int, int, int, int]]: ...
def drag_int_range2(
    label: str,
    current_min: int,
    current_max: int,
    speed: float = 1.0,
    min_value: int = 0,
    max_value: int = 0,
    format: str = "%d",
    format_max: str | None = None,
    flags: SliderFlags = SLIDER_FLAGS_NONE,
) -> tuple[bool, int, int]: ...
def drag_scalar(
    label: str,
    data_type: DataType,
    data: bytes,
    change_speed: float,
    min_value: bytes | None = None,
    max_value: bytes | None = None,
    format: str | None = None,
    flags: SliderFlags = SLIDER_FLAGS_NONE,
) -> tuple[bool, bytes]: ...
def drag_scalar_N(
    label: str,
    data_type: DataType,
    data: bytes,
    components: int,
    change_speed: float,
    min_value: bytes | None = None,
    max_value: bytes | None = None,
    format: str | None = None,
    flags: SliderFlags = SLIDER_FLAGS_NONE,
) -> tuple[bool, bytes]: ...
def input_text(
    label: str,
    value: str,
    buffer_length: int = -1,
    flags: TextInputFlags = INPUT_TEXT_NONE,
    callback: Callable[[_ImGuiInputTextCallbackData], int | None] | None = None,
    user_data: Any = None,  # User-provided callback data
) -> tuple[bool, str]: ...
def input_text_multiline(
    label: str,
    value: str,
    buffer_length: int = -1,
    width: float = 0.0,
    height: float = 0.0,
    flags: TextInputFlags = INPUT_TEXT_NONE,
    callback: Callable[[_ImGuiInputTextCallbackData], int | None] | None = None,
    user_data: Any = None,  # User-provided callback data
) -> tuple[bool, str]: ...
def input_text_with_hint(
    label: str,
    hint: str,
    value: str,
    buffer_length: int = -1,
    flags: TextInputFlags = INPUT_TEXT_NONE,
    callback: Callable[[_ImGuiInputTextCallbackData], int | None] | None = None,
    user_data: Any = None,  # User-provided callback data
) -> tuple[bool, str]: ...
def input_float(
    label: str,
    value: float,
    step: float = 0.0,
    step_fast: float = 0.0,
    format: str = "%.3f",
    flags: TextInputFlags = INPUT_TEXT_NONE,
) -> tuple[bool, float]: ...
def input_float2(
    label: str, value0: float, value1: float, format: str = "%.3f", flags: TextInputFlags = INPUT_TEXT_NONE
) -> tuple[bool, tuple[float, float]]: ...
def input_float3(
    label: str, value0: float, value1: float, value2: float, format: str = "%.3f", flags: TextInputFlags = INPUT_TEXT_NONE
) -> tuple[bool, tuple[float, float, float]]: ...
def input_float4(
    label: str,
    value0: float,
    value1: float,
    value2: float,
    value3: float,
    format: str = "%.3f",
    flags: TextInputFlags = INPUT_TEXT_NONE,
) -> tuple[bool, tuple[float, float, float, float]]: ...
def input_int(
    label: str, value: int, step: int = 1, step_fast: int = 100, flags: TextInputFlags = INPUT_TEXT_NONE
) -> tuple[bool, int]: ...
def input_int2(label: str, value0: int, value1: int, flags: TextInputFlags = INPUT_TEXT_NONE) -> tuple[bool, tuple[int, int]]: ...
def input_int3(
    label: str, value0: int, value1: int, value2: int, flags: TextInputFlags = INPUT_TEXT_NONE
) -> tuple[bool, tuple[int, int, int]]: ...
def input_int4(
    label: str, value0: int, value1: int, value2: int, value3: int, flags: TextInputFlags = INPUT_TEXT_NONE
) -> tuple[bool, tuple[int, int, int, int]]: ...
def input_double(
    label: str,
    value: float,
    step: float = 0.0,
    step_fast: float = 0.0,
    format: str = "%.6f",
    flags: TextInputFlags = INPUT_TEXT_NONE,
) -> tuple[bool, float]: ...
def input_scalar(
    label: str,
    data_type: DataType,
    data: bytes,
    step: bytes | None = None,
    step_fast: bytes | None = None,
    format: str | None = None,
    flags: TextInputFlags = INPUT_TEXT_NONE,
) -> tuple[int, bytes]: ...
def input_scalar_N(
    label: str,
    data_type: DataType,
    data: bytes,
    components: int,
    step: bytes | None = None,
    step_fast: bytes | None = None,
    format: str | None = None,
    flags: TextInputFlags = INPUT_TEXT_NONE,
) -> tuple[int, bytes]: ...
def slider_float(
    label: str,
    value: float,
    min_value: float,
    max_value: float,
    format: str = "%.3f",
    flags: SliderFlags = SLIDER_FLAGS_NONE,
    power: float = 1.0,
) -> tuple[bool, float]: ...
def slider_float2(
    label: str,
    value0: float,
    value1: float,
    min_value: float,
    max_value: float,
    format: str = "%.3f",
    flags: SliderFlags = SLIDER_FLAGS_NONE,
    power: float = 1.0,
) -> tuple[bool, tuple[float, float]]: ...
def slider_float3(
    label: str,
    value0: float,
    value1: float,
    value2: float,
    min_value: float,
    max_value: float,
    format: str = "%.3f",
    flags: SliderFlags = SLIDER_FLAGS_NONE,
    power: float = 1.0,
) -> tuple[bool, tuple[float, float, float]]: ...
def slider_float4(
    label: str,
    value0: float,
    value1: float,
    value2: float,
    value3: float,
    min_value: float,
    max_value: float,
    format: str = "%.3f",
    flags: SliderFlags = SLIDER_FLAGS_NONE,
    power: float = 1.0,
) -> tuple[bool, tuple[float, float, float, float]]: ...
def slider_angle(
    label: str,
    rad_value: float,
    value_degrees_min: float = -360.0,
    value_degrees_max: float = 360.0,
    format: str = "%.0f deg",
    flags: SliderFlags = SLIDER_FLAGS_NONE,
) -> tuple[bool, float]: ...
def slider_int(
    label: str, value: int, min_value: int, max_value: int, format: str = "%.3f", flags: SliderFlags = SLIDER_FLAGS_NONE
) -> tuple[bool, int]: ...
def slider_int2(
    label: str,
    value0: int,
    value1: int,
    min_value: int,
    max_value: int,
    format: str = "%.3f",
    flags: SliderFlags = SLIDER_FLAGS_NONE,
) -> tuple[bool, tuple[int, int]]: ...
def slider_int3(
    label: str,
    value0: int,
    value1: int,
    value2: int,
    min_value: int,
    max_value: int,
    format: str = "%.3f",
    flags: SliderFlags = SLIDER_FLAGS_NONE,
) -> tuple[bool, tuple[int, int, int]]: ...
def slider_int4(
    label: str,
    value0: int,
    value1: int,
    value2: int,
    value3: int,
    min_value: int,
    max_value: int,
    format: str = "%.3f",
    flags: SliderFlags = SLIDER_FLAGS_NONE,
) -> tuple[bool, tuple[int, int, int, int]]: ...
def slider_scalar(
    label: str,
    data_type: DataType,
    data: bytes,
    min_value: bytes,
    max_value: bytes,
    format: str | None = None,
    flags: SliderFlags = SLIDER_FLAGS_NONE,
) -> tuple[bool, bytes]: ...
def slider_scalar_N(
    label: str,
    data_type: DataType,
    data: bytes,
    components: int,
    min_value: bytes,
    max_value: bytes,
    format: str | None = None,
    flags: SliderFlags = SLIDER_FLAGS_NONE,
) -> tuple[bool, bytes]: ...
def v_slider_float(
    label: str,
    width: float,
    height: float,
    value: float,
    min_value: float,
    max_value: float,
    format: str = "%.f",
    flags: SliderFlags = SLIDER_FLAGS_NONE,
) -> tuple[bool, float]: ...
def v_slider_int(
    label: str,
    width: float,
    height: float,
    value: int,
    min_value: int,
    max_value: int,
    format: str = "%d",
    flags: SliderFlags = SLIDER_FLAGS_NONE,
) -> tuple[bool, int]: ...
def v_slider_scalar(
    label: str,
    width: float,
    height: float,
    data_type: DataType,
    data: bytes,
    min_value: bytes,
    max_value: bytes,
    format: str | None = None,
    flags: SliderFlags = SLIDER_FLAGS_NONE,
) -> tuple[bool, bytes]: ...
def plot_lines(
    label: str,
    values: Buffer,  # values should only accept buffer of floats
    values_count: int = -1,
    values_offset: int = 0,
    overlay_text: str | None = None,
    scale_min: float = ...,
    scale_max: float = ...,
    graph_size: tuple[float, float] = (0.0, 0.0),
    stride: int = ...,
) -> None: ...
def plot_histogram(
    label: str,
    values: Buffer,  # values should only accept buffer of floats
    values_count: int = -1,
    values_offset: int = 0,
    overlay_text: str | None = None,
    scale_min: float = ...,
    scale_max: float = ...,
    stride: int = ...,
) -> None: ...
def progress_bar(fraction: float, size: tuple[float, float] = ..., overlay: str = "") -> None: ...
def is_window_appearing() -> bool: ...
def set_item_default_focus() -> None: ...
def set_keyboard_focus_here(offset: int = 0) -> None: ...
def is_item_hovered(flags: int = 0) -> bool: ...
def is_item_focused() -> bool: ...
def is_item_active() -> bool: ...
def is_item_clicked(mouse_button: int = 0) -> bool: ...
def is_item_visible() -> bool: ...
def is_item_edited() -> bool: ...
def is_item_activated() -> bool: ...
def is_item_deactivated() -> bool: ...
def is_item_deactivated_after_edit() -> bool: ...
def is_item_toggled_open() -> bool: ...
def is_any_item_hovered() -> bool: ...
def is_any_item_active() -> bool: ...
def is_any_item_focused() -> bool: ...
def get_item_rect_min() -> Vec2: ...
def get_item_rect_max() -> Vec2: ...
def get_item_rect_size() -> Vec2: ...
def set_item_allow_overlap() -> None: ...
def get_main_viewport() -> _ImGuiViewport: ...
def is_window_hovered(flags: HoverFlags = HOVERED_NONE) -> bool: ...
def is_window_focused(flags: FocusFlags = FOCUS_NONE) -> bool: ...
def is_rect_visible(size_width: float, size_height: float) -> bool: ...
def get_style_color_name(index: int) -> str: ...
def get_time() -> float: ...
def get_background_draw_list() -> _DrawList: ...
def get_foreground_draw_list() -> _DrawList: ...
def get_key_index(key: Key) -> int: ...
def is_key_pressed(key_index: Key, repeat: bool = False) -> bool: ...
def is_key_down(key_index: Key) -> bool: ...
def is_mouse_hovering_rect(r_min_x: float, r_min_y: float, r_max_x: float, r_max_y: float, clip: bool = True) -> bool: ...
def is_mouse_double_clicked(button: int = 0) -> bool: ...
def is_mouse_clicked(button: int = 0, repeat: bool = False) -> bool: ...
def is_mouse_released(button: int = 0) -> bool: ...
def is_mouse_down(button: int = 0) -> bool: ...
def is_mouse_dragging(button: int, lock_threshold: float = -1.0) -> bool: ...
def get_mouse_drag_delta(button: int = 0, lock_threshold: float = -1.0) -> Vec2: ...
def get_mouse_pos() -> Vec2: ...
def get_mouse_position() -> Vec2: ...
def reset_mouse_drag_delta(button: int = 0) -> None: ...
def get_mouse_cursor() -> int: ...
def set_mouse_cursor(mouse_cursor_type: int) -> None: ...
def capture_mouse_from_app(want_capture_mouse_value: bool = True) -> None: ...
def get_clipboard_text() -> str: ...
def load_ini_settings_from_disk(ini_file_name: str) -> None: ...
def load_ini_settings_from_memory(ini_data: str) -> None: ...
def save_ini_settings_to_disk(ini_file_name: str) -> None: ...
def save_ini_settings_to_memory() -> str: ...
def set_clipboard_text(text: str) -> None: ...
def set_scroll_here_x(center_x_ratio: float = 0.5) -> None: ...
def set_scroll_here_y(center_y_ratio: float = 0.5) -> None: ...
def set_scroll_from_pos_x(local_x: float, center_x_ratio: float = 0.5) -> None: ...
def set_scroll_from_pos_y(local_y: float, center_y_ratio: float = 0.5) -> None: ...
def push_font(font: _Font) -> None: ...
def pop_font() -> _Font: ...
def calc_text_size(text: str, hide_text_after_double_hash: bool = False, wrap_width: float = -1.0) -> Vec2: ...
def color_convert_u32_to_float4(in_: int) -> Vec4: ...
def color_convert_float4_to_u32(r: float, g: float, b: float, a: float) -> int: ...
def color_convert_rgb_to_hsv(r: float, g: float, b: float) -> tuple[float, float, float]: ...
def color_convert_hsv_to_rgb(h: float, s: float, v: float) -> tuple[float, float, float]: ...
def push_style_var(variable: StyleVar, value: float | tuple[float, float]) -> None: ...
def push_style_color(variable: int, r: float, g: float, b: float, a: float = 1.0) -> None: ...
def pop_style_var(count: int = 1) -> None: ...
def get_font_size() -> float: ...
def get_style_color_vec_4(idx: int) -> Vec4: ...
def get_font_tex_uv_white_pixel() -> Vec2: ...
def get_color_u32_idx(idx: int, alpha_mul: float = 1.0) -> int: ...
def get_color_u32_rgba(r: float, g: float, b: float, a: float) -> int: ...
def get_color_u32(col: int) -> int: ...
def push_item_width(item_width: float) -> None: ...
def pop_item_width() -> None: ...
def set_next_item_width(item_width: float) -> None: ...
def calculate_item_width() -> None: ...
def push_text_wrap_pos(wrap_pos_x: float = 0.0) -> None: ...
def push_text_wrap_position(wrap_pos_x: float = 0.0) -> None: ...
def pop_text_wrap_pos() -> None: ...
def pop_text_wrap_position() -> None: ...
def push_allow_keyboard_focus(allow_focus: bool) -> None: ...
def pop_allow_keyboard_focus() -> None: ...
def push_button_repeat(repeat: bool) -> None: ...
def pop_button_repeat() -> None: ...
def pop_style_color(count: int = 1) -> None: ...
def separator() -> None: ...
def same_line(position: float = 0.0, spacing: float = -1.0) -> None: ...
def new_line() -> None: ...
def spacing() -> None: ...
def dummy(width: float, height: float) -> None: ...
def indent(width: float = 0.0) -> None: ...
def unindent(width: float = 0.0) -> None: ...
def columns(count: int = 1, identifier: str | None = None, border: bool = True) -> None: ...
def next_column() -> None: ...
def get_column_index() -> int: ...
def get_column_offset(column_index: int = -1) -> float: ...
def set_column_offset(column_index: int, offset_x: float) -> None: ...
def get_column_width(column_index: int = -1) -> float: ...
def set_column_width(column_index: int, width: float) -> None: ...
def get_columns_count() -> int: ...
def begin_tab_bar(identifier: str, flags: TabBarFlags = TAB_BAR_NONE) -> _BeginEndTabBar: ...
def end_tab_bar() -> None: ...
def begin_tab_item(label: str, opened: bool | None = None, flags: TabItemFlags = TAB_ITEM_NONE) -> _BeginEndTabItem: ...
def end_tab_item() -> None: ...
def tab_item_button(label: str, flags: TabItemFlags = TAB_ITEM_NONE) -> bool: ...
def set_tab_item_closed(tab_or_docked_window_label: str) -> None: ...
def begin_drag_drop_source(flags: DragDropFlags = DRAG_DROP_NONE) -> _BeginEndDragDropSource: ...
def set_drag_drop_payload(type: str, data: bytes, condition: Condition = ALWAYS) -> bool: ...
def end_drag_drop_source() -> None: ...
def begin_drag_drop_target() -> _BeginEndDragDropTarget: ...
def accept_drag_drop_payload(
    type: str,
    flags: DragDropAcceptFlags = cast(
        DragDropAcceptFlags, 0
    ),  # cast is required here as pyimgui does not define required _NONE enum value for DragDropAcceptFlags
) -> bytes | None: ...
def end_drag_drop_target() -> None: ...
def get_drag_drop_payload() -> bytes | None: ...
def push_clip_rect(
    clip_rect_min_x: float,
    clip_rect_min_y: float,
    clip_rect_max_x: float,
    clip_rect_max_y: float,
    intersect_with_current_clip_rect: bool = False,
) -> None: ...
def pop_clip_rect() -> None: ...
def begin_group() -> _BeginEndGroup: ...
def end_group() -> None: ...
def get_cursor_pos() -> Vec2: ...
def get_cursor_pos_x() -> float: ...
def get_cursor_pos_y() -> float: ...
def set_cursor_pos(local_pos: tuple[float, float]) -> None: ...
def set_cursor_pos_x(x: float) -> None: ...
def set_cursor_pos_y(y: float) -> None: ...
def get_cursor_start_pos() -> Vec2: ...
def get_cursor_screen_pos() -> Vec2: ...
def set_cursor_screen_pos(screen_pos: tuple[float, float]) -> None: ...
def get_cursor_position() -> Vec2: ...
def set_cursor_position(local_pos: tuple[float, float]) -> None: ...
def get_cursor_start_position() -> Vec2: ...
def get_cursor_screen_position() -> Vec2: ...
def set_cursor_screen_position(screen_pos: tuple[float, float]) -> None: ...
def align_text_to_frame_padding() -> None: ...
def get_text_line_height() -> int: ...
def get_text_line_height_with_spacing() -> int: ...
def get_frame_height() -> float: ...
def get_frame_height_with_spacing() -> float: ...
def create_context(shared_font_atlas: _FontAtlas | None = None) -> _ImGuiContext: ...
def destroy_context(ctx: _ImGuiContext | None = None) -> None: ...
def get_current_context() -> _ImGuiContext: ...
def set_current_context(ctx: _ImGuiContext) -> None: ...
def push_id(str_id: str) -> None: ...
def pop_id() -> None: ...
def _ansifeed_text_ansi(text: str) -> None: ...
def _ansifeed_text_ansi_colored(text: str, r: float, g: float, b: float, a: float = 1.0) -> None: ...
@contextmanager
def _py_font(font: _Font) -> Iterator[None]: ...
@contextmanager
def _py_styled(variable: StyleVar, value: float | tuple[float, float]) -> Iterator[None]: ...
@contextmanager
def _py_colored(variable: int, r: float, g: float, b: float, a: float = 1.0) -> Iterator[None]: ...
@contextmanager
def _py_istyled(*variables_and_values: tuple[StyleVar, float | tuple[float, float]]) -> Iterator[None]: ...
@contextmanager
def _py_scoped(str_id: str) -> Iterator[None]: ...
def _py_vertex_buffer_vertex_pos_offset() -> int: ...
def _py_vertex_buffer_vertex_uv_offset() -> int: ...
def _py_vertex_buffer_vertex_col_offset() -> int: ...
def _py_vertex_buffer_vertex_size() -> int: ...
def _py_index_buffer_index_size() -> int: ...
