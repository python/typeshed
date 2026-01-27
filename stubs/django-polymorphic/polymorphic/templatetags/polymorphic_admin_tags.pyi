from typing_extensions import Self

from django.template import Context, Library, Node, NodeList
from django.template.base import FilterExpression, Parser, Token

register: Library

class BreadcrumbScope(Node):
    base_opts: FilterExpression
    nodelist: NodeList
    def __init__(self, base_opts: FilterExpression, nodelist: NodeList) -> None: ...
    @classmethod
    def parse(cls, parser: Parser, token: Token) -> Self: ...
    def render(self, context: Context) -> str: ...

def breadcrumb_scope(parser: Parser, token: Token) -> BreadcrumbScope: ...
