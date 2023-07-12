from typing import Callable, MutableSequence, Sequence, TypeVar, Union, overload

import vtkmodules.vtkCommonCore
import vtkmodules.vtkCommonDataModel

Callback = Union[Callable[..., None], None]
Buffer = TypeVar("Buffer")
Pointer = TypeVar("Pointer")
Template = TypeVar("Template")


class vtkColorSeries(vtkmodules.vtkCommonCore.vtkObject):
    class ColorSchemes(int):
        ...

    class LUTMode(int):
        ...
    BLUES: ColorSchemes
    BREWER_DIVERGING_BROWN_BLUE_GREEN_10: ColorSchemes
    BREWER_DIVERGING_BROWN_BLUE_GREEN_11: ColorSchemes
    BREWER_DIVERGING_BROWN_BLUE_GREEN_3: ColorSchemes
    BREWER_DIVERGING_BROWN_BLUE_GREEN_4: ColorSchemes
    BREWER_DIVERGING_BROWN_BLUE_GREEN_5: ColorSchemes
    BREWER_DIVERGING_BROWN_BLUE_GREEN_6: ColorSchemes
    BREWER_DIVERGING_BROWN_BLUE_GREEN_7: ColorSchemes
    BREWER_DIVERGING_BROWN_BLUE_GREEN_8: ColorSchemes
    BREWER_DIVERGING_BROWN_BLUE_GREEN_9: ColorSchemes
    BREWER_DIVERGING_PURPLE_ORANGE_10: ColorSchemes
    BREWER_DIVERGING_PURPLE_ORANGE_11: ColorSchemes
    BREWER_DIVERGING_PURPLE_ORANGE_3: ColorSchemes
    BREWER_DIVERGING_PURPLE_ORANGE_4: ColorSchemes
    BREWER_DIVERGING_PURPLE_ORANGE_5: ColorSchemes
    BREWER_DIVERGING_PURPLE_ORANGE_6: ColorSchemes
    BREWER_DIVERGING_PURPLE_ORANGE_7: ColorSchemes
    BREWER_DIVERGING_PURPLE_ORANGE_8: ColorSchemes
    BREWER_DIVERGING_PURPLE_ORANGE_9: ColorSchemes
    BREWER_DIVERGING_SPECTRAL_10: ColorSchemes
    BREWER_DIVERGING_SPECTRAL_11: ColorSchemes
    BREWER_DIVERGING_SPECTRAL_3: ColorSchemes
    BREWER_DIVERGING_SPECTRAL_4: ColorSchemes
    BREWER_DIVERGING_SPECTRAL_5: ColorSchemes
    BREWER_DIVERGING_SPECTRAL_6: ColorSchemes
    BREWER_DIVERGING_SPECTRAL_7: ColorSchemes
    BREWER_DIVERGING_SPECTRAL_8: ColorSchemes
    BREWER_DIVERGING_SPECTRAL_9: ColorSchemes
    BREWER_QUALITATIVE_ACCENT: ColorSchemes
    BREWER_QUALITATIVE_DARK2: ColorSchemes
    BREWER_QUALITATIVE_PAIRED: ColorSchemes
    BREWER_QUALITATIVE_PASTEL1: ColorSchemes
    BREWER_QUALITATIVE_PASTEL2: ColorSchemes
    BREWER_QUALITATIVE_SET1: ColorSchemes
    BREWER_QUALITATIVE_SET2: ColorSchemes
    BREWER_QUALITATIVE_SET3: ColorSchemes
    BREWER_SEQUENTIAL_BLUE_GREEN_3: ColorSchemes
    BREWER_SEQUENTIAL_BLUE_GREEN_4: ColorSchemes
    BREWER_SEQUENTIAL_BLUE_GREEN_5: ColorSchemes
    BREWER_SEQUENTIAL_BLUE_GREEN_6: ColorSchemes
    BREWER_SEQUENTIAL_BLUE_GREEN_7: ColorSchemes
    BREWER_SEQUENTIAL_BLUE_GREEN_8: ColorSchemes
    BREWER_SEQUENTIAL_BLUE_GREEN_9: ColorSchemes
    BREWER_SEQUENTIAL_BLUE_PURPLE_3: ColorSchemes
    BREWER_SEQUENTIAL_BLUE_PURPLE_4: ColorSchemes
    BREWER_SEQUENTIAL_BLUE_PURPLE_5: ColorSchemes
    BREWER_SEQUENTIAL_BLUE_PURPLE_6: ColorSchemes
    BREWER_SEQUENTIAL_BLUE_PURPLE_7: ColorSchemes
    BREWER_SEQUENTIAL_BLUE_PURPLE_8: ColorSchemes
    BREWER_SEQUENTIAL_BLUE_PURPLE_9: ColorSchemes
    BREWER_SEQUENTIAL_YELLOW_ORANGE_BROWN_3: ColorSchemes
    BREWER_SEQUENTIAL_YELLOW_ORANGE_BROWN_4: ColorSchemes
    BREWER_SEQUENTIAL_YELLOW_ORANGE_BROWN_5: ColorSchemes
    BREWER_SEQUENTIAL_YELLOW_ORANGE_BROWN_6: ColorSchemes
    BREWER_SEQUENTIAL_YELLOW_ORANGE_BROWN_7: ColorSchemes
    BREWER_SEQUENTIAL_YELLOW_ORANGE_BROWN_8: ColorSchemes
    BREWER_SEQUENTIAL_YELLOW_ORANGE_BROWN_9: ColorSchemes
    CATEGORICAL: LUTMode
    CITRUS: ColorSchemes
    COOL: ColorSchemes
    CUSTOM: ColorSchemes
    ORDINAL: LUTMode
    SPECTRUM: ColorSchemes
    WARM: ColorSchemes
    WILD_FLOWER: ColorSchemes

    def AddColor(
        self, color: vtkmodules.vtkCommonDataModel.vtkColor3ub) -> None: ...
    def BuildLookupTable(
        self, lkup: vtkmodules.vtkCommonCore.vtkLookupTable, lutIndexing: int = ...) -> None: ...

    def ClearColors(self) -> None: ...
    def CreateLookupTable(
        self, lutIndexing: int = ...) -> vtkmodules.vtkCommonCore.vtkLookupTable: ...

    def DeepCopy(self, chartColors: vtkColorSeries) -> None: ...

    def GetColor(
        self, index: int) -> vtkmodules.vtkCommonDataModel.vtkColor3ub: ...
    def GetColorRepeating(
        self, index: int) -> vtkmodules.vtkCommonDataModel.vtkColor3ub: ...

    def GetColorScheme(self) -> int: ...
    def GetColorSchemeName(self) -> str: ...
    def GetNumberOfColorSchemes(self) -> int: ...
    def GetNumberOfColors(self) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def InsertColor(
        self, index: int, color: vtkmodules.vtkCommonDataModel.vtkColor3ub) -> None: ...

    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkColorSeries: ...
    def RemoveColor(self, index: int) -> None: ...

    @staticmethod
    def SafeDownCast(
        o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkColorSeries: ...
    def SetColor(self, index: int,
                 color: vtkmodules.vtkCommonDataModel.vtkColor3ub) -> None: ...

    def SetColorScheme(self, scheme: int) -> None: ...
    def SetColorSchemeByName(self, schemeName: str) -> int: ...
    def SetColorSchemeName(self, name: str) -> None: ...
    def SetNumberOfColors(self, numColors: int) -> None: ...


class vtkNamedColors(vtkmodules.vtkCommonCore.vtkObject):
    def ColorExists(self, name: str) -> bool: ...
    @overload
    def GetColor(self, name: str, r: int, g: int, b: int, a: int) -> None: ...
    @overload
    def GetColor(self, name: str, rgba: MutableSequence[int]) -> None: ...

    @overload
    def GetColor(self, name: str,
                 rgba: vtkmodules.vtkCommonDataModel.vtkColor4ub) -> None: ...

    @overload
    def GetColor(self, name: str, r: float, g: float,
                 b: float, a: float) -> None: ...

    @overload
    def GetColor(self, name: str, rgba: MutableSequence[float]) -> None: ...

    @overload
    def GetColor(self, name: str,
                 rgba: vtkmodules.vtkCommonDataModel.vtkColor4d) -> None: ...

    @overload
    def GetColor(self, name: str, r: float, g: float, b: float) -> None: ...

    @overload
    def GetColor(self, name: str,
                 rgb: vtkmodules.vtkCommonDataModel.vtkColor3ub) -> None: ...

    @overload
    def GetColor(self, name: str,
                 rgb: vtkmodules.vtkCommonDataModel.vtkColor3d) -> None: ...

    def GetColor3d(
        self, name: str) -> vtkmodules.vtkCommonDataModel.vtkColor3d: ...

    def GetColor3ub(
        self, name: str) -> vtkmodules.vtkCommonDataModel.vtkColor3ub: ...

    def GetColor4d(
        self, name: str) -> vtkmodules.vtkCommonDataModel.vtkColor4d: ...
    def GetColor4ub(
        self, name: str) -> vtkmodules.vtkCommonDataModel.vtkColor4ub: ...

    @overload
    def GetColorNames(self) -> str: ...

    @overload
    def GetColorNames(
        self, colorNames: vtkmodules.vtkCommonCore.vtkStringArray) -> None: ...

    def GetColorRGB(self, name: str, rgb: MutableSequence[float]) -> None: ...
    def GetNumberOfColors(self) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetSynonyms(self) -> str: ...

    def HTMLColorToRGB(
        self, colorString: str) -> vtkmodules.vtkCommonDataModel.vtkColor3ub: ...
    def HTMLColorToRGBA(
        self, colorString: str) -> vtkmodules.vtkCommonDataModel.vtkColor4ub: ...

    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkNamedColors: ...

    def RGBAToHTMLColor(
        self, rgba: vtkmodules.vtkCommonDataModel.vtkColor4ub) -> str: ...
    def RGBToHTMLColor(
        self, rgb: vtkmodules.vtkCommonDataModel.vtkColor3ub) -> str: ...

    def RemoveColor(self, name: str) -> None: ...
    def ResetColors(self) -> None: ...

    @staticmethod
    def SafeDownCast(
        o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkNamedColors: ...

    @overload
    def SetColor(self, name: str, r: int, g: int,
                 b: int, a: int = 255) -> None: ...

    @overload
    def SetColor(self, name: str, r: float, g: float,
                 b: float, a: float = 1) -> None: ...

    @overload
    def SetColor(self, name: str, rgba: Sequence[int]) -> None: ...

    @overload
    def SetColor(self, name: str,
                 rgba: vtkmodules.vtkCommonDataModel.vtkColor4ub) -> None: ...

    @overload
    def SetColor(self, name: str,
                 rgb: vtkmodules.vtkCommonDataModel.vtkColor3ub) -> None: ...

    @overload
    def SetColor(self, name: str, rgba: Sequence[float]) -> None: ...

    @overload
    def SetColor(self, name: str,
                 rgba: vtkmodules.vtkCommonDataModel.vtkColor4d) -> None: ...

    @overload
    def SetColor(self, name: str,
                 rgb: vtkmodules.vtkCommonDataModel.vtkColor3d) -> None: ...

    @overload
    def SetColor(self, name: str, htmlString: str) -> None: ...
