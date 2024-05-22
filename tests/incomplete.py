#!/usr/bin/env python3

from __future__ import annotations

import ast
import sys
from argparse import ArgumentParser
from pathlib import Path
from typing import NoReturn

from _metadata import read_metadata
from _utils import distribution_path

FIXED_TYPING_NAMES = ("TypeAlias", "TypeVar", "ParamSpec", "TypeVarTuple", "TypedDict", "NewType")
FIXED_TYPESHED_NAMES = ("Incomplete",)


def main() -> None:
    dists, verbose_level = parse_args()

    success = True
    for i, dist in enumerate(dists):
        if verbose_level >= 2 and i > 0:
            print()
        if not check_distribution(dist, verbose_level):
            success = False

    if not success:
        sys.exit(1)


def parse_args() -> tuple[list[str], int]:
    parser = ArgumentParser()
    parser.add_argument("dist", nargs="+", help="The distributions to check")
    parser.add_argument("-v", "--verbose", action="count", default=0)
    args = parser.parse_args()
    return args.dist, args.verbose


def check_distribution(dist: str, verbose_level: int) -> bool:
    if verbose_level >= 2:
        print(f"Checking {dist}...")

    dist_path = distribution_path(dist)
    if not dist_path.exists():
        print(f"Distribution {dist!r} does not exist", file=sys.stderr)
        return False

    meta = read_metadata(dist)
    unannotated, incomplete = count_incompletes_in_dist(dist_path, verbose_level)

    if verbose_level >= 1:
        print(f"{dist} total: {unannotated} unannotated, {incomplete} incomplete")

    total = unannotated + incomplete
    if total == 0 and meta.incomplete:
        print(f"{dist}: Marked as 'incomplete', but no incomplete annotations found", file=sys.stderr)
        return False
    if total > 0 and not meta.incomplete:
        msg = f"{dist}: Found "
        if unannotated:
            msg += f"{unannotated} unannotated"
            if incomplete:
                msg += " and "
        if incomplete:
            msg += f"{incomplete} incomplete"
        msg += " annotations, but not marked as 'incomplete'"
        print(msg, file=sys.stderr)
        return False

    return True


def count_incompletes_in_dist(dist_path: Path, verbose_level: int) -> tuple[int, int]:
    unannotated = 0
    incomplete = 0
    for file in dist_path.glob("**/*.pyi"):
        un, inc = count_incompletes_in_file(file)
        unannotated += un
        incomplete += inc
        if verbose_level >= 2:
            print(f"{file.relative_to(dist_path)}: {un} unannotated, {inc} incomplete")
    return unannotated, incomplete


def count_incompletes_in_file(file: Path) -> tuple[int, int]:
    mod = ast.parse(file.read_text())
    return ModuleCounter(file).count(mod)


