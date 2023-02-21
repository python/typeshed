from _typeshed import Incomplete
from pgen2 import grammar

class Converter(grammar.Grammar):
    def run(self, graminit_h, graminit_c) -> None: ...
    symbol2number: Incomplete
    number2symbol: Incomplete
    def parse_graminit_h(self, filename): ...
    states: Incomplete
    dfas: Incomplete
    labels: Incomplete
    start: Incomplete
    def parse_graminit_c(self, filename): ...
    keywords: Incomplete
    tokens: Incomplete
    def finish_off(self) -> None: ...
