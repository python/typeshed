import contextlib as _contextlib
import ctypes as _ct
import enum as _enum
import sys as _sys
import typing as _t
from collections.abc import Buffer as _Buffer

# Condition enum
Condition = _t.NewType('Condition', _enum.IntFlag)
NONE = _t.cast(Condition, ...)
ALWAYS = _t.cast(Condition, ...)
ONCE = _t.cast(Condition, ...)
FIRST_USE_EVER = _t.cast(Condition, ...)
APPEARING = _t.cast(Condition, ...)

StyleVar = _t.NewType('StyleVar', _enum.IntFlag)
STYLE_ALPHA = _t.cast(StyleVar, ...)
STYLE_WINDOW_PADDING = _t.cast(StyleVar, ...)
STYLE_WINDOW_ROUNDING = _t.cast(StyleVar, ...)
STYLE_WINDOW_BORDERSIZE = _t.cast(StyleVar, ...)
STYLE_WINDOW_MIN_SIZE = _t.cast(StyleVar, ...)
STYLE_WINDOW_TITLE_ALIGN = _t.cast(StyleVar, ...)
STYLE_CHILD_ROUNDING = _t.cast(StyleVar, ...)
STYLE_CHILD_BORDERSIZE = _t.cast(StyleVar, ...)
STYLE_POPUP_ROUNDING = _t.cast(StyleVar, ...)
STYLE_POPUP_BORDERSIZE = _t.cast(StyleVar, ...)
STYLE_FRAME_PADDING = _t.cast(StyleVar, ...)
STYLE_FRAME_ROUNDING = _t.cast(StyleVar, ...)
STYLE_FRAME_BORDERSIZE = _t.cast(StyleVar, ...)
STYLE_ITEM_SPACING = _t.cast(StyleVar, ...)
STYLE_ITEM_INNER_SPACING = _t.cast(StyleVar, ...)
STYLE_INDENT_SPACING = _t.cast(StyleVar, ...)
STYLE_CELL_PADDING = _t.cast(StyleVar, ...)
STYLE_SCROLLBAR_SIZE = _t.cast(StyleVar, ...)
STYLE_SCROLLBAR_ROUNDING = _t.cast(StyleVar, ...)
STYLE_GRAB_MIN_SIZE = _t.cast(StyleVar, ...)
STYLE_GRAB_ROUNDING = _t.cast(StyleVar, ...)
STYLE_TAB_ROUNDING = _t.cast(StyleVar, ...)
STYLE_BUTTON_TEXT_ALIGN = _t.cast(StyleVar, ...)
STYLE_SELECTABLE_TEXT_ALIGN = _t.cast(StyleVar, ...)

ButtonFlags = _t.NewType('ButtonFlags', _enum.IntFlag)
BUTTON_NONE = _t.cast(ButtonFlags, ...)
BUTTON_MOUSE_BUTTON_LEFT = _t.cast(ButtonFlags, ...)
BUTTON_MOUSE_BUTTON_RIGHT = _t.cast(ButtonFlags, ...)
BUTTON_MOUSE_BUTTON_MIDDLE = _t.cast(ButtonFlags, ...)

KEY_TAB = _t.cast(int, ...)
KEY_LEFT_ARROW = _t.cast(int, ...)
KEY_RIGHT_ARROW = _t.cast(int, ...)
KEY_UP_ARROW = _t.cast(int, ...)
KEY_DOWN_ARROW = _t.cast(int, ...)
KEY_PAGE_UP = _t.cast(int, ...)
KEY_PAGE_DOWN = _t.cast(int, ...)
KEY_HOME = _t.cast(int, ...)
KEY_END = _t.cast(int, ...)
KEY_INSERT = _t.cast(int, ...)
KEY_DELETE = _t.cast(int, ...)
KEY_BACKSPACE = _t.cast(int, ...)
KEY_SPACE = _t.cast(int, ...)
KEY_ENTER = _t.cast(int, ...)
KEY_ESCAPE = _t.cast(int, ...)
KEY_PAD_ENTER = _t.cast(int, ...)
KEY_A = _t.cast(int, ...)
KEY_C = _t.cast(int, ...)
KEY_V = _t.cast(int, ...)
KEY_X = _t.cast(int, ...)
KEY_Y = _t.cast(int, ...)
KEY_Z = _t.cast(int, ...)

KEY_MOD_NONE = _t.cast(int, ...)
KEY_MOD_CTRL = _t.cast(int, ...)
KEY_MOD_SHIFT = _t.cast(int, ...)
KEY_MOD_ALT = _t.cast(int, ...)
KEY_MOD_SUPER = _t.cast(int, ...)

NAV_INPUT_ACTIVATE = _t.cast(int, ...)
NAV_INPUT_CANCEL = _t.cast(int, ...)
NAV_INPUT_INPUT = _t.cast(int, ...)
NAV_INPUT_MENU = _t.cast(int, ...)
NAV_INPUT_DPAD_LEFT = _t.cast(int, ...)
NAV_INPUT_DPAD_RIGHT = _t.cast(int, ...)
NAV_INPUT_DPAD_UP = _t.cast(int, ...)
NAV_INPUT_DPAD_DOWN = _t.cast(int, ...)
NAV_INPUT_L_STICK_LEFT = _t.cast(int, ...)
NAV_INPUT_L_STICK_RIGHT = _t.cast(int, ...)
NAV_INPUT_L_STICK_UP = _t.cast(int, ...)
NAV_INPUT_L_STICK_DOWN = _t.cast(int, ...)
NAV_INPUT_FOCUS_PREV = _t.cast(int, ...)
NAV_INPUT_FOCUS_NEXT = _t.cast(int, ...)
NAV_INPUT_TWEAK_SLOW = _t.cast(int, ...)
NAV_INPUT_TWEAK_FAST = _t.cast(int, ...)
NAV_INPUT_COUNT = _t.cast(int, ...)

WindowFlags = _t.NewType('WindowFlags', _enum.IntFlag)
WINDOW_NONE = _t.cast(WindowFlags, ...)
WINDOW_NO_TITLE_BAR = _t.cast(WindowFlags, ...)
WINDOW_NO_RESIZE = _t.cast(WindowFlags, ...)
WINDOW_NO_MOVE = _t.cast(WindowFlags, ...)
WINDOW_NO_SCROLLBAR = _t.cast(WindowFlags, ...)
WINDOW_NO_SCROLL_WITH_MOUSE = _t.cast(WindowFlags, ...)
WINDOW_NO_COLLAPSE = _t.cast(WindowFlags, ...)
WINDOW_ALWAYS_AUTO_RESIZE = _t.cast(WindowFlags, ...)
WINDOW_NO_BACKGROUND = _t.cast(WindowFlags, ...)
WINDOW_NO_SAVED_SETTINGS = _t.cast(WindowFlags, ...)
WINDOW_NO_MOUSE_INPUTS = _t.cast(WindowFlags, ...)
WINDOW_MENU_BAR = _t.cast(WindowFlags, ...)
WINDOW_HORIZONTAL_SCROLLING_BAR = _t.cast(WindowFlags, ...)
WINDOW_NO_FOCUS_ON_APPEARING = _t.cast(WindowFlags, ...)
WINDOW_NO_BRING_TO_FRONT_ON_FOCUS = _t.cast(WindowFlags, ...)
WINDOW_ALWAYS_VERTICAL_SCROLLBAR = _t.cast(WindowFlags, ...)
WINDOW_ALWAYS_HORIZONTAL_SCROLLBAR = _t.cast(WindowFlags, ...)
WINDOW_ALWAYS_USE_WINDOW_PADDING = _t.cast(WindowFlags, ...)
WINDOW_NO_NAV_INPUTS = _t.cast(WindowFlags, ...)
WINDOW_NO_NAV_FOCUS = _t.cast(WindowFlags, ...)
WINDOW_UNSAVED_DOCUMENT = _t.cast(WindowFlags, ...)
WINDOW_NO_NAV = _t.cast(WindowFlags, ...)
WINDOW_NO_DECORATION = _t.cast(WindowFlags, ...)
WINDOW_NO_INPUTS = _t.cast(WindowFlags, ...)

ColorEditFlags = _t.NewType('ColorEditFlags', _enum.IntFlag)
COLOR_EDIT_NONE = _t.cast(ColorEditFlags, ...)
COLOR_EDIT_NO_ALPHA = _t.cast(ColorEditFlags, ...)
COLOR_EDIT_NO_PICKER = _t.cast(ColorEditFlags, ...)
COLOR_EDIT_NO_OPTIONS = _t.cast(ColorEditFlags, ...)
COLOR_EDIT_NO_SMALL_PREVIEW = _t.cast(ColorEditFlags, ...)
COLOR_EDIT_NO_INPUTS = _t.cast(ColorEditFlags, ...)
COLOR_EDIT_NO_TOOLTIP = _t.cast(ColorEditFlags, ...)
COLOR_EDIT_NO_LABEL = _t.cast(ColorEditFlags, ...)
COLOR_EDIT_NO_SIDE_PREVIEW = _t.cast(ColorEditFlags, ...)
COLOR_EDIT_NO_DRAG_DROP = _t.cast(ColorEditFlags, ...)
COLOR_EDIT_NO_BORDER = _t.cast(ColorEditFlags, ...)

COLOR_EDIT_ALPHA_BAR = _t.cast(ColorEditFlags, ...)
COLOR_EDIT_ALPHA_PREVIEW = _t.cast(ColorEditFlags, ...)
COLOR_EDIT_ALPHA_PREVIEW_HALF = _t.cast(ColorEditFlags, ...)
COLOR_EDIT_HDR = _t.cast(ColorEditFlags, ...)
COLOR_EDIT_DISPLAY_RGB = _t.cast(ColorEditFlags, ...)
COLOR_EDIT_DISPLAY_HSV = _t.cast(ColorEditFlags, ...)
COLOR_EDIT_DISPLAY_HEX = _t.cast(ColorEditFlags, ...)
COLOR_EDIT_UINT8 = _t.cast(ColorEditFlags, ...)
COLOR_EDIT_FLOAT = _t.cast(ColorEditFlags, ...)
COLOR_EDIT_PICKER_HUE_BAR = _t.cast(ColorEditFlags, ...)
COLOR_EDIT_PICKER_HUE_WHEEL = _t.cast(ColorEditFlags, ...)
COLOR_EDIT_INPUT_RGB = _t.cast(ColorEditFlags, ...)
COLOR_EDIT_INPUT_HSV = _t.cast(ColorEditFlags, ...)

COLOR_EDIT_DEFAULT_OPTIONS = _t.cast(ColorEditFlags, ...)

TreeNodeFlags = _t.NewType('TreeNodeFlags', _enum.IntFlag)
TREE_NODE_NONE = _t.cast(TreeNodeFlags, ...)
TREE_NODE_SELECTED = _t.cast(TreeNodeFlags, ...)
TREE_NODE_FRAMED = _t.cast(TreeNodeFlags, ...)
TREE_NODE_ALLOW_ITEM_OVERLAP = _t.cast(TreeNodeFlags, ...)
TREE_NODE_NO_TREE_PUSH_ON_OPEN = _t.cast(TreeNodeFlags, ...)
TREE_NODE_NO_AUTO_OPEN_ON_LOG = _t.cast(TreeNodeFlags, ...)
TREE_NODE_DEFAULT_OPEN = _t.cast(TreeNodeFlags, ...)
TREE_NODE_OPEN_ON_DOUBLE_CLICK = _t.cast(TreeNodeFlags, ...)
TREE_NODE_OPEN_ON_ARROW = _t.cast(TreeNodeFlags, ...)
TREE_NODE_LEAF = _t.cast(TreeNodeFlags, ...)
TREE_NODE_BULLET = _t.cast(TreeNodeFlags, ...)
TREE_NODE_FRAME_PADDING = _t.cast(TreeNodeFlags, ...)
TREE_NODE_SPAN_AVAILABLE_WIDTH = _t.cast(TreeNodeFlags, ...)
TREE_NODE_SPAN_FULL_WIDTH = _t.cast(TreeNodeFlags, ...)
TREE_NODE_NAV_LEFT_JUPS_BACK_HERE = _t.cast(TreeNodeFlags, ...)
TREE_NODE_COLLAPSING_HEADER = _t.cast(TreeNodeFlags, ...)

PopupFlags = _t.NewType('PopupFlags', _enum.IntFlag)
POPUP_NONE = _t.cast(PopupFlags, ...)
POPUP_MOUSE_BUTTON_LEFT = _t.cast(PopupFlags, ...)
POPUP_MOUSE_BUTTON_RIGHT = _t.cast(PopupFlags, ...)
POPUP_MOUSE_BUTTON_MIDDLE = _t.cast(PopupFlags, ...)
POPUP_MOUSE_BUTTON_MASK = _t.cast(PopupFlags, ...)
POPUP_MOUSE_BUTTON_DEFAULT = _t.cast(PopupFlags, ...)
POPUP_NO_OPEN_OVER_EXISTING_POPUP = _t.cast(PopupFlags, ...)
POPUP_NO_OPEN_OVER_ITEMS = _t.cast(PopupFlags, ...)
POPUP_ANY_POPUP_ID = _t.cast(PopupFlags, ...)
POPUP_ANY_POPUP_LEVEL = _t.cast(PopupFlags, ...)
POPUP_ANY_POPUP = _t.cast(PopupFlags, ...)

SelectableFlags = _t.NewType('SelectableFlags', _enum.IntFlag)
SELECTABLE_NONE = _t.cast(SelectableFlags, ...)
SELECTABLE_DONT_CLOSE_POPUPS = _t.cast(SelectableFlags, ...)
SELECTABLE_SPAN_ALL_COLUMNS = _t.cast(SelectableFlags, ...)
SELECTABLE_ALLOW_DOUBLE_CLICK = _t.cast(SelectableFlags, ...)
SELECTABLE_DISABLED = _t.cast(SelectableFlags, ...)
SELECTABLE_ALLOW_ITEM_OVERLAP = _t.cast(SelectableFlags, ...)

ComboFlags = _t.NewType('ComboFlags', _enum.IntFlag)
COMBO_NONE = _t.cast(ComboFlags, ...)
COMBO_POPUP_ALIGN_LEFT = _t.cast(ComboFlags, ...)
COMBO_HEIGHT_SMALL = _t.cast(ComboFlags, ...)
COMBO_HEIGHT_REGULAR = _t.cast(ComboFlags, ...)
COMBO_HEIGHT_LARGE = _t.cast(ComboFlags, ...)
COMBO_HEIGHT_LARGEST = _t.cast(ComboFlags, ...)
COMBO_NO_ARROW_BUTTON = _t.cast(ComboFlags, ...)
COMBO_NO_PREVIEW = _t.cast(ComboFlags, ...)
COMBO_HEIGHT_MASK = _t.cast(ComboFlags, ...)

TabBarFlags = _t.NewType('TabBarFlags', _enum.IntFlag)
TAB_BAR_NONE = _t.cast(TabBarFlags, ...)
TAB_BAR_REORDERABLE = _t.cast(TabBarFlags, ...)
TAB_BAR_AUTO_SELECT_NEW_TABS = _t.cast(TabBarFlags, ...)
TAB_BAR_TAB_LIST_POPUP_BUTTON = _t.cast(TabBarFlags, ...)
TAB_BAR_NO_CLOSE_WITH_MIDDLE_MOUSE_BUTTON = _t.cast(TabBarFlags, ...)
TAB_BAR_NO_TAB_LIST_SCROLLING_BUTTONS = _t.cast(TabBarFlags, ...)
TAB_BAR_NO_TOOLTIP = _t.cast(TabBarFlags, ...)
TAB_BAR_FITTING_POLICY_RESIZE_DOWN = _t.cast(TabBarFlags, ...)
TAB_BAR_FITTING_POLICY_SCROLL = _t.cast(TabBarFlags, ...)
TAB_BAR_FITTING_POLICY_MASK = _t.cast(TabBarFlags, ...)
TAB_BAR_FITTING_POLICY_DEFAULT = _t.cast(TabBarFlags, ...)

TabItemFlags = _t.NewType('TabItemFlags', _enum.IntFlag)
TAB_ITEM_NONE = _t.cast(TabItemFlags, ...)
TAB_ITEM_UNSAVED_DOCUMENT = _t.cast(TabItemFlags, ...)
TAB_ITEM_SET_SELECTED = _t.cast(TabItemFlags, ...)
TAB_ITEM_NO_CLOSE_WITH_MIDDLE_MOUSE_BUTTON = _t.cast(TabItemFlags, ...)
TAB_ITEM_NO_PUSH_ID = _t.cast(TabItemFlags, ...)
TAB_ITEM_NO_TOOLTIP = _t.cast(TabItemFlags, ...)
TAB_ITEM_NO_REORDER = _t.cast(TabItemFlags, ...)
TAB_ITEM_LEADING = _t.cast(TabItemFlags, ...)
TAB_ITEM_TRAILING = _t.cast(TabItemFlags, ...)

TableFlags = _t.NewType('TableFlags', _enum.IntFlag)
TABLE_NONE = _t.cast(TableFlags, ...)
TABLE_RESIZABLE = _t.cast(TableFlags, ...)
TABLE_REORDERABLE = _t.cast(TableFlags, ...)
TABLE_HIDEABLE = _t.cast(TableFlags, ...)
TABLE_SORTABLE = _t.cast(TableFlags, ...)
TABLE_NO_SAVED_SETTINGS = _t.cast(TableFlags, ...)
TABLE_CONTEXT_MENU_IN_BODY = _t.cast(TableFlags, ...)
TABLE_ROW_BACKGROUND = _t.cast(TableFlags, ...)
TABLE_BORDERS_INNER_HORIZONTAL = _t.cast(TableFlags, ...)
TABLE_BORDERS_OUTER_HORIZONTAL = _t.cast(TableFlags, ...)
TABLE_BORDERS_INNER_VERTICAL = _t.cast(TableFlags, ...)
TABLE_BORDERS_OUTER_VERTICAL = _t.cast(TableFlags, ...)
TABLE_BORDERS_HORIZONTAL = _t.cast(TableFlags, ...)
TABLE_BORDERS_VERTICAL = _t.cast(TableFlags, ...)
TABLE_BORDERS_INNER = _t.cast(TableFlags, ...)
TABLE_BORDERS_OUTER = _t.cast(TableFlags, ...)
TABLE_BORDERS = _t.cast(TableFlags, ...)
TABLE_NO_BORDERS_IN_BODY = _t.cast(TableFlags, ...)
TABLE_NO_BORDERS_IN_BODY_UTIL_RESIZE = _t.cast(TableFlags, ...)
TABLE_SIZING_FIXED_FIT = _t.cast(TableFlags, ...)
TABLE_SIZING_FIXED_SAME = _t.cast(TableFlags, ...)
TABLE_SIZING_STRETCH_PROP = _t.cast(TableFlags, ...)
TABLE_SIZING_STRETCH_SAME = _t.cast(TableFlags, ...)
TABLE_NO_HOST_EXTEND_X = _t.cast(TableFlags, ...)
TABLE_NO_HOST_EXTEND_Y = _t.cast(TableFlags, ...)
TABLE_NO_KEEP_COLUMNS_VISIBLE = _t.cast(TableFlags, ...)
TABLE_PRECISE_WIDTHS = _t.cast(TableFlags, ...)
TABLE_NO_CLIP = _t.cast(TableFlags, ...)
TABLE_PAD_OUTER_X = _t.cast(TableFlags, ...)
TABLE_NO_PAD_OUTER_X = _t.cast(TableFlags, ...)
TABLE_NO_PAD_INNER_X = _t.cast(TableFlags, ...)
TABLE_SCROLL_X = _t.cast(TableFlags, ...)
TABLE_SCROLL_Y = _t.cast(TableFlags, ...)
TABLE_SORT_MULTI = _t.cast(TableFlags, ...)
TABLE_SORT_TRISTATE = _t.cast(TableFlags, ...)

TableColumnFlags = _t.NewType('TableColumnFlags', _enum.IntFlag)
TABLE_COLUMN_NONE = _t.cast(TableColumnFlags, ...)
TABLE_COLUMN_DEFAULT_HIDE = _t.cast(TableColumnFlags, ...)
TABLE_COLUMN_DEFAULT_SORT = _t.cast(TableColumnFlags, ...)
TABLE_COLUMN_WIDTH_STRETCH = _t.cast(TableColumnFlags, ...)
TABLE_COLUMN_WIDTH_FIXED = _t.cast(TableColumnFlags, ...)
TABLE_COLUMN_NO_RESIZE = _t.cast(TableColumnFlags, ...)
TABLE_COLUMN_NO_REORDER = _t.cast(TableColumnFlags, ...)
TABLE_COLUMN_NO_HIDE = _t.cast(TableColumnFlags, ...)
TABLE_COLUMN_NO_CLIP = _t.cast(TableColumnFlags, ...)
TABLE_COLUMN_NO_SORT = _t.cast(TableColumnFlags, ...)
TABLE_COLUMN_NO_SORT_ASCENDING = _t.cast(TableColumnFlags, ...)
TABLE_COLUMN_NO_SORT_DESCENDING = _t.cast(TableColumnFlags, ...)
TABLE_COLUMN_NO_HEADER_WIDTH = _t.cast(TableColumnFlags, ...)
TABLE_COLUMN_PREFER_SORT_ASCENDING = _t.cast(TableColumnFlags, ...)
TABLE_COLUMN_PREFER_SORT_DESCENDING = _t.cast(TableColumnFlags, ...)
TABLE_COLUMN_INDENT_ENABLE = _t.cast(TableColumnFlags, ...)
TABLE_COLUMN_INDENT_DISABLE = _t.cast(TableColumnFlags, ...)
TABLE_COLUMN_IS_ENABLED = _t.cast(TableColumnFlags, ...)
TABLE_COLUMN_IS_VISIBLE = _t.cast(TableColumnFlags, ...)
TABLE_COLUMN_IS_SORTED = _t.cast(TableColumnFlags, ...)
TABLE_COLUMN_IS_HOVERED = _t.cast(TableColumnFlags, ...)

TableRowFlags = _t.NewType('TableRowFlags', _enum.IntFlag)
TABLE_ROW_NONE = _t.cast(TableRowFlags, ...)
TABLE_ROW_HEADERS = _t.cast(TableRowFlags, ...)

TableBackgroundTarget = _t.NewType('TableBackgroundTarget', int)
TABLE_BACKGROUND_TARGET_NONE = _t.cast(TableBackgroundTarget, ...)
TABLE_BACKGROUND_TARGET_ROW_BG0 = _t.cast(TableBackgroundTarget, ...)
TABLE_BACKGROUND_TARGET_ROW_BG1 = _t.cast(TableBackgroundTarget, ...)
TABLE_BACKGROUND_TARGET_CELL_BG = _t.cast(TableBackgroundTarget, ...)

FocusFlags = _t.NewType('FocusFlags', _enum.IntFlag)
FOCUS_NONE = _t.cast(FocusFlags, ...)
FOCUS_CHILD_WINDOWS = _t.cast(FocusFlags, ...)
FOCUS_ROOT_WINDOW = _t.cast(FocusFlags, ...)
FOCUS_ANY_WINDOW = _t.cast(FocusFlags, ...)
FOCUS_ROOT_AND_CHILD_WINDOWS = _t.cast(FocusFlags, ...)

HoverFlags = _t.NewType('HoverFlags', _enum.IntFlag)
HOVERED_NONE = _t.cast(HoverFlags, ...)
HOVERED_CHILD_WINDOWS = _t.cast(HoverFlags, ...)
HOVERED_ROOT_WINDOW = _t.cast(HoverFlags, ...)
HOVERED_ANY_WINDOW = _t.cast(HoverFlags, ...)
HOVERED_ALLOW_WHEN_BLOCKED_BY_POPUP = _t.cast(HoverFlags, ...)
HOVERED_ALLOW_WHEN_BLOCKED_BY_ACTIVE_ITEM = _t.cast(HoverFlags, ...)
HOVERED_ALLOW_WHEN_OVERLAPPED = _t.cast(HoverFlags, ...)
HOVERED_ALLOW_WHEN_DISABLED = _t.cast(HoverFlags, ...)
HOVERED_RECT_ONLY = _t.cast(HoverFlags, ...)
HOVERED_ROOT_AND_CHILD_WINDOWS = _t.cast(HoverFlags, ...)

DragDropFlags = _t.NewType('DragDropFlags', _enum.IntFlag)
DRAG_DROP_NONE = _t.cast(DragDropFlags, ...)
DRAG_DROP_SOURCE_NO_PREVIEW_TOOLTIP = _t.cast(DragDropFlags, ...)
DRAG_DROP_SOURCE_NO_DISABLE_HOVER = _t.cast(DragDropFlags, ...)
DRAG_DROP_SOURCE_NO_HOLD_TO_OPEN_OTHERS = _t.cast(DragDropFlags, ...)
DRAG_DROP_SOURCE_ALLOW_NULL_ID = _t.cast(DragDropFlags, ...)
DRAG_DROP_SOURCE_EXTERN = _t.cast(DragDropFlags, ...)
DRAG_DROP_SOURCE_AUTO_EXPIRE_PAYLOAD = _t.cast(DragDropFlags, ...)

DragDropAcceptFlags = _t.NewType('DragDropAcceptFlags', _enum.IntFlag)
DRAG_DROP_ACCEPT_BEFORE_DELIVERY = _t.cast(DragDropAcceptFlags, ...)
DRAG_DROP_ACCEPT_NO_DRAW_DEFAULT_RECT = _t.cast(DragDropAcceptFlags, ...)
DRAG_DROP_ACCEPT_NO_PREVIEW_TOOLTIP = _t.cast(DragDropAcceptFlags, ...)
DRAG_DROP_ACCEPT_PEEK_ONLY = _t.cast(DragDropAcceptFlags, ...)

Direction = _t.NewType('Direction', int)
DIRECTION_NONE = _t.cast(Direction, ...)
DIRECTION_LEFT = _t.cast(Direction, ...)
DIRECTION_RIGHT = _t.cast(Direction, ...)
DIRECTION_UP = _t.cast(Direction, ...)
DIRECTION_DOWN = _t.cast(Direction, ...)

SortDirection = _t.NewType('SortDirection', int)
SORT_DIRECTION_NONE = _t.cast(SortDirection, ...)
SORT_DIRECTION_ASCENDING = _t.cast(SortDirection, ...)
SORT_DIRECTION_DESCENDING = _t.cast(SortDirection, ...)

MouseCursor = _t.NewType('MouseCursor', int)
MOUSE_CURSOR_NONE = _t.cast(MouseCursor, ...)
MOUSE_CURSOR_ARROW = _t.cast(MouseCursor, ...)
MOUSE_CURSOR_TEXT_INPUT = _t.cast(MouseCursor, ...)
MOUSE_CURSOR_RESIZE_ALL = _t.cast(MouseCursor, ...)
MOUSE_CURSOR_RESIZE_NS = _t.cast(MouseCursor, ...)
MOUSE_CURSOR_RESIZE_EW = _t.cast(MouseCursor, ...)
MOUSE_CURSOR_RESIZE_NESW = _t.cast(MouseCursor, ...)
MOUSE_CURSOR_RESIZE_NWSE = _t.cast(MouseCursor, ...)
MOUSE_CURSOR_HAND = _t.cast(MouseCursor, ...)
MOUSE_CURSOR_NOT_ALLOWED = _t.cast(MouseCursor, ...)

Color = _t.NewType('Color', int)
COLOR_TEXT = _t.cast(Color, ...)
COLOR_TEXT_DISABLED = _t.cast(Color, ...)
COLOR_WINDOW_BACKGROUND = _t.cast(Color, ...)
COLOR_CHILD_BACKGROUND = _t.cast(Color, ...)
COLOR_POPUP_BACKGROUND = _t.cast(Color, ...)
COLOR_BORDER = _t.cast(Color, ...)
COLOR_BORDER_SHADOW = _t.cast(Color, ...)
COLOR_FRAME_BACKGROUND = _t.cast(Color, ...)
COLOR_FRAME_BACKGROUND_HOVERED = _t.cast(Color, ...)
COLOR_FRAME_BACKGROUND_ACTIVE = _t.cast(Color, ...)
COLOR_TITLE_BACKGROUND = _t.cast(Color, ...)
COLOR_TITLE_BACKGROUND_ACTIVE = _t.cast(Color, ...)
COLOR_TITLE_BACKGROUND_COLLAPSED = _t.cast(Color, ...)
COLOR_MENUBAR_BACKGROUND = _t.cast(Color, ...)
COLOR_SCROLLBAR_BACKGROUND = _t.cast(Color, ...)
COLOR_SCROLLBAR_GRAB = _t.cast(Color, ...)
COLOR_SCROLLBAR_GRAB_HOVERED = _t.cast(Color, ...)
COLOR_SCROLLBAR_GRAB_ACTIVE = _t.cast(Color, ...)
COLOR_CHECK_MARK = _t.cast(Color, ...)
COLOR_SLIDER_GRAB = _t.cast(Color, ...)
COLOR_SLIDER_GRAB_ACTIVE = _t.cast(Color, ...)
COLOR_BUTTON = _t.cast(Color, ...)
COLOR_BUTTON_HOVERED = _t.cast(Color, ...)
COLOR_BUTTON_ACTIVE = _t.cast(Color, ...)
COLOR_HEADER = _t.cast(Color, ...)
COLOR_HEADER_HOVERED = _t.cast(Color, ...)
COLOR_HEADER_ACTIVE = _t.cast(Color, ...)
COLOR_SEPARATOR = _t.cast(Color, ...)
COLOR_SEPARATOR_HOVERED = _t.cast(Color, ...)
COLOR_SEPARATOR_ACTIVE = _t.cast(Color, ...)
COLOR_RESIZE_GRIP = _t.cast(Color, ...)
COLOR_RESIZE_GRIP_HOVERED = _t.cast(Color, ...)
COLOR_RESIZE_GRIP_ACTIVE = _t.cast(Color, ...)
COLOR_TAB = _t.cast(Color, ...)
COLOR_TAB_HOVERED = _t.cast(Color, ...)
COLOR_TAB_ACTIVE = _t.cast(Color, ...)
COLOR_TAB_UNFOCUSED = _t.cast(Color, ...)
COLOR_TAB_UNFOCUSED_ACTIVE = _t.cast(Color, ...)
COLOR_PLOT_LINES = _t.cast(Color, ...)
COLOR_PLOT_LINES_HOVERED = _t.cast(Color, ...)
COLOR_PLOT_HISTOGRAM = _t.cast(Color, ...)
COLOR_PLOT_HISTOGRAM_HOVERED = _t.cast(Color, ...)
COLOR_TABLE_HEADER_BACKGROUND = _t.cast(Color, ...)
COLOR_TABLE_BORDER_STRONG = _t.cast(Color, ...)
COLOR_TABLE_BORDER_LIGHT = _t.cast(Color, ...)
COLOR_TABLE_ROW_BACKGROUND = _t.cast(Color, ...)
COLOR_TABLE_ROW_BACKGROUND_ALT = _t.cast(Color, ...)
COLOR_TEXT_SELECTED_BACKGROUND = _t.cast(Color, ...)
COLOR_DRAG_DROP_TARGET = _t.cast(Color, ...)
COLOR_NAV_HIGHLIGHT = _t.cast(Color, ...)
COLOR_NAV_WINDOWING_HIGHLIGHT = _t.cast(Color, ...)
COLOR_NAV_WINDOWING_DIM_BACKGROUND = _t.cast(Color, ...)
COLOR_MODAL_WINDOW_DIM_BACKGROUND = _t.cast(Color, ...)
COLOR_COUNT = _t.cast(Color, ...)

