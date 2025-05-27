from typing import Optional
from mypy.plugin import Plugin, FunctionContext
from mypy.types import Type, Instance
from mypy.nodes import ARG_POS

class CompileFilenamePlugin(Plugin):
    def get_function_hook(self, fullname: str):
        # Hook only the built-in compile function
        if fullname == "builtins.compile":
            return compile_hook
        return None

def compile_hook(ctx: FunctionContext) -> Type:
    # Arguments to compile: source, filename, mode, ...
    # filename is arg index 1 (zero-based)
    if len(ctx.arg_types) > 1 and ctx.arg_types[1]:
        filename_type = ctx.arg_types[1][0]  # first argument passed for filename param
        if is_bytearray_type(filename_type):
            ctx.api.fail(
                "Passing 'bytearray' as filename to 'compile()' is not allowed",
                ctx.args[1][0]
            )
    return ctx.default_return_type

def is_bytearray_type(typ: Type) -> bool:
    # Check if the type is exactly bytearray
    if isinstance(typ, Instance):
        # The full name for builtins.bytearray is 'builtins.bytearray'
        return typ.type.fullname == "builtins.bytearray"
    return False

def plugin(version: str):
    return CompileFilenamePlugin