class ModuleCounter:
    def __init__(self, file: Path) -> None:
        self.file = file
        self.unannotated = 0
        self.incomplete = 0
        self.typing_imports: set[str] = set()
        self.typeshed_imports: set[str] = set()
        self.has_incomplete_import = False
        self._in_class = 0

    def _not_implemented(self, node: ast.stmt | ast.expr | ast.type_param, message: str) -> NoReturn:
        raise NotImplementedError(f"{self.file}:{node.lineno}: {message}")

    def count(self, mod: ast.Module) -> tuple[int, int]:
        self.count_body(mod.body)
        if self.has_incomplete_import and self.incomplete == 0:
            raise RuntimeError(
                f"{self.file}: Incomplete import without any incomplete annotations. "
                + "This is likely a bug in the imcomplete.py script."
            )
        return self.unannotated, self.incomplete

    def count_body(self, body: list[ast.stmt]) -> None:
        for stmt in body:
            match stmt:
                case ast.Import():
                    self.handle_import(stmt)
                case ast.ImportFrom():
                    self.handle_import_from(stmt)
                case ast.Assign():
                    self.count_assign(stmt)
                case ast.AugAssign():
                    pass  # ignore
                case ast.AnnAssign():
                    self.count_ann_assign(stmt)
                case ast.FunctionDef() | ast.AsyncFunctionDef():
                    self.count_function(stmt)
                case ast.ClassDef():
                    self.count_class(stmt)
                case ast.If():
                    self.count_body(stmt.body)
                    if stmt.orelse:
                        self.count_body(stmt.orelse)
                case ast.Expr():
                    match stmt.value:
                        case ast.Constant():
                            pass
                        case _:
                            self._not_implemented(stmt, f"Node type {type(stmt.value)} not supported: {ast.unparse(stmt.value)}")
                case _:
                    self._not_implemented(stmt, f"Node type {type(stmt)} not supported: {ast.unparse(stmt)}")

    def handle_import(self, imp: ast.Import) -> None:
        for im in imp.names:
            if im.name in ("typing", "typing_extensions"):
                self.typing_imports.add(im.asname or im.name)
            if im.name == "_typeshed":
                self.typeshed_imports.add(im.asname or im.name)

    def handle_import_from(self, imp: ast.ImportFrom) -> None:
        if imp.module in ("typing", "typing_extensions"):
            for alias in imp.names:
                if alias.name in FIXED_TYPING_NAMES:
                    if alias.asname is not None:
                        self._not_implemented(imp, f"typing.{alias.name} import with alias not supported")
        if imp.module == "_typeshed":
            for alias in imp.names:
                if alias.name in FIXED_TYPESHED_NAMES:
                    if alias.asname is not None:
                        self._not_implemented(imp, f"_typeshed.{alias.name} import with alias not supported")
                    self.has_incomplete_import = True

    def count_assign(self, assign: ast.Assign | ast.AnnAssign) -> None:
        match assign.value:
            case ast.Name() | ast.Attribute():
                if self.is_incomplete(assign.value):
                    self.incomplete += 1
            case ast.Constant() | ast.UnaryOp() | ast.List() | ast.Tuple():
                pass  # ignore
            case ast.Call():
                self.count_assign_call(assign.value)
            case _:
                self._not_implemented(assign, f"Assign value type {type(assign.value)} not supported")

    def count_assign_call(self, call: ast.Call) -> None:
        func = call.func
        match func:
            case ast.Name(id):
                self.count_typing_calls(call, id)
            case ast.Attribute():
                if not isinstance(func.value, ast.Name):
                    self._not_implemented(func, f"Call with value type {type(func.value)} not supported")
                if func.value.id in self.typing_imports:
                    self.count_typing_calls(call, func.attr)
            case _:
                self._not_implemented(func, f"Call type {type(func)} not supported")

    def count_typing_calls(self, call: ast.Call, name: str) -> None:
        match name:
            case "TypeVar":
                for arg in call.args:
                    self.count_annotation(arg)
                for kwarg in call.keywords:
                    if kwarg.arg in ("bound", "default"):
                        self.count_annotation(kwarg.value)
            case "ParamSpec":
                for kwarg in call.keywords:
                    if kwarg.arg in ("bound", "default"):
                        self.count_annotation(kwarg.value)
            case "TypeVarTuple":
                for kwarg in call.keywords:
                    if kwarg.arg == "default":
                        self.count_annotation(kwarg.value)
            case "TypedDict":
                if len(call.args) < 2 or not isinstance(call.args[1], ast.Dict):
                    self._not_implemented(call, f"Unsupported TypedDict call: {ast.unparse(call)}")
                for v in call.args[1].values:
                    self.count_annotation(v)
            case "NewType":
                if len(call.args) >= 2:
                    self.count_annotation(call.args[1])
                for kwarg in call.keywords:
                    if kwarg.arg == "tp":
                        self.count_annotation(kwarg.value)
            case _:
                pass  # ignore

    def count_ann_assign(self, assign: ast.AnnAssign) -> None:
        if self.is_typing_name(assign.annotation, "TypeAlias"):
            self.count_annotation(assign.value)
        else:
            self.count_annotation(assign.annotation)
            if assign.value is not None:
                self.count_assign(assign)

    def count_function(self, func: ast.FunctionDef | ast.AsyncFunctionDef) -> None:
        if sys.version_info >= (3, 12):
            for param in func.type_params:
                self.count_type_param(param)
        all_args = func.args.posonlyargs + func.args.args + func.args.kwonlyargs
        if func.args.vararg:
            all_args.append(func.args.vararg)
        if func.args.kwarg:
            all_args.append(func.args.kwarg)
        for i, arg in enumerate(all_args):
            if i == 0 and arg.annotation is None and self.has_self_argument(func):
                continue
            self.count_annotation(arg.annotation)
        self.count_annotation(func.returns)

    def has_self_argument(self, func: ast.FunctionDef | ast.AsyncFunctionDef) -> bool:
        if not self._in_class:
            return False
        if len(func.args.posonlyargs + func.args.args) == 0:
            return False
        return not any(self.is_staticmethod(dec) for dec in func.decorator_list)

    def count_class(self, cls: ast.ClassDef) -> None:
        self._in_class += 1
        try:
            self.incomplete += sum(self.is_incomplete(base) for base in cls.bases)
            if sys.version_info >= (3, 12):
                for param in cls.type_params:
                    self.count_type_param(param)
            if not has_ellipsis_body(cls.body):
                self.count_body(cls.body)
        finally:
            self._in_class -= 1

    def count_type_param(self, param: ast.type_param) -> None:
        match param:
            case ast.TypeVar():
                self.count_annotation(param.bound)
                if sys.version_info >= (3, 13):
                    self.count_annotation(param.default_value)
            case _:
                self._not_implemented(param, f"Type param type {type(param)} not supported")

    def count_annotation(self, annotation: ast.expr | None) -> None:
        if annotation is None:
            self.unannotated += 1
        elif self.is_incomplete(annotation):
            self.incomplete += 1

    def is_incomplete(self, annotation: ast.expr) -> bool:
        match annotation:
            case ast.Constant():
                return False
            case ast.Name() | ast.Attribute():
                return self.is_typeshed_name(annotation, "Incomplete")
            case ast.Tuple() | ast.List():
                return any(self.is_incomplete(el) for el in annotation.elts)
            case ast.Subscript():
                return self.is_incomplete(annotation.slice)
            case ast.BinOp():
                return self.is_incomplete(annotation.left) or self.is_incomplete(annotation.right)
            case ast.UnaryOp():
                return self.is_incomplete(annotation.operand)
            case _:
                self._not_implemented(annotation, f"Annotation type {type(annotation)} not supported: {ast.unparse(annotation)}")

    def is_staticmethod(self, expr: ast.expr) -> bool:
        return isinstance(expr, ast.Name) and expr.id == "staticmethod"

    def is_typing_name(self, expr: ast.expr, name: str) -> bool:
        if isinstance(expr, ast.Name):
            return expr.id == name
        if isinstance(expr, ast.Attribute):
            return isinstance(expr.value, ast.Name) and expr.value.id in self.typing_imports and expr.attr == name
        return False

    def is_typeshed_name(self, expr: ast.expr, name: str) -> bool:
        if isinstance(expr, ast.Name):
            return expr.id == name
        if isinstance(expr, ast.Attribute):
            return isinstance(expr.value, ast.Name) and expr.value.id in self.typeshed_imports and expr.attr == name
        return False


def has_ellipsis_body(stmts: list[ast.stmt]) -> bool:
    if len(stmts) != 1:
        return False
    stmt = stmts[0]
    return isinstance(stmt, ast.Expr) and isinstance(stmt.value, ast.Constant) and stmt.value.value is Ellipsis


if __name__ == "__main__":
    main()