DataType = _t.NewType('DataType', int)
DATA_TYPE_S8 = _t.cast(DataType, ...)
DATA_TYPE_U8 = _t.cast(DataType, ...)
DATA_TYPE_S16 = _t.cast(DataType, ...)
DATA_TYPE_U16 = _t.cast(DataType, ...)
DATA_TYPE_S32 = _t.cast(DataType, ...)
DATA_TYPE_U32 = _t.cast(DataType, ...)
DATA_TYPE_S64 = _t.cast(DataType, ...)
DATA_TYPE_U64 = _t.cast(DataType, ...)
DATA_TYPE_FLOAT = _t.cast(DataType, ...)
DATA_TYPE_DOUBLE = _t.cast(DataType, ...)

TextInputFlags = _t.NewType('TextInputFlags', _enum.IntFlag)
INPUT_TEXT_NONE = _t.cast(TextInputFlags, ...)
INPUT_TEXT_CHARS_DECIMAL = _t.cast(TextInputFlags, ...)
INPUT_TEXT_CHARS_HEXADECIMAL = _t.cast(TextInputFlags, ...)
INPUT_TEXT_CHARS_UPPERCASE = _t.cast(TextInputFlags, ...)
INPUT_TEXT_CHARS_NO_BLANK = _t.cast(TextInputFlags, ...)
INPUT_TEXT_AUTO_SELECT_ALL = _t.cast(TextInputFlags, ...)
INPUT_TEXT_ENTER_RETURNS_TRUE = _t.cast(TextInputFlags, ...)
INPUT_TEXT_CALLBACK_COMPLETION = _t.cast(TextInputFlags, ...)
INPUT_TEXT_CALLBACK_HISTORY = _t.cast(TextInputFlags, ...)
INPUT_TEXT_CALLBACK_ALWAYS = _t.cast(TextInputFlags, ...)
INPUT_TEXT_CALLBACK_CHAR_FILTER = _t.cast(TextInputFlags, ...)
INPUT_TEXT_ALLOW_TAB_INPUT = _t.cast(TextInputFlags, ...)
INPUT_TEXT_CTRL_ENTER_FOR_NEW_LINE = _t.cast(TextInputFlags, ...)
INPUT_TEXT_NO_HORIZONTAL_SCROLL = _t.cast(TextInputFlags, ...)
INPUT_TEXT_ALWAYS_OVERWRITE = _t.cast(TextInputFlags, ...)
INPUT_TEXT_ALWAYS_INSERT_MODE = _t.cast(TextInputFlags, ...)
INPUT_TEXT_READ_ONLY = _t.cast(TextInputFlags, ...)
INPUT_TEXT_PASSWORD = _t.cast(TextInputFlags, ...)
INPUT_TEXT_NO_UNDO_REDO = _t.cast(TextInputFlags, ...)
INPUT_TEXT_CHARS_SCIENTIFIC = _t.cast(TextInputFlags, ...)
INPUT_TEXT_CALLBACK_RESIZE = _t.cast(TextInputFlags, ...)
INPUT_TEXT_CALLBACK_EDIT = _t.cast(TextInputFlags, ...)

DrawCornerFlags = _t.NewType('DrawCornerFlags', _enum.IntFlag)
DRAW_CORNER_NONE = _t.cast(DrawCornerFlags, ...)
DRAW_CORNER_TOP_LEFT = _t.cast(DrawCornerFlags, ...)
DRAW_CORNER_TOP_RIGHT = _t.cast(DrawCornerFlags, ...)
DRAW_CORNER_BOTTOM_LEFT = _t.cast(DrawCornerFlags, ...)
DRAW_CORNER_BOTTOM_RIGHT = _t.cast(DrawCornerFlags, ...)
DRAW_CORNER_TOP = _t.cast(DrawCornerFlags, ...)
DRAW_CORNER_BOTTOM = _t.cast(DrawCornerFlags, ...)
DRAW_CORNER_LEFT = _t.cast(DrawCornerFlags, ...)
DRAW_CORNER_RIGHT = _t.cast(DrawCornerFlags, ...)
DRAW_CORNER_ALL = _t.cast(DrawCornerFlags, ...)

DrawFlags = _t.NewType('DrawFlags', _enum.IntFlag)
DRAW_NONE = _t.cast(DrawFlags, ...)
DRAW_CLOSED = _t.cast(DrawFlags, ...)
DRAW_ROUND_CORNERS_TOP_LEFT = _t.cast(DrawFlags, ...)
DRAW_ROUND_CORNERS_TOP_RIGHT = _t.cast(DrawFlags, ...)
DRAW_ROUND_CORNERS_BOTTOM_LEFT = _t.cast(DrawFlags, ...)
DRAW_ROUND_CORNERS_BOTTOM_RIGHT = _t.cast(DrawFlags, ...)
DRAW_ROUND_CORNERS_NONE = _t.cast(DrawFlags, ...)
DRAW_ROUND_CORNERS_TOP = _t.cast(DrawFlags, ...)
DRAW_ROUND_CORNERS_BOTTOM = _t.cast(DrawFlags, ...)
DRAW_ROUND_CORNERS_LEFT = _t.cast(DrawFlags, ...)
DRAW_ROUND_CORNERS_RIGHT = _t.cast(DrawFlags, ...)
DRAW_ROUND_CORNERS_ALL = _t.cast(DrawFlags, ...)

DrawListFlags = _t.NewType('DrawListFlags', _enum.IntFlag)
DRAW_LIST_NONE = _t.cast(DrawListFlags, ...)
DRAW_LIST_ANTI_ALIASED_LINES = _t.cast(DrawListFlags, ...)
DRAW_LIST_ANTI_ALIASED_LINES_USE_TEX = _t.cast(DrawListFlags, ...)
DRAW_LIST_ANTI_ALIASED_FILL = _t.cast(DrawListFlags, ...)
DRAW_LIST_ALLOW_VTX_OFFSET = _t.cast(DrawListFlags, ...)

FontAtlasFlags = _t.NewType('FontAtlasFlags', _enum.IntFlag)
FONT_ATLAS_NONE = _t.cast(FontAtlasFlags, ...)
FONT_ATLAS_NO_POWER_OF_TWO_HEIGHT = _t.cast(FontAtlasFlags, ...)
FONT_ATLAS_NO_MOUSE_CURSOR = _t.cast(FontAtlasFlags, ...)
FONT_ATLAS_NO_BAKED_LINES = _t.cast(FontAtlasFlags, ...)

ConfigFlags = _t.NewType('ConfigFlags', _enum.IntFlag)
CONFIG_NONE = _t.cast(ConfigFlags, ...)
CONFIG_NAV_ENABLE_KEYBOARD = _t.cast(ConfigFlags, ...)
CONFIG_NAV_ENABLE_GAMEPAD = _t.cast(ConfigFlags, ...)
CONFIG_NAV_ENABLE_SET_MOUSE_POS = _t.cast(ConfigFlags, ...)
CONFIG_NAV_NO_CAPTURE_KEYBOARD = _t.cast(ConfigFlags, ...)
CONFIG_NO_MOUSE = _t.cast(ConfigFlags, ...)
CONFIG_NO_MOUSE_CURSOR_CHANGE = _t.cast(ConfigFlags, ...)
CONFIG_IS_RGB = _t.cast(ConfigFlags, ...)
CONFIG_IS_TOUCH_SCREEN = _t.cast(ConfigFlags, ...)

BackendFlags = _t.NewType('BackendFlags', _enum.IntFlag)
BACKEND_NONE = _t.cast(BackendFlags, ...)
BACKEND_HAS_GAMEPAD = _t.cast(BackendFlags, ...)
BACKEND_HAS_MOUSE_CURSORS = _t.cast(BackendFlags, ...)
BACKEND_HAS_SET_MOUSE_POS = _t.cast(BackendFlags, ...)
BACKEND_RENDERER_HAS_VTX_OFFSET = _t.cast(BackendFlags, ...)

SliderFlags = _t.NewType('SliderFlags', _enum.IntFlag)
SLIDER_FLAGS_NONE = _t.cast(SliderFlags, ...)
SLIDER_FLAGS_ALWAYS_CLAMP = _t.cast(SliderFlags, ...)
SLIDER_FLAGS_LOGARITHMIC = _t.cast(SliderFlags, ...)
SLIDER_FLAGS_NO_ROUND_TO_FORMAT = _t.cast(SliderFlags, ...)
SLIDER_FLAGS_NO_INPUT = _t.cast(SliderFlags, ...)

MouseButton = _t.NewType('MouseButton', int)
MOUSE_BUTTON_LEFT = _t.cast(MouseButton, ...)
MOUSE_BUTTON_RIGHT = _t.cast(MouseButton, ...)
MOUSE_BUTTON_MIDDLE = _t.cast(MouseButton, ...)

ViewportFlags = _t.NewType('ViewportFlags', _enum.IntFlag)
VIEWPORT_FLAGS_NONE = _t.cast(ViewportFlags, ...)
VIEWPORT_FLAGS_IS_PLATFORM_WINDOW = _t.cast(ViewportFlags, ...)
VIEWPORT_FLAGS_IS_PLATFORM_MONITOR = _t.cast(ViewportFlags, ...)
VIEWPORT_FLAGS_OWNED_BY_APP = _t.cast(ViewportFlags, ...)

Vec2 = _t.NamedTuple('Vec2', [('x', float), ('y', float)])
Vec4 = _t.NamedTuple('Vec4', [('x', float), ('y', float), ('z', float), ('w', float)])

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

    def push_clip_rect(self,
                       clip_rect_min_x: float,
                       clip_rect_min_y: float,
                       clip_rect_max_x: float,
                       clip_rect_max_y: float,
                       intersect_with_current_clip_rect: bool = False) -> None: ...

    def push_clip_rect_full_screen(self) -> None: ...

    def pop_clip_rect(self) -> None: ...

    def push_texture_id(self, texture_id: int) -> None: ...

    def pop_texture_id(self) -> None: ...

    def get_clip_rect_min(self) -> Vec2: ...

    def get_clip_rect_max(self) -> Vec2: ...

    def add_line(self,
                 start_x: float,
                 start_y: float,
                 end_x: float,
                 end_y: float,
                 col: int,
                 thickness: float = 1.0) -> None: ...

    def add_rect(self,
                 upper_left_x: float,
                 upper_left_y: float,
                 lower_right_x: float,
                 lower_right_y: float,
                 col: int,
                 rounding: float = 0.0,
                 flags: int = 0,
                 thickness: float = 1.0) -> None: ...

    def add_rect_filled(self,
                        upper_left_x: float,
                        upper_left_y: float,
                        lower_right_x: float,
                        lower_right_y: float,
                        col: int,
                        rounding: float = 0.0,
                        flags: int = 0) -> None: ...

    def add_rect_filled_multicolor(self,
                                   upper_left_x: float,
                                   upper_left_y: float,
                                   lower_right_x: float,
                                   lower_right_y: float,
                                   col_upr_left: int,
                                   col_upr_right: int,
                                   col_bot_right: int,
                                   col_bot_left: int) -> None: ...

    def add_quad(self,
                 point1_x: float,
                 point1_y: float,
                 point2_x: float,
                 point2_y: float,
                 point3_x: float,
                 point3_y: float,
                 point4_x: float,
                 point4_y: float,
                 col: int,
                 thickness: float = 1.0) -> None: ...

    def add_quad_filled(self,
                        point1_x: float,
                        point1_y: float,
                        point2_x: float,
                        point2_y: float,
                        point3_x: float,
                        point3_y: float,
                        point4_x: float,
                        point4_y: float,
                        col: int) -> None: ...

    def add_triangle(self,
                     point1_x: float,
                     point1_y: float,
                     point2_x: float,
                     point2_y: float,
                     point3_x: float,
                     point3_y: float,
                     col: int,
                     thickness: float = 1.0) -> None: ...

    def add_triangle_filled(self,
                            point1_x: float,
                            point1_y: float,
                            point2_x: float,
                            point2_y: float,
                            point3_x: float,
                            point3_y: float,
                            col: int) -> None: ...

    def add_bezier_cubic(self,
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
                         num_segments: int = 0) -> None: ...

    def add_bezier_quadratic(self,
                             point1_x: float,
                             point1_y: float,
                             point2_x: float,
                             point2_y: float,
                             point3_x: float,
                             point3_y: float,
                             col: int,
                             thickness: float,
                             num_segments: int = 0) -> None: ...

    def add_circle(self,
                   centre_x: float,
                   centre_y: float,
                   radius: float,
                   col: int,
                   num_segments: int = 0,
                   thickness: float = 1.0) -> None: ...

    def add_circle_filled(self,
                          centre_x: float,
                          centre_y: float,
                          radius: float,
                          col: int,
                          num_segments: int = 0) -> None: ...

    def add_ngon(self,
                 centre_x: float,
                 centre_y: float,
                 radius: float,
                 col: int,
                 num_segments: int,
                 thickness: float = 1.0) -> None: ...

    def add_ngon_filled(self,
                        centre_x: float,
                        centre_y: float,
                        radius: float,
                        col: int,
                        num_segments: int) -> None: ...

    def add_text(self,
                 pos_x: float,
                 pos_y: float,
                 col: int,
                 text: str) -> None: ...

    def add_image(self,
                  texture_id: int,
                  a: tuple[int, int],
                  b: tuple[int, int],
                  uv_a: tuple[int, int] = (0, 0),
                  uv_b: tuple[int, int] = (1, 1),
                  col: int = 0xffffffff) -> None: ...

    def add_image_rounded(self,
                          texture_id: int,
                          a: tuple[int, int],
                          b: tuple[int, int],
                          uv_a: tuple[int, int] = (0, 0),
                          uv_b: tuple[int, int] = (1, 1),
                          col: int = 0xffffffff,
                          rounding: float = 0.0,
                          flags: int = 0) -> None: ...

    def add_polyline(self,
                     points: list[tuple[float, float]],
                     col: int,
                     flags: int = 0,
                     thickness: float = 1.0) -> None: ...

    def path_clear(self) -> None: ...

    def path_line_to(self, x: float, y: float) -> None: ...

    def path_arc_to(self,
                    center_x: float,
                    center_y: float,
                    radius: float,
                    a_min: float,
                    a_max: float,
                    num_segments: int = 0) -> None: ...

    def path_arc_to_fast(self,
                         center_x: float,
                         center_y: float,
                         radius: float,
                         a_min_of_12: float,
                         a_max_of_12: float) -> None: ...

    def path_rect(self,
                  point1_x: float,
                  point1_y: float,
                  point2_x: float,
                  point2_y: float,
                  rounding: float = 0.0,
                  flags: int = 0) -> None: ...

    def path_fill_convex(self, col: int) -> None: ...

    def path_stroke(self,
                    col: int,
                    flags: int = 0,
                    thickness: float = 1.0) -> None: ...

    def channels_split(self, channels_count: int) -> None: ...

    def channels_set_current(self, idx: int) -> None: ...

    def channels_merge(self) -> None: ...

    def prim_reserve(self, idx_count: int, vtx_count: int) -> None: ...

    def prim_unreserve(self, idx_count: int, vtx_count: int) -> None: ...

    def prim_rect(self,
                  a_x: float,
                  a_y: float,
                  b_x: float,
                  b_y: float,
                  color: int = 0xffffffff) -> None: ...

    def prim_rect_UV(self,
                     a_x: float,
                     a_y: float,
                     b_x: float,
                     b_y: float,
                     uv_a_u: float,
                     uv_a_v: float,
                     uv_b_u: float,
                     uv_b_v: float,
                     color: int = 0xffffffff) -> None: ...

    def prim_quad_UV(self,
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
                     color: int = 0xffffffff) -> None: ...

    def prim_write_vtx(self,
                       pos_x: float,
                       pos_y: float,
                       u: float,
                       v: float,
                       color: int = 0xffffffff) -> None: ...

    def prim_write_idx(self, idx: int) -> None: ...

    def prim_vtx(self,
                 pos_x: float,
                 pos_y: float,
                 u: float,
                 v: float,
                 color: int = 0xffffffff) -> None: ...

    @property
    def commands(self) -> list[_DrawCmd]: ...

class _Colors:
    def __init__(self, gui_style: 'GuiStyle') -> None: ...

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
    def create() -> 'GuiStyle': ...

    def color(self, variable: int) -> Vec4: ...

    @property
    def colors(self) -> _Colors: ...

    def __eq__(self, other: object) -> bool: ...

class _ImGuiTableColumnSortSpecs:
    column_user_id: _t.Any # TODO _ImGuiTableColumnSortSpecs.column_user_id
    column_index: int
    sort_order: int
    sord_direction: int

    def __init__(self) -> None: ...

    def _require_pointer(self) -> None: ...

class _ImGuiTableColumnSortSpecs_array:
    def __init__(self) -> None: ...

    def __getitem__(self, idx: int) -> _ImGuiTableColumnSortSpecs: ...

    def __iter__(self) -> _t.Self: ...

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

class _StaticGlyphRanges:
    pass

class GlyphRanges:
    def __init__(self, glyph_ranges: _t.Iterable[int]) -> None: ...

class FontConfig:
    def __init__(self,
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
                 ellipsis_char: _t.Any | None = None) -> None: ... # TODO FontConfig.__init__:ellipsis_char

class _Font:
    pass

class _FontAtlas:
    texture_id: int
    texture_desired_width: int

    def __init__(self) -> None: ...

    def add_font_default(self) -> _Font: ...

    def add_font_from_file_ttf(self,
                               filename: str,
                               size_pixels: float,
                               font_config: FontConfig | None = None,
                               glyph_ranges: GlyphRanges | _StaticGlyphRanges | None = None) -> _Font: ...

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
    get_clipboard_text_fn: _t.Callable[[], str | None] | None
    set_clipboard_text_fn: _t.Callable[[str], _t.Any] | None
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
    def key_map(self) -> _t.Mapping[int, int]: ... # TODO Real type would be `cython.view.array`

    @property
    def fonts(self) -> _FontAtlas: ...

    @property
    def mouse_down(self) -> _t.Mapping[int, int]: ... # TODO Real type would be `cython.view.array`

    @property
    def keys_down(self) -> _t.Mapping[int, int]: ... # TODO Real type would be `cython.view.array`

    @property
    def nav_inputs(self) -> _t.Mapping[int, float]: ... # TODO Real type would be `cython.view.array`

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

class _InputTextSharedBuffer:
    pass

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
    def user_data(self) -> _t.Any: ...

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
    def user_data(self) -> _t.Any: ...

    @property
    def pos(self) -> Vec2: ...

    @property
    def current_size(self) -> Vec2: ...

    def _require_pointer(self) -> None: ...

class _callback_user_info:
    def __init__(self) -> None: ...

    def populate(self, callback_fn: _t.Callable[[_ImGuiInputTextCallbackData | _ImGuiSizeCallbackData], _t.Any], user_data: _t.Any) -> None: ...

class _BeginEndGroup:
    def __enter__(self) -> _t.Self: ...

    def __exit__(self, exc_type, exc_val, exc_tb) -> None: ...

    def __eq__(self, other: object) -> bool: ...

class _BeginEndDragDropSource:
    @property
    def dragging(self) -> bool: ...

    def __enter__(self) -> _t.Self: ...

    def __exit__(self, exc_type, exc_val, exc_tb) -> None: ...

    def __bool__(self) -> bool: ...

    def __eq__(self, other: object) -> bool: ...

class _BeginEndDragDropTarget:
    @property
    def hovered(self) -> bool: ...

    def __enter__(self) -> _t.Self: ...

    def __exit__(self, exc_type, exc_val, exc_tb) -> None: ...

    def __bool__(self) -> bool: ...

    def __eq__(self, other: object) -> bool: ...

class _BeginEndTabItem:
    @property
    def opened(self) -> bool: ...

    @property
    def selected(self) -> bool: ...

    def __enter__(self) -> _t.Self: ...

    def __exit__(self, exc_type, exc_val, exc_tb) -> None: ...

    def __getitem__(self, item: int) -> bool: ...

    def __iter__(self) -> _t.Iterator[bool]: ...

    def __eq__(self, other: object) -> bool: ...

class _BeginEndTabBar:
    @property
    def opened(self) -> bool: ...

    def __enter__(self) -> _t.Self: ...

    def __exit__(self, exc_type, exc_val, exc_tb) -> None: ...

    def __getitem__(self, item: int) -> bool: ...

    def __eq__(self, other: object) -> bool: ...

class _BeginEnd:
    @property
    def expanded(self) -> bool: ...

    @property
    def opened(self) -> bool: ...

    def __enter__(self) -> _t.Self: ...

    def __exit__(self, exc_type, exc_val, exc_tb) -> None: ...

    def __getitem__(self, item: int) -> bool: ...

    def __eq__(self, other: object) -> bool: ...

class _BeginEndChild:
    @property
    def visible(self) -> bool: ...

    def __enter__(self) -> _t.Self: ...

    def __exit__(self, exc_type, exc_val, exc_tb) -> None: ...

    def __bool__(self) -> bool: ...

    def __eq__(self, other: object) -> bool: ...

class _BeginEndListBox:
    @property
    def opened(self) -> bool: ...

    def __enter__(self) -> _t.Self: ...

    def __exit__(self, exc_type, exc_val, exc_tb) -> None: ...

    def __bool__(self) -> bool: ...

    def __eq__(self, other: object) -> bool: ...

class _BeginEndTooltip:
    def __enter__(self) -> _t.Self: ...

    def __exit__(self, exc_type, exc_val, exc_tb) -> None: ...

class _BeginEndMainMenuBar:
    @property
    def opened(self) -> bool: ...

    def __enter__(self) -> _t.Self: ...

    def __exit__(self, exc_type, exc_val, exc_tb) -> None: ...

    def __bool__(self) -> bool: ...

    def __eq__(self, other: object) -> bool: ...

class _BeginEndMenuBar:
    @property
    def opened(self) -> bool: ...

    def __enter__(self) -> _t.Self: ...

    def __exit__(self, exc_type, exc_val, exc_tb) -> None: ...

    def __bool__(self) -> bool: ...

    def __eq__(self, other: object) -> bool: ...

class _BeginEndMenu:
    @property
    def opened(self) -> bool: ...

    def __enter__(self) -> _t.Self: ...

    def __exit__(self, exc_type, exc_val, exc_tb) -> None: ...

    def __bool__(self) -> bool: ...

    def __eq__(self, other: object) -> bool: ...

class _BeginEndPopup:
    @property
    def opened(self) -> bool: ...

    def __enter__(self) -> _t.Self: ...

    def __exit__(self, exc_type, exc_val, exc_tb) -> None: ...

    def __bool__(self) -> bool: ...

    def __eq__(self, other: object) -> bool: ...

class _BeginEndPopupModal:
    @property
    def opened(self) -> bool: ...

    @property
    def visible(self) -> bool: ...

    def __enter__(self) -> _t.Self: ...

    def __exit__(self, exc_type, exc_val, exc_tb) -> None: ...

    def __getitem__(self, item: int) -> bool: ...

    def __iter__(self) -> _t.Iterator[bool]: ...

    def __eq__(self, other: object) -> bool: ...

class _BeginEndTable:
    @property
    def opened(self) -> bool: ...

    def __enter__(self) -> _t.Self: ...

    def __exit__(self, exc_type, exc_val, exc_tb) -> None: ...

    def __bool__(self) -> bool: ...

    def __eq__(self, other: object) -> bool: ...

class _BeginEndCombo:
    @property
    def opened(self) -> bool: ...

    def __enter__(self) -> _t.Self: ...

    def __exit__(self, exc_type, exc_val, exc_tb) -> None: ...

    def __bool__(self) -> bool: ...

    def __eq__(self, other: object) -> bool: ...

def get_io() -> _IO: ...

def get_style() -> GuiStyle: ...

def new_frame() -> None:
    '''
    Start a new frame.

    After calling this you can submit any command from this point until
    next :any:`new_frame()` or :any:`render()`.

    .. wraps::
        void NewFrame()
    '''

def end_frame() -> None:
    '''
    End a frame.

    ends the ImGui frame. automatically called by Render(), so most likely
    don't need to ever call that yourself directly. If you don't need to
    render you may call end_frame() but you'll have wasted CPU already.
    If you don't need to render, better to not create any imgui windows
    instead!

    .. wraps::
        void EndFrame()
    '''

def render() -> None:
    '''
    Finalize frame, set rendering data, and run render callback (if set).

    .. wraps::
        void Render()
    '''

def show_user_guide() -> None:
    '''
    Show ImGui user guide editor.

    .. visual-example::
        :width: 700
        :height: 500
        :auto_layout:

        imgui.begin('Example: user guide')
        imgui.show_user_guide()
        imgui.end()


    .. wraps::
        void ShowUserGuide()
    '''

def get_version() -> str:
    '''
    Get the version of Dear ImGui.

    .. wraps::
        void GetVersion()
    '''

def style_colors_dark(dst: GuiStyle | None = None) -> None:
    '''
    Set the style to Dark.

       new, recommended style (default)

    .. wraps::
        void StyleColorsDark(ImGuiStyle* dst = NULL)
    '''

def style_colors_classic(dst: GuiStyle | None = None) -> None:
    '''
    Set the style to Classic.

       classic imgui style.

    .. wraps::
        void StyleColorsClassic(ImGuiStyle* dst = NULL)
    '''

def style_colors_light(dst: GuiStyle | None = None) -> None:
    '''
    Set the style to Light.

       best used with borders and a custom, thicker font

    .. wraps::
        void StyleColorsLight(ImGuiStyle* dst = NULL)
    '''

def show_style_editor(style: GuiStyle | None = None) -> None:
    '''
    Show ImGui style editor.

    .. visual-example::
        :width: 300
        :height: 300
        :auto_layout:

        imgui.begin('Example: my style editor')
        imgui.show_style_editor()
        imgui.end()

    Args:
        style (GuiStyle): style editor state container.

    .. wraps::
        void ShowStyleEditor(ImGuiStyle* ref = NULL)
    '''

def show_demo_window(closable: bool = False) -> bool:
    '''
    Show ImGui demo window.

    .. visual-example::
        :width: 700
        :height: 600
        :auto_layout:

        imgui.show_demo_window()

    Args:
        closable (bool): define if window is closable.

    Returns:
        bool: True if window is not closed (False trigerred by close button).

    .. wraps::
        void ShowDemoWindow(bool* p_open = NULL)
    '''

def show_about_window(closable: bool = False) -> bool:
    '''
    Create About window.
    Display Dear ImGui version, credits and build/system information.

    Args:
        closable (bool): define if window is closable

    Return:
        bool: True if window is not closed (False trigerred by close button).

    .. wraps::
        void ShowAboutWindow(bool* p_open = NULL)
    '''

def show_test_window() -> None:
    '''
    Show ImGui demo window.

    .. visual-example::
        :width: 700
        :height: 600
        :auto_layout:

        imgui.show_test_window()

    .. wraps::
        void ShowDemoWindow()
    '''

def show_metrics_window(closable: bool = False) -> bool:
    '''
    Show ImGui metrics window.

    .. visual-example::
        :width: 700
        :height: 200
        :auto_layout:

        imgui.show_metrics_window()

    Args:
        closable (bool): define if window is closable.

    Returns:
        bool: True if window is not closed (False trigerred by close button).

    .. wraps::
        void ShowMetricsWindow(bool* p_open = NULL)
    '''

def show_style_selector(label: str) -> bool: ...

def show_font_selector(label: str) -> None: ...

def begin(label: str,
          closable: bool = False,
          flags: WindowFlags = WINDOW_NONE) -> _BeginEnd:
    '''
    Begin a window.

    .. visual-example::
        :auto_layout:

        with imgui.begin('Example: empty window'):
            pass

    Example::
        imgui.begin('Example: empty window')
        imgui.end()

    Args:
        label (str): label of the window.
        closable (bool): define if window is closable.
        flags: Window flags. See:
            :ref:`list of available flags <window-flag-options>`.

    Returns:
        _BeginEnd: ``(expanded, opened)`` struct of bools. If window is collapsed
        ``expanded==True``. The value of ``opened`` is always True for
        non-closable and open windows but changes state to False on close
        button click for closable windows. Use with ``with`` to automatically call
        :func:`end` when the block ends.

    .. wraps::
        Begin(
            const char* name,
            bool* p_open = NULL,
            ImGuiWindowFlags flags = 0
        )
    '''

def get_draw_data() -> _DrawData:
    '''
    Get draw data.

    valid after :any:`render()` and until the next call
    to :any:`new_frame()`.  This is what you have to render.

    Returns:
        _DrawData: draw data for all draw calls required to display gui

    .. wraps::
        ImDrawData* GetDrawData()
    '''

def end() -> None:
    '''
    End a window.

    This finishes appending to current window, and pops it off the window
    stack. See: :any:`begin()`.

    .. wraps::
        void End()
    '''

def begin_child(label: str | int,
                width: float = 0.0,
                height: float = 0.0,
                border: bool = False,
                flags: WindowFlags = WINDOW_NONE) -> _BeginEndChild:
    '''
    Begin a scrolling region.

    **Note:** sizing of child region allows for three modes:
    * ``0.0`` - use remaining window size
    * ``>0.0`` - fixed size
    * ``<0.0`` - use remaining window size minus abs(size)

    .. visual-example::
        :width: 200
        :height: 200
        :auto_layout:

        with imgui.begin('Example: child region'):
            with imgui.begin_child('region', 150, -50, border=True):
                imgui.text('inside region')
            imgui.text('outside region')

    Example::
        imgui.begin('Example: child region')

        imgui.begin_child('region', 150, -50, border=True)
        imgui.text('inside region')
        imgui.end_child()

        imgui.text('outside region')
        imgui.end()

    Args:
        label (str or int): Child region identifier.
        width (float): Region width. See note about sizing.
        height (float): Region height. See note about sizing.
        border (bool): True if should display border. Defaults to False.
        flags: Window flags. See:
            :ref:`list of available flags <window-flag-options>`.

    Returns:
        _BeginEndChild: Struct with ``visible`` bool attribute. Use with ``with``
        to automatically call :func:`end_child` when the block ends.`

    .. wraps::
        bool BeginChild(
            const char* str_id,
            const ImVec2& size = ImVec2(0,0),
            bool border = false,
            ImGuiWindowFlags flags = 0
        )

        bool BeginChild(
            ImGuiID id,
            const ImVec2& size = ImVec2(0,0),
            bool border = false,
            ImGuiWindowFlags flags = 0
        )
    '''

