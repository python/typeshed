# -*- coding: utf-8 -*-
"""
    click
    ~~~~~

    Click is a simple Python module that wraps the stdlib's optparse to make
    writing command line scripts fun.  Unlike other modules, it's based around
    a simple API that does not come with too much magic and is composable.

    In case optparse ever gets removed from the stdlib, it will be shipped by
    this module.

    :copyright: (c) 2014 by Armin Ronacher.
    :license: BSD, see LICENSE for more details.
"""

# fmt: off
# Core classes
from .core import Argument as Argument
from .core import BaseCommand as BaseCommand
from .core import Command as Command
from .core import CommandCollection as CommandCollection
from .core import Context as Context
from .core import Group as Group
from .core import MultiCommand as MultiCommand
from .core import Option as Option
from .core import Parameter as Parameter
# Decorators
from .decorators import argument as argument
from .decorators import command as command
from .decorators import confirmation_option as confirmation_option
from .decorators import group as group
from .decorators import help_option as help_option
from .decorators import make_pass_decorator as make_pass_decorator
from .decorators import option as option
from .decorators import pass_context as pass_context
from .decorators import pass_obj as pass_obj
from .decorators import password_option as password_option
from .decorators import version_option as version_option
# Exceptions
from .exceptions import Abort as Abort
from .exceptions import BadArgumentUsage as BadArgumentUsage
from .exceptions import BadOptionUsage as BadOptionUsage
from .exceptions import BadParameter as BadParameter
from .exceptions import ClickException as ClickException
from .exceptions import FileError as FileError
from .exceptions import MissingParameter as MissingParameter
from .exceptions import NoSuchOption as NoSuchOption
from .exceptions import UsageError as UsageError
# Formatting
from .formatting import HelpFormatter as HelpFormatter
from .formatting import wrap_text as wrap_text
# Globals
from .globals import get_current_context as get_current_context
# Parsing
from .parser import OptionParser as OptionParser
# Terminal functions
from .termui import clear as clear
from .termui import confirm as confirm
from .termui import echo_via_pager as echo_via_pager
from .termui import edit as edit
from .termui import get_terminal_size as get_terminal_size
from .termui import getchar as getchar
from .termui import launch as launch
from .termui import pause as pause
from .termui import progressbar as progressbar
from .termui import prompt as prompt
from .termui import secho as secho
from .termui import style as style
from .termui import unstyle as unstyle
# Types
from .types import BOOL as BOOL
from .types import FLOAT as FLOAT
from .types import INT as INT
from .types import STRING as STRING
from .types import UNPROCESSED as UNPROCESSED
from .types import UUID as UUID
from .types import Choice as Choice
from .types import File as File
from .types import IntRange as IntRange
from .types import ParamType as ParamType
from .types import Path as Path
from .types import Tuple as Tuple
# Utilities
from .utils import echo as echo
from .utils import format_filename as format_filename
from .utils import get_app_dir as get_app_dir
from .utils import get_binary_stream as get_binary_stream
from .utils import get_os_args as get_os_args
from .utils import get_text_stream as get_text_stream
from .utils import open_file as open_file

# fmt: on

# Controls if click should emit the warning about the use of unicode
# literals.
disable_unicode_literals_warning: bool

__version__: str
