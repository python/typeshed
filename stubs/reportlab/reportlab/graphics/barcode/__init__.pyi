def registerWidget(widget) -> None: ...
def getCodes(): ...
def getCodeNames(): ...
def createBarcodeDrawing(codeName, **options): ...
def createBarcodeImageInMemory(codeName, **options): ...

__all__ = ("registerWidget", "getCodes", "getCodeNames", "createBarcodeDrawing", "createBarcodeImageInMemory")