def end_child() -> None:
    '''
    End scrolling region.
    Only call if ``begin_child().visible`` is True.

    .. wraps::
        void EndChild()
    '''

def get_content_region_max() -> Vec2:
    '''
    Get current content boundaries in window coordinates.

    Typically window boundaries include scrolling, or current
    column boundaries.

    Returns:
        Vec2: content boundaries two-tuple ``(width, height)``

    .. wraps::
        ImVec2 GetContentRegionMax()
    '''

def get_content_region_available() -> Vec2:
    '''
    Get available content region.

    It is shortcut for:

    .. code-block: python
        imgui.get_content_region_max() - imgui.get_cursor_position()

    Returns:
        Vec2: available content region size two-tuple ``(width, height)``

    .. wraps::
        ImVec2 GetContentRegionMax()
    '''

def get_content_region_available_width() -> float:
    '''
    Get available content region width.

    Returns:
        float: available content region width.

    .. wraps::
        float GetContentRegionAvailWidth()
    '''

def get_window_content_region_min() -> Vec2:
    '''
    Get minimal current window content boundaries in window coordinates.

    It translates roughly to: ``(0, 0) - Scroll``

    Returns:
        Vec2: content boundaries two-tuple ``(width, height)``

    .. wraps::
        ImVec2 GetWindowContentRegionMin()
    '''

def get_window_content_region_max() -> Vec2:
    '''
    Get maximal current window content boundaries in window coordinates.

    It translates roughly to: ``(0, 0) + Size - Scroll``

    Returns:
        Vec2: content boundaries two-tuple ``(width, height)``

    .. wraps::
        ImVec2 GetWindowContentRegionMin()
    '''

def get_window_content_region_width() -> float:
    '''
    Get available current window content region width.

    Returns:
        float: available content region width.

    .. wraps::
        float GetWindowContentRegionWidth()
    '''

def set_window_focus() -> None:
    '''
    Set window to be focused

    Call inside :func:`begin()`.

    .. visual-example::
        :title: Window focus
        :height: 100

        imgui.begin('Window 1')
        imgui.end()

        imgui.begin('Window 2')
        imgui.set_window_focus()
        imgui.end()

    .. wraps::
        void SetWindowFocus()
    '''

def set_window_focus_labeled(label: str) -> None:
    '''
    Set focus to the window named label

    Args:
        label(string): the name of the window that will be focused

    .. visual-example::
        :title: Window focus
        :height: 100

        imgui.set_window_focus_labeled('Window 2')

        imgui.begin('Window 1', True)
        imgui.text('Apples')
        imgui.end()

        imgui.begin('Window 2', True)
        imgui.text('Orange')
        imgui.end()

        imgui.begin('Window 3', True)
        imgui.text('Mango')
        imgui.end()

    .. wraps::
        void SetWindowFocus(
            const char* name
        )
    '''

def set_window_size(width: float,
                    height: float,
                    condition: Condition = ONCE) -> None:
    '''
    Set window size

    Call inside :func:`begin()`.

    **Note:** usage of this function is not recommended. prefer using
    :func:`set_next_window_size()` as this may incur tearing and minor
    side-effects.

    Args:
        width (float): window width. Value 0.0 enables autofit.
        height (float): window height. Value 0.0 enables autofit.
        condition (:ref:`condition flag <condition-options>`): defines on which
            condition value should be set. Defaults to :any:`imgui.ONCE`.

    .. visual-example::
        :title: window sizing
        :height: 200

        imgui.begin('Window size')
        imgui.set_window_size(80, 180)
        imgui.end()

    .. wraps::
        void SetWindowSize(
            const ImVec2& size,
            ImGuiCond cond = 0,
        )
    '''

def set_window_size_named(label: str,
                          width: float,
                          height: float,
                          condition: Condition = ONCE) -> None:
    '''
    Set the window with label to some size

    Args:
        label(string): name of the window
        width(float): new width of the window
        height(float): new height of the window
        condition (:ref:`condition flag <condition-options>`): defines on which
            condition value should be set. Defaults to :any:`imgui.ONCE`.

    .. visual-example::
        :title: Window size
        :height: 200

        imgui.set_window_size_named('Window 1',100,100)
        imgui.set_window_size_named('Window 2',100,200)

        imgui.begin('Window 1')
        imgui.end()

        imgui.begin('Window 2')
        imgui.end()

    .. wraps::
        void SetWindowSize(
            const char* name,
            const ImVec2& size,
             ImGuiCond cond
        )

    '''

def get_scroll_x() -> int:
    '''
    Get scrolling amount [0..GetScrollMaxX()]

    Returns:
        float: the current scroll X value

    .. wraps::
        int GetScrollX()
    '''

def get_scroll_y() -> int:
    '''
    Get scrolling amount [0..GetScrollMaxY()]

    Returns:
        float: the current scroll Y value

    .. wraps::
        int GetScrollY()
    '''

def get_scroll_max_x() -> int:
    '''
    Get maximum scrolling amount ~~ ContentSize.X - WindowSize.X

    Returns:
        float: the maximum scroll X amount

    .. wraps::
        int GetScrollMaxX()
    '''

def get_scroll_max_y() -> int:
    '''
    Get maximum scrolling amount ~~ ContentSize.X - WindowSize.X

    Returns:
        float: the maximum scroll Y amount

    .. wraps::
        int GetScrollMaxY()
    '''

def set_scroll_x(scroll_x: float) -> None:
    '''
    Set scrolling amount [0..SetScrollMaxX()]

    .. wraps::
        int SetScrollX(float)
    '''

def set_scroll_y(scroll_y: float) -> None:
    '''
    Set scrolling amount [0..SetScrollMaxY()]

    .. wraps::
        int SetScrollY(flot)
    '''

def set_window_font_scale(scale: float) -> None:
    '''
    Adjust per-window font scale for current window.

    Function should be called inside window context so after calling
    :any:`begin()`.

    Note: use ``get_io().font_global_scale`` if you want to scale all windows.

    .. visual-example::
        :auto_layout:
        :height: 100

        imgui.begin('Example: font scale')
        imgui.set_window_font_scale(2.0)
        imgui.text('Bigger font')
        imgui.end()

    Args:
        scale (float): font scale

    .. wraps::
        void SetWindowFontScale(float scale)
    '''

def set_next_window_collapsed(collapsed: bool,
                              condition: Condition = ALWAYS) -> None:
    '''
    Set next window collapsed state.

    .. visual-example::
        :auto_layout:
        :height: 60
        :width: 400

        imgui.set_next_window_collapsed(True)
        imgui.begin('Example: collapsed window')
        imgui.end()


    Args:
        collapsed (bool): set to True if window has to be collapsed.
        condition (:ref:`condition flag <condition-options>`): defines on
            which condition value should be set. Defaults to
            :any:`imgui.ALWAYS`.

    .. wraps::
         void SetNextWindowCollapsed(
             bool collapsed, ImGuiCond cond = 0
         )

    '''

def set_next_window_focus() -> None:
    '''
    Set next window to be focused (most front).

    .. wraps::
        void SetNextWindowFocus()
    '''

def set_next_window_bg_alpha(alpha: float) -> None:
    '''
    Set next window background color alpha. Helper to easily modify ImGuiCol_WindowBg/ChildBg/PopupBg.

    .. wraps::
        void SetNextWindowBgAlpha(float)
    '''

def get_window_draw_list() -> _DrawList:
    '''
    Get the draw list associated with the window, to append your own drawing primitives

    It may be useful if you want to do your own drawing via the :class:`_DrawList`
    API.

    .. visual-example::
        :auto_layout:
        :height: 100
        :width: 200
        :click: 10 10


        pos_x = 10
        pos_y = 10
        sz = 20

        draw_list = imgui.get_window_draw_list()

        for i in range(0, imgui.COLOR_COUNT):
            name = imgui.get_style_color_name(i);
            draw_list.add_rect_filled(pos_x, pos_y, pos_x+sz, pos_y+sz, imgui.get_color_u32_idx(i));
            imgui.dummy(sz, sz);
            imgui.same_line();

        rgba_color = imgui.get_color_u32_rgba(1, 1, 0, 1);
        draw_list.add_rect_filled(pos_x, pos_y, pos_x+sz, pos_y+sz, rgba_color);


    Returns:
        ImDrawList*

    .. wraps::
        ImDrawList* GetWindowDrawList()
    '''

def get_overlay_draw_list() -> _DrawList:
    '''
    Get a special draw list that will be drawn last (over all windows).

    Useful for drawing overlays.

    Returns:
        ImDrawList*

    .. wraps::
        ImDrawList* GetWindowDrawList()
    '''

def get_window_position() -> Vec2:
    '''
    Get current window position.

    It may be useful if you want to do your own drawing via the DrawList
    api.

    Returns:
        Vec2: two-tuple of window coordinates in screen space.

    .. wraps::
        ImVec2 GetWindowPos()
    '''

def get_window_size() -> Vec2:
    '''
    Get current window size.

    Returns:
        Vec2: two-tuple of window dimensions.

    .. wraps::
        ImVec2 GetWindowSize()
    '''

def get_window_width() -> float:
    '''
    Get current window width.

    Returns:
        float: width of current window.

    .. wraps::
        float GetWindowWidth()
    '''

def get_window_height() -> float:
    '''
    Get current window height.

    Returns:
        float: height of current window.

    .. wraps::
        float GetWindowHeight()
    '''

def set_next_window_position(x: float,
                             y: float,
                             condition: Condition = ALWAYS,
                             pivot_x: float = 0.0,
                             pivot_y: float = 0.0) -> None:
    '''
    Set next window position.

    Call before :func:`begin()`.

    Args:
        x (float): x window coordinate
        y (float): y window coordinate
        condition (:ref:`condition flag <condition-options>`): defines on which
            condition value should be set. Defaults to :any:`imgui.ALWAYS`.
        pivot_x (float): pivot x window coordinate
        pivot_y (float): pivot y window coordinate

    .. visual-example::
        :title: window positioning
        :height: 50

        imgui.set_next_window_size(20, 20)

        for index in range(5):
            imgui.set_next_window_position(index * 40, 5)
            imgui.begin(str(index))
            imgui.end()

    .. wraps::
        void SetNextWindowPos(
            const ImVec2& pos,
            ImGuiCond cond = 0,
            const ImVec2& pivot = ImVec2(0,0)
        )
    '''

def set_next_window_size(width: float,
                         height: float,
                         condition: Condition = ALWAYS) -> None:
    '''
    Set next window size.

    Call before :func:`begin()`.

    Args:
        width (float): window width. Value 0.0 enables autofit.
        height (float): window height. Value 0.0 enables autofit.
        condition (:ref:`condition flag <condition-options>`): defines on which
            condition value should be set. Defaults to :any:`imgui.ALWAYS`.

    .. visual-example::
        :title: window sizing
        :height: 200

        imgui.set_next_window_position(io.display_size.x * 0.5, io.display_size.y * 0.5, 1, pivot_x = 0.5, pivot_y = 0.5)

        imgui.set_next_window_size(80, 180)
        imgui.begin('High')
        imgui.end()


    .. wraps::
        void SetNextWindowSize(
            const ImVec2& size, ImGuiCond cond = 0
        )
    '''

def set_next_window_size_constraints(size_min: tuple[float, float],
                                     size_max: tuple[float, float],
                                     callback: _t.Callable[[_ImGuiSizeCallbackData], None] | None = None,
                                     user_data: _t.Any = None) -> None:
    '''
    Set next window size limits. use -1,-1 on either X/Y axis to preserve the current size.
    Sizes will be rounded down.

    Call before :func:`begin()`.

    Args:
        size_min (tuple): Minimum window size, use -1 to conserve current size
        size_max (tuple): Maximum window size, use -1 to conserve current size
        callback (callable): a callable.
            Callable takes an imgui._ImGuiSizeCallbackData object as argument
            Callable should return None
        user_data: Any data that the user want to use in the callback.

    .. visual-example::
        :title: Window size constraints
        :height: 200

        imgui.set_next_window_size_constraints((175,50), (200, 100))
        imgui.begin('Constrained Window')
        imgui.text('...')
        imgui.end()

    .. wraps::
        void SetNextWindowSizeConstraints(
            const ImVec2& size_min,
            const ImVec2& size_max,
            ImGuiSizeCallback custom_callback = NULL,
            void* custom_callback_user_data = NULL
        )
    '''

def set_next_window_content_size(width: float, height: float) -> None:
    '''
    Set content size of the next window. Show scrollbars
    if content doesn't fit in the window

    Call before :func:`begin()`.

    Args:
        width(float): width of the content area
        height(float): height of the content area

    .. visual-example::
        :title: Content Size Demo
        :height: 30

        imgui.set_window_size(20,20)
        imgui.set_next_window_content_size(100,100)

        imgui.begin('Window', True)
        imgui.text('Some example text')
        imgui.end()

    .. wraps::
        void SetNextWindowContentSize(
            const ImVec2& size
        )
    '''

def set_window_position(x: float,
                        y: float,
                        condition: Condition = ALWAYS) -> None:
    '''
    Set the size of the current window

    Call inside: func: 'begin()'

    Args:
        x(float): position on the x axis
        y(float): position on the y axis
        condition (:ref:`condition flag <condition-options>`): defines on which
            condition value should be set. Defaults to :any:`imgui.ALWAYS`.

    .. visual-example::
        :title: Window Size Demo
        :height: 200

        imgui.begin('Window 1')
        imgui.set_window_position(20,20)
        imgui.end()

        imgui.begin('Window 2')
        imgui.set_window_position(20,50)
        imgui.end()

    .. wraps::
        void SetWindowPos(
            const ImVec2& pos,
            ImGuiCond cond
        )
    '''

def set_window_position_labeled(label: str,
                                x: float,
                                y: float,
                                condition: Condition = ALWAYS) -> None:
    '''
    Set the size of the window with label

    Args:
        label(str): name of the window to be resized
        x(float): position on the x axis
        y(float): position on the y axis
        condition (:ref:`condition flag <condition-options>`): defines on which
            condition value should be set. Defaults to :any:`imgui.ALWAYS`.

    .. visual-example::
        :title: Window Size Demo
        :height: 200

        imgui.set_window_position_labeled('Window 1', 20, 50)
        imgui.set_window_position_labeled('Window 2', 20, 100)

        imgui.begin('Window 1')
        imgui.end()

        imgui.begin('Window 2')
        imgui.end()

    .. wraps::
        void SetWindowPos(
            const char* name,
            const ImVec2& pos,
            ImGuiCond cond
        )

    '''

def set_window_collapsed(collapsed: bool,
                         condition: Condition = ALWAYS) -> None:
    '''
    Set the current window to be collapsed

    Call inside: func: 'begin()'

    Args:
        collapsed(bool): set boolean for collapsing the window. Set True for closed
        condition (:ref:`condition flag <condition-options>`): defines on which
            condition value should be set. Defaults to :any:`imgui.ALWAYS`.

    .. visual-example::
        :title: Window Collapsed Demo
        :height: 200

        imgui.begin('Window 1')
        imgui.set_window_collapsed(True)
        imgui.end()

    .. wraps::
        void SetWindowCollapsed(
            bool collapsed,
            ImGuiCond cond
        )
    '''

def set_window_collapsed_labeled(label: str,
                                 collapsed: bool,
                                 condition: Condition = ALWAYS) -> None:
    '''
    Set window with label to collapse

    Args:
        label(string): name of the window
        collapsed(bool): set boolean for collapsing the window. Set True for closed
        condition (:ref:`condition flag <condition-options>`): defines on which
            condition value should be set. Defaults to :any:`imgui.ALWAYS`.

    .. visual-example::
        :title: Window Collapsed Demo
        :height: 200

        imgui.set_window_collapsed_labeled('Window 1', True)
        imgui.begin('Window 1')
        imgui.end()

    .. wraps::
        void SetWindowCollapsed(
            const char* name,
            bool collapsed,
            ImGuiCond cond
        )
    '''

def is_window_collapsed() -> bool:
    '''
    Check if current window is collapsed.

    Returns:
        bool: True if window is collapsed
    '''

def tree_node(text: str, flags: TreeNodeFlags = TREE_NODE_NONE) -> bool:
    '''
    Draw a tree node.

    Returns 'true' if the node is drawn, call :func:`tree_pop()` to finish.

    .. visual-example::
        :auto_layout:
        :height: 100
        :width: 200
        :click: 80 40

        imgui.begin('Example: tree node')
        if imgui.tree_node('Expand me!', imgui.TREE_NODE_DEFAULT_OPEN):
            imgui.text('Lorem Ipsum')
            imgui.tree_pop()
        imgui.end()

    Args:
        text (str): Tree node label
        flags: TreeNode flags. See:
            :ref:`list of available flags <treenode-flag-options>`.

    Returns:
        bool: True if tree node is displayed (opened).

    .. wraps::
        bool TreeNode(const char* label)
        bool TreeNodeEx(const char* label, ImGuiTreeNodeFlags flags = 0)
    '''

def tree_pop() -> None:
    '''
    Called to clear the tree nodes stack and return back the identation.

    For a tree example see :func:`tree_node()`.
    Same as calls to :func:`unindent()` and :func:`pop_id()`.

    .. wraps::
        void TreePop()
    '''

def get_tree_node_to_label_spacing() -> float:
    '''
    Horizontal distance preceding label when using ``tree_node*()``
    or ``bullet() == (g.FontSize + style.FramePadding.x*2)`` for a
    regular unframed TreeNode

    Returns:
        float: spacing

    .. visual-example::
        :auto_layout:
        :height: 100
        :width: 200

        imgui.begin('TreeNode')
        imgui.text('<- 0px offset here')
        if imgui.tree_node('Expand me!', imgui.TREE_NODE_DEFAULT_OPEN):
            imgui.text('<- %.2fpx offset here' % imgui.get_tree_node_to_label_spacing())
            imgui.tree_pop()
        imgui.end()

    .. wraps::
        float GetTreeNodeToLabelSpacing()
    '''

def collapsing_header(text: str,
                      visible: bool | None = None,
                      flags: TreeNodeFlags = TREE_NODE_NONE) -> bool:
    '''
    Collapsable/Expandable header view.

    Returns 'true' if the header is open. Doesn't indent or push to stack,
    so no need to call any pop function.

    .. visual-example::
        :auto_layout:
        :height: 100
        :width: 200
        :click: 80 40

        visible = True

        imgui.begin('Example: collapsing header')
        expanded, visible = imgui.collapsing_header('Expand me!', visible)

        if expanded:
            imgui.text('Now you see me!')
        imgui.end()

    Args:
        text (str): Tree node label
        visible (bool or None): Force visibility of a header. If set to True
            shows additional (X) close button. If set to False header is not
            visible at all. If set to None header is always visible and close
            button is not displayed.
        flags: TreeNode flags. See:
            :ref:`list of available flags <treenode-flag-options>`.

    Returns:
        tuple: a ``(expanded, visible)`` two-tuple indicating if item was
        expanded and whether the header is visible or not (only if ``visible``
        input argument is True/False).

    .. wraps::
        bool CollapsingHeader(const char* label, ImGuiTreeNodeFlags flags = 0)

        bool CollapsingHeader(
            const char* label,
            bool* p_visible,
            ImGuiTreeNodeFlags flags = 0
        )
    '''

def set_next_item_open(is_open: bool,
                       condition: Condition = NONE) -> None:
    '''
    Set next TreeNode/CollapsingHeader open state.

    Args:
        is_open (bool):
        condition (:ref:`condition flag <condition-options>`): defines on which
            condition value should be set. Defaults to :any:`imgui.NONE`.

    .. wraps::
        void SetNextItemOpen(bool is_open, ImGuiCond cond = 0)
    '''

def selectable(label: str,
               selected: bool = False,
               flags: SelectableFlags = SELECTABLE_NONE,
               width: float = 0.0,
               height: float = 0.0) -> bool:
    '''
    Selectable text. Returns 'true' if the item is pressed.

    Width of 0.0 will use the available width in the parent container.
    Height of 0.0 will use the available height in the parent container.

    .. visual-example::
        :auto_layout:
        :height: 200
        :width: 200
        :click: 80 40

        selected = [False, False]
        imgui.begin('Example: selectable')
        _, selected[0] = imgui.selectable(
            '1. I am selectable', selected[0]
        )
        _, selected[1] = imgui.selectable(
            '2. I am selectable too', selected[1]
        )
        imgui.text('3. I am not selectable')
        imgui.end()

    Args:
        label (str): The label.
        selected (bool): defines if item is selected or not.
        flags: Selectable flags. See:
            :ref:`list of available flags <selectable-flag-options>`.
        width (float): button width.
        height (float): button height.

    Returns:
        tuple: a ``(opened, selected)`` two-tuple indicating if item was
        clicked by the user and the current state of item.

    .. wraps::
        bool Selectable(
            const char* label,
            bool selected = false,
            ImGuiSelectableFlags flags = 0,
            const ImVec2& size = ImVec2(0,0)
        )

        bool Selectable(
            const char* label,
            bool* selected,
            ImGuiSelectableFlags flags = 0,
            const ImVec2& size = ImVec2(0,0)
        )
    '''

def listbox(label: str,
            current: int,
            items: _t.Iterable[str],
            height_in_items: int = -1) -> tuple[bool, int]:
    '''
    Show listbox widget.

    .. visual-example::
        :auto_layout:
        :height: 100
        :width: 200

        current = 2
        imgui.begin('Example: listbox widget')

        clicked, current = imgui.listbox(
            'List', current, ['first', 'second', 'third']
        )

        imgui.end()

    Args:
        label (str): The label.
        current (int): index of selected item.
        items (list): list of string labels for items.
        height_in_items (int): height of dropdown in items. Defaults to -1
            (autosized).

    Returns:
        tuple: a ``(changed, current)`` tuple indicating change of selection
        and current index of selected item.

    .. wraps::
        bool ListBox(
            const char* label,
            int* current_item,
            const char* items[],
            int items_count,
            int height_in_items = -1
        )

    '''

def begin_list_box(label: str,
                   width: float = 0.0,
                   height: float = 0.0) -> _BeginEndListBox:
    '''
    Open a framed scrolling region.

    For use if you want to reimplement :func:`listbox` with custom data
    or interactions. You need to call :func:`end_list_box` at the end
    if ``opened`` is True, or use ``with`` to do so automatically.

    .. visual-example::
        :auto_layout:
        :height: 200
        :width: 200
        :click: 80 40

        with imgui.begin('Example: custom listbox'):
            with imgui.begin_list_box('List', 200, 100) as list_box:
                if list_box.opened:
                    imgui.selectable('Selected', True)
                    imgui.selectable('Not Selected', False)

    Example::
        imgui.begin('Example: custom listbox')

        if imgui.begin_list_box('List', 200, 100).opened:

            imgui.selectable('Selected', True)
            imgui.selectable('Not Selected', False)

            imgui.end_list_box()

        imgui.end()

    Args:
        label (str): The label.
        width (float): Button width. w > 0.0f: custom; w < 0.0f or -FLT_MIN: right-align; w = 0.0f (default): use current ItemWidth
        height (float): Button height. h > 0.0f: custom; h < 0.0f or -FLT_MIN: bottom-align; h = 0.0f (default): arbitrary default height which can fit ~7 items

    Returns:
        _BeginEndListBox: Use ``opened`` bool attribute to tell if the item is opened or closed.
        Only call :func:`end_list_box` if ``opened`` is True.
        Use with ``with`` to automatically call :func:`end_list_box` if necessary when the block ends.

    .. wraps::
        bool BeginListBox(
            const char* label,
            const ImVec2& size = ImVec2(0,0)
        )

    '''

def listbox_header(label: str,
                   width: float = 0.0,
                   height: float = 0.0) -> bool:
    '''
    *Obsoleted in imgui v1.81 from February 2021, refer to :func:`begin_list_box()`*

    For use if you want to reimplement :func:`listbox()` with custom data
    or interactions. You need to call :func:`listbox_footer()` at the end.

    Args:
        label (str): The label.
        width (float): button width.
        height (float): button height.

    Returns:
        opened (bool): If the item is opened or closed.

    .. wraps::
        bool ListBoxHeader(
            const char* label,
            const ImVec2& size = ImVec2(0,0)
        )
    '''

def end_list_box() -> None:
    '''
    Closing the listbox, previously opened by :func:`begin_list_box()`.
    Only call if ``begin_list_box().opened`` is True.

    See :func:`begin_list_box()` for usage example.

    .. wraps::
        void EndListBox()
    '''

def listbox_footer() -> None:
    '''
    *Obsoleted in imgui v1.81 from February 2021, refer to :func:`end_list_box()`*

    Closing the listbox, previously opened by :func:`listbox_header()`.

    See :func:`listbox_header()` for usage example.

    .. wraps::
        void ListBoxFooter()
    '''

def set_tooltip(text: str) -> None:
    '''
    Set tooltip under mouse-cursor.

    Usually used with :func:`is_item_hovered()`.
    For a complex tooltip window see :func:`begin_tooltip()`.

    .. visual-example::
        :auto_layout:
        :height: 100
        :width: 200
        :click: 80 40

        imgui.begin('Example: tooltip')
        imgui.button('Hover me!')
        if imgui.is_item_hovered():
            imgui.set_tooltip('Please?')
        imgui.end()

    .. wraps::
        void SetTooltip(const char* fmt, ...)
    '''

def begin_tooltip() -> _BeginEndTooltip:
    '''
    Use to create full-featured tooltip windows that aren't just text.

    .. visual-example::
        :auto_layout:
        :width: 600
        :height: 200
        :click: 80 40

        with imgui.begin('Example: tooltip'):
            imgui.button('Click me!')
            if imgui.is_item_hovered():
                with imgui.begin_tooltip():
                    imgui.text('This button is clickable.')
                    imgui.text('This button has full window tooltip.')
                    texture_id = imgui.get_io().fonts.texture_id
                    imgui.image(texture_id, 512, 64, border_color=(1, 0, 0, 1))

    .. wraps::
        void BeginTooltip()

    Returns:
        _BeginEndTooltip: Use with ``with`` to automatically call :func:`end_tooltip` when the block ends.


    '''

def end_tooltip() -> None:
    '''
    End tooltip window.

    See :func:`begin_tooltip()` for full usage example.

    .. wraps::
        void EndTooltip()
    '''

def begin_main_menu_bar() -> _BeginEndMainMenuBar:
    '''
    Create new full-screen menu bar.

    Use with ``with`` to automatically call :func:`end_main_menu_bar` if necessary.
    Otherwise, only call :func:`end_main_menu_bar` if ``opened`` is True.

    .. visual-example::
        :auto_layout:
        :height: 100
        :width: 200
        :click: 10 10

        with imgui.begin_main_menu_bar() as main_menu_bar:
            if main_menu_bar.opened:
                # first menu dropdown
                with imgui.begin_menu('File', True) as file_menu:
                    if file_menu.opened:
                        imgui.menu_item('New', 'Ctrl+N', False, True)
                        imgui.menu_item('Open ...', 'Ctrl+O', False, True)

                        # submenu
                        with imgui.begin_menu('Open Recent', True) as open_recent_menu:
                            if open_recent_menu.opened:
                                imgui.menu_item('doc.txt', None, False, True)

    Example::

        if imgui.begin_main_menu_bar().opened:
            # first menu dropdown
            if imgui.begin_menu('File', True).opened:
                imgui.menu_item('New', 'Ctrl+N', False, True)
                imgui.menu_item('Open ...', 'Ctrl+O', False, True)

                # submenu
                if imgui.begin_menu('Open Recent', True).opened:
                    imgui.menu_item('doc.txt', None, False, True)
                    imgui.end_menu()

                imgui.end_menu()

            imgui.end_main_menu_bar()

    Returns:
        _BeginEndMainMenuBar: Use ``opened`` to tell if main menu bar is displayed (opened).
        Only call :func:`end_main_menu_bar` if ``opened`` is True.
        Use with ``with`` to automatically call :func:`end_main_menu_bar` if necessary when the block ends.

    .. wraps::
        bool BeginMainMenuBar()
    '''

def end_main_menu_bar() -> None:
    '''
    Close main menu bar context.

    Only call this function if the ``end_main_menu_bar().opened`` is True.

    For practical example how to use this function see documentation of
    :func:`begin_main_menu_bar`.

    .. wraps::
        bool EndMainMenuBar()
    '''

def begin_menu_bar() -> _BeginEndMenuBar:
    '''
    Append new menu menu bar to current window.

    This function is different from :func:`begin_main_menu_bar`, as this is
    child-window specific. Use with ``with`` to automatically call
    :func:`end_menu_bar` if necessary.
    Otherwise, only call :func:`end_menu_bar` if ``opened`` is True.

    **Note:** this requires :ref:`WINDOW_MENU_BAR <window-flag-options>` flag
    to be set for the current window. Without this flag set the
    ``begin_menu_bar()`` function will always return ``False``.

    .. visual-example::
        :auto_layout:
        :click: 25 30

        flags = imgui.WINDOW_MENU_BAR

        with imgui.begin('Child Window - File Browser', flags=flags):
            with imgui.begin_menu_bar() as menu_bar:
                if menu_bar.opened:
                    with imgui.begin_menu('File') as file_menu:
                        if file_menu.opened:
                            imgui.menu_item('Close')

    Example::

        flags = imgui.WINDOW_MENU_BAR

        imgui.begin('Child Window - File Browser', flags=flags)

        if imgui.begin_menu_bar().opened:
            if imgui.begin_menu('File').opened:
                imgui.menu_item('Close')
                imgui.end_menu()

            imgui.end_menu_bar()

        imgui.end()

    Returns:
        _BeginEndMenuBar: Use ``opened`` to tell if menu bar is displayed (opened).
        Only call :func:`end_menu_bar` if ``opened`` is True.
        Use with ``with`` to automatically call :func:`end_menu_bar` if necessary when the block ends.

    .. wraps::
        bool BeginMenuBar()
    '''

def end_menu_bar() -> None:
    '''
    Close menu bar context.

    Only call this function if ``begin_menu_bar().opened`` is True.

    For practical example how to use this function see documentation of
    :func:`begin_menu_bar`.

    .. wraps::
        void EndMenuBar()
    '''

