import argparse
import sys
from collections.abc import Sequence

def main_inner(parser: argparse.ArgumentParser, argns: argparse.Namespace) -> int: ...

class HelpFormatter(argparse.HelpFormatter):
    def __init__(self, prog: str, indent_increment: int = 2, max_help_position: int = 16, width: int | None = None) -> None: ...

def main(args: Sequence[str] = sys.argv) -> int: ...
