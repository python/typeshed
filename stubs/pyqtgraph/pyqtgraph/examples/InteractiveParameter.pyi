from _typeshed import Incomplete

app: Incomplete

class LAST_RESULT:
    value: Incomplete

def printResult(func): ...

host: Incomplete
interactor: Incomplete

@printResult
def easySample(a: int = 5, b: int = 6): ...
@printResult
def stringParams(a: str = "5", b: str = "6"): ...
@printResult
def requiredParam(a, b: int = 10): ...
@printResult
def ignoredAParam(a: int = 10, b: int = 20): ...
@printResult
def runOnButton(a: int = 10, b: int = 20): ...

x: int

@printResult
def accessVarInDifferentScope(x, y: int = 10): ...

func_interactive: Incomplete

@printResult
def capslocknames(a: int = 5): ...
@printResult
def runOnBtnOrChange_listOpts(a: int = 5): ...
@printResult
def onlyTheArgumentsAppear(thisIsAFunctionArg: bool = True): ...

tree: Incomplete