def begin_menu(label: str, enabled: bool = True) -> _BeginEndMenu:
    '''
    Create new expandable menu in current menu bar.

    Use with ``with`` to automatically call :func:`end_menu` if necessary.
    Otherwise, only call :func:`end_menu` if ``opened`` is True.

    For practical example how to use this function, please see documentation
    of :func:`begin_main_menu_bar` or :func:`begin_menu_bar`.

    Args:
        label (str): label of the menu.
        enabled (bool): define if menu is enabled or disabled.

    Returns:
        _BeginEndMenu: Use ``opened`` to tell if the menu is displayed (opened).
        Only call :func:`end_menu` if ``opened`` is True.
        Use with ``with`` to automatically call :func:`end_menu` if necessary when the block ends.

    .. wraps::
        bool BeginMenu(
            const char* label,
            bool enabled
        )
    '''

def end_menu() -> None:
    '''
    Close menu context.

    Only call this function if ``begin_menu().opened`` returns True.

    For practical example how to use this function, please see documentation
    of :func:`begin_main_menu_bar` or :func:`begin_menu_bar`.

    .. wraps::
        void EndMenu()
    '''

def menu_item(label: str,
              shortcut: str | None = None,
              selected: bool = False,
              enabled: bool = True) -> tuple[bool, bool]:
    '''
    Create a menu item.

    Item shortcuts are displayed for convenience but not processed by ImGui at
    the moment. Using ``selected`` argument it is possible to show and trigger
    a check mark next to the menu item label.

    For practical example how to use this function, please see documentation
    of :func:`begin_main_menu_bar` or :func:`begin_menu_bar`.

    Args:
        label (str): label of the menu item.
        shortcut (str): shortcut text of the menu item.
        selected (bool): define if menu item is selected.
        enabled (bool): define if menu item is enabled or disabled.

    Returns:
        tuple: a ``(clicked, state)`` two-tuple indicating if item was
        clicked by the user and the current state of item (visibility of
        the check mark).

    .. wraps::
        MenuItem(
            const char* label,
            const char* shortcut,
            bool* p_selected,
            bool enabled = true
        )
    '''

def open_popup(label: str, flags: PopupFlags = POPUP_NONE) -> None:
    '''
    Open a popup window.

    Marks a popup window as open. Popups are closed when user click outside,
    or activate a pressable item, or :func:`close_current_popup()` is
    called within a :func:`begin_popup()`/:func:`end_popup()` block.
    Popup identifiers are relative to the current ID-stack
    (so :func:`open_popup` and :func:`begin_popup` needs to be at
    the same level).

    .. visual-example::
        :title: Simple popup window
        :height: 100
        :width: 220
        :auto_layout:

        imgui.begin('Example: simple popup')
        if imgui.button('Toggle..'):
            imgui.open_popup('toggle')
        if imgui.begin_popup('toggle'):
            if imgui.begin_menu('Sub-menu'):
                _, _ = imgui.menu_item('Click me')
                imgui.end_menu()
            imgui.end_popup()
        imgui.end()

    Args:
        label (str): label of the modal window.

    .. wraps::
        void OpenPopup(
            const char* str_id,
            ImGuiPopupFlags popup_flags = 0
        )
    '''

def open_popup_on_item_click(label: str | None = None,
                             popup_flags: PopupFlags = POPUP_MOUSE_BUTTON_RIGHT) -> None:
    '''
    Helper to open popup when clicked on last item.
    (note: actually triggers on the mouse _released_ event to be consistent with popup behaviors)

    Args:
        label (str): label of the modal window
        flags: ImGuiWindowFlags

    .. wraps::
        void OpenPopupOnItemClick(const char* str_id = NULL, ImGuiPopupFlags popup_flags = 1)
    '''

def begin_popup(label: str, flags: WindowFlags = WINDOW_NONE) -> _BeginEndPopup:
    '''
    Open a popup window.

    The attribute ``opened`` is True if the popup is open and you can start outputting
    content to it.
    Use with ``with`` to automatically call :func:`end_popup` if necessary.
    Otherwise, only call :func:`end_popup` if ``opened`` is True.

    .. visual-example::
        :title: Simple popup window
        :height: 100
        :width: 220
        :auto_layout:

        with imgui.begin('Example: simple popup'):
            if imgui.button('select'):
                imgui.open_popup('select-popup')

            imgui.same_line()

            with imgui.begin_popup('select-popup') as select_popup:
                if select_popup.opened:
                    imgui.text('Select one')
                    imgui.separator()
                    imgui.selectable('One')
                    imgui.selectable('Two')
                    imgui.selectable('Three')

    Example::

        imgui.begin('Example: simple popup')

        if imgui.button('select'):
            imgui.open_popup('select-popup')

        imgui.same_line()

        if imgui.begin_popup('select-popup'):
            imgui.text('Select one')
            imgui.separator()
            imgui.selectable('One')
            imgui.selectable('Two')
            imgui.selectable('Three')
            imgui.end_popup()

        imgui.end()

    Args:
        label (str): label of the modal window.

    Returns:
        _BeginEndPopup: Use ``opened`` bool attribute to tell if the popup is opened.
        Only call :func:`end_popup` if ``opened`` is True.
        Use with ``with`` to automatically call :func:`end_popup` if necessary when the block ends.

    .. wraps::
        bool BeginPopup(
            const char* str_id,
            ImGuiWindowFlags flags = 0
        )
    '''

def begin_popup_modal(title: str,
                      visible: bool | None = None,
                      flags: WindowFlags = WINDOW_NONE) -> _BeginEndPopupModal:
    '''
    Begin pouring popup contents.

    Differs from :func:`begin_popup` with its modality - meaning it
    opens up on top of every other window.

    The attribute ``opened`` is True if the popup is open and you can start outputting
    content to it.
    Use with ``with`` to automatically call :func:`end_popup` if necessary.
    Otherwise, only call :func:`end_popup` if ``opened`` is True.

    .. visual-example::
        :title: Simple popup window
        :height: 100
        :width: 220
        :auto_layout:

        with imgui.begin('Example: simple popup modal'):
            if imgui.button('Open Modal popup'):
                imgui.open_popup('select-popup')

            imgui.same_line()

            with imgui.begin_popup_modal('select-popup') as select_popup:
                if select_popup.opened:
                    imgui.text('Select an option:')
                    imgui.separator()
                    imgui.selectable('One')
                    imgui.selectable('Two')
                    imgui.selectable('Three')

    Example::

        imgui.begin('Example: simple popup modal')

        if imgui.button('Open Modal popup'):
            imgui.open_popup('select-popup')

        imgui.same_line()

        if imgui.begin_popup_modal('select-popup').opened:
            imgui.text('Select an option:')
            imgui.separator()
            imgui.selectable('One')
            imgui.selectable('Two')
            imgui.selectable('Three')
            imgui.end_popup()

        imgui.end()

    Args:
        title (str): label of the modal window.
        visible (bool): define if popup is visible or not.
        flags: Window flags. See:
            :ref:`list of available flags <window-flag-options>`.

    Returns:
        _BeginEndPopupModal: ``(opened, visible)`` struct of bools.
        Only call :func:`end_popup` if ``opened`` is True.
        Use with ``with`` to automatically call :func:`end_popup` if necessary when the block ends.
        The ``opened`` attribute can be False when the popup is completely clipped
        (e.g. zero size display).

    .. wraps::
        bool BeginPopupModal(
            const char* name,
            bool* p_open = NULL,
            ImGuiWindowFlags extra_flags = 0
        )
    '''

def begin_popup_context_item(label: str | None = None,
                             mouse_button: PopupFlags = POPUP_MOUSE_BUTTON_RIGHT) -> _BeginEndPopup:
    '''
    This is a helper function to handle the most simple case of associating
    one named popup to one given widget.

    .. visual-example::
        :title: Popup context view
        :height: 100
        :width: 200
        :auto_layout:
        :click: 40 40

        with imgui.begin('Example: popup context view'):
            imgui.text('Right-click to set value.')
            with imgui.begin_popup_context_item('Item Context Menu', mouse_button=0) as popup:
                if popup.opened:
                    imgui.selectable('Set to Zero')

    Example::

        imgui.begin('Example: popup context view')
        imgui.text('Right-click to set value.')
        if imgui.begin_popup_context_item('Item Context Menu', mouse_button=0):
            imgui.selectable('Set to Zero')
            imgui.end_popup()
        imgui.end()

    Args:
        label (str): label of item.
        mouse_button: ImGuiPopupFlags

    Returns:
        _BeginEndPopup: Use ``opened`` bool attribute to tell if the popup is opened.
        Only call :func:`end_popup` if ``opened`` is True.
        Use with ``with`` to automatically call :func:`end_popup` if necessary when the block ends.

    .. wraps::
        bool BeginPopupContextItem(
            const char* str_id = NULL,
            int mouse_button = 1
        )
    '''

def begin_popup_context_window(label: str | None = None,
                               popup_flags: PopupFlags = POPUP_MOUSE_BUTTON_RIGHT,
                               also_over_items: bool = True) -> _BeginEndPopup:
    '''
    Helper function to open and begin popup when clicked on current window.

    As all popup functions it should end with :func:`end_popup`.

    .. visual-example::
        :title: Popup context view
        :height: 100
        :width: 200
        :auto_layout:
        :click: 40 40

        with imgui.begin('Example: popup context window'):
            with imgui.begin_popup_context_window(popup_flags=imgui.POPUP_NONE) as context_window:
                if context_window.opened:
                    imgui.selectable('Clear')

    Example::

        imgui.begin('Example: popup context window')
        if imgui.begin_popup_context_window(popup_flags=imgui.POPUP_NONE):
            imgui.selectable('Clear')
            imgui.end_popup()
        imgui.end()

    Args:
        label (str): label of the window
        popup_flags: ImGuiPopupFlags
        also_over_items (bool): display on top of widget. OBSOLETED in ImGui 1.77 (from June 2020)

    Returns:
        _BeginEndPopup: Use ``opened`` bool attribute to tell if the context window is opened.
        Only call :func:`end_popup` if ``opened`` is True.
        Use with ``with`` to automatically call :func:`end_popup` if necessary when the block ends.

    .. wraps::
        bool BeginPopupContextWindow(
            const char* str_id = NULL,
            ImGuiPopupFlags popup_flags = 1
        )
    '''

def begin_popup_context_void(label: str | None = None,
                             popup_flags: PopupFlags = POPUP_MOUSE_BUTTON_RIGHT) -> _BeginEndPopup:
    '''
    Open+begin popup when clicked in void (where there are no windows).

    Args:
        label (str): label of the window
        popup_flags: ImGuiPopupFlags

    Returns:
        _BeginEndPopup: Use ``opened`` bool attribute to tell if the context window is opened.
        Only call :func:`end_popup` if ``opened`` is True.
        Use with ``with`` to automatically call :func:`end_popup` if necessary when the block ends.

    .. wraps::
        bool BeginPopupContextVoid(const char* str_id = NULL, ImGuiPopupFlags popup_flags = 1)
    '''

def is_popup_open(label: str, flags: PopupFlags = POPUP_NONE) -> bool:
    '''
    Popups: test function

    * ``is_popup_open()`` with POPUP_ANY_POPUP_ID: return true if any popup is open at the current BeginPopup() level of the popup stack.
    * ``is_popup_open()`` with POPUP_ANY_POPUP_ID + POPUP_ANY_POPUP_LEVEL: return true if any popup is open.

    Returns:
        bool: True if the popup is open at the current ``begin_popup()`` level of the popup stack.

    .. wraps::
        bool IsPopupOpen(const char* str_id, ImGuiPopupFlags flags = 0)
    '''

def end_popup() -> None:
    '''
    End a popup window.

    Should be called after each XYZPopupXYZ function.
    Only call this function if ``begin_popup_XYZ().opened`` is True.

    For practical example how to use this function, please see documentation
    of :func:`open_popup`.

    .. wraps::
        void EndPopup()
    '''

def close_current_popup() -> None:
    '''
    Close the current popup window begin-ed directly above this call.
    Clicking on a :func:`menu_item()` or :func:`selectable()` automatically
    close the current popup.

    For practical example how to use this function, please see documentation
    of :func:`open_popup`.

    .. wraps::
        void CloseCurrentPopup()
    '''

def begin_table(label: str,
                column: int,
                flags: TableFlags = TABLE_NONE,
                outer_size_width: float = 0.0,
                outer_size_height: float = 0.0,
                inner_width: float = 0.0) -> _BeginEndTable:
    '''

    Returns:
        _BeginEndPopup: Use ``opened`` bool attribute to tell if the table is opened.
        Only call :func:`end_table` if ``opened`` is True.
        Use with ``with`` to automatically call :func:`end_table` if necessary when the block ends.

    .. wraps::
        bool BeginTable(
            const char* str_id,
            int column,
            ImGuiTableFlags flags = 0,
            const ImVec2& outer_size = ImVec2(0.0f, 0.0f),
            float inner_width = 0.0f
        )
    '''

def end_table() -> None:
    '''
    End a previously opened table.
    Only call this function if ``begin_table().opened`` is True.

    .. wraps::
        void EndTable()
    '''

def table_next_row(row_flags: TableRowFlags = TABLE_ROW_NONE, min_row_height: float = 0.0) -> None:
    '''

    .. wraps::
        void TableNextRow(
            ImGuiTableRowFlags row_flags = 0,
            float min_row_height = 0.0f
        )
    '''

def table_next_column() -> bool:
    '''

    .. wraps::
        bool TableNextColumn()
    '''

def table_set_column_index(column_n: int) -> bool:
    '''

    .. wraps::
        bool TableSetColumnIndex(int column_n)
    '''

def table_setup_column(label: str,
                       flags: TableColumnFlags = TABLE_COLUMN_NONE,
                       init_width_or_weight: float = 0.0,
                       user_id: int = 0) -> None:
    '''

    .. wraps::
        void TableSetupColumn(
            const char* label,
            ImGuiTableColumnFlags flags = 0,
            float init_width_or_weight = 0.0f,
            ImU32 user_id  = 0
        )
    '''

def table_setup_scroll_freeze(cols: int, rows: int) -> None:
    '''

    .. wraps::
        void TableSetupScrollFreeze(int cols, int rows)
    '''

def table_headers_row() -> None:
    '''

    .. wraps::
        void TableHeadersRow()
    '''

def table_header(label: str) -> None:
    '''

    .. wraps::
        void TableHeader(const char* label)
    '''

def table_get_sort_specs() -> _ImGuiTableSortSpecs:
    '''

    .. wraps::
        ImGuiTableSortSpecs* TableGetSortSpecs()
    '''

def table_get_column_count() -> int:
    '''

    .. wraps::
        int TableGetColumnCount()
    '''

def table_get_column_index() -> int:
    '''

    .. wraps::
        int TableGetColumnIndex()
    '''

def table_get_row_index() -> int:
    '''

    .. wraps::
        int TableGetRowIndex()
    '''

def table_get_column_name(column_n: int = -1) -> str:
    '''

    .. wraps::
        const char* TableGetColumnName(
            int column_n  = -1
        )
    '''

def table_get_column_flags(column_n: int = -1) -> TableColumnFlags:
    '''

    .. wraps::
        ImGuiTableColumnFlags TableGetColumnFlags(
            int column_n = -1
        )
    '''

def table_set_background_color(target: int, color: int, column_n: int = -1) -> None:
    '''

    .. wraps::
        void TableSetBgColor(
            ImGuiTableBgTarget target,
            ImU32 color,
            int column_n  = -1
        )
    '''

def text(text: str) -> None:
    '''
    Add text to current widget stack.

    .. visual-example::
        :title: simple text widget
        :height: 80
        :auto_layout:

        imgui.begin('Example: simple text')
        imgui.text('Simple text')
        imgui.end()

    Args:
        text (str): text to display.

    .. wraps::
        Text(const char* fmt, ...)
    '''

def text_colored(text: str,
                 r: float,
                 g: float,
                 b: float,
                 a: float = 1.0) -> None:
    '''
    Add colored text to current widget stack.

    It is a shortcut for:

    .. code-block:: python

        imgui.push_style_color(imgui.COLOR_TEXT, r, g, b, a)
        imgui.text(text)
        imgui.pop_style_color()


    .. visual-example::
        :title: colored text widget
        :height: 100
        :auto_layout:

        imgui.begin('Example: colored text')
        imgui.text_colored('Colored text', 1, 0, 0)
        imgui.end()

    Args:
        text (str): text to display.
        r (float): red color intensity.
        g (float): green color intensity.
        b (float): blue color instensity.
        a (float): alpha intensity.

    .. wraps::
        TextColored(const ImVec4& col, const char* fmt, ...)
    '''

def text_disabled(text: str) -> None:
    '''
    Add disabled(grayed out) text to current widget stack.

    .. visual-example::
        :title: disabled text widget
        :height: 80
        :auto_layout:

        imgui.begin('Example: disabled text')
        imgui.text_disabled('Disabled text')
        imgui.end()

    Args:
        text (str): text to display.

    .. wraps::
        TextDisabled(const char*, ...)
    '''

def text_wrapped(text: str) -> None:
    '''
    Add wrappable text to current widget stack.

    .. visual-example::
        :title: Wrappable Text
        :height: 80
        :width: 40
        :auto_layout:

        imgui.begin('Text wrap')
        # Resize the window to see text wrapping
        imgui.text_wrapped('This text will wrap around.')
        imgui.end()

    Args:
        text (str): text to display

    .. wraps::
        TextWrapped(const char* fmt, ...)
    '''

def label_text(label: str, text: str) -> None:
    '''
    Display text+label aligned the same way as value+label widgets.

    .. visual-example::
        :auto_layout:
        :height: 80
        :width: 300

        imgui.begin('Example: text with label')
        imgui.label_text('my label', 'my text')
        imgui.end()

    Args:
        label (str): label to display.
        text (str): text to display.

    .. wraps::
        void LabelText(const char* label, const char* fmt, ...)
    '''

def text_unformatted(text: str) -> None:
    '''
    Big area text display - the size is defined by it's container.
    Recommended for long chunks of text.

    .. visual-example::
        :title: simple text widget
        :height: 100
        :width: 200
        :auto_layout:

        imgui.begin('Example: unformatted text')
        imgui.text_unformatted('Really ... long ... text')
        imgui.end()

    Args:
        text (str): text to display.

    .. wraps::
        TextUnformatted(const char* text, const char* text_end = NULL)
    '''

def bullet() -> None:
    '''
    Display a small circle and keep the cursor on the same line.

    .. advance cursor x position by ``get_tree_node_to_label_spacing()``,
       same distance that TreeNode() uses

    .. visual-example::
        :auto_layout:
        :height: 80

        imgui.begin('Example: bullets')

        for i in range(10):
            imgui.bullet()

        imgui.end()

    .. wraps::
        void Bullet()
    '''

def bullet_text(text: str) -> None:
    '''
    Display bullet and text.

    This is shortcut for:

    .. code-block:: python

        imgui.bullet()
        imgui.text(text)

    .. visual-example::
        :auto_layout:
        :height: 100

        imgui.begin('Example: bullet text')
        imgui.bullet_text('Bullet 1')
        imgui.bullet_text('Bullet 2')
        imgui.bullet_text('Bullet 3')
        imgui.end()

    Args:
        text (str): text to display.

    .. wraps::
        void BulletText(const char* fmt, ...)
    '''

def button(label: str, width: int = 0, height: int = 0) -> bool:
    '''
    Display button.

    .. visual-example::
        :auto_layout:
        :height: 100

        imgui.begin('Example: button')
        imgui.button('Button 1')
        imgui.button('Button 2')
        imgui.end()

    Args:
        label (str): button label.
        width (float): button width.
        height (float): button height.

    Returns:
        bool: True if clicked.

    .. wraps::
        bool Button(const char* label, const ImVec2& size = ImVec2(0,0))
    '''

def small_button(label: str) -> bool:
    '''
    Display small button (with 0 frame padding).

    .. visual-example::
        :auto_layout:
        :height: 100

        imgui.begin('Example: button')
        imgui.small_button('Button 1')
        imgui.small_button('Button 2')
        imgui.end()

    Args:
        label (str): button label.

    Returns:
        bool: True if clicked.

    .. wraps::
        bool SmallButton(const char* label)
    '''

def arrow_button(label: str, direction: int = DIRECTION_NONE) -> bool:
    '''
    Display an arrow button

    .. visual-example::
        :auto_layout:
        :height: 100

        imgui.begin('Arrow button')
        imgui.arrow_button('Button', imgui.DIRECTION_LEFT)
        imgui.end()

    Args:
        label (str): button label.
        direction = imgui direction constant

    Returns:
        bool: True if clicked.

    .. wraps::
        bool ArrowButton(const char*, ImGuiDir)
    '''

def invisible_button(identifier: str,
                     width: float,
                     height: float,
                     flags: ButtonFlags = BUTTON_NONE) -> bool:
    '''
    Create invisible button.

    Flexible button behavior without the visuals, frequently useful to build custom behaviors using the public api (along with IsItemActive, IsItemHovered, etc.)

    .. visual-example::
        :auto_layout:
        :height: 300
        :width: 300

        imgui.begin('Example: invisible button :)')
        imgui.invisible_button('Button 1', 200, 200)
        imgui.small_button('Button 2')
        imgui.end()

    Args:
        identifier (str): Button identifier. Like label on :any:`button()`
            but it is not displayed.
        width (float): button width.
        height (float): button height.
        flags: ImGuiButtonFlags

    Returns:
        bool: True if button is clicked.

    .. wraps::
        bool InvisibleButton(const char* str_id, const ImVec2& size, ImGuiButtonFlags flags = 0)
    '''

def color_button(desc_id: str,
                 r: float,
                 g: float,
                 b: float,
                 a: float = 1.0,
                 width: float = 0.0,
                 height: float = 0.0) -> bool:
    '''
    Display colored button.

    .. visual-example::
        :auto_layout:
        :height: 150

        imgui.begin('Example: color button')
        imgui.color_button('Button 1', 1, 0, 0, 1, 0, 10, 10)
        imgui.color_button('Button 2', 0, 1, 0, 1, 0, 10, 10)
        imgui.color_button('Wide Button', 0, 0, 1, 1, 0, 20, 10)
        imgui.color_button('Tall Button', 1, 0, 1, 1, 0, 10, 20)
        imgui.end()

    Args:
        #r (float): red color intensity.
        #g (float): green color intensity.
        #b (float): blue color instensity.
        #a (float): alpha intensity.
        #ImGuiColorEditFlags: Color edit flags.  Zero for none.
        #width (float): Width of the color button
        #height (float): Height of the color button

    Returns:
        bool: True if button is clicked.

    .. wraps::
        bool ColorButton(
            const char* desc_id,
            const ImVec4& col,
            ImGuiColorEditFlags flags,
            ImVec2 size
        )
    '''

def image_button(texture_id: int,
                 width: float,
                 height: float,
                 uv0: tuple[float, float] = (0.0, 0.0),
                 uv1: tuple[float, float] = (1.0, 1.0),
                 tint_color: tuple[float, float, float, float] = (1.0, 1.0, 1.0, 1.0),
                 border_color: tuple[float, float, float, float] = (0.0, 0.0, 0.0, 0.0),
                 frame_padding: int = -1) -> bool:
    '''
    Display image.

    .. todo:: add example with some preconfigured image

    Args:
        texture_id (object): user data defining texture id. Argument type
            is implementation dependent. For OpenGL it is usually an integer.
        size (Vec2): image display size two-tuple.
        uv0 (Vec2): UV coordinates for 1st corner (lower-left for OpenGL).
            Defaults to ``(0, 0)``.
        uv1 (Vec2): UV coordinates for 2nd corner (upper-right for OpenGL).
            Defaults to ``(1, 1)``.
        tint_color (Vec4): Image tint color. Defaults to white.
        border_color (Vec4): Image border color. Defaults to transparent.
        frame_padding (int): Frame padding (``0``: no padding, ``<0`` default
            padding).

    Returns:
        bool: True if clicked.

    .. wraps::
        bool ImageButton(
            ImTextureID user_texture_id,
            const ImVec2& size,
            const ImVec2& uv0 = ImVec2(0,0),
            const ImVec2& uv1 = ImVec2(1,1),
            int frame_padding = -1,
            const ImVec4& bg_col = ImVec4(0,0,0,0),
            const ImVec4& tint_col = ImVec4(1,1,1,1)
        )
    '''

def image(texture_id: int,
          width: float,
          height: float,
          uv0: tuple[float, float] = (0.0, 0.0),
          uv1: tuple[float, float] = (1.0, 1.0),
          tint_color: tuple[float, float, float, float] = (1.0, 1.0, 1.0, 1.0),
          border_color: tuple[float, float, float, float] = (0.0, 0.0, 0.0, 0.0)) -> None:
    '''
    Display image.

    .. visual-example::
        :auto_layout:
        :width: 550
        :height: 200

        texture_id = imgui.get_io().fonts.texture_id

        imgui.begin('Example: image display')
        imgui.image(texture_id, 512, 64, border_color=(1, 0, 0, 1))
        imgui.end()

    Args:
        texture_id (object): user data defining texture id. Argument type
            is implementation dependent. For OpenGL it is usually an integer.
        size (Vec2): image display size two-tuple.
        uv0 (Vec2): UV coordinates for 1st corner (lower-left for OpenGL).
            Defaults to ``(0, 0)``.
        uv1 (Vec2): UV coordinates for 2nd corner (upper-right for OpenGL).
            Defaults to ``(1, 1)``.
        tint_color(Vec4): Image tint color. Defaults to white.
        border_color(Vec4): Image border color. Defaults to transparent.

    .. wraps::
        void Image(
            ImTextureID user_texture_id,
            const ImVec2& size,
            const ImVec2& uv0 = ImVec2(0,0),
            const ImVec2& uv1 = ImVec2(1,1),
            const ImVec4& tint_col = ImVec4(1,1,1,1),
            const ImVec4& border_col = ImVec4(0,0,0,0)
        )
    '''

def checkbox(label: str, state: bool) -> tuple[bool, bool]:
    '''
    Display checkbox widget.

    .. visual-example::
        :auto_layout:
        :width: 400


        # note: these should be initialized outside of the main interaction
        #       loop
        checkbox1_enabled = True
        checkbox2_enabled = False

        imgui.new_frame()
        imgui.begin('Example: checkboxes')

        # note: first element of return two-tuple notifies if there was a click
        #       event in currently processed frame and second element is actual
        #       checkbox state.
        _, checkbox1_enabled = imgui.checkbox('Checkbox 1', checkbox1_enabled)
        _, checkbox2_enabled = imgui.checkbox('Checkbox 2', checkbox2_enabled)

        imgui.text('Checkbox 1 state value: {}'.format(checkbox1_enabled))
        imgui.text('Checkbox 2 state value: {}'.format(checkbox2_enabled))

        imgui.end()


    Args:
        label (str): text label for checkbox widget.
        state (bool): current (desired) state of the checkbox. If it has to
            change, the new state will be returned as a second item of
            the return value.

    Returns:
        tuple: a ``(clicked, state)`` two-tuple indicating click event and the
        current state of the checkbox.

    .. wraps::
        bool Checkbox(const char* label, bool* v)
    '''

def checkbox_flags(label: str, flags: int, flags_value: int) -> tuple[bool, int]:
    '''
    Display checkbox widget that handle integer flags (bit fields).

    It is useful for handling window/style flags or any kind of flags
    implemented as integer bitfields.

    .. visual-example::
        :auto_layout:
        :width: 500

        flags = imgui.WINDOW_NO_RESIZE | imgui.WINDOW_NO_MOVE

        imgui.begin('Example: checkboxes for flags', flags=flags)

        clicked, flags = imgui.checkbox_flags(
            'No resize', flags, imgui.WINDOW_NO_RESIZE
        )
        clicked, flags = imgui.checkbox_flags(
            'No move', flags, imgui.WINDOW_NO_MOVE
        )
        clicked, flags = imgui.checkbox_flags(
            'No collapse', flags, imgui.WINDOW_NO_COLLAPSE
        )
        # note: it also allows to use multiple flags at once
        clicked, flags = imgui.checkbox_flags(
            'No resize & no move', flags,
            imgui.WINDOW_NO_RESIZE | imgui.WINDOW_NO_MOVE
        )
        imgui.text('Current flags value: {0:b}'.format(flags))
        imgui.end()

    Args:
        label (str): text label for checkbox widget.
        flags (int): current state of the flags associated with checkbox.
            Actual state of checkbox (toggled/untoggled) is calculated from
            this argument and ``flags_value`` argument. If it has to change,
            the new state will be returned as a second item of the return
            value.
        flags_value (int): values of flags this widget can toggle. Represents
            bitmask in flags bitfield. Allows multiple flags to be toggled
            at once (specify using bit OR operator `|`, see example above).

    Returns:
        tuple: a ``(clicked, flags)`` two-tuple indicating click event and the
        current state of the flags controlled with this checkbox.

    .. wraps::
        bool CheckboxFlags(
            const char* label, unsigned int* flags,
            unsigned int flags_value
        )
    '''

def radio_button(label: str, active: bool) -> bool:
    '''Display radio button widget

    .. visual-example::
        :auto_layout:
        :height: 100

        # note: the variable that contains the state of the radio_button, should be initialized
        #       outside of the main interaction loop
        radio_active = True

        imgui.begin('Example: radio buttons')

        if imgui.radio_button('Radio button', radio_active):
            radio_active = not radio_active

        imgui.end()

    Args:
        label (str): button label.
        active (bool): state of the radio button.

    Returns:
        bool: True if clicked.

    .. wraps::
        bool RadioButton(const char* label, bool active)
    '''

def begin_combo(label: str,
                preview_value: str,
                flags: ComboFlags = COMBO_NONE) -> _BeginEndCombo:
    '''
    Begin a combo box with control over how items are displayed.

    .. visual-example::
        :width: 200
        :height: 200
        :auto_layout:

        selected = 0
        items = ['AAAA', 'BBBB', 'CCCC', 'DDDD']

        # ...

        with imgui.begin('Example: begin combo'):
            with imgui.begin_combo('combo', items[selected]) as combo:
                if combo.opened:
                    for i, item in enumerate(items):
                        is_selected = (i == selected)
                        if imgui.selectable(item, is_selected)[0]:
                            selected = i

                        # Set the initial focus when opening the combo (scrolling + keyboard navigation focus)
                        if is_selected:
                            imgui.set_item_default_focus()

    Example::

        selected = 0
        items = ['AAAA', 'BBBB', 'CCCC', 'DDDD']

        # ...

        imgui.begin('Example: begin combo')
        if imgui.begin_combo('combo', items[selected]):
            for i, item in enumerate(items):
                is_selected = (i == selected)
                if imgui.selectable(item, is_selected)[0]:
                    selected = i

                # Set the initial focus when opening the combo (scrolling + keyboard navigation focus)
                if is_selected:
                    imgui.set_item_default_focus()

            imgui.end_combo()

        imgui.end()

    Args:
        label (str): Identifier for the combo box.
        preview_value (str): String preview for currently selected item.
        flags: Combo flags. See:
            :ref:`list of available flags <combo-flag-options>`.

    Returns:
        _BeginEndCombo: Struct with ``opened`` bool attribute. Use with ``with`` to automatically call :func:`end_combo` when the block ends.`

    .. wraps::
        bool BeginCombo(
            const char* label,
            const char* preview_value,
            ImGuiComboFlags flags = 0
        )

    '''

