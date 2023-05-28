#!/usr/bin/env python3

from __future__ import annotations

import ast
import sys
from itertools import chain
from pathlib import Path


def check_new_syntax(tree: ast.AST, path: Path, stub: str) -> list[str]:
    errors: list[str] = []

    class IfFinder(ast.NodeVisitor):
        def visit_If(self, node: ast.If) -> None:
            if (
                isinstance(node.test, ast.Compare)
                and ast.unparse(node.test).startswith("sys.version_info < ")
                and node.orelse
                and not (len(node.orelse) == 1 and isinstance(node.orelse[0], ast.If))  # elif statement (#6728)
            ):
                new_syntax = "if " + ast.unparse(node.test).replace("<", ">=", 1)
                errors.append(
                    f"{path}:{node.lineno}: When using if/else with sys.version_info, "
                    f"put the code for new Python versions first, e.g. `{new_syntax}`"
                )
            self.generic_visit(node)

    IfFinder().visit(tree)
    return errors


def main() -> None:
    errors: list[str] = []
    for path in chain(Path("stdlib").rglob("*.pyi"), Path("stubs").rglob("*.pyi")):
        with open(path, encoding="UTF-8") as f:
            stub = f.read()
            tree = ast.parse(stub)
        errors.extend(check_new_syntax(tree, path, stub))

    if errors:
        print("\n".join(errors))
        sys.exit(1)


if __name__ == "__main__":
    main()
