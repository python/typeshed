import ast
from typing_extensions import assert_type

# Test with Module input
mod1: ast.Module = ast.Module([], [])
assert_type(ast.parse(mod1), ast.Module)
assert_type(ast.parse(mod1, mode="exec"), ast.Module)
mod2: ast.Module = ast.Module(body=[ast.Expr(value=ast.Constant(value=42))], type_ignores=[])
assert_type(ast.parse(mod2), ast.Module)

# Test with Expression input
expr1: ast.Expression = ast.Expression(body=ast.Constant(value=42))
assert_type(ast.parse(expr1, mode="eval"), ast.Expression)

# Test with Interactive input
inter1: ast.Interactive = ast.Interactive(body=[])
assert_type(ast.parse(inter1, mode="single"), ast.Interactive)

# Test with FunctionType input
func1: ast.FunctionType = ast.FunctionType(argtypes=[], returns=ast.Constant(value=None))
assert_type(ast.parse(func1, mode="func_type"), ast.FunctionType)