def end_combo() -> None:
    '''
    End combo box.
    Only call if ``begin_combo().opened`` is True.

    .. wraps::
        void EndCombo()
    '''

def combo(label: str,
          current: int,
          items: list[str],
          height_in_items: int = -1) -> tuple[bool, int]:
    '''
    Display combo widget.

    .. visual-example::
        :auto_layout:
        :height: 200
        :click: 80 40

        current = 2
        imgui.begin('Example: combo widget')

        clicked, current = imgui.combo(
            'combo', current, ['first', 'second', 'third']
        )

        imgui.end()

    Args:
        label (str): combo label.
        current (int): index of selected item.
        items (list): list of string labels for items.
        height_in_items (int): height of dropdown in items. Defaults to -1
            (autosized).

    Returns:
        tuple: a ``(changed, current)`` tuple indicating change of selection and current index of selected item.

    .. wraps::
        bool Combo(
            const char* label, int* current_item,
            const char* items_separated_by_zeros,
            int height_in_items = -1
        )

    '''

def color_edit3(label: str,
                r: float,
                g: float,
                b: float,
                flags: ColorEditFlags = COLOR_EDIT_NONE) -> tuple[bool, tuple[float, float, float]]:
    '''
    Display color edit widget for color without alpha value.

    .. visual-example::
        :auto_layout:
        :width: 300

        # note: the variable that contains the color data, should be initialized
        #       outside of the main interaction loop
        color_1 = 1., .0, .5
        color_2 = 0., .8, .3

        imgui.begin('Example: color edit without alpha')

        # note: first element of return two-tuple notifies if the color was changed
        #       in currently processed frame and second element is current value
        #       of color
        changed, color_1 = imgui.color_edit3('Color 1', *color_1)
        changed, color_2 = imgui.color_edit3('Color 2', *color_2)

        imgui.end()

    Args:
        label (str): color edit label.
        r (float): red color intensity.
        g (float): green color intensity.
        b (float): blue color instensity.
        flags (ImGuiColorEditFlags): Color edit flags.  Zero for none.

    Returns:
        tuple: a ``(bool changed, float color[3])`` tuple that contains indicator of color
        change and current value of color

    .. wraps::
        bool ColorEdit3(const char* label, float col[3], ImGuiColorEditFlags flags = 0)
    '''

def color_edit4(label: str,
                r: float,
                g: float,
                b: float,
                a: float,
                flags: ColorEditFlags = COLOR_EDIT_NONE) -> tuple[bool, tuple[float, float, float, float]]:
    '''
    Display color edit widget for color with alpha value.

    .. visual-example::
        :auto_layout:
        :width: 400

        # note: the variable that contains the color data, should be initialized
        #       outside of the main interaction loop
        color = 1., .0, .5, 1.

        imgui.begin('Example: color edit with alpha')

        # note: first element of return two-tuple notifies if the color was changed
        #       in currently processed frame and second element is current value
        #       of color and alpha
        _, color = imgui.color_edit4('Alpha', *color)
        _, color = imgui.color_edit4('No alpha', *color, imgui.COLOR_EDIT_NO_ALPHA)

        imgui.end()

    Args:
        label (str): color edit label.
        r (float): red color intensity.
        g (float): green color intensity.
        b (float): blue color instensity.
        a (float): alpha intensity.
        flags (ImGuiColorEditFlags): Color edit flags.  Zero for none.

    Returns:
        tuple: a ``(bool changed, float color[4])`` tuple that contains indicator of color
        change and current value of color and alpha

    .. wraps::
        ColorEdit4(
            const char* label, float col[4], ImGuiColorEditFlags flags
        )
    '''

def drag_float(label: str,
               value: float,
               change_speed: float = 1.0,
               min_value: float = 0.0,
               max_value: float = 0.0,
               format: str = '%.3f',
               flags: SliderFlags = SLIDER_FLAGS_NONE,
               power: float = 1.0) -> tuple[bool, float]:
    '''
    Display float drag widget.

    .. todo::
        Consider replacing ``format`` with something that allows
        for safer way to specify display format without loosing the
        functionality of wrapped function.

    .. visual-example::
        :auto_layout:
        :width: 400
        :height: 130

        value = 42.0

        imgui.begin('Example: drag float')
        changed, value = imgui.drag_float(
            'Default', value,
        )
        changed, value = imgui.drag_float(
            'Less precise', value, format='%.1f'
        )
        imgui.text('Changed: %s, Value: %s' % (changed, value))
        imgui.end()

    Args:
        label (str): widget label.
        value (float): drag values,
        change_speed (float): how fast values change on drag.
        min_value (float): min value allowed by widget.
        max_value (float): max value allowed by widget.
        format (str): display format string as C-style ``printf``
            format string. **Warning:** Highly unsafe when used without care.
            May lead to segmentation faults and other memory violation issues.
        flags: SliderFlags flags. See:
            :ref:`list of available flags <slider-flag-options>`.
        power (float): OBSOLETED in ImGui 1.78 (from June 2020)

    Returns:
        tuple: a ``(changed, value)`` tuple that contains indicator of
        widget state change and the current drag value.

    .. wraps::
        bool DragFloat(
            const char* label,
            float* v,
            float v_speed = 1.0f,
            float v_min = 0.0f,
            float v_max = 0.0f,
            const char* format = '%.3f',
            ImGuiSliderFlags flags = 0
        )
    '''

def drag_float2(label: str,
                value0: float,
                value1: float,
                change_speed: float = 1.0,
                min_value: float = 0.0,
                max_value: float = 0.0,
                format: str = '%.3f',
                flags: SliderFlags = SLIDER_FLAGS_NONE,
                power: float = 1.0) -> tuple[bool, tuple[float, float]]:
    '''
    Display float drag widget with 2 values.

    .. visual-example::
        :auto_layout:
        :width: 400
        :height: 130

        values = 88.0, 42.0

        imgui.begin('Example: drag float')
        changed, values = imgui.drag_float2(
            'Default', *values
        )
        changed, values = imgui.drag_float2(
            'Less precise', *values, format='%.1f'
        )
        imgui.text('Changed: %s, Values: %s' % (changed, values))
        imgui.end()

    Args:
        label (str): widget label.
        value0, value1 (float): drag values.
        change_speed (float): how fast values change on drag.
        min_value (float): min value allowed by widget.
        max_value (float): max value allowed by widget.
        format (str): display format string as C-style ``printf``
            format string. **Warning:** highly unsafe. See :any:`drag_float()`.
        flags: SliderFlags flags. See:
            :ref:`list of available flags <slider-flag-options>`.
        power (float): OBSOLETED in ImGui 1.78 (from June 2020)

    Returns:
        tuple: a ``(changed, values)`` tuple that contains indicator of
        widget state change and the tuple of current drag values.

    .. wraps::
        bool DragFloat2(
            const char* label,
            float v[2],
            float v_speed = 1.0f,
            float v_min = 0.0f,
            float v_max = 0.0f,
            const char* format = '%.3f',
            ImGuiSliderFlags flags = 0
        )
    '''

def drag_float3(label: str,
                value0: float,
                value1: float,
                value2: float,
                change_speed: float = 1.0,
                min_value: float = 0.0,
                max_value: float = 0.0,
                format: str = '%.3f',
                flags: SliderFlags = SLIDER_FLAGS_NONE,
                power: float = 1.0) -> tuple[bool, tuple[float, float, float]]:
    '''
    Display float drag widget with 3 values.

    .. visual-example::
        :auto_layout:
        :width: 400
        :height: 130

        values = 88.0, 42.0, 69.0

        imgui.begin('Example: drag float')
        changed, values = imgui.drag_float3(
            'Default', *values
        )
        changed, values = imgui.drag_float3(
            'Less precise', *values, format='%.1f'
        )
        imgui.text('Changed: %s, Values: %s' % (changed, values))
        imgui.end()

    Args:
        label (str): widget label.
        value0, value1, value2 (float): drag values.
        change_speed (float): how fast values change on drag.
        min_value (float): min value allowed by widget.
        max_value (float): max value allowed by widget.
        format (str): display format string as C-style ``printf``
            format string. **Warning:** highly unsafe. See :any:`drag_float()`.
        flags: SliderFlags flags. See:
            :ref:`list of available flags <slider-flag-options>`.
        power (float): OBSOLETED in ImGui 1.78 (from June 2020)

    Returns:
        tuple: a ``(changed, values)`` tuple that contains indicator of
        widget state change and the tuple of current drag values.

    .. wraps::
        bool DragFloat3(
            const char* label,
            float v[3],
            float v_speed = 1.0f,
            float v_min = 0.0f,
            float v_max = 0.0f,
            const char* format = '%.3f',
            ImGuiSliderFlags flags = 0
        )
    '''

def drag_float4(label: str,
                value0: float,
                value1: float,
                value2: float,
                value3: float,
                change_speed: float = 1.0,
                min_value: float = 0.0,
                max_value: float = 0.0,
                format: str = '%.3f',
                flags: SliderFlags = SLIDER_FLAGS_NONE,
                power: float = 1.0) -> tuple[bool, tuple[float, float, float, float]]:
    '''
    Display float drag widget with 4 values.

    .. visual-example::
        :auto_layout:
        :width: 400
        :height: 130

        values = 88.0, 42.0, 69.0, 0.0

        imgui.begin('Example: drag float')
        changed, values = imgui.drag_float4(
            'Default', *values
        )
        changed, values = imgui.drag_float4(
            'Less precise', *values, format='%.1f'
        )
        imgui.text('Changed: %s, Values: %s' % (changed, values))
        imgui.end()

    Args:
        label (str): widget label.
        value0, value1, value2, value3 (float): drag values.
        change_speed (float): how fast values change on drag.
        min_value (float): min value allowed by widget.
        max_value (float): max value allowed by widget.
        format (str): display format string as C-style ``printf``
            format string. **Warning:** highly unsafe. See :any:`drag_float()`.
        flags: SliderFlags flags. See:
            :ref:`list of available flags <slider-flag-options>`.
        power (float): OBSOLETED in ImGui 1.78 (from June 2020)

    Returns:
        tuple: a ``(changed, values)`` tuple that contains indicator of
        widget state change and the tuple of current drag values.

    .. wraps::
        bool DragFloat4(
            const char* label,
            float v[4],
            float v_speed = 1.0f,
            float v_min = 0.0f,
            float v_max = 0.0f,
            const char* format = '%.3f',
            ImGuiSliderFlags flags = 0
        )
    '''

def drag_float_range2(label: str,
                      current_min: float,
                      current_max: float,
                      speed: float = 1.0,
                      min_value: float = 0.0,
                      max_value: float = 0.0,
                      format: str = '%.3f',
                      format_max: str | None = None,
                      flags: SliderFlags = SLIDER_FLAGS_NONE) -> tuple[bool, float, float]:
    '''
    Display drag float range widget

    Args:
        label (str): widget label
        current_min (float): current value of minimum
        current_max (float): current value of maximum
        speed (float): widget speed of change
        min_value (float): minimal possible value
        max_value (float): maximal possible value
        format (str): display format
        format_max (str): display format for maximum. If None, ``format`` parameter is used.
        flags: SliderFlags flags. See:
            :ref:`list of available flags <slider-flag-options>`.

    Returns:
        tuple: a (changed, current_min, current_max) tuple, where ``changed`` indicate
               that the value has been updated.

    .. visual-example::
        :auto_layout:
        :width: 400
        :height: 130

        vmin = 0
        vmax = 100

        imgui.begin('Example: drag float range')
        changed, vmin, vmax = imgui.drag_float_range2( 'Drag Range', vmin, vmax )
        imgui.text('Changed: %s, Range: (%.2f, %.2f)' % (changed, vmin, vmax))
        imgui.end()


    .. wraps::
        bool DragFloatRange2(
            const char* label,
            float* v_current_min,
            float* v_current_max,
            float v_speed = 1.0f,
            float v_min = 0.0f,
            float v_max = 0.0f,
            const char* format = '%.3f',
            const char* format_max = NULL,
            ImGuiSliderFlags flags = 0
        )
    '''

def drag_int(label: str,
             value: int,
             change_speed: float = 1.0,
             min_value: int = 0,
             max_value: int = 0,
             format: str = '%d',
             flags: SliderFlags = SLIDER_FLAGS_NONE) -> tuple[bool, int]:
    '''
    Display int drag widget.

    .. todo::
        Consider replacing ``format`` with something that allows
        for safer way to specify display format without loosing the
        functionality of wrapped function.

    .. visual-example::
        :auto_layout:
        :width: 400
        :height: 130

        value = 42

        imgui.begin('Example: drag int')
        changed, value = imgui.drag_int('drag int', value,)
        imgui.text('Changed: %s, Value: %s' % (changed, value))
        imgui.end()

    Args:
        label (str): widget label.
        value (int): drag value,
        change_speed (float): how fast values change on drag.
        min_value (int): min value allowed by widget.
        max_value (int): max value allowed by widget.
        format (str): display format string as C-style ``printf``
            format string. **Warning:** Highly unsafe when used without care.
            May lead to segmentation faults and other memory violation issues.
        flags: SliderFlags flags. See:
            :ref:`list of available flags <slider-flag-options>`.

    Returns:
        tuple: a ``(changed, value)`` tuple that contains indicator of
        widget state change and the current drag value.

    .. wraps::
        bool DragInt(
            const char* label,
            int* v,
            float v_speed = 1.0f,
            int v_min = 0.0f,
            int v_max = 0.0f,
            const char* format = '%d',
            ImGuiSliderFlags flags = 0
        )
    '''

def drag_int2(label: str,
              value0: int,
              value1: int,
              change_speed: float = 1.0,
              min_value: int = 0,
              max_value: int = 0,
              format: str = '%d',
              flags: SliderFlags = SLIDER_FLAGS_NONE) -> tuple[bool, tuple[int, int]]:
    '''
    Display int drag widget with 2 values.

    .. visual-example::
        :auto_layout:
        :width: 400
        :height: 130

        values = 88, 42

        imgui.begin('Example: drag int')
        changed, values = imgui.drag_int2(
            'drag ints', *values
        )
        imgui.text('Changed: %s, Values: %s' % (changed, values))
        imgui.end()

    Args:
        label (str): widget label.
        value0, value1 (int): drag values.
        change_speed (float): how fast values change on drag.
        min_value (int): min value allowed by widget.
        max_value (int): max value allowed by widget.
        format (str): display format string as C-style ``printf``
            format string. **Warning:** highly unsafe. See :any:`drag_int()`.
        flags: SliderFlags flags. See:
            :ref:`list of available flags <slider-flag-options>`.

    Returns:
        tuple: a ``(changed, values)`` tuple that contains indicator of
        widget state change and the tuple of current drag values.

    .. wraps::
        bool DragInt2(
            const char* label,
            int v[2],
            float v_speed = 1.0f,
            int v_min = 0.0f,
            int v_max = 0.0f,
            const char* format = '%d',
            ImGuiSliderFlags flags = 0
        )
    '''

def drag_int3(label: str,
              value0: int,
              value1: int,
              value2: int,
              change_speed: float = 1.0,
              min_value: int = 0,
              max_value: int = 0,
              format: str = '%d',
              flags: SliderFlags = SLIDER_FLAGS_NONE) -> tuple[bool, tuple[int, int, int]]:
    '''
    Display int drag widget with 3 values.

    .. visual-example::
        :auto_layout:
        :width: 400
        :height: 130

        values = 88, 42, 69

        imgui.begin('Example: drag int')
        changed, values = imgui.drag_int3(
            'drag ints', *values
        )
        imgui.text('Changed: %s, Values: %s' % (changed, values))
        imgui.end()

    Args:
        label (str): widget label.
        value0, value1 (int): drag values.
        change_speed (float): how fast values change on drag.
        min_value (int): min value allowed by widget.
        max_value (int): max value allowed by widget.
        format (str): display format string as C-style ``printf``
            format string. **Warning:** highly unsafe. See :any:`drag_int()`.
        flags: SliderFlags flags. See:
            :ref:`list of available flags <slider-flag-options>`.

    Returns:
        tuple: a ``(changed, values)`` tuple that contains indicator of
        widget state change and the tuple of current drag values.

    .. wraps::
        bool DragInt3(
            const char* label,
            int v[3],
            float v_speed = 1.0f,
            int v_min = 0.0f,
            int v_max = 0.0f,
            const char* format = '%d',
            ImGuiSliderFlags flags = 0
        )
    '''

def drag_int4(label: str,
              value0: int,
              value1: int,
              value2: int,
              value3: int,
              change_speed: float = 1.0,
              min_value: int = 0,
              max_value: int = 0,
              format: str = '%d',
              flags: SliderFlags = SLIDER_FLAGS_NONE) -> tuple[bool, tuple[int, int, int, int]]:
    '''
    Display int drag widget with 4 values.

    .. visual-example::
        :auto_layout:
        :width: 400
        :height: 130

        values = 88, 42, 69, 0

        imgui.begin('Example: drag int')
        changed, values = imgui.drag_int4(
            'drag ints', *values
        )
        imgui.text('Changed: %s, Values: %s' % (changed, values))
        imgui.end()

    Args:
        label (str): widget label.
        value0, value1 (int): drag values.
        change_speed (float): how fast values change on drag.
        min_value (int): min value allowed by widget.
        max_value (int): max value allowed by widget.
        format (str): display format string as C-style ``printf``
            format string. **Warning:** highly unsafe. See :any:`drag_int()`.
        flags: SliderFlags flags. See:
            :ref:`list of available flags <slider-flag-options>`.

    Returns:
        tuple: a ``(changed, values)`` tuple that contains indicator of
        widget state change and the tuple of current drag values.

    .. wraps::
        bool DragInt4(
            const char* label,
            int v[4],
            float v_speed = 1.0f,
            int v_min = 0.0f,
            int v_max = 0.0f,
            const char* format = '%d',
            ImGuiSliderFlags flags = 0
        )
    '''

def drag_int_range2(label: str,
                    current_min: int,
                    current_max: int,
                    speed: float = 1.0,
                    min_value: int = 0,
                    max_value: int = 0,
                    format: str = '%d',
                    format_max: str | None = None,
                    flags: SliderFlags = SLIDER_FLAGS_NONE) -> tuple[bool, int, int]:
    '''
    Display drag int range widget

    Args:
        label (str): widget label
        current_min (int): current value of minimum
        current_max (int): current value of maximum
        speed (float): widget speed of change
        min_value (int): minimal possible value
        max_value (int): maximal possible value
        format (str): display format
        format_max (str): display format for maximum. If None, ``format`` parameter is used.
        flags: SliderFlags flags. See:
            :ref:`list of available flags <slider-flag-options>`.

    Returns:
        tuple: a (changed, current_min, current_max) tuple, where ``changed`` indicate
               that the value has been updated.

    .. visual-example::
        :auto_layout:
        :width: 400
        :height: 130

        vmin = 0
        vmax = 100

        imgui.begin('Example: drag float range')
        changed, vmin, vmax = imgui.drag_int_range2( 'Drag Range', vmin, vmax )
        imgui.text('Changed: %s, Range: (%d, %d)' % (changed, vmin, vmax))
        imgui.end()


    .. wraps::
        bool DragIntRange2(
            const char* label,
            int* v_current_min,
            int* v_current_max,
            float v_speed = 1.0f,
            int v_min = 0,
            int v_max = 0,
            const char* format = '%d',
            const char* format_max = NULL,
            ImGuiSliderFlags flags = 0
        )
    '''

def drag_scalar(label: str,
                data_type: DataType,
                data: bytes,
                change_speed: float,
                min_value: bytes | None = None,
                max_value: bytes | None = None,
                format: str | None = None,
                flags: SliderFlags = SLIDER_FLAGS_NONE) -> tuple[bool, bytes]:
    '''
    Display scalar drag widget.
    Data is passed via ``bytes`` and the type is separatelly given using ``data_type``.
    This is useful to work with specific types (e.g. unsigned 8bit integer, float, double)
    like when interfacing with Numpy.

    Args:
        label (str): widget label
        data_type: ImGuiDataType enum, type of the given data
        data (bytes): data value as a bytes array
        change_speed (float): how fast values change on drag
        min_value (bytes): min value allowed by widget
        max_value (bytes): max value allowed by widget
        format (str): display format string as C-style ``printf``
            format string. **Warning:** highly unsafe. See :any:`drag_int()`.
        flags: ImGuiSlider flags. See:
            :ref:`list of available flags <slider-flag-options>`.

    Returns:
        tuple: a ``(changed, value)`` tuple that contains indicator of
        drag state change and the current drag content.

    .. wraps::
        bool DragScalar(
            const char* label,
            ImGuiDataType data_type,
            void* p_data,
            float v_speed,
            const void* p_min = NULL,
            const void* p_max = NULL,
            const char* format = NULL,
            ImGuiSliderFlags flags = 0
        )
    '''

def drag_scalar_N(label: str,
                  data_type: DataType,
                  data: bytes,
                  components: int,
                  change_speed: float,
                  min_value: bytes | None = None,
                  max_value: bytes | None = None,
                  format: str | None = None,
                  flags: SliderFlags = SLIDER_FLAGS_NONE) -> tuple[bool, bytes]:
    '''
    Display multiple scalar drag widget.
    Data is passed via ``bytes`` and the type is separatelly given using ``data_type``.
    This is useful to work with specific types (e.g. unsigned 8bit integer, float, double)
    like when interfacing with Numpy.

    Args:
        label (str): widget label
        data_type: ImGuiDataType enum, type of the given data
        data (bytes): data value as a bytes array
        components (int): number of widgets
        change_speed (float): how fast values change on drag
        min_value (bytes): min value allowed by widget
        max_value (bytes): max value allowed by widget
        format (str): display format string as C-style ``printf``
            format string. **Warning:** highly unsafe. See :any:`drag_int()`.
        flags: ImGuiSlider flags. See:
            :ref:`list of available flags <slider-flag-options>`.

    Returns:
        tuple: a ``(changed, value)`` tuple that contains indicator of
        drag state change and the current drag content.

    .. wraps::
        bool DragScalarN(
            const char* label,
            ImGuiDataType data_type,
            void* p_data,
            int components,
            float v_speed,
            const void* p_min = NULL,
            const void* p_max = NULL,
            const char* format = NULL,
            ImGuiSliderFlags flags = 0
        )
    '''

def input_text(label: str,
               value: str,
               buffer_length: int = -1,
               flags: TextInputFlags = INPUT_TEXT_NONE,
               callback: _t.Callable[[_ImGuiInputTextCallbackData], int | None] | None = None,
               user_data: _t.Any = None) -> tuple[bool, str]:
    '''
    Display text input widget.

    The ``buffer_length`` is the maximum allowed length of the content. It is the size in bytes, which may not correspond to the number of characters.
    If set to -1, the internal buffer will have an adaptive size, which is equivalent to using the ``imgui.INPUT_TEXT_CALLBACK_RESIZE`` flag.
    When a callback is provided, it is called after the internal buffer has been resized.

    .. visual-example::
        :auto_layout:
        :width: 400
        :height: 100

        text_val = 'Please, type the coefficient here.'
        imgui.begin('Example: text input')
        changed, text_val = imgui.input_text('Coefficient:', text_val)
        imgui.text('You wrote:')
        imgui.same_line()
        imgui.text(text_val)
        imgui.end()

    Args:
        label (str): widget label.
        value (str): textbox value
        buffer_length (int): length of the content buffer
        flags: InputText flags. See:
            :ref:`list of available flags <inputtext-flag-options>`.
        callback (callable): a callable that is called depending on choosen flags.
            Callable takes an imgui._ImGuiInputTextCallbackData object as argument
            Callable should return None or integer
        user_data: Any data that the user want to use in the callback.

    Returns:
        tuple: a ``(changed, value)`` tuple that contains indicator of
        textbox state change and the current text contents.

    .. wraps::
        bool InputText(
            const char* label,
            char* buf,
            size_t buf_size,
            ImGuiInputTextFlags flags = 0,
            ImGuiInputTextCallback callback = NULL,
            void* user_data = NULL
        )
    '''

def input_text_multiline(label: str,
                         value: str,
                         buffer_length: int = -1,
                         width: float = 0.0,
                         height: float = 0.0,
                         flags: TextInputFlags = INPUT_TEXT_NONE,
                         callback: _t.Callable[[_ImGuiInputTextCallbackData], int | None] | None = None,
                         user_data: _t.Any = None) -> tuple[bool, str]:
    '''
    Display multiline text input widget.

    The ``buffer_length`` is the maximum allowed length of the content. It is the size in bytes, which may not correspond to the number of characters.
    If set to -1, the internal buffer will have an adaptive size, which is equivalent to using the ``imgui.INPUT_TEXT_CALLBACK_RESIZE`` flag.
    When a callback is provided, it is called after the internal buffer has been resized.

    .. visual-example::
        :auto_layout:
        :width: 400
        :height: 200

        text_val = 'Type the your message here.'
        imgui.begin('Example: text input')
        changed, text_val = imgui.input_text_multiline(
            'Message:',
            text_val,
            2056
        )
        imgui.text('You wrote:')
        imgui.same_line()
        imgui.text(text_val)
        imgui.end()

    Args:
        label (str): widget label.
        value (str): textbox value
        buffer_length (int): length of the content buffer
        width (float): width of the textbox
        height (float): height of the textbox
        flags: InputText flags. See:
            :ref:`list of available flags <inputtext-flag-options>`.
        callback (callable): a callable that is called depending on choosen flags.
            Callable takes an imgui._ImGuiInputTextCallbackData object as argument
            Callable should return None or integer
        user_data: Any data that the user want to use in the callback.

    Returns:
        tuple: a ``(changed, value)`` tuple that contains indicator of
        textbox state change and the current text contents.

    .. wraps::
        bool InputTextMultiline(
            const char* label,
            char* buf,
            size_t buf_size,
            const ImVec2& size = ImVec2(0,0),
            ImGuiInputTextFlags flags = 0,
            ImGuiInputTextCallback callback = NULL,
            void* user_data = NULL
        )
    '''

def input_text_with_hint(label: str,
                         hint: str,
                         value: str,
                         buffer_length: int = -1,
                         flags: TextInputFlags = INPUT_TEXT_NONE,
                         callback: _t.Callable[[_ImGuiInputTextCallbackData], int | None] | None = None,
                         user_data: _t.Any = None) -> tuple[bool, str]:
    '''
    Display a text box, if the text is empty a hint on how to fill the box is given.

    The ``buffer_length`` is the maximum allowed length of the content. It is the size in bytes, which may not correspond to the number of characters.
    If set to -1, the internal buffer will have an adaptive size, which is equivalent to using the ``imgui.INPUT_TEXT_CALLBACK_RESIZE`` flag.
    When a callback is provided, it is called after the internal buffer has been resized.

    Args:
        label (str): Widget label
        hing (str): Hint displayed if text value empty
        value (str): Text value
        buffer_length (int): Length of the content buffer
        flags: InputText flags. See:
            :ref:`list of available flags <inputtext-flag-options>`.
        callback (callable): a callable that is called depending on choosen flags.
            Callable takes an imgui._ImGuiInputTextCallbackData object as argument
            Callable should return None or integer
        user_data: Any data that the user want to use in the callback.

    Returns:
        tuple: a ``(changed, value)`` tuple that contains indicator of
        textbox state change and the current text contents.

    .. visual-example::
        :auto_layout:
        :width: 400
        :height: 200

        text_val = ''
        imgui.begin('Example Text With hing')
        changed, text_val = imgui.input_text_with_hint(
            'Email', 'your@email.com',
            text_val, 255)
        imgui.end()

    .. wraps::
        bool InputTextWithHint(
            const char* label,
            const char* hint,
            char* buf,
            size_t buf_size,
            ImGuiInputTextFlags flags = 0,
            ImGuiInputTextCallback callback = NULL,
            void* user_data = NULL
        )
    '''

def input_float(label: str,
                value: float,
                step: float = 0.0,
                step_fast: float = 0.0,
                format: str = '%.3f',
                flags: TextInputFlags = INPUT_TEXT_NONE) -> tuple[bool, float]:
    '''
    Display float input widget.

    .. visual-example::
        :auto_layout:
        :width: 400
        :height: 100

        float_val = 0.4
        imgui.begin('Example: float input')
        changed, float_val = imgui.input_float('Type coefficient:', float_val)
        imgui.text('You wrote: %f' % float_val)
        imgui.end()

    Args:
        label (str): widget label.
        value (float): textbox value
        step (float): incremental step
        step_fast (float): fast incremental step
        format = (str): format string
        flags: InputText flags. See:
            :ref:`list of available flags <inputtext-flag-options>`.

    Returns:
        tuple: a ``(changed, value)`` tuple that contains indicator of
        textbox state change and the current textbox content.

    .. wraps::
        bool InputFloat(
            const char* label,
            float* v,
            float step = 0.0f,
            float step_fast = 0.0f,
            const char* format = '%.3f',
            ImGuiInputTextFlags extra_flags = 0
        )
    '''

def input_float2(label: str,
                 value0: float,
                 value1: float,
                 format: str = '%.3f',
                 flags: TextInputFlags = INPUT_TEXT_NONE) -> tuple[bool, tuple[float, float]]:
    '''
    Display two-float input widget.

    .. visual-example::
        :auto_layout:
        :width: 400
        :height: 100

        values = 0.4, 3.2
        imgui.begin('Example: two float inputs')
        changed, values = imgui.input_float2('Type here:', *values)
        imgui.text('Changed: %s, Values: %s' % (changed, values))
        imgui.end()

    Args:
        label (str): widget label.
        value0, value1 (float): input values.
        format = (str): format string
        flags: InputText flags. See:
            :ref:`list of available flags <inputtext-flag-options>`.

    Returns:
        tuple: a ``(changed, values)`` tuple that contains indicator of
        textbox state change and the tuple of current values.

    .. wraps::
        bool InputFloat2(
            const char* label,
            float v[2],
            const char* format = '%.3f',
            ImGuiInputTextFlags extra_flags = 0
        )
    '''

def input_float3(label: str,
                 value0: float,
                 value1: float,
                 value2: float,
                 format: str = '%.3f',
                 flags: TextInputFlags = INPUT_TEXT_NONE) -> tuple[bool, tuple[float, float, float]]:
    '''
    Display three-float input widget.

    .. visual-example::
        :auto_layout:
        :width: 400
        :height: 100

        values = 0.4, 3.2, 29.3
        imgui.begin('Example: three float inputs')
        changed, values = imgui.input_float3('Type here:', *values)
        imgui.text('Changed: %s, Values: %s' % (changed, values))
        imgui.end()

    Args:
        label (str): widget label.
        value0, value1, value2 (float): input values.
        format = (str): format string
        flags: InputText flags. See:
            :ref:`list of available flags <inputtext-flag-options>`.

    Returns:
        tuple: a ``(changed, values)`` tuple that contains indicator of
        textbox state change and the tuple of current values.

    .. wraps::
        bool InputFloat3(
            const char* label,
            float v[3],
            const char* format = '%.3f',
            ImGuiInputTextFlags extra_flags = 0
        )
    '''

def input_float4(label: str,
                 value0: float,
                 value1: float,
                 value2: float,
                 value3: float,
                 format: str = '%.3f',
                 flags: TextInputFlags = INPUT_TEXT_NONE) -> tuple[bool, tuple[float, float, float, float]]:
    '''
    Display four-float input widget.

    .. visual-example::
        :auto_layout:
        :width: 400
        :height: 100

        values = 0.4, 3.2, 29.3, 12.9
        imgui.begin('Example: four float inputs')
        changed, values = imgui.input_float4('Type here:', *values)
        imgui.text('Changed: %s, Values: %s' % (changed, values))
        imgui.end()

    Args:
        label (str): widget label.
        value0, value1, value2, value3 (float): input values.
        format = (str): format string
        flags: InputText flags. See:
            :ref:`list of available flags <inputtext-flag-options>`.

    Returns:
        tuple: a ``(changed, values)`` tuple that contains indicator of
        textbox state change and the tuple of current values.

    .. wraps::
        bool InputFloat4(
            const char* label,
            float v[4],
            const char* format = '%.3f',
            ImGuiInputTextFlags extra_flags = 0
        )
    '''

def input_int(label: str,
              value: int,
              step: int = 1,
              step_fast: int = 100,
              flags: TextInputFlags = INPUT_TEXT_NONE) -> tuple[bool, int]:
    '''
    Display integer input widget.

    .. visual-example::
        :auto_layout:
        :width: 400
        :height: 100

        int_val = 3
        imgui.begin('Example: integer input')
        changed, int_val = imgui.input_int('Type multiplier:', int_val)
        imgui.text('You wrote: %i' % int_val)
        imgui.end()

    Args:
        label (str): widget label.
        value (int): textbox value
        step (int): incremental step
        step_fast (int): fast incremental step
        flags: InputText flags. See:
            :ref:`list of available flags <inputtext-flag-options>`.

    Returns:
        tuple: a ``(changed, value)`` tuple that contains indicator of
        textbox state change and the current textbox content.

    .. wraps::
        bool InputInt(
            const char* label,
            int* v,
            int step = 1,
            int step_fast = 100,
            ImGuiInputTextFlags extra_flags = 0
        )
    '''

def input_int2(label: str,
               value0: int,
               value1: int,
               flags: TextInputFlags = INPUT_TEXT_NONE) -> tuple[bool, tuple[int, int]]:
    '''
    Display two-integer input widget.

    .. visual-example::
        :auto_layout:
        :width: 400
        :height: 100

        values = 4, 12
        imgui.begin('Example: two int inputs')
        changed, values = imgui.input_int2('Type here:', *values)
        imgui.text('Changed: %s, Values: %s' % (changed, values))
        imgui.end()

    Args:
        label (str): widget label.
        value0, value1 (int): textbox values
        flags: InputText flags. See:
            :ref:`list of available flags <inputtext-flag-options>`.

    Returns:
        tuple: a ``(changed, value)`` tuple that contains indicator of
        textbox state change and the current textbox content.

    .. wraps::
        bool InputInt2(
            const char* label,
            int v[2],
            ImGuiInputTextFlags extra_flags = 0
        )
    '''

def input_int3(label: str,
               value0: int,
               value1: int,
               value2: int,
               flags: TextInputFlags = INPUT_TEXT_NONE) -> tuple[bool, tuple[int, int, int]]:
    '''
    Display three-integer input widget.

    .. visual-example::
        :auto_layout:
        :width: 400
        :height: 100

        values = 4, 12, 28
        imgui.begin('Example: three int inputs')
        changed, values = imgui.input_int3('Type here:', *values)
        imgui.text('Changed: %s, Values: %s' % (changed, values))
        imgui.end()

    Args:
        label (str): widget label.
        value0, value1, value2 (int): textbox values
        flags: InputText flags. See:
            :ref:`list of available flags <inputtext-flag-options>`.

    Returns:
        tuple: a ``(changed, value)`` tuple that contains indicator of
        textbox state change and the current textbox content.

    .. wraps::
        bool InputInt3(
            const char* label,
            int v[3],
            ImGuiInputTextFlags extra_flags = 0
        )
    '''

def input_int4(label: str,
               value0: int,
               value1: int,
               value2: int,
               value3: int,
               flags: TextInputFlags = INPUT_TEXT_NONE) -> tuple[bool, tuple[int, int, int, int]]:
    '''
    Display four-integer input widget.

    .. visual-example::
        :auto_layout:
        :width: 400
        :height: 100

        values = 4, 12, 28, 73
        imgui.begin('Example: four int inputs')
        changed, values = imgui.input_int4('Type here:', *values)
        imgui.text('Changed: %s, Values: %s' % (changed, values))
        imgui.end()

    Args:
        label (str): widget label.
        value0, value1, value2, value3 (int): textbox values
        flags: InputText flags. See:
            :ref:`list of available flags <inputtext-flag-options>`.

    Returns:
        tuple: a ``(changed, value)`` tuple that contains indicator of
        textbox state change and the current textbox content.

    .. wraps::
        bool InputInt4(
            const char* label,
            int v[4],
            ImGuiInputTextFlags extra_flags = 0
        )
    '''

def input_double(label: str,
                 value: float,
                 step: float = 0.0,
                 step_fast: float = 0.0,
                 format: str = '%.6f',
                 flags: TextInputFlags = INPUT_TEXT_NONE) -> tuple[bool, float]:
    '''
    Display double input widget.

    .. visual-example::
        :auto_layout:
        :width: 400
        :height: 100

        double_val = 3.14159265358979323846
        imgui.begin('Example: double input')
        changed, double_val = imgui.input_double('Type multiplier:', double_val)
        imgui.text('You wrote: %i' % double_val)
        imgui.end()

    Args:
        label (str): widget label.
        value (double): textbox value
        step (double): incremental step
        step_fast (double): fast incremental step
        format = (str): format string
        flags: InputText flags. See:
            :ref:`list of available flags <inputtext-flag-options>`.

    Returns:
        tuple: a ``(changed, value)`` tuple that contains indicator of
        textbox state change and the current textbox content.

    .. wraps::
        bool InputDouble(
            const char* label,
            double* v,
            double step = 0.0,
            double step_fast = 0.0,
            _bytes(format),
            ImGuiInputTextFlags extra_flags = 0
        )
    '''

def input_scalar(label: str,
                 data_type: DataType,
                 data: bytes,
                 step: bytes | None = None,
                 step_fast: bytes | None = None,
                 format: str | None = None,
                 flags: TextInputFlags = INPUT_TEXT_NONE) -> tuple[int, bytes]:
    '''
    Display scalar input widget.
    Data is passed via ``bytes`` and the type is separatelly given using ``data_type``.
    This is useful to work with specific types (e.g. unsigned 8bit integer, float, double)
    like when interfacing with Numpy.

    Args:
        label (str): widget label
        data_type: ImGuiDataType enum, type of the given data
        data (bytes): data value as a bytes array
        step (bytes): incremental step
        step_fast (bytes): fast incremental step
        format (str): format string
        flags: InputText flags. See:
            :ref:`list of available flags <inputtext-flag-options>`.

    Returns:
        tuple: a ``(changed, value)`` tuple that contains indicator of
        input state change and the current input content.

    .. wraps::
        bool InputScalar(
            const char* label,
            ImGuiDataType data_type,
            void* p_data,
            const void* p_step = NULL,
            const void* p_step_fast = NULL,
            const char* format = NULL,
            ImGuiInputTextFlags flags = 0
        )
    '''

def input_scalar_N(label: str,
                   data_type: DataType,
                   data: bytes,
                   components: int,
                   step: bytes | None = None,
                   step_fast: bytes | None = None,
                   format: str | None = None,
                   flags: TextInputFlags = INPUT_TEXT_NONE) -> tuple[int, bytes]:
    '''
    Display multiple scalar input widget.
    Data is passed via ``bytes`` and the type is separatelly given using ``data_type``.
    This is useful to work with specific types (e.g. unsigned 8bit integer, float, double)
    like when interfacing with Numpy.

    Args:
        label (str): widget label
        data_type: ImGuiDataType enum, type of the given data
        data (bytes): data value as a bytes array
        components (int): number of components to display
        step (bytes): incremental step
        step_fast (bytes): fast incremental step
        format (str): format string
        flags: InputText flags. See:
            :ref:`list of available flags <inputtext-flag-options>`.

    Returns:
        tuple: a ``(changed, value)`` tuple that contains indicator of
        input state change and the current input content.

    .. wraps::
        bool InputScalarN(
            const char* label,
            ImGuiDataType data_type,
            void* p_data,
            int components,
            const void* p_step = NULL,
            const void* p_step_fast = NULL,
            const char* format = NULL,
            ImGuiInputTextFlags flags = 0
        )
    '''

def slider_float(label: str,
                 value: float,
                 min_value: float,
                 max_value: float,
                 format: str = '%.3f',
                 flags: SliderFlags = SLIDER_FLAGS_NONE,
                 power: float = 1.0) -> tuple[bool, float]:
    '''
    Display float slider widget.
    Manually input values aren't clamped and can go off-bounds.

    .. visual-example::
        :auto_layout:
        :width: 400
        :height: 130

        value = 88.2

        imgui.begin('Example: slider float')
        changed, value = imgui.slider_float(
            'slide floats', value,
            min_value=0.0, max_value=100.0,
            format='%.0f'
        )
        imgui.text('Changed: %s, Value: %s' % (changed, value))
        imgui.end()

    Args:
        label (str): widget label.
        value (float): slider values.
        min_value (float): min value allowed by widget.
        max_value (float): max value allowed by widget.
        format (str): display format string as C-style ``printf``
            format string. **Warning:** highly unsafe.
            See :any:`slider_float()`.
        flags: SliderFlags flags. See:
            :ref:`list of available flags <slider-flag-options>`.
        power (float): OBSOLETED in ImGui 1.78 (from June 2020)

    Returns:
        tuple: a ``(changed, values)`` tuple that contains indicator of
        widget state change and the current slider value.

    .. wraps::
        bool SliderFloat(
            const char* label,
            float v,
            float v_min,
            float v_max,
            const char* format = '%.3f',
            ImGuiSliderFlags flags = 0
        )
    '''

def slider_float2(label: str,
                  value0: float,
                  value1: float,
                  min_value: float,
                  max_value: float,
                  format: str = '%.3f',
                  flags: SliderFlags = SLIDER_FLAGS_NONE,
                  power: float = 1.0) -> tuple[bool, tuple[float, float]]:
    '''
    Display float slider widget with 2 values.
    Manually input values aren't clamped and can go off-bounds.

    .. visual-example::
        :auto_layout:
        :width: 400
        :height: 130

        values = 88.2, 42.6

        imgui.begin('Example: slider float2')
        changed, values = imgui.slider_float2(
            'slide floats', *values,
            min_value=0.0, max_value=100.0,
            format='%.0f'
        )
        imgui.text('Changed: %s, Values: %s' % (changed, values))
        imgui.end()

    Args:
        label (str): widget label.
        value0, value1 (float): slider values.
        min_value (float): min value allowed by widget.
        max_value (float): max value allowed by widget.
        format (str): display format string as C-style ``printf``
            format string. **Warning:** highly unsafe.
            See :any:`slider_float()`.
        flags: SliderFlags flags. See:
            :ref:`list of available flags <slider-flag-options>`.
        power (float): OBSOLETED in ImGui 1.78 (from June 2020)

    Returns:
        tuple: a ``(changed, values)`` tuple that contains indicator of
        widget state change and the tuple of current slider values.

    .. wraps::
        bool SliderFloat2(
            const char* label,
            float v[2],
            float v_min,
            float v_max,
            const char* format = '%.3f',
            ImGuiSliderFlags flags = 0
        )

    '''

def slider_float3(label: str,
                  value0: float,
                  value1: float,
                  value2: float,
                  min_value: float,
                  max_value: float,
                  format: str = '%.3f',
                  flags: SliderFlags = SLIDER_FLAGS_NONE,
                  power: float = 1.0) -> tuple[bool, tuple[float, float, float]]:
    '''
    Display float slider widget with 3 values.
    Manually input values aren't clamped and can go off-bounds.

    .. visual-example::
        :auto_layout:
        :width: 400
        :height: 130

        values = 88.2, 42.6, 69.1

        imgui.begin('Example: slider float3')
        changed, values = imgui.slider_float3(
            'slide floats', *values,
            min_value=0.0, max_value=100.0,
            format='%.0f'
        )
        imgui.text('Changed: %s, Values: %s' % (changed, values))
        imgui.end()

    Args:
        label (str): widget label.
        value0, value1, value2 (float): slider values.
        min_value (float): min value allowed by widget.
        max_value (float): max value allowed by widget.
        format (str): display format string as C-style ``printf``
            format string. **Warning:** highly unsafe.
            See :any:`slider_float()`.
        flags: SliderFlags flags. See:
            :ref:`list of available flags <slider-flag-options>`.
        power (float): OBSOLETED in ImGui 1.78 (from June 2020)

    Returns:
        tuple: a ``(changed, values)`` tuple that contains indicator of
        widget state change and the tuple of current slider values.

    .. wraps::
        bool SliderFloat3(
            const char* label,
            float v[3],
            float v_min,
            float v_max,
            const char* format = '%.3f',
            ImGuiSliderFlags flags = 0
        )
    '''

def slider_float4(label: str,
                  value0: float,
                  value1: float,
                  value2: float,
                  value3: float,
                  min_value: float,
                  max_value: float,
                  format: str = '%.3f',
                  flags: SliderFlags = SLIDER_FLAGS_NONE,
                  power: float = 1.0) -> tuple[bool, tuple[float, float, float, float]]:
    '''
    Display float slider widget with 4 values.
    Manually input values aren't clamped and can go off-bounds.

    .. visual-example::
        :auto_layout:
        :width: 400
        :height: 130

        values = 88.2, 42.6, 69.1, 0.3

        imgui.begin('Example: slider float4')
        changed, values = imgui.slider_float4(
            'slide floats', *values,
            min_value=0.0, max_value=100.0,
            format='%.0f'
        )
        imgui.text('Changed: %s, Values: %s' % (changed, values))
        imgui.end()

    Args:
        label (str): widget label.
        value0, value1, value2, value3 (float): slider values.
        min_value (float): min value allowed by widget.
        max_value (float): max value allowed by widget.
        format (str): display format string as C-style ``printf``
            format string. **Warning:** highly unsafe.
            See :any:`slider_float()`.
        flags: SliderFlags flags. See:
            :ref:`list of available flags <slider-flag-options>`.
        power (float): OBSOLETED in ImGui 1.78 (from June 2020)

    Returns:
        tuple: a ``(changed, values)`` tuple that contains indicator of
        widget state change and the tuple of current slider values.

    .. wraps::
        bool SliderFloat4(
            const char* label,
            float v[4],
            float v_min,
            float v_max,
            const char* format = '%.3f',
            ImGuiSliderFlags flags = 0
        )
    '''

def slider_angle(label: str,
                 rad_value: float,
                 value_degrees_min: float = -360.0,
                 value_degrees_max: float = 360.0,
                 format: str = '%.0f deg',
                 flags: SliderFlags = SLIDER_FLAGS_NONE) -> tuple[bool, float]:
    '''
    Display angle slider widget.

    .. visual-example::
        :auto_layout:
        :width: 400
        :height: 130

        radian = 3.1415/4

        imgui.begin('Example: slider angle')
        changed, radian = imgui.slider_angle(
            'slider angle', radian,
            value_degrees_min=0.0, value_degrees_max=180.0)
        imgui.text('Changed: %s, Value: %s' % (changed, radian))
        imgui.end()

    Args:
        labal (str): widget label
        rad_value (float): slider value in radian
        value_degrees_min (float): min value allowed in degrees
        value_degrees_max (float): max value allowed in degrees
        format (str): display format string as C-style ``printf``
            format string. **Warning:** highly unsafe.
        flags: SliderFlags flags. See:
            :ref:`list of available flags <slider-flag-options>`.

    Returns:
        tuple: a ``(changed, rad_value)`` tuple that contains indicator of
        widget state change and the current slider value in radian.


    .. wraps::
        bool SliderAngle(
            const char* label,
            float* v_rad, float
            v_degrees_min = -360.0f,
            float v_degrees_max = +360.0f,
            const char* format = '%.0f deg',
            ImGuiSliderFlags flags = 0
        )

    '''

def slider_int(label: str,
               value: int,
               min_value: int,
               max_value: int,
               format: str = '%.3f',
               flags: SliderFlags = SLIDER_FLAGS_NONE) -> tuple[bool, int]:
    '''
    Display int slider widget

    .. visual-example::
        :auto_layout:
        :width: 400
        :height: 130

        value = 88

        imgui.begin('Example: slider int')
        changed, values = imgui.slider_int(
            'slide ints', value,
            min_value=0, max_value=100,
            format='%d'
        )
        imgui.text('Changed: %s, Values: %s' % (changed, value))
        imgui.end()

    Args:
        label (str): widget label.
        value (int): slider value.
        min_value (int): min value allowed by widget.
        max_value (int): max value allowed by widget.
        format (str): display format string as C-style ``printf``
            format string. **Warning:** highly unsafe.
            See :any:`slider_int()`.
        flags: SliderFlags flags. See:
            :ref:`list of available flags <slider-flag-options>`.

    Returns:
        tuple: a ``(changed, value)`` tuple that contains indicator of
        widget state change and the slider value.

    .. wraps::
        bool SliderInt(
            const char* label,
            int v,
            int v_min,
            int v_max,
            const char* format = '%.3f',
            ImGuiSliderFlags flags = 0
        )
    '''

def slider_int2(label: str,
                value0: int,
                value1: int,
                min_value: int,
                max_value: int,
                format: str = '%.3f',
                flags: SliderFlags = SLIDER_FLAGS_NONE) -> tuple[bool, tuple[int, int]]:
    '''
    Display int slider widget with 2 values.

    .. visual-example::
        :auto_layout:
        :width: 400
        :height: 130

        values = 88, 27

        imgui.begin('Example: slider int2')
        changed, values = imgui.slider_int2(
            'slide ints2', *values,
            min_value=0, max_value=100,
            format='%d'
        )
        imgui.text('Changed: %s, Values: %s' % (changed, values))
        imgui.end()

    Args:
        label (str): widget label.
        value0, value1 (int): slider values.
        min_value (int): min value allowed by widget.
        max_value (int): max value allowed by widget.
        format (str): display format string as C-style ``printf``
            format string. **Warning:** highly unsafe.
            See :any:`slider_int()`.
        flags: SliderFlags flags. See:
            :ref:`list of available flags <slider-flag-options>`.

    Returns:
        tuple: a ``(changed, values)`` tuple that contains indicator of
        widget state change and the tuple of current slider values.

    .. wraps::
        bool SliderInt2(
            const char* label,
            int v[2],
            int v_min,
            int v_max,
            const char* format = '%.3f',
            ImGuiSliderFlags flags = 0
        )
    '''

def slider_int3(label: str,
                value0: int,
                value1: int,
                value2: int,
                min_value: int,
                max_value: int,
                format: str = '%.3f',
                flags: SliderFlags = SLIDER_FLAGS_NONE) -> tuple[bool, tuple[int, int, int]]:
    '''
    Display int slider widget with 3 values.

    .. visual-example::
        :auto_layout:
        :width: 400
        :height: 130

        values = 88, 27, 3

        imgui.begin('Example: slider int3')
        changed, values = imgui.slider_int3(
            'slide ints3', *values,
            min_value=0, max_value=100,
            format='%d'
        )
        imgui.text('Changed: %s, Values: %s' % (changed, values))
        imgui.end()

    Args:
        label (str): widget label.
        value0, value1, value2 (int): slider values.
        min_value (int): min value allowed by widget.
        max_value (int): max value allowed by widget.
        format (str): display format string as C-style ``printf``
            format string. **Warning:** highly unsafe.
            See :any:`slider_int()`.
        flags: SliderFlags flags. See:
            :ref:`list of available flags <slider-flag-options>`.

    Returns:
        tuple: a ``(changed, values)`` tuple that contains indicator of
        widget state change and the tuple of current slider values.

    .. wraps::
        bool SliderInt3(
            const char* label,
            int v[3],
            int v_min,
            int v_max,
            const char* format = '%.3f',
            ImGuiSliderFlags flags = 0
        )
    '''

def slider_int4(label: str,
                value0: int,
                value1: int,
                value2: int,
                value3: int,
                min_value: int,
                max_value: int,
                format: str = '%.3f',
                flags: SliderFlags = SLIDER_FLAGS_NONE) -> tuple[bool, tuple[int, int, int, int]]:
    '''
    Display int slider widget with 4 values.

    .. visual-example::
        :auto_layout:
        :width: 400
        :height: 130

        values = 88, 42, 69, 0

        imgui.begin('Example: slider int4')
        changed, values = imgui.slider_int4(
            'slide ints', *values,
            min_value=0, max_value=100, format='%d'
        )
        imgui.text('Changed: %s, Values: %s' % (changed, values))
        imgui.end()

    Args:
        label (str): widget label.
        value0, value1, value2, value3 (int): slider values.
        min_value (int): min value allowed by widget.
        max_value (int): max value allowed by widget.
        format (str): display format string as C-style ``printf``
            format string. **Warning:** highly unsafe.
            See :any:`slider_int()`.
        flags: SliderFlags flags. See:
            :ref:`list of available flags <slider-flag-options>`.

    Returns:
        tuple: a ``(changed, values)`` tuple that contains indicator of
        widget state change and the tuple of current slider values.

    .. wraps::
        bool SliderInt4(
            const char* label,
            int v[4],
            int v_min,
            int v_max,
            const char* format = '%.3f',
            ImGuiSliderFlags flags = 0
        )
    '''

def slider_scalar(label: str,
                  data_type: DataType,
                  data: bytes,
                  min_value: bytes,
                  max_value: bytes,
                  format: str | None = None,
                  flags: SliderFlags = SLIDER_FLAGS_NONE) -> tuple[bool, bytes]:
    '''
    Display scalar slider widget.
    Data is passed via ``bytes`` and the type is separatelly given using ``data_type``.
    This is useful to work with specific types (e.g. unsigned 8bit integer, float, double)
    like when interfacing with Numpy.

    Args:
        label (str): widget label
        data_type: ImGuiDataType enum, type of the given data
        data (bytes): data value as a bytes array
        min_value (bytes): min value allowed by widget
        max_value (bytes): max value allowed by widget
        format (str): display format string as C-style ``printf``
            format string. **Warning:** highly unsafe. See :any:`drag_int()`.
        flags: ImGuiSlider flags. See:
            :ref:`list of available flags <slider-flag-options>`.

    Returns:
        tuple: a ``(changed, value)`` tuple that contains indicator of
        slider state change and the current slider content.

    .. wraps::
        bool SliderScalar(
            const char* label,
            ImGuiDataType data_type,
            void* p_data,
            const void* p_min,
            const void* p_max,
            const char* format = NULL,
            ImGuiSliderFlags flags = 0
        )
    '''

def slider_scalar_N(label: str,
                    data_type: DataType,
                    data: bytes,
                    components: int,
                    min_value: bytes,
                    max_value: bytes,
                    format: str | None = None,
                    flags: SliderFlags = SLIDER_FLAGS_NONE) -> tuple[bool, bytes]:
    '''
    Display multiple scalar slider widget.
    Data is passed via ``bytes`` and the type is separatelly given using ``data_type``.
    This is useful to work with specific types (e.g. unsigned 8bit integer, float, double)
    like when interfacing with Numpy.

    Args:
        label (str): widget label
        data_type: ImGuiDataType enum, type of the given data
        data (bytes): data value as a bytes array
        components (int): number of widgets
        min_value (bytes): min value allowed by widget
        max_value (bytes): max value allowed by widget
        format (str): display format string as C-style ``printf``
            format string. **Warning:** highly unsafe. See :any:`drag_int()`.
        flags: ImGuiSlider flags. See:
            :ref:`list of available flags <slider-flag-options>`.

    Returns:
        tuple: a ``(changed, value)`` tuple that contains indicator of
        slider state change and the current slider content.

    .. wraps::
        bool SliderScalarN(
            const char* label,
            ImGuiDataType data_type,
            void* p_data,
            int components,
            const void* p_min,
            const void* p_max,
            const char* format = NULL,
            ImGuiSliderFlags flags = 0
        )
    '''

def v_slider_float(label: str,
                   width: float,
                   height: float,
                   value: float,
                   min_value: float,
                   max_value: float,
                   format: str = '%.f',
                   flags: SliderFlags = SLIDER_FLAGS_NONE) -> tuple[bool, float]:
    '''
    Display vertical float slider widget with the specified width and
    height.

    .. visual-example::
        :auto_layout:
        :width: 400
        :height: 130

        width = 20
        height = 100
        value = 88

        imgui.begin('Example: vertical slider float')
        changed, values = imgui.v_slider_float(
            'vertical slider float',
            width, height, value,
            min_value=0, max_value=100,
            format='%0.3f', flags=imgui.SLIDER_FLAGS_NONE
        )
        imgui.text('Changed: %s, Values: %s' % (changed, values))
        imgui.end()

    Args:
        label (str): widget label.
        value (float): slider value.
        min_value (float): min value allowed by widget.
        max_value (float): max value allowed by widget.
        format (str): display format string as C-style ``printf``
            format string. **Warning:** highly unsafe.
            See :any:`slider_float()`.
        flags: SliderFlags flags. See:
            :ref:`list of available flags <slider-flag-options>`.

    Returns:
        tuple: a ``(changed, value)`` tuple that contains indicator of
        widget state change and the slider value.

    .. wraps::
        bool VSliderFloat(
            const char* label,
            const ImVec2& size,
            float v,
            float v_min,
            floatint v_max,
            const char* format = '%.3f',
            ImGuiSliderFlags flags = 0
        )
    '''

def v_slider_int(label: str,
                 width: float,
                 height: float,
                 value: int,
                 min_value: int,
                 max_value: int,
                 format: str = '%d',
                 flags: SliderFlags = SLIDER_FLAGS_NONE) -> tuple[bool, int]:
    '''
    Display vertical int slider widget with the specified width and height.

    .. visual-example::
        :auto_layout:
        :width: 400
        :height: 130

        width = 20
        height = 100
        value = 88

        imgui.begin('Example: vertical slider int')
        changed, values = imgui.v_slider_int(
            'vertical slider int',
            width, height, value,
            min_value=0, max_value=100,
            format='%d'
        )
        imgui.text('Changed: %s, Values: %s' % (changed, values))
        imgui.end()

    Args:
        label (str): widget label.
        value (int): slider value.
        min_value (int): min value allowed by widget.
        max_value (int): max value allowed by widget.
        format (str): display format string as C-style ``printf``
            format string. **Warning:** highly unsafe.
            See :any:`slider_int()`.
        flags: SliderFlags flags. See:
            :ref:`list of available flags <slider-flag-options>`.

    Returns:
        tuple: a ``(changed, value)`` tuple that contains indicator of
        widget state change and the slider value.

    .. wraps::
        bool VSliderInt(
            const char* label,
            const ImVec2& size,
            int v,
            int v_min,
            int v_max,
            const char* format = '%.3f',
            ImGuiSliderFlags flags = 0
        )
    '''

def v_slider_scalar(label: str,
                    width: float,
                    height: float,
                    data_type: DataType,
                    data: bytes,
                    min_value: bytes,
                    max_value: bytes,
                    format: str | None = None,
                    flags: SliderFlags = SLIDER_FLAGS_NONE) -> tuple[bool, bytes]:
    '''
    Display vertical scalar slider widget.
    Data is passed via ``bytes`` and the type is separatelly given using ``data_type``.
    This is useful to work with specific types (e.g. unsigned 8bit integer, float, double)
    like when interfacing with Numpy.

    Args:
        label (str): widget label
        width (float): width of the slider
        height (float): height of the slider
        data_type: ImGuiDataType enum, type of the given data
        data (bytes): data value as a bytes array
        min_value (bytes): min value allowed by widget
        max_value (bytes): max value allowed by widget
        format (str): display format string as C-style ``printf``
            format string. **Warning:** highly unsafe. See :any:`drag_int()`.
        flags: ImGuiSlider flags. See:
            :ref:`list of available flags <slider-flag-options>`.

    Returns:
        tuple: a ``(changed, value)`` tuple that contains indicator of
        slider state change and the current slider content.

    .. wraps::
        bool VSliderScalar(
            const char* label,
            const ImVec2& size,
            ImGuiDataType data_type,
            void* p_data,
            const void* p_min,
            const void* p_max,
            const char* format = NULL,
            ImGuiSliderFlags flags = 0
        )
    '''

def plot_lines(label: str,
               values: _Buffer, # TODO `plot_lines:values` accept only buffer of floats
               values_count: int = -1,
               values_offset: int = 0,
               overlay_text: str | None = None,
               scale_min: float = _sys.float_info.max,
               scale_max: float = _sys.float_info.min,
               graph_size: tuple[float, float] = (0.0, 0.0),
               stride: int = _ct.sizeof(_ct.c_float)) -> None:
    '''
    Plot a 1D array of float values.

    Args:
        label (str): A plot label that will be displayed on the plot's right
            side. If you want the label to be invisible, add :code:`'##'`
            before the label's text: :code:`'my_label' -> '##my_label'`

        values (array of floats): the y-values.
            It must be a type that supports Cython's Memoryviews,
            (See: http://docs.cython.org/en/latest/src/userguide/memoryviews.html)
            for example a numpy array.

        overlay_text (str or None, optional): Overlay text.

        scale_min (float, optional): y-value at the bottom of the plot.
        scale_max (float, optional): y-value at the top of the plot.

        graph_size (tuple of two floats, optional): plot size in pixels.
            **Note:** In ImGui 1.49, (-1,-1) will NOT auto-size the plot.
            To do that, use :func:`get_content_region_available` and pass
            in the right size.

    **Note:** These low-level parameters are exposed if needed for
    performance:

    * **values_offset** (*int*): Index of first element to display
    * **values_count** (*int*): Number of values to display. -1 will use the
        entire array.
    * **stride** (*int*): Number of bytes to move to read next element.

    .. visual-example::
        :auto_layout:
        :width: 400
        :height: 130

        from array import array
        from math import sin
        # NOTE: this example will not work under py27 due do incompatible
        # implementation of array and memoryview().
        plot_values = array('f', [sin(x * 0.1) for x in range(100)])

        imgui.begin('Plot example')
        imgui.plot_lines('Sin(t)', plot_values)
        imgui.end()

    .. wraps::
            void PlotLines(
                const char* label, const float* values, int values_count,

                int values_offset = 0,
                const char* overlay_text = NULL,
                float scale_min = FLT_MAX,
                float scale_max = FLT_MAX,
                ImVec2 graph_size = ImVec2(0,0),
                int stride = sizeof(float)
            )
    '''

def plot_histogram(label: str,
                   values: _Buffer, # TODO `plot_histogram:values` accept only buffer of floats
                   values_count: int = -1,
                   values_offset: int = 0,
                   overlay_text: str | None = None,
                   scale_min: float = _sys.float_info.max,
                   scale_max: float = _sys.float_info.min,
                   stride: int = _ct.sizeof(_ct.c_float)) -> None:
    '''
    Plot a histogram of float values.

    Args:
        label (str): A plot label that will be displayed on the plot's right
            side. If you want the label to be invisible, add :code:`'##'`
            before the label's text: :code:`'my_label' -> '##my_label'`

        values (array of floats): the y-values.
            It must be a type that supports Cython's Memoryviews,
            (See: http://docs.cython.org/en/latest/src/userguide/memoryviews.html)
            for example a numpy array.

        overlay_text (str or None, optional): Overlay text.

        scale_min (float, optional): y-value at the bottom of the plot.
        scale_max (float, optional): y-value at the top of the plot.

        graph_size (tuple of two floats, optional): plot size in pixels.
            **Note:** In ImGui 1.49, (-1,-1) will NOT auto-size the plot.
            To do that, use :func:`get_content_region_available` and pass
            in the right size.

    **Note:** These low-level parameters are exposed if needed for
    performance:

    * **values_offset** (*int*): Index of first element to display
    * **values_count** (*int*): Number of values to display. -1 will use the
        entire array.
    * **stride** (*int*): Number of bytes to move to read next element.

    .. visual-example::
        :auto_layout:
        :width: 400
        :height: 130

        from array import array
        from random import random

        # NOTE: this example will not work under py27 due do incompatible
        # implementation of array and memoryview().
        histogram_values = array('f', [random() for _ in range(20)])

        imgui.begin('Plot example')
        imgui.plot_histogram('histogram(random())', histogram_values)
        imgui.end()

    .. wraps::
            void PlotHistogram(
                const char* label, const float* values, int values_count,
                # note: optional
                int values_offset,
                const char* overlay_text,
                float scale_min,
                float scale_max,
                ImVec2 graph_size,
                int stride
            )
    '''

def progress_bar(fraction: float,
                 size: tuple[float, float] = (-_sys.float_info.min, 0.0),
                 overlay: str = '') -> None:
    '''
    Show a progress bar.

    .. visual-example::
        :auto_layout:
        :width: 400
        :height: 200

        imgui.begin('Progress bar example')
        imgui.progress_bar(0.7, (100,20), 'Overlay text')
        imgui.end()

    Args:
        fraction (float): A floating point number between 0.0 and 1.0
            0.0 means no progress and 1.0 means progress is completed
        size : a tuple (width, height) that sets the width and height
            of the progress bar
        overlay (str): Optional text that will be shown in the progress bar

    .. wraps::
        void ProgressBar(
            float fraction,
            const ImVec2& size_arg = ImVec2(-FLT_MIN, 0),
            const char* overlay = NULL
        )
    '''

def is_window_appearing() -> bool:
    '''
    Check if current window is appearing.

    Returns:
        bool: True if window is appearing
    '''

def set_item_default_focus() -> None:
    '''
    Make last item the default focused item of a window.
    Please use instead of 'if (is_window_appearing()) set_scroll_here()' to signify 'default item'.

    .. wraps::
        void SetItemDefaultFocus()
    '''

def set_keyboard_focus_here(offset: int = 0) -> None:
    '''
    Focus keyboard on the next widget.
    Use positive 'offset' to access sub components of a multiple component widget. Use -1 to access previous widget.

    .. wraps::
        void SetKeyboardFocusHere(int offset = 0)
    '''

def is_item_hovered(flags: int = 0) -> bool:
    '''
    Check if the last item is hovered by mouse.

    Returns:
        bool: True if item is hovered by mouse, otherwise False.

    .. wraps::
        bool IsItemHovered(ImGuiHoveredFlags flags = 0)
    '''

def is_item_focused() -> bool:
    '''
    Check if the last item is focused

    Returns:
        bool: True if item is focused, otherwise False.

    .. wraps::
        bool IsItemFocused()
    '''

def is_item_active() -> bool:
    '''
    Was the last item active? For ex. button being held or text field
    being edited. Items that don't interact will always return false.

    Returns:
        bool: True if item is active, otherwise False.

    .. wraps::
        bool IsItemActive()
    '''

def is_item_clicked(mouse_button: int = 0) -> bool:
    '''
    Was the last item hovered and mouse clicked on?
    Button or node that was just being clicked on.

    Args:
        mouse_button: ImGuiMouseButton

    Returns:
        bool: True if item is clicked, otherwise False.

    .. wraps::
        bool IsItemClicked(int mouse_button = 0)
    '''

def is_item_visible() -> bool:
    '''
    Was the last item visible? Aka not out of sight due to
    clipping/scrolling.

    Returns:
        bool: True if item is visible, otherwise False.

    .. wraps::
        bool IsItemVisible()
    '''

def is_item_edited() -> bool:
    '''
    Did the last item modify its underlying value this frame? or was pressed?
    This is generally the same as the 'bool' return value of many widgets.

    Returns:
        bool: True if item is edited, otherwise False.

    .. wraps::
        bool IsItemEdited()
    '''

def is_item_activated() -> bool:
    '''
    Was the last item just made active (item was previously inactive)?

    Returns:
        bool: True if item was just made active

    .. wraps::
        bool IsItemActivated()
    '''

def is_item_deactivated() -> bool:
    '''
    Was the last item just made inactive (item was previously active)?
    Useful for Undo/Redo patterns with widgets that requires continuous editing.

    Results:
        bool: True if item just made inactive

    .. wraps:
        bool IsItemDeactivated()
    '''

def is_item_deactivated_after_edit() -> bool:
    '''
    Was the last item just made inactive and made a value change when it was active? (e.g. Slider/Drag moved).
    Useful for Undo/Redo patterns with widgets that requires continuous editing.
    Note that you may get false positives (some widgets such as Combo()/ListBox()/Selectable() will return true even when clicking an already selected item).

    Results:
        bool: True if item just made inactive after an edition

    .. wraps::
        bool IsItemDeactivatedAfterEdit()
    '''

def is_item_toggled_open() -> bool:
    '''
    Was the last item open state toggled? set by TreeNode().

    .. wraps::
        bool IsItemToggledOpen()
    '''

def is_any_item_hovered() -> bool:
    '''
    Was any of the items hovered.

    Returns:
        bool: True if any item is hovered, otherwise False.

    .. wraps::
        bool IsAnyItemHovered()
    '''


def is_any_item_active() -> bool:
    '''
    Was any of the items active.

    Returns:
        bool: True if any item is active, otherwise False.

    .. wraps::
        bool IsAnyItemActive()
    '''


def is_any_item_focused() -> bool:
    '''
    Is any of the items focused.

    Returns:
        bool: True if any item is focused, otherwise False.

    .. wraps::
        bool IsAnyItemFocused()
    '''

def get_item_rect_min() -> Vec2:
    '''
    Get bounding rect of the last item in screen space.

    Returns:
        Vec2: item minimum boundaries two-tuple ``(width, height)``

    .. wraps::
        ImVec2 GetItemRectMin()
    '''


def get_item_rect_max() -> Vec2:
    '''
    Get bounding rect of the last item in screen space.

    Returns:
        Vec2: item maximum boundaries two-tuple ``(width, height)``

    .. wraps::
        ImVec2 GetItemRectMax()
    '''


def get_item_rect_size() -> Vec2:
    '''
    Get bounding rect of the last item in screen space.

    Returns:
        Vec2: item boundaries two-tuple ``(width, height)``

    .. wraps::
        ImVec2 GetItemRectSize()
    '''

def set_item_allow_overlap() -> None:
    '''
    Allow last item to be overlapped by a subsequent item.
    Sometimes useful with invisible buttons, selectables, etc.
    to catch unused area.

    .. wraps::
        void SetItemAllowOverlap()
    '''

def get_main_viewport() -> _ImGuiViewport:
    '''
    Currently represents the Platform Window created by the application which is hosting
    our Dear ImGui windows.

    In the future we will extend this concept further to also represent Platform Monitor
    and support a 'no main platform window' operation mode.

    Returns:
        _ImGuiViewport: Viewport

    .. wraps::
        ImGuiViewport* GetMainViewport()
    '''

def is_window_hovered(flags: HoverFlags = HOVERED_NONE) -> bool:
    '''
    Is current window hovered and hoverable (not blocked by a popup).
    Differentiate child windows from each others.

    Returns:
        bool: True if current window is hovered, otherwise False.

    .. wraps::
        bool IsWindowHovered(ImGuiFocusedFlags flags = 0)
    '''

def is_window_focused(flags: FocusFlags = FOCUS_NONE) -> bool:
    '''
    Is current window focused.

    Returns:
        bool: True if current window is on focus, otherwise False.

    .. wraps::
        bool IsWindowFocused(ImGuiFocusedFlags flags = 0)
    '''


def is_rect_visible(size_width: float, size_height: float) -> bool:
    '''
    Test if a rectangle of the given size, starting from the cursor
    position is visible (not clipped).

    Args:
        size_width (float): width of the rect
        size_height (float): height of the rect

    Returns:
        bool: True if rect is visible, otherwise False.

    .. wraps::
        bool IsRectVisible(const ImVec2& size)
    '''

def get_style_color_name(index: int) -> str:
    '''
    Get the style color name for a given ImGuiCol index.

    .. wraps::
        const char* GetStyleColorName(ImGuiCol idx)
    '''

def get_time() -> float:
    '''Seconds since program start.

    Returns:
        float: the time (seconds since program start)

    .. wraps::
        float GetTime()
    '''


def get_background_draw_list() -> _DrawList:
    '''
    This draw list will be the first rendering one.
    Useful to quickly draw shapes/text behind dear imgui contents.

    Returns:
        DrawList*

    .. wraps::
        ImDrawList* GetBackgroundDrawList()
    '''

def get_foreground_draw_list() -> _DrawList:
    '''
    This draw list will be the last rendered one.
    Useful to quickly draw shapes/text over dear imgui contents.

    Returns:
        DrawList*

    .. wraps::
        ImDrawList* GetForegroundDrawList()
    '''

def get_key_index(key: int) -> int:
    '''
    Map ImGuiKey_* values into user's key index. == io.KeyMap[key]

    Returns:
       int: io.KeyMap[key]

    .. wraps::
        int GetKeyIndex(ImGuiKey imgui_key)
    '''

def is_key_pressed(key_index: int, repeat: bool = False) -> bool:
    '''
    Was key pressed (went from !Down to Down).
    If repeat=true, uses io.KeyRepeatDelay / KeyRepeatRate

    Returns:
        bool: True if specified key was pressed this frame

    .. wraps::
        bool IsKeyPressed(int user_key_index)
    '''


def is_key_down(key_index: int) -> bool:
    '''
    Returns if key is being held -- io.KeysDown[user_key_index].
    Note that imgui doesn't know the semantic of each entry of
    io.KeysDown[]. Use your own indices/enums according to how
    your backend/engine stored them into io.KeysDown[]!

    Returns:
        bool: True if specified key is being held.

    .. wraps::
        bool IsKeyDown(int user_key_index)
    '''

def is_mouse_hovering_rect(r_min_x: float,
                           r_min_y: float,
                           r_max_x: float,
                           r_max_y: float,
                           clip: bool = True) -> bool:
    '''
    Test if mouse is hovering rectangle with given coordinates.

    Args:
        r_min_x, r_min_y (float): x,y coordinate of the upper-left corner
        r_max_x, r_max_y (float): x,y coordinate of the lower-right corner

    Returns:
        bool: True if mouse is hovering the rectangle.

    .. wraps::
        bool IsMouseHoveringRect(
            const ImVec2& r_min,
            const ImVec2& r_max,
            bool clip = true
        )
    '''

def is_mouse_double_clicked(button: int = 0) -> bool:
    '''
    Return True if mouse was double-clicked.

    **Note:** A double-click returns false in IsMouseClicked().

    Args:
        button (int): mouse button index.

    Returns:
        bool: if mouse is double clicked.

    .. wraps::
         bool IsMouseDoubleClicked(int button);
    '''

def is_mouse_clicked(button: int = 0, repeat: bool = False) -> bool:
    '''Returns if the mouse was clicked this frame.

    Args:
        button (int): mouse button index.
        repeat (float):

    Returns:
        bool: if the mouse was clicked this frame.

    .. wraps::
        bool IsMouseClicked(int button, bool repeat = false)
    '''

def is_mouse_released(button: int = 0) -> bool:
    '''
    Returns if the mouse was released this frame.

    Args:
        button (int): mouse button index.

    Returns:
        bool: if the mouse was released this frame.

    .. wraps::
        bool IsMouseReleased(int button)
    '''


def is_mouse_down(button: int = 0) -> bool:
    '''
    Returns if the mouse is down.

    Args:
        button (int): mouse button index.

    Returns:
        bool: if the mouse is down.

    .. wraps::
        bool IsMouseDown(int button)
    '''


def is_mouse_dragging(button: int,
                      lock_threshold: float = -1.0) -> bool:
    '''
    Returns if mouse is dragging.

    Args:
        button (int): mouse button index.
        lock_threshold (float): if less than -1.0
            uses io.MouseDraggingThreshold.

    Returns:
        bool: if mouse is dragging.

    .. wraps::
        bool IsMouseDragging(int button = 0, float lock_threshold = -1.0f)
    '''

def get_mouse_drag_delta(button: int = 0,
                         lock_threshold: float = -1.0) -> Vec2:
    '''
    Dragging amount since clicking.

    Args:
        button (int): mouse button index.
        lock_threshold (float): if less than -1.0
            uses io.MouseDraggingThreshold.

    Returns:
        Vec2: mouse position two-tuple ``(x, y)``

    .. wraps::
        ImVec2 GetMouseDragDelta(int button = 0, float lock_threshold = -1.0f)
    '''

def get_mouse_pos() -> Vec2:
    '''
    Current mouse position.

    Returns:
        Vec2: mouse position two-tuple ``(x, y)``

    .. wraps::
        ImVec2 GetMousePos()
    '''

def get_mouse_position() -> Vec2:
    '''
    Current mouse position.

    Returns:
        Vec2: mouse position two-tuple ``(x, y)``

    .. wraps::
        ImVec2 GetMousePos()
    '''

def reset_mouse_drag_delta(button: int = 0) -> None:
    '''Reset the mouse dragging delta.

    Args:
        button (int): mouse button index.

    .. wraps::
        void ResetMouseDragDelta(int button = 0)
    '''

def get_mouse_cursor() -> int:
    '''
    Return the mouse cursor id.

    .. wraps::
        ImGuiMouseCursor GetMouseCursor()
    '''

def set_mouse_cursor(mouse_cursor_type: int) -> None:
    '''
    Set the mouse cursor id.

    Args:
        mouse_cursor_type (ImGuiMouseCursor): mouse cursor type.

    .. wraps::
        void SetMouseCursor(ImGuiMouseCursor type)
    '''

def capture_mouse_from_app(want_capture_mouse_value: bool = True) -> None:
    '''
    Attention: misleading name!
    Manually override io.WantCaptureMouse flag next frame
    (said flag is entirely left for your application to handle).

    This is equivalent to setting 'io.WantCaptureMouse = want_capture_mouse_value;'
    after the next NewFrame() call.

    .. wraps::
        void CaptureMouseFromApp(bool want_capture_mouse_value = true)
    '''

def get_clipboard_text() -> str:
    '''
    Also see the ``log_to_clipboard()`` function to capture GUI into clipboard,
    or easily output text data to the clipboard.

    Returns:
        str: Text content of the clipboard

    .. wraps::
        const char* GetClipboardText()
    '''

def load_ini_settings_from_disk(ini_file_name: str) -> None:
    '''
    Call after ``create_context()`` and before the first call to ``new_frame()``.
    ``new_frame()`` automatically calls ``load_ini_settings_from_disk(io.ini_file_name)``.

    Args:
        ini_file_name (str): Filename to load settings from.

    .. wraps::
        void LoadIniSettingsFromDisk(const char* ini_filename)
    '''

def load_ini_settings_from_memory(ini_data: str) -> None:
    '''
    Call after ``create_context()`` and before the first call to ``new_frame()``
    to provide .ini data from your own data source.

    .. wraps::
        void LoadIniSettingsFromMemory(const char* ini_data, size_t ini_size=0)
    '''

def save_ini_settings_to_disk(ini_file_name: str) -> None:
    '''
    This is automatically called (if ``io.ini_file_name`` is not empty)
    a few seconds after any modification that should be reflected in the .ini file
    (and also by ``destroy_context``).

    Args:
        ini_file_name (str): Filename to save settings to.

    .. wraps::
        void SaveIniSettingsToDisk(const char* ini_filename)
    '''

def save_ini_settings_to_memory() -> str:
    '''
    Return a string with the .ini data which you can save by your own mean.
    Call when ``io.want_save_ini_settings`` is set, then save data by your own mean
    and clear ``io.want_save_ini_settings``.

    Returns:
        str: Settings data

    .. wraps::
       const char* SaveIniSettingsToMemory(size_t* out_ini_size = NULL)
    '''

def set_clipboard_text(text: str) -> None:
    '''
    Set the clipboard content

    Args:
        text (str): Text to copy in clipboard

    .. wraps:
        void SetClipboardText(const char* text)
    '''

def set_scroll_here_x(center_x_ratio: float = 0.5) -> None:
    '''Set scroll here X.

    Adjust scrolling amount to make current cursor position visible.
    center_x_ratio =
    0.0: left,
    0.5: center,
    1.0: right.

    When using to make a 'default/current item' visible, consider using SetItemDefaultFocus() instead.

    Args:
        float center_x_ratio = 0.5f

    .. wraps::
        void SetScrollHereX(float center_x_ratio = 0.5f)
    '''

def set_scroll_here_y(center_y_ratio: float = 0.5) -> None:
    '''
    Set scroll here Y.

    Adjust scrolling amount to make current cursor position visible.
    center_y_ratio =
    0.0: top,
    0.5: center,
    1.0: bottom.

    When using to make a 'default/current item' visible, consider using SetItemDefaultFocus() instead.

    Args:
        float center_y_ratio = 0.5f

    .. wraps::
        void SetScrollHereY(float center_y_ratio = 0.5f)
    '''

def set_scroll_from_pos_x(local_x: float,
                          center_x_ratio: float = 0.5) -> None:
    '''
    Set scroll from position X

    Adjust scrolling amount to make given position visible.
    Generally GetCursorStartPos() + offset to compute a valid position.

    Args:
        float local_x
        float center_x_ratio = 0.5f

    .. wraps::
        void SetScrollFromPosX(float local_x, float center_x_ratio = 0.5f)
    '''

def set_scroll_from_pos_y(local_y: float,
                          center_y_ratio: float = 0.5) -> None:
    '''
    Set scroll from position Y

    Adjust scrolling amount to make given position visible.
    Generally GetCursorStartPos() + offset to compute a valid position.

    Args:
        float local_y
        float center_y_ratio = 0.5f

    .. wraps::
        void SetScrollFromPosY(float local_y, float center_y_ratio = 0.5f)
    '''

def push_font(font: _Font) -> None:
    '''
    Push font on a stack.

    .. visual-example::
        :auto_layout:
        :height: 100
        :width: 320

        io = imgui.get_io()

        new_font = io.fonts.add_font_from_file_ttf(
            'DroidSans.ttf', 20,
        )
        impl.refresh_font_texture()

        # later in frame code

        imgui.begin('Default Window')

        imgui.text('Text displayed using default font')

        imgui.push_font(new_font)
        imgui.text('Text displayed using custom font')
        imgui.pop_font()

        imgui.end()

    **Note:** Pushed fonts should be poped with :func:`pop_font()` within the
    same frame. In order to avoid manual push/pop functions you can use the
    :func:`font()` context manager.

    Args:
        font (_Font): font object retrieved from :any:`add_font_from_file_ttf`.

    .. wraps::
        void PushFont(ImFont*)
    '''

def pop_font() -> _Font:
    '''
    Pop font on a stack.

    For example usage see :func:`push_font()`.

    Args:
        font (_Font): font object retrieved from :any:`add_font_from_file_ttf`.

    .. wraps::
        void PopFont()
    '''

def calc_text_size(text: str,
                   hide_text_after_double_hash: bool = False,
                   wrap_width: float = -1.0) -> Vec2:
    '''
    Calculate text size.
    Text can be multi-line.
    Optionally ignore text after a ## marker.

    .. visual-example::
        :auto_layout:
        :width: 300
        :height: 100

        imgui.begin('Text size calculation')
        text_content = 'This is a ##text##!'
        text_size1 = imgui.calc_text_size(text_content)
        imgui.text(''%s' has size %ix%i' % (text_content, text_size1[0], text_size1[1]))
        text_size2 = imgui.calc_text_size(text_content, True)
        imgui.text(''%s' has size %ix%i' % (text_content, text_size2[0], text_size2[1]))
        text_size3 = imgui.calc_text_size(text_content, False, 30.0)
        imgui.text(''%s' has size %ix%i' % (text_content, text_size3[0], text_size3[1]))
        imgui.end()

    Args:
        text (str): text
        hide_text_after_double_hash (bool): if True, text after '##' is ignored
        wrap_width (float): if > 0.0 calculate size using text wrapping

    .. wraps::
        CalcTextSize(const char* text, const char* text_end, bool hide_text_after_double_hash, float wrap_width)
    '''

def color_convert_u32_to_float4(in_: int) -> Vec4:
    '''
    Convert an unsigned int 32 to 4 component r, g, b, a

    Args:
        in_ (ImU32): Color in unsigned int 32 format

    Return:
        tuple: r, g, b, a components of the color

    .. wraps::
        ImVec4 ColorConvertU32ToFloat4(ImU32 in)
    '''

def color_convert_float4_to_u32(r: float, g: float, b: float, a: float) -> int:
    '''
    Convert a set of r, g, b, a floats to unsigned int 32 color

    Args:
        r, g, b, a (float): Components of the color

    Returns:
        ImU32: Unsigned int 32 color format

    .. wraps::
        ImU32 ColorConvertFloat4ToU32(const ImVec4& in)
    '''

def color_convert_rgb_to_hsv(r: float, g: float, b: float) -> tuple[float, float, float]:
    '''
    Convert color from RGB space to HSV space

    Args:
        r, g, b (float): RGB color format

    Returns:
        tuple: h, s, v HSV color format

    .. wraps::
        void ColorConvertRGBtoHSV(float r, float g, float b, float& out_h, float& out_s, float& out_v)
    '''

def color_convert_hsv_to_rgb(h: float, s: float, v: float) -> tuple[float, float, float]:
    '''
    Convert color from HSV space to RGB space

    Args:
        h, s, v (float): HSV color format

    Returns:
        tuple: r, g, b RGB color format

    .. wraps::
        void ColorConvertHSVtoRGB(float h, float s, float v, float& out_r, float& out_g, float& out_b)
    '''

def push_style_var(variable: StyleVar,
                   value: float | tuple[float, float]) -> None:
    '''
    Push style variable on stack.

    This function accepts both float and float two-tuples as ``value``
    argument. ImGui core implementation will verify if passed value has
    type compatibile with given style variable. If not, it will raise
    exception.

    **Note:** variables pushed on stack need to be poped using
    :func:`pop_style_var()` until the end of current frame. This
    implementation guards you from segfaults caused by redundant stack pops
    (raises exception if this happens) but generally it is safer and easier to
    use :func:`styled` or :func:`istyled` context managers.

    .. visual-example::
        :auto_layout:
        :width: 200
        :height: 80

        imgui.begin('Example: style variables')
        imgui.push_style_var(imgui.STYLE_ALPHA, 0.2)
        imgui.text('Alpha text')
        imgui.pop_style_var(1)
        imgui.end()

    Args:
        variable: imgui style variable constant
        value (float or two-tuple): style variable value


    .. wraps::
        PushStyleVar(ImGuiStyleVar idx, float val)
    '''

def push_style_color(variable: int,
                     r: float,
                     g: float,
                     b: float,
                     a: float = 1.0) -> None:
    '''
    Push style color on stack.

    **Note:** variables pushed on stack need to be popped using
    :func:`pop_style_color()` until the end of current frame. This
    implementation guards you from segfaults caused by redundant stack pops
    (raises exception if this happens) but generally it is safer and easier to
    use :func:`styled` or :func:`istyled` context managers.

    .. visual-example::
        :auto_layout:
        :width: 200
        :height: 80

        imgui.begin('Example: Color variables')
        imgui.push_style_color(imgui.COLOR_TEXT, 1.0, 0.0, 0.0)
        imgui.text('Colored text')
        imgui.pop_style_color(1)
        imgui.end()

    Args:
        variable: imgui style color constant
        r (float): red color intensity.
        g (float): green color intensity.
        b (float): blue color instensity.
        a (float): alpha intensity.

    .. wraps::
        PushStyleColor(ImGuiCol idx, const ImVec4& col)
    '''

def pop_style_var(count: int = 1) -> None:
    '''
    Pop style variables from stack.

    **Note:** This implementation guards you from segfaults caused by
    redundant stack pops (raises exception if this happens) but generally
    it is safer and easier to use :func:`styled` or :func:`istyled` context
    managers. See: :any:`push_style_var()`.

    Args:
        count (int): number of variables to pop from style variable stack.

    .. wraps::
        void PopStyleVar(int count = 1)
    '''

def get_font_size() -> float:
    '''
    Get current font size (= height in pixels) of current font with current scale applied

    Returns:
        float: current font size (height in pixels)

    .. wraps::
        float GetFontSize()
    '''

def get_style_color_vec_4(idx: int) -> Vec4: ...

def get_font_tex_uv_white_pixel() -> Vec2: ...

def get_color_u32_idx(idx: int, alpha_mul: float = 1.0) -> int:
    '''
    Retrieve given style color with style alpha applied and optional extra alpha multiplier

    Returns:
        ImU32: 32-bit RGBA color

    .. wraps::
        ImU32 GetColorU32(ImGuiCol idx, alpha_mul)
    '''

def get_color_u32_rgba(r: float, g: float, b: float, a: float) -> int:
    '''
    Retrieve given color with style alpha applied

    Returns:
        ImU32: 32-bit RGBA color

    .. wraps::
        ImU32 GetColorU32(const ImVec4& col)
    '''

def get_color_u32(col: int) -> int:
    '''
    Retrieve given style color with style alpha applied and optional extra alpha multiplier

    Returns:
        ImU32: 32-bit RGBA color

    .. wraps::
        ImU32 GetColorU32(ImU32 col)
    '''

def push_item_width(item_width: float) -> None:
    '''
    Push item width in the stack.

    **Note:** sizing of child region allows for three modes:

    * ``0.0`` - default to ~2/3 of windows width
    * ``>0.0`` - width in pixels
    * ``<0.0`` - align xx pixels to the right of window
      (so -FLOAT_MIN always align width to the right side)

    **Note:** width pushed on stack need to be poped using
    :func:`pop_item_width()` or it will be applied to all subsequent
    children components.

    .. visual-example::
        :auto_layout:
        :width: 200
        :height: 200

        imgui.begin('Example: item width')

        # custom width
        imgui.push_item_width(imgui.get_window_width() * 0.33)
        imgui.text('Lorem Ipsum ...')
        imgui.slider_float('float slider', 10.2, 0.0, 20.0, '%.2f', 1.0)
        imgui.pop_item_width()

        # default width
        imgui.text('Lorem Ipsum ...')
        imgui.slider_float('float slider', 10.2, 0.0, 20.0, '%.2f', 1.0)

        imgui.end()

    Args:
        item_width (float): width of the component

    .. wraps::
        void PushItemWidth(float item_width)
    '''

def pop_item_width() -> None:
    '''
    Reset width back to the default width.

    **Note:** This implementation guards you from segfaults caused by
    redundant stack pops (raises exception if this happens) but generally
    it is safer and easier to use :func:`styled` or :func:`istyled` context
    managers. See: :any:`push_item_width()`.

    .. wraps::
        void PopItemWidth()
    '''

def set_next_item_width(item_width: float) -> None:
    '''
    Set width of the _next_ common large 'item+label' widget.
    * ``>0.0`` - width in pixels
    * ``<0.0`` - align xx pixels to the right of window
    (so -FLOAT_MIN always align width to the right side)

    Helper to avoid using ``push_item_width()``/``pop_item_width()`` for single items.

    Args:
        item_width (float): width of the component

    .. visual-example::
        :auto_layout:
        :width: 200
        :height: 200

        imgui.begin('Exemple: Next item width')
        imgui.set_next_item_width(imgui.get_window_width() * 0.33)
        imgui.slider_float('Slider 1', 10.2, 0.0, 20.0, '%.2f', 1.0)
        imgui.slider_float('Slider 2', 10.2, 0.0, 20.0, '%.2f', 1.0)
        imgui.end()

    .. wraps::
        void SetNextItemWidth(float item_width)
    '''

def calculate_item_width() -> None:
    '''
    Calculate and return the current item width.

    Returns:
        float: calculated item width.

    .. wraps::
        float CalcItemWidth()
    '''

def push_text_wrap_pos(wrap_pos_x: float = 0.0) -> None:
    '''
    Word-wrapping function for text*() commands.

    **Note:** wrapping position allows these modes:
    * ``0.0`` - wrap to end of window (or column)
    * ``>0.0`` - wrap at 'wrap_pos_x' position in window local space
    * ``<0.0`` - no wrapping

    Args:
        wrap_pos_x (float): calculated item width.

    .. wraps::
        float PushTextWrapPos(float wrap_pos_x = 0.0f)
    '''

def push_text_wrap_position(wrap_pos_x: float = 0.0) -> None:
    '''
    Word-wrapping function for text*() commands.

    **Note:** wrapping position allows these modes:
    * ``0.0`` - wrap to end of window (or column)
    * ``>0.0`` - wrap at 'wrap_pos_x' position in window local space
    * ``<0.0`` - no wrapping

    Args:
        wrap_pos_x (float): calculated item width.

    .. wraps::
        float PushTextWrapPos(float wrap_pos_x = 0.0f)
    '''

def pop_text_wrap_pos() -> None:
    '''
    Pop the text wrapping position from the stack.

    **Note:** This implementation guards you from segfaults caused by
    redundant stack pops (raises exception if this happens) but generally
    it is safer and easier to use :func:`styled` or :func:`istyled` context
    managers. See: :func:`push_text_wrap_pos()`.

    .. wraps::
        void PopTextWrapPos()
    '''

def pop_text_wrap_position() -> None:
    '''
    Pop the text wrapping position from the stack.

    **Note:** This implementation guards you from segfaults caused by
    redundant stack pops (raises exception if this happens) but generally
    it is safer and easier to use :func:`styled` or :func:`istyled` context
    managers. See: :func:`push_text_wrap_pos()`.

    .. wraps::
        void PopTextWrapPos()
    '''

def push_allow_keyboard_focus(allow_focus: bool) -> None: ...
def pop_allow_keyboard_focus() -> None: ...
def push_button_repeat(repeat: bool) -> None: ...
def pop_button_repeat() -> None: ...

def pop_style_color(count: int = 1) -> None:
    '''
    Pop style color from stack.

    **Note:** This implementation guards you from segfaults caused by
    redundant stack pops (raises exception if this happens) but generally
    it is safer and easier to use :func:`styled` or :func:`istyled` context
    managers. See: :any:`push_style_color()`.

    Args:
        count (int): number of variables to pop from style color stack.

    .. wraps::
        void PopStyleColor(int count = 1)
    '''

def separator() -> None:
    '''
    Add vertical line as a separator beween elements.

    .. visual-example::
        :auto_layout:
        :width: 300

        imgui.begin('Example: separators')

        imgui.text('Some text with bullets')
        imgui.bullet_text('Bullet A')
        imgui.bullet_text('Bullet A')

        imgui.separator()

        imgui.text('Another text with bullets')
        imgui.bullet_text('Bullet A')
        imgui.bullet_text('Bullet A')

        imgui.end()

    .. wraps::
        void Separator()
    '''

def same_line(position: float = 0.0, spacing: float = -1.0) -> None:
    '''
    Call between widgets or groups to layout them horizontally.

    .. visual-example::
        :auto_layout:
        :width: 300

        imgui.begin('Example: same line widgets')

        imgui.text('same_line() with defaults:')
        imgui.button('yes'); imgui.same_line()
        imgui.button('no')

        imgui.text('same_line() with fixed position:')
        imgui.button('yes'); imgui.same_line(position=50)
        imgui.button('no')

        imgui.text('same_line() with spacing:')
        imgui.button('yes'); imgui.same_line(spacing=50)
        imgui.button('no')

        imgui.end()

    Args:
        position (float): fixed horizontal position position.
        spacing (float): spacing between elements.

    .. wraps::
        void SameLine(float pos_x = 0.0f, float spacing_w = -1.0f)
    '''

def new_line() -> None:
    '''
    Undo :any:`same_line()` call.

    .. wraps::
        void NewLine()
    '''

def spacing() -> None:
    '''
    Add vertical spacing beween elements.

    .. visual-example::
        :auto_layout:
        :width: 300

        imgui.begin('Example: vertical spacing')

        imgui.text('Some text with bullets:')
        imgui.bullet_text('Bullet A')
        imgui.bullet_text('Bullet A')

        imgui.spacing(); imgui.spacing()

        imgui.text('Another text with bullets:')
        imgui.bullet_text('Bullet A')
        imgui.bullet_text('Bullet A')

        imgui.end()

    .. wraps::
        void Spacing()
    '''

def dummy(width: float, height: float) -> None:
    '''
    Add dummy element of given size.

    .. visual-example::
        :auto_layout:
        :width: 300

        imgui.begin('Example: dummy elements')

        imgui.text('Some text with bullets:')
        imgui.bullet_text('Bullet A')
        imgui.bullet_text('Bullet B')

        imgui.dummy(0, 50)
        imgui.bullet_text('Text after dummy')

        imgui.end()

    .. wraps::
        void Dummy(const ImVec2& size)
    '''

def indent(width: float = 0.0) -> None:
    '''
    Move content to right by indent width.

    .. visual-example::
        :auto_layout:
        :width: 300

        imgui.begin('Example: item indenting')

        imgui.text('Some text with bullets:')

        imgui.bullet_text('Bullet A')
        imgui.indent()
        imgui.bullet_text('Bullet B (first indented)')
        imgui.bullet_text('Bullet C (indent continues)')
        imgui.unindent()
        imgui.bullet_text('Bullet D (indent cleared)')

        imgui.end()

    Args:
        width (float): fixed width of indent. If less or equal 0 it defaults
            to global indent spacing or value set using style value  stack
            (see :any:`push_style_var`).

    .. wraps::
        void Indent(float indent_w = 0.0f)
    '''

def unindent(width: float = 0.0) -> None:
    '''
    Move content to left by indent width.

    .. visual-example::
        :auto_layout:
        :width: 300

        imgui.begin('Example: item unindenting')

        imgui.text('Some text with bullets:')

        imgui.bullet_text('Bullet A')
        imgui.unindent(10)
        imgui.bullet_text('Bullet B (first unindented)')
        imgui.bullet_text('Bullet C (unindent continues)')
        imgui.indent(10)
        imgui.bullet_text('Bullet C (unindent cleared)')

        imgui.end()

    Args:
        width (float): fixed width of indent. If less or equal 0 it defaults
            to global indent spacing or value set using style value stack
            (see :any:`push_style_var`).

    .. wraps::
        void Unindent(float indent_w = 0.0f)
    '''

def columns(count: int = 1,
            identifier: str | None = None,
            border: bool = True) -> None:
    '''
    Setup number of columns. Use an identifier to distinguish multiple
    column sets. close with ``columns(1)``.

    Legacy Columns API (2020: prefer using Tables!)

    .. visual-example::
        :auto_layout:
        :width: 500
        :height: 300

        imgui.begin('Example: Columns - File list')
        imgui.columns(4, 'fileLlist')
        imgui.separator()
        imgui.text('ID')
        imgui.next_column()
        imgui.text('File')
        imgui.next_column()
        imgui.text('Size')
        imgui.next_column()
        imgui.text('Last Modified')
        imgui.next_column()
        imgui.separator()
        imgui.set_column_offset(1, 40)

        imgui.next_column()
        imgui.text('FileA.txt')
        imgui.next_column()
        imgui.text('57 Kb')
        imgui.next_column()
        imgui.text('12th Feb, 2016 12:19:01')
        imgui.next_column()

        imgui.next_column()
        imgui.text('ImageQ.png')
        imgui.next_column()
        imgui.text('349 Kb')
        imgui.next_column()
        imgui.text('1st Mar, 2016 06:38:22')
        imgui.next_column()

        imgui.columns(1)
        imgui.end()

    Args:
        count (int): Columns count.
        identifier (str): Table identifier.
        border (bool): Display border, defaults to ``True``.

    .. wraps::
        void Columns(
            int count = 1,
            const char* id = NULL,
            bool border = true
        )
    '''

def next_column() -> None:
    '''Move to the next column drawing.

    For a complete example see :func:`columns()`.

    Legacy Columns API (2020: prefer using Tables!)

    .. wraps::
        void NextColumn()
    '''

def get_column_index() -> int:
    '''
    Returns the current column index.

    For a complete example see :func:`columns()`.

    Legacy Columns API (2020: prefer using Tables!)

    Returns:
        int: the current column index.

    .. wraps::
        int GetColumnIndex()
    '''

def get_column_offset(column_index: int = -1) -> float:
    '''
    Returns position of column line (in pixels, from the left side of the
    contents region). Pass -1 to use current column, otherwise 0 to
    :func:`get_columns_count()`. Column 0 is usually 0.0f and not resizable
    unless you call this method.

    For a complete example see :func:`columns()`.

    Legacy Columns API (2020: prefer using Tables!)

    Args:
        column_index (int): index of the column to get the offset for.

    Returns:
        float: the position in pixels from the left side.

    .. wraps::
        float GetColumnOffset(int column_index = -1)
    '''

def set_column_offset(column_index: int, offset_x: float) -> None:
    '''
    Set the position of column line (in pixels, from the left side of the
    contents region). Pass -1 to use current column.

    For a complete example see :func:`columns()`.

    Legacy Columns API (2020: prefer using Tables!)

    Args:
        column_index (int): index of the column to get the offset for.
        offset_x (float): offset in pixels.

    .. wraps::
        void SetColumnOffset(int column_index, float offset_x)
    '''

def get_column_width(column_index: int = -1) -> float:
    '''
    Return the column width.

    For a complete example see :func:`columns()`.

    Legacy Columns API (2020: prefer using Tables!)

    Args:
        column_index (int): index of the column to get the width for.

    .. wraps::
        float GetColumnWidth(int column_index = -1)
    '''

def set_column_width(column_index: int, width: float) -> None:
    '''
    Set the position of column line (in pixels, from the left side of the
    contents region). Pass -1 to use current column.

    For a complete example see :func:`columns()`.

    Legacy Columns API (2020: prefer using Tables!)

    Args:
        column_index (int): index of the column to set the width for.
        width (float): width in pixels.

    .. wraps::
        void SetColumnWidth(int column_index, float width)
    '''

def get_columns_count() -> int:
    '''
    Get count of the columns in the current table.

    For a complete example see :func:`columns()`.

    Legacy Columns API (2020: prefer using Tables!)

    Returns:
        int: columns count.

    .. wraps::
        int GetColumnsCount()
    '''

def begin_tab_bar(identifier: str,
                  flags: TabBarFlags = TAB_BAR_NONE) -> _BeginEndTabBar:
    '''
    Create and append into a TabBar

    Args:
        identifier(str): String identifier of the tab window
        flags: ImGuiTabBarFlags flags. See:
            :ref:`list of available flags <tabbar-flag-options>`.

    Returns:
        _BeginEndTabBar: Use ``opened`` bool attribute to tell if the Tab Bar is open.
        Only call :func:`end_tab_bar` if ``opened`` is True.
        Use with ``with`` to automatically call :func:`end_tab_bar` if necessary when the block ends.

    .. wraps::
        bool BeginTabBar(const char* str_id, ImGuiTabBarFlags flags = 0)

    '''

def end_tab_bar() -> None:
    '''
    End a previously opened tab bar.
    Only call this function if ``begin_tab_bar().opened`` is True.

    .. wraps::
        void EndTabBar()
    '''

def begin_tab_item(label: str,
                   opened: bool | None = None,
                   flags: TabItemFlags = TAB_ITEM_NONE) -> _BeginEndTabItem:
    '''
    Create a Tab.

    .. visual-example::
        :auto_layout:
        :width: 300

        opened_state = True

        #...

        with imgui.begin('Example Tab Bar'):
            with imgui.begin_tab_bar('MyTabBar') as tab_bar:
                if tab_bar.opened:
                    with imgui.begin_tab_item('Item 1') as item1:
                        if item1.selected:
                            imgui.text('Here is the tab content!')

                    with imgui.begin_tab_item('Item 2') as item2:
                        if item2.selected:
                            imgui.text('Another content...')

                    with imgui.begin_tab_item('Item 3', opened=opened_state) as item3:
                        opened_state = item3.opened
                        if item3.selected:
                            imgui.text('Hello Saylor!')

    Example::

        opened_state = True

        #...

        imgui.begin('Example Tab Bar')
        if imgui.begin_tab_bar('MyTabBar'):

            if imgui.begin_tab_item('Item 1').selected:
                imgui.text('Here is the tab content!')
                imgui.end_tab_item()

            if imgui.begin_tab_item('Item 2').selected:
                imgui.text('Another content...')
                imgui.end_tab_item()

            selected, opened_state = imgui.begin_tab_item('Item 3', opened=opened_state)
            if selected:
                imgui.text('Hello Saylor!')
                imgui.end_tab_item()

            imgui.end_tab_bar()
        imgui.end()

    Args:
        label (str): Label of the tab item
        removable (bool): If True, the tab item can be removed
        flags: ImGuiTabItemFlags flags. See:
            :ref:`list of available flags <tabitem-flag-options>`.

    Returns:
        _BeginEndTabItem: ``(selected, opened)`` struct of bools. If tab item is selected
        ``selected==True``. The value of ``opened`` is always True for
        non-removable and open tab items but changes state to False on close
        button click for removable tab items.
        Only call :func:`end_tab_item` if ``selected`` is True.
        Use with ``with`` to automatically call :func:`end_tab_item` if necessary when the block ends.

    .. wraps::
        bool BeginTabItem(
            const char* label,
            bool* p_open = NULL,
            ImGuiTabItemFlags flags = 0
        )
    '''

def end_tab_item() -> None:
    '''
    End a previously opened tab item.
    Only call this function if ``begin_tab_item().selected`` is True.

    .. wraps::
        void EndTabItem()
    '''

def tab_item_button(label: str, flags: TabItemFlags = TAB_ITEM_NONE) -> bool:
    '''
    Create a Tab behaving like a button.
    Cannot be selected in the tab bar.

    Args:
        label (str): Label of the button
        flags: ImGuiTabItemFlags flags. See:
            :ref:`list of available flags <tabitem-flag-options>`.

    Returns:
        (bool): Return true when clicked.

    .. visual-example:
        :auto_layout:
        :width: 300

        imgui.begin('Example Tab Bar')
        if imgui.begin_tab_bar('MyTabBar'):

            if imgui.begin_tab_item('Item 1')[0]:
                imgui.text('Here is the tab content!')
                imgui.end_tab_item()

            if imgui.tab_item_button('Click me!'):
                print('Clicked!')

            imgui.end_tab_bar()
        imgui.end()

    .. wraps::
        bool TabItemButton(const char* label, ImGuiTabItemFlags flags = 0)
    '''

def set_tab_item_closed(tab_or_docked_window_label: str) -> None:
    '''
    Notify TabBar or Docking system of a closed tab/window ahead (useful to reduce visual flicker on reorderable tab bars).
    For tab-bar: call after BeginTabBar() and before Tab submissions.
    Otherwise call with a window name.

    Args:
        tab_or_docked_window_label (str): Label of the targeted tab or docked window

    .. visual-example:
        :auto_layout:
        :width: 300

        imgui.begin('Example Tab Bar')
        if imgui.begin_tab_bar('MyTabBar'):

            if imgui.begin_tab_item('Item 1')[0]:
                imgui.text('Here is the tab content!')
                imgui.end_tab_item()

            if imgui.begin_tab_item('Item 2')[0]:
                imgui.text('This item won't whow !')
                imgui.end_tab_item()

            imgui.set_tab_item_closed('Item 2')

            imgui.end_tab_bar()
        imgui.end()

    .. wraps:
        void SetTabItemClosed(const char* tab_or_docked_window_label)
    '''

def begin_drag_drop_source(flags: DragDropFlags = DRAG_DROP_NONE) -> _BeginEndDragDropSource:
    '''
    Set the current item as a drag and drop source. If ``dragging`` is True, you
    can call :func:`set_drag_drop_payload` and :func:`end_drag_drop_source`.
    Use with ``with`` to automatically call :func:`end_drag_drop_source` if necessary.

    **Note:** this is a beta API.

    .. visual-example::
        :auto_layout:
        :width: 300

        with imgui.begin('Example: drag and drop'):

            imgui.button('source')
            with imgui.begin_drag_drop_source() as drag_drop_src:
                if drag_drop_src.dragging:
                    imgui.set_drag_drop_payload('itemtype', b'payload')
                    imgui.button('dragged source')

            imgui.button('dest')
            with imgui.begin_drag_drop_target() as drag_drop_dst:
                if drag_drop_dst.hovered:
                    payload = imgui.accept_drag_drop_payload('itemtype')
                    if payload is not None:
                        print('Received:', payload)

    Example::

        imgui.begin('Example: drag and drop')

        imgui.button('source')
        if imgui.begin_drag_drop_source():
            imgui.set_drag_drop_payload('itemtype', b'payload')
            imgui.button('dragged source')
            imgui.end_drag_drop_source()

        imgui.button('dest')
        if imgui.begin_drag_drop_target():
            payload = imgui.accept_drag_drop_payload('itemtype')
            if payload is not None:
                print('Received:', payload)
            imgui.end_drag_drop_target()

        imgui.end()

    Args:
        flags (ImGuiDragDropFlags): DragDrop flags.

    Returns:
        _BeginEndDragDropSource: Use ``dragging`` to tell if a drag starting at this source is occurring.
        Only call :func:`end_drag_drop_source` if ``dragging`` is True.
        Use with ``with`` to automatically call :func:`end_drag_drop_source` if necessary when the block ends.

    .. wraps::
        bool BeginDragDropSource(ImGuiDragDropFlags flags = 0)
    '''

def set_drag_drop_payload(type: str,
                          data: bytes,
                          condition: Condition = ALWAYS) -> bool:
    '''
    Set the payload for a drag and drop source. Only call after
    :func:`begin_drag_drop_source` returns True.

    **Note:** this is a beta API.

    For a complete example see :func:`begin_drag_drop_source`.

    Args:
        type (str): user defined type with maximum 32 bytes.
        data (bytes): the data for the payload; will be copied and stored internally.
        condition (:ref:`condition flag <condition-options>`): defines on which
            condition value should be set. Defaults to :any:`imgui.ALWAYS`.

    .. wraps::
        bool SetDragDropPayload(const char* type, const void* data, size_t size, ImGuiCond cond = 0)
    '''

def end_drag_drop_source() -> None:
    '''
    End the drag and drop source.
    Only call if ``begin_drag_drop_source().dragging`` is True.

    **Note:** this is a beta API.

    For a complete example see :func:`begin_drag_drop_source`.

    .. wraps::
        void EndDragDropSource()
    '''

def begin_drag_drop_target() -> _BeginEndDragDropTarget:
    '''
    Set the current item as a drag and drop target. If ``hovered`` is True, you
    can call :func:`accept_drag_drop_payload` and :func:`end_drag_drop_target`.
    Use with ``with`` to automatically call :func:`end_drag_drop_target` if necessary.

    For a complete example see :func:`begin_drag_drop_source`.

    **Note:** this is a beta API.

    Returns:
        _BeginEndDragDropTarget: Use ``hovered` to tell if a drag hovers over the target.
        Only call :func:`end_drag_drop_target` if ``hovered`` is True.
        Use with ``with`` to automatically call :func:`end_drag_drop_target` if necessary when the block ends.

    .. wraps::
        bool BeginDragDropTarget()
    '''

# TODO Fix DragDropAcceptFlags not having default value for NONE
def accept_drag_drop_payload(type: str,
                             flags: DragDropAcceptFlags = _t.cast(DragDropAcceptFlags, 0)) -> bytes | None:
    '''
    Get the drag and drop payload. Only call after :func:`begin_drag_drop_target`
    returns True.

    **Note:** this is a beta API.

    For a complete example see :func:`begin_drag_drop_source`.

    Args:
        type (str): user defined type with maximum 32 bytes.
        flags (ImGuiDragDropFlags): DragDrop flags.

    Returns:
        bytes: the payload data that was set by :func:`set_drag_drop_payload`.

    .. wraps::
        const ImGuiPayload* AcceptDragDropPayload(const char* type, ImGuiDragDropFlags flags = 0)
    '''

def end_drag_drop_target() -> None:
    '''
    End the drag and drop source.
    Only call this function if ``begin_drag_drop_target().hovered`` is True.

    **Note:** this is a beta API.

    For a complete example see :func:`begin_drag_drop_source`.

    .. wraps::
        void EndDragDropTarget()
    '''

def get_drag_drop_payload() -> bytes | None:
    '''
    Peek directly into the current payload from anywhere.
    May return NULL.

    .. todo:: Map ImGuiPayload::IsDataType() to test for the payload type.

    .. wraps::
        const ImGuiPayload* GetDragDropPayload()
    '''

def push_clip_rect(clip_rect_min_x: float,
                   clip_rect_min_y: float,
                   clip_rect_max_x: float,
                   clip_rect_max_y: float,
                   intersect_with_current_clip_rect: bool = False) -> None:
    '''
    Push the clip region, i.e. the area of the screen to be rendered,on the stack.
    If ``intersect_with_current_clip_rect`` is ``True``, the intersection between pushed
    clip region and previous one is added on the stack.
    See: :func:`pop_clip_rect()`

    Args:
        clip_rect_min_x, clip_rect_min_y (float): Position of the minimum point of the rectangle
        clip_rect_max_x, clip_rect_max_y (float): Position of the maximum point of the rectangle
        intersect_with_current_clip_rect (bool): If True, intersection with current clip region is pushed on stack.

    .. visual-example::
        :auto_layout:
        :width: 150
        :height: 150

        imgui.begin('Example Cliprect')

        winpos = imgui.get_window_position()
        imgui.push_clip_rect(0+winpos.x,0+winpos.y,100+winpos.x,100+winpos.y)
        imgui.push_clip_rect(50+winpos.x,50+winpos.y,100+winpos.x,100+winpos.y, True)

        imgui.text('Lorem ipsum dolor sit amet, consectetur adipiscing elit.')
        imgui.text('Vivamus mattis velit ac ex auctor gravida.')
        imgui.text('Quisque varius erat finibus porta interdum.')
        imgui.text('Nam neque magna, dapibus placerat urna eget, facilisis malesuada ipsum.')

        imgui.pop_clip_rect()
        imgui.pop_clip_rect()

        imgui.end()

    .. wraps::
        void PushClipRect(
            const ImVec2& clip_rect_min,
            const ImVec2& clip_rect_max,
            bool intersect_with_current_clip_rect
        )
    '''

def pop_clip_rect() -> None:
    '''
    Pop the last clip region from the stack. See: :func:`push_clip_rect()`.

    .. wraps::
        void PopClipRect()
    '''

def begin_group() -> _BeginEndGroup:
    '''
    Start item group and lock its horizontal starting position.

    Captures group bounding box into one 'item'. Thanks to this you can use
    :any:`is_item_hovered()` or layout primitives such as :any:`same_line()`
    on whole group, etc.

    .. visual-example::
        :auto_layout:
        :width: 500

        with imgui.begin('Example: item groups'):

            with imgui.begin_group():
                imgui.text('First group (buttons):')
                imgui.button('Button A')
                imgui.button('Button B')

            imgui.same_line(spacing=50)

            with imgui.begin_group():
                imgui.text('Second group (text and bullet texts):')
                imgui.bullet_text('Bullet A')
                imgui.bullet_text('Bullet B')

    Example::

        imgui.begin('Example: item groups')

        imgui.begin_group()
        imgui.text('First group (buttons):')
        imgui.button('Button A')
        imgui.button('Button B')
        imgui.end_group()

        imgui.same_line(spacing=50)

        imgui.begin_group()
        imgui.text('Second group (text and bullet texts):')
        imgui.bullet_text('Bullet A')
        imgui.bullet_text('Bullet B')
        imgui.end_group()

        imgui.end()

    Returns:
        _BeginEndGrouop; use with ``with`` to automatically call :func:`end_group` when the block ends.

    .. wraps::
        void BeginGroup()
    '''

def end_group() -> None:
    '''
    End group (see: :any:`begin_group`).

    .. wraps::
        void EndGroup()
    '''

def get_cursor_pos() -> Vec2:
    '''
    Get the cursor position.

    .. wraps::
        ImVec2 GetCursorPos()
    '''

def get_cursor_pos_x() -> float: ...

def get_cursor_pos_y() -> float: ...

def set_cursor_pos(local_pos: tuple[float, float]):
    '''
    Set the cursor position in local coordinates [0..<window size>] (useful to work with ImDrawList API)

    .. wraps::
        ImVec2 SetCursorScreenPos(const ImVec2& screen_pos)
    '''

def set_cursor_pos_x(x: float) -> None: ...

def set_cursor_pos_y(y: float) -> None: ...

def get_cursor_start_pos() -> Vec2:
    '''
    Get the initial cursor position.

    .. wraps::
        ImVec2 GetCursorStartPos()
    '''

def get_cursor_screen_pos() -> Vec2:
    '''
    Get the cursor position in absolute screen coordinates [0..io.DisplaySize] (useful to work with ImDrawList API)

    .. wraps::
        ImVec2 GetCursorScreenPos()
    '''

def set_cursor_screen_pos(screen_pos: tuple[float, float]) -> None:
    '''
    Set the cursor position in absolute screen coordinates [0..io.DisplaySize] (useful to work with ImDrawList API)

    .. wraps::
        ImVec2 SetCursorScreenPos(const ImVec2& screen_pos)
    '''

def get_cursor_position() -> Vec2:
    '''
    Get the cursor position.

    .. wraps::
        ImVec2 GetCursorPos()
    '''

def set_cursor_position(local_pos: tuple[float, float]):
    '''
    Set the cursor position in local coordinates [0..<window size>] (useful to work with ImDrawList API)

    .. wraps::
        ImVec2 SetCursorScreenPos(const ImVec2& screen_pos)
    '''

def get_cursor_start_position() -> Vec2:
    '''
    Get the initial cursor position.

    .. wraps::
        ImVec2 GetCursorStartPos()
    '''

def get_cursor_screen_position() -> Vec2:
    '''
    Get the cursor position in absolute screen coordinates [0..io.DisplaySize] (useful to work with ImDrawList API)

    .. wraps::
        ImVec2 GetCursorScreenPos()
    '''

def set_cursor_screen_position(screen_pos: tuple[float, float]) -> None:
    '''
    Set the cursor position in absolute screen coordinates [0..io.DisplaySize] (useful to work with ImDrawList API)

    .. wraps::
        ImVec2 SetCursorScreenPos(const ImVec2& screen_pos)
    '''

def align_text_to_frame_padding() -> None: ...

def get_text_line_height() -> int:
    '''
    Get text line height.

    Returns:
        int: text line height.

    .. wraps::
        void GetTextLineHeight()
    '''

def get_text_line_height_with_spacing() -> int:
    '''
    Get text line height, with spacing.

    Returns:
        int: text line height, with spacing.

    .. wraps::
        void GetTextLineHeightWithSpacing()
    '''

def get_frame_height() -> float:
    '''
    ~ FontSize + style.FramePadding.y * 2

    .. wraps::
        float GetFrameHeight()
        float GetFrameHeightWithSpacing() except +
    '''

def get_frame_height_with_spacing() -> float:
    '''
    ~ FontSize + style.FramePadding.y * 2 + style.ItemSpacing.y (distance in pixels between 2 consecutive lines of framed widgets)

    .. wraps::
        float GetFrameHeightWithSpacing()
    '''

def create_context(shared_font_atlas: _FontAtlas | None = None) -> _ImGuiContext:
    '''
    CreateContext

    .. todo::
        Add an example

    .. wraps::
        ImGuiContext* CreateContext(
                # note: optional
                ImFontAtlas* shared_font_atlas = NULL);
    '''

def destroy_context(ctx: _ImGuiContext | None = None) -> None:
    '''
    DestroyContext

    .. wraps::
        DestroyContext(
                # note: optional
                ImGuiContext* ctx = NULL);
    '''

def get_current_context() -> _ImGuiContext:
    '''
    GetCurrentContext

    .. wraps::
        ImGuiContext* GetCurrentContext();
    '''

def set_current_context(ctx: _ImGuiContext) -> None:
    '''
    SetCurrentContext

    .. wraps::
        SetCurrentContext(ImGuiContext *ctx);
    '''

def push_id(str_id: str) -> None:
    '''Push an ID into the ID stack

    Args:
        str_id (str): ID to push

      wraps::
        PushID(const char* str_id)
    '''

def pop_id() -> None:
    '''
    Pop from the ID stack

      wraps::
        PopID()
    '''

def _ansifeed_text_ansi(text: str) -> None:
    '''Add ANSI-escape-formatted text to current widget stack.

    Similar to imgui.text, but with ANSI parsing.
    imgui.text documentation below:

    .. visual-example::
        :title: simple text widget
        :height: 80
        :auto_layout:

        imgui.begin('Example: simple text')
        imgui.extra.text_ansi('Default \033[31m colored \033[m default')
        imgui.end()

    Args:
        text (str): text to display.

    .. wraps::
        Text(const char* fmt, ...)
    '''

def _ansifeed_text_ansi_colored(text: str,
                                r: float,
                                g: float,
                                b: float,
                                a: float = 1.0) -> None:
    '''
    Add pre-colored ANSI-escape-formatted text to current widget stack.

    Similar to imgui.text_colored, but with ANSI parsing.
    imgui.text_colored documentation below:

    It is a shortcut for:

    .. code-block:: python

        imgui.push_style_color(imgui.COLOR_TEXT, r, g, b, a)
        imgui.extra.text_ansi(text)
        imgui.pop_style_color()


    .. visual-example::
        :title: colored text widget
        :height: 100
        :auto_layout:

        imgui.begin('Example: colored text')
        imgui.text_ansi_colored('Default \033[31m colored \033[m default', 1, 0, 0)
        imgui.end()

    Args:
        text (str): text to display.
        r (float): red color intensity.
        g (float): green color intensity.
        b (float): blue color instensity.
        a (float): alpha intensity.

    .. wraps::
        TextColored(const ImVec4& col, const char* fmt, ...)
    '''

@_contextlib.contextmanager
def _py_font(font: _Font):
    '''
    Use specified font in given context.

    .. visual-example::
        :auto_layout:
        :height: 100
        :width: 320

        io = imgui.get_io()

        new_font = io.fonts.add_font_from_file_ttf('DroidSans.ttf', 20)
        impl.refresh_font_texture()

        # later in frame code

        imgui.begin('Default Window')

        imgui.text('Text displayed using default font')
        with imgui.font(new_font):
            imgui.text('Text displayed using custom font')

        imgui.end()

    Args:
        font (_Font): font object retrieved from :any:`add_font_from_file_ttf`.
    '''

@_contextlib.contextmanager
def _py_styled(variable: StyleVar, value: float | tuple[float, float]): ...

@_contextlib.contextmanager
def _py_colored(variable: int,
                r: float,
                g: float,
                b: float,
                a: float = 1.0): ...

@_contextlib.contextmanager
def _py_istyled(*variables_and_values: tuple[StyleVar, float | tuple[float, float]]): ...

@_contextlib.contextmanager
def _py_scoped(str_id: str):
    '''
    Use scoped ID within a block of code.

    This context manager can be used to distinguish widgets sharing
    same implicit identifiers without manual calling of :func:`push_id`
    :func:`pop_id` functions.

    Example:

    Args:
        str_id (str): ID to push and pop within marked scope
    '''

def _py_vertex_buffer_vertex_pos_offset() -> int: ...

def _py_vertex_buffer_vertex_uv_offset() -> int: ...

def _py_vertex_buffer_vertex_col_offset() -> int: ...

def _py_vertex_buffer_vertex_size() -> int: ...

def _py_index_buffer_index_size() -> int: ...
