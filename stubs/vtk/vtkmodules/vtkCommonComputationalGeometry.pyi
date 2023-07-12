from typing import Callable, MutableSequence, TypeVar, Union, overload

import vtkmodules.vtkCommonCore
import vtkmodules.vtkCommonDataModel

Callback = Union[Callable[..., None], None]
Buffer = TypeVar("Buffer")
Pointer = TypeVar("Pointer")
Template = TypeVar("Template")


class vtkBilinearQuadIntersection:
    @overload
    def __init__(
        self,
        pt00: vtkmodules.vtkCommonDataModel.vtkVector3d,
        Pt01: vtkmodules.vtkCommonDataModel.vtkVector3d,
        Pt10: vtkmodules.vtkCommonDataModel.vtkVector3d,
        Pt11: vtkmodules.vtkCommonDataModel.vtkVector3d,
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, __a: vtkBilinearQuadIntersection) -> None: ...
    def ComputeCartesianCoordinates(
        self, u: float, v: float) -> vtkmodules.vtkCommonDataModel.vtkVector3d: ...

    def GetP00Data(self) -> Pointer: ...
    def GetP01Data(self) -> Pointer: ...
    def GetP10Data(self) -> Pointer: ...
    def GetP11Data(self) -> Pointer: ...

    def RayIntersection(
        self,
        r: vtkmodules.vtkCommonDataModel.vtkVector3d,
        q: vtkmodules.vtkCommonDataModel.vtkVector3d,
        uv: vtkmodules.vtkCommonDataModel.vtkVector3d,
    ) -> bool: ...


class vtkCardinalSpline(vtkmodules.vtkCommonDataModel.vtkSpline):
    def Compute(self) -> None: ...
    def DeepCopy(self, s: vtkmodules.vtkCommonDataModel.vtkSpline) -> None: ...
    def Evaluate(self, t: float) -> float: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkCardinalSpline: ...

    @staticmethod
    def SafeDownCast(
        o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkCardinalSpline: ...


class vtkKochanekSpline(vtkmodules.vtkCommonDataModel.vtkSpline):
    def Compute(self) -> None: ...
    def DeepCopy(self, s: vtkmodules.vtkCommonDataModel.vtkSpline) -> None: ...
    def Evaluate(self, t: float) -> float: ...
    def GetDefaultBias(self) -> float: ...
    def GetDefaultContinuity(self) -> float: ...
    def GetDefaultTension(self) -> float: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkKochanekSpline: ...

    @staticmethod
    def SafeDownCast(
        o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkKochanekSpline: ...

    def SetDefaultBias(self, _arg: float) -> None: ...
    def SetDefaultContinuity(self, _arg: float) -> None: ...
    def SetDefaultTension(self, _arg: float) -> None: ...


class vtkParametricFunction(vtkmodules.vtkCommonCore.vtkObject):
    def ClockwiseOrderingOff(self) -> None: ...
    def ClockwiseOrderingOn(self) -> None: ...
    def DerivativesAvailableOff(self) -> None: ...
    def DerivativesAvailableOn(self) -> None: ...

    def Evaluate(self, uvw: MutableSequence[float],
                 Pt: MutableSequence[float], Duvw: MutableSequence[float]) -> None: ...
    def EvaluateScalar(
        self, uvw: MutableSequence[float], Pt: MutableSequence[float], Duvw: MutableSequence[float]) -> float: ...

    def GetClockwiseOrdering(self) -> int: ...
    def GetClockwiseOrderingMaxValue(self) -> int: ...
    def GetClockwiseOrderingMinValue(self) -> int: ...
    def GetDerivativesAvailable(self) -> int: ...
    def GetDerivativesAvailableMaxValue(self) -> int: ...
    def GetDerivativesAvailableMinValue(self) -> int: ...
    def GetDimension(self) -> int: ...
    def GetJoinU(self) -> int: ...
    def GetJoinUMaxValue(self) -> int: ...
    def GetJoinUMinValue(self) -> int: ...
    def GetJoinV(self) -> int: ...
    def GetJoinVMaxValue(self) -> int: ...
    def GetJoinVMinValue(self) -> int: ...
    def GetJoinW(self) -> int: ...
    def GetJoinWMaxValue(self) -> int: ...
    def GetJoinWMinValue(self) -> int: ...
    def GetMaximumU(self) -> float: ...
    def GetMaximumV(self) -> float: ...
    def GetMaximumW(self) -> float: ...
    def GetMinimumU(self) -> float: ...
    def GetMinimumV(self) -> float: ...
    def GetMinimumW(self) -> float: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetTwistU(self) -> int: ...
    def GetTwistUMaxValue(self) -> int: ...
    def GetTwistUMinValue(self) -> int: ...
    def GetTwistV(self) -> int: ...
    def GetTwistVMaxValue(self) -> int: ...
    def GetTwistVMinValue(self) -> int: ...
    def GetTwistW(self) -> int: ...
    def GetTwistWMaxValue(self) -> int: ...
    def GetTwistWMinValue(self) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def JoinUOff(self) -> None: ...
    def JoinUOn(self) -> None: ...
    def JoinVOff(self) -> None: ...
    def JoinVOn(self) -> None: ...
    def JoinWOff(self) -> None: ...
    def JoinWOn(self) -> None: ...
    def NewInstance(self) -> vtkParametricFunction: ...

    @staticmethod
    def SafeDownCast(
        o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkParametricFunction: ...

    def SetClockwiseOrdering(self, _arg: int) -> None: ...
    def SetDerivativesAvailable(self, _arg: int) -> None: ...
    def SetJoinU(self, _arg: int) -> None: ...
    def SetJoinV(self, _arg: int) -> None: ...
    def SetJoinW(self, _arg: int) -> None: ...
    def SetMaximumU(self, _arg: float) -> None: ...
    def SetMaximumV(self, _arg: float) -> None: ...
    def SetMaximumW(self, _arg: float) -> None: ...
    def SetMinimumU(self, _arg: float) -> None: ...
    def SetMinimumV(self, _arg: float) -> None: ...
    def SetMinimumW(self, _arg: float) -> None: ...
    def SetTwistU(self, _arg: int) -> None: ...
    def SetTwistV(self, _arg: int) -> None: ...
    def SetTwistW(self, _arg: int) -> None: ...
    def TwistUOff(self) -> None: ...
    def TwistUOn(self) -> None: ...
    def TwistVOff(self) -> None: ...
    def TwistVOn(self) -> None: ...
    def TwistWOff(self) -> None: ...
    def TwistWOn(self) -> None: ...


class vtkParametricBohemianDome(vtkParametricFunction):
    def Evaluate(self, uvw: MutableSequence[float],
                 Pt: MutableSequence[float], Duvw: MutableSequence[float]) -> None: ...
    def EvaluateScalar(
        self, uvw: MutableSequence[float], Pt: MutableSequence[float], Duvw: MutableSequence[float]) -> float: ...

    def GetA(self) -> float: ...
    def GetB(self) -> float: ...
    def GetC(self) -> float: ...
    def GetDimension(self) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkParametricBohemianDome: ...

    @staticmethod
    def SafeDownCast(
        o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkParametricBohemianDome: ...

    def SetA(self, _arg: float) -> None: ...
    def SetB(self, _arg: float) -> None: ...
    def SetC(self, _arg: float) -> None: ...


class vtkParametricBour(vtkParametricFunction):
    def Evaluate(self, uvw: MutableSequence[float],
                 Pt: MutableSequence[float], Duvw: MutableSequence[float]) -> None: ...
    def EvaluateScalar(
        self, uvw: MutableSequence[float], Pt: MutableSequence[float], Duvw: MutableSequence[float]) -> float: ...

    def GetDimension(self) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkParametricBour: ...

    @staticmethod
    def SafeDownCast(
        o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkParametricBour: ...


class vtkParametricBoy(vtkParametricFunction):
    def Evaluate(self, uvw: MutableSequence[float],
                 Pt: MutableSequence[float], Duvw: MutableSequence[float]) -> None: ...
    def EvaluateScalar(
        self, uvw: MutableSequence[float], Pt: MutableSequence[float], Duvw: MutableSequence[float]) -> float: ...

    def GetDimension(self) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetZScale(self) -> float: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkParametricBoy: ...

    @staticmethod
    def SafeDownCast(
        o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkParametricBoy: ...

    def SetZScale(self, _arg: float) -> None: ...


class vtkParametricCatalanMinimal(vtkParametricFunction):
    def Evaluate(self, uvw: MutableSequence[float],
                 Pt: MutableSequence[float], Duvw: MutableSequence[float]) -> None: ...
    def EvaluateScalar(
        self, uvw: MutableSequence[float], Pt: MutableSequence[float], Duvw: MutableSequence[float]) -> float: ...

    def GetDimension(self) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkParametricCatalanMinimal: ...

    @staticmethod
    def SafeDownCast(
        o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkParametricCatalanMinimal: ...


class vtkParametricConicSpiral(vtkParametricFunction):
    def Evaluate(self, uvw: MutableSequence[float],
                 Pt: MutableSequence[float], Duvw: MutableSequence[float]) -> None: ...
    def EvaluateScalar(
        self, uvw: MutableSequence[float], Pt: MutableSequence[float], Duvw: MutableSequence[float]) -> float: ...

    def GetA(self) -> float: ...
    def GetB(self) -> float: ...
    def GetC(self) -> float: ...
    def GetDimension(self) -> int: ...
    def GetN(self) -> float: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkParametricConicSpiral: ...

    @staticmethod
    def SafeDownCast(
        o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkParametricConicSpiral: ...

    def SetA(self, _arg: float) -> None: ...
    def SetB(self, _arg: float) -> None: ...
    def SetC(self, _arg: float) -> None: ...
    def SetN(self, _arg: float) -> None: ...


class vtkParametricCrossCap(vtkParametricFunction):
    def Evaluate(self, uvw: MutableSequence[float],
                 Pt: MutableSequence[float], Duvw: MutableSequence[float]) -> None: ...
    def EvaluateScalar(
        self, uvw: MutableSequence[float], Pt: MutableSequence[float], Duvw: MutableSequence[float]) -> float: ...

    def GetDimension(self) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkParametricCrossCap: ...

    @staticmethod
    def SafeDownCast(
        o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkParametricCrossCap: ...


class vtkParametricDini(vtkParametricFunction):
    def Evaluate(self, uvw: MutableSequence[float],
                 Pt: MutableSequence[float], Duvw: MutableSequence[float]) -> None: ...
    def EvaluateScalar(
        self, uvw: MutableSequence[float], Pt: MutableSequence[float], Duvw: MutableSequence[float]) -> float: ...

    def GetA(self) -> float: ...
    def GetB(self) -> float: ...
    def GetDimension(self) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkParametricDini: ...

    @staticmethod
    def SafeDownCast(
        o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkParametricDini: ...

    def SetA(self, _arg: float) -> None: ...
    def SetB(self, _arg: float) -> None: ...


class vtkParametricEllipsoid(vtkParametricFunction):
    def Evaluate(self, uvw: MutableSequence[float],
                 Pt: MutableSequence[float], Duvw: MutableSequence[float]) -> None: ...
    def EvaluateScalar(
        self, uvw: MutableSequence[float], Pt: MutableSequence[float], Duvw: MutableSequence[float]) -> float: ...

    def GetDimension(self) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetXRadius(self) -> float: ...
    def GetYRadius(self) -> float: ...
    def GetZRadius(self) -> float: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkParametricEllipsoid: ...

    @staticmethod
    def SafeDownCast(
        o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkParametricEllipsoid: ...

    def SetXRadius(self, _arg: float) -> None: ...
    def SetYRadius(self, _arg: float) -> None: ...
    def SetZRadius(self, _arg: float) -> None: ...


class vtkParametricEnneper(vtkParametricFunction):
    def Evaluate(self, uvw: MutableSequence[float],
                 Pt: MutableSequence[float], Duvw: MutableSequence[float]) -> None: ...
    def EvaluateScalar(
        self, uvw: MutableSequence[float], Pt: MutableSequence[float], Duvw: MutableSequence[float]) -> float: ...

    def GetDimension(self) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkParametricEnneper: ...

    @staticmethod
    def SafeDownCast(
        o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkParametricEnneper: ...


class vtkParametricFigure8Klein(vtkParametricFunction):
    def Evaluate(self, uvw: MutableSequence[float],
                 Pt: MutableSequence[float], Duvw: MutableSequence[float]) -> None: ...
    def EvaluateScalar(
        self, uvw: MutableSequence[float], Pt: MutableSequence[float], Duvw: MutableSequence[float]) -> float: ...

    def GetDimension(self) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetRadius(self) -> float: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkParametricFigure8Klein: ...

    @staticmethod
    def SafeDownCast(
        o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkParametricFigure8Klein: ...

    def SetRadius(self, _arg: float) -> None: ...


class vtkParametricHenneberg(vtkParametricFunction):
    def Evaluate(self, uvw: MutableSequence[float],
                 Pt: MutableSequence[float], Duvw: MutableSequence[float]) -> None: ...
    def EvaluateScalar(
        self, uvw: MutableSequence[float], Pt: MutableSequence[float], Duvw: MutableSequence[float]) -> float: ...

    def GetDimension(self) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkParametricHenneberg: ...

    @staticmethod
    def SafeDownCast(
        o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkParametricHenneberg: ...


class vtkParametricKlein(vtkParametricFunction):
    def Evaluate(self, uvw: MutableSequence[float],
                 Pt: MutableSequence[float], Duvw: MutableSequence[float]) -> None: ...
    def EvaluateScalar(
        self, uvw: MutableSequence[float], Pt: MutableSequence[float], Duvw: MutableSequence[float]) -> float: ...

    def GetDimension(self) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkParametricKlein: ...

    @staticmethod
    def SafeDownCast(
        o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkParametricKlein: ...


class vtkParametricKuen(vtkParametricFunction):
    def Evaluate(self, uvw: MutableSequence[float],
                 Pt: MutableSequence[float], Duvw: MutableSequence[float]) -> None: ...
    def EvaluateScalar(
        self, uvw: MutableSequence[float], Pt: MutableSequence[float], Duvw: MutableSequence[float]) -> float: ...

    def GetDeltaV0(self) -> float: ...
    def GetDimension(self) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkParametricKuen: ...

    @staticmethod
    def SafeDownCast(
        o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkParametricKuen: ...

    def SetDeltaV0(self, _arg: float) -> None: ...


class vtkParametricMobius(vtkParametricFunction):
    def Evaluate(self, uvw: MutableSequence[float],
                 Pt: MutableSequence[float], Duvw: MutableSequence[float]) -> None: ...
    def EvaluateScalar(
        self, uvw: MutableSequence[float], Pt: MutableSequence[float], Duvw: MutableSequence[float]) -> float: ...

    def GetDimension(self) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetRadius(self) -> float: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkParametricMobius: ...

    @staticmethod
    def SafeDownCast(
        o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkParametricMobius: ...

    def SetRadius(self, _arg: float) -> None: ...


class vtkParametricPluckerConoid(vtkParametricFunction):
    def Evaluate(self, uvw: MutableSequence[float],
                 Pt: MutableSequence[float], Duvw: MutableSequence[float]) -> None: ...
    def EvaluateScalar(
        self, uvw: MutableSequence[float], Pt: MutableSequence[float], Duvw: MutableSequence[float]) -> float: ...

    def GetDimension(self) -> int: ...
    def GetN(self) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkParametricPluckerConoid: ...

    @staticmethod
    def SafeDownCast(
        o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkParametricPluckerConoid: ...

    def SetN(self, _arg: int) -> None: ...


class vtkParametricPseudosphere(vtkParametricFunction):
    def Evaluate(self, uvw: MutableSequence[float],
                 Pt: MutableSequence[float], Duvw: MutableSequence[float]) -> None: ...
    def EvaluateScalar(
        self, uvw: MutableSequence[float], Pt: MutableSequence[float], Duvw: MutableSequence[float]) -> float: ...

    def GetDimension(self) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkParametricPseudosphere: ...

    @staticmethod
    def SafeDownCast(
        o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkParametricPseudosphere: ...


class vtkParametricRandomHills(vtkParametricFunction):
    def AllowRandomGenerationOff(self) -> None: ...
    def AllowRandomGenerationOn(self) -> None: ...

    def Evaluate(self, uvw: MutableSequence[float],
                 Pt: MutableSequence[float], Duvw: MutableSequence[float]) -> None: ...
    def EvaluateScalar(
        self, uvw: MutableSequence[float], Pt: MutableSequence[float], Duvw: MutableSequence[float]) -> float: ...

    def GetAllowRandomGeneration(self) -> int: ...
    def GetAllowRandomGenerationMaxValue(self) -> int: ...
    def GetAllowRandomGenerationMinValue(self) -> int: ...
    def GetAmplitudeScaleFactor(self) -> float: ...
    def GetDimension(self) -> int: ...
    def GetHillAmplitude(self) -> float: ...
    def GetHillXVariance(self) -> float: ...
    def GetHillYVariance(self) -> float: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetNumberOfHills(self) -> int: ...
    def GetRandomSeed(self) -> int: ...
    def GetXVarianceScaleFactor(self) -> float: ...
    def GetYVarianceScaleFactor(self) -> float: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkParametricRandomHills: ...

    @staticmethod
    def SafeDownCast(
        o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkParametricRandomHills: ...

    def SetAllowRandomGeneration(self, _arg: int) -> None: ...
    def SetAmplitudeScaleFactor(self, _arg: float) -> None: ...
    def SetHillAmplitude(self, _arg: float) -> None: ...
    def SetHillXVariance(self, _arg: float) -> None: ...
    def SetHillYVariance(self, _arg: float) -> None: ...
    def SetNumberOfHills(self, _arg: int) -> None: ...
    def SetRandomSeed(self, _arg: int) -> None: ...
    def SetXVarianceScaleFactor(self, _arg: float) -> None: ...
    def SetYVarianceScaleFactor(self, _arg: float) -> None: ...


class vtkParametricRoman(vtkParametricFunction):
    def Evaluate(self, uvw: MutableSequence[float],
                 Pt: MutableSequence[float], Duvw: MutableSequence[float]) -> None: ...
    def EvaluateScalar(
        self, uvw: MutableSequence[float], Pt: MutableSequence[float], Duvw: MutableSequence[float]) -> float: ...

    def GetDimension(self) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetRadius(self) -> float: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkParametricRoman: ...

    @staticmethod
    def SafeDownCast(
        o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkParametricRoman: ...

    def SetRadius(self, _arg: float) -> None: ...


class vtkParametricSpline(vtkParametricFunction):
    def ClosedOff(self) -> None: ...
    def ClosedOn(self) -> None: ...

    def Evaluate(
        self, u: MutableSequence[float], Pt: MutableSequence[float], Du: MutableSequence[float]) -> None: ...
    def EvaluateScalar(
        self, u: MutableSequence[float], Pt: MutableSequence[float], Du: MutableSequence[float]) -> float: ...

    def GetClosed(self) -> int: ...
    def GetDimension(self) -> int: ...
    def GetLeftConstraint(self) -> int: ...
    def GetLeftConstraintMaxValue(self) -> int: ...
    def GetLeftConstraintMinValue(self) -> int: ...
    def GetLeftValue(self) -> float: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetParameterizeByLength(self) -> int: ...
    def GetPoints(self) -> vtkmodules.vtkCommonCore.vtkPoints: ...
    def GetRightConstraint(self) -> int: ...
    def GetRightConstraintMaxValue(self) -> int: ...
    def GetRightConstraintMinValue(self) -> int: ...
    def GetRightValue(self) -> float: ...
    def GetXSpline(self) -> vtkmodules.vtkCommonDataModel.vtkSpline: ...
    def GetYSpline(self) -> vtkmodules.vtkCommonDataModel.vtkSpline: ...
    def GetZSpline(self) -> vtkmodules.vtkCommonDataModel.vtkSpline: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkParametricSpline: ...
    def ParameterizeByLengthOff(self) -> None: ...
    def ParameterizeByLengthOn(self) -> None: ...

    @staticmethod
    def SafeDownCast(
        o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkParametricSpline: ...

    def SetClosed(self, _arg: int) -> None: ...
    def SetLeftConstraint(self, _arg: int) -> None: ...
    def SetLeftValue(self, _arg: float) -> None: ...
    def SetNumberOfPoints(self, numPts: int) -> None: ...
    def SetParameterizeByLength(self, _arg: int) -> None: ...
    def SetPoint(self, index: int, x: float, y: float, z: float) -> None: ...
    def SetPoints(self, __a: vtkmodules.vtkCommonCore.vtkPoints) -> None: ...
    def SetRightConstraint(self, _arg: int) -> None: ...
    def SetRightValue(self, _arg: float) -> None: ...

    def SetXSpline(
        self, __a: vtkmodules.vtkCommonDataModel.vtkSpline) -> None: ...

    def SetYSpline(
        self, __a: vtkmodules.vtkCommonDataModel.vtkSpline) -> None: ...
    def SetZSpline(
        self, __a: vtkmodules.vtkCommonDataModel.vtkSpline) -> None: ...


class vtkParametricSuperEllipsoid(vtkParametricFunction):
    def Evaluate(self, uvw: MutableSequence[float],
                 Pt: MutableSequence[float], Duvw: MutableSequence[float]) -> None: ...
    def EvaluateScalar(
        self, uvw: MutableSequence[float], Pt: MutableSequence[float], Duvw: MutableSequence[float]) -> float: ...

    def GetDimension(self) -> int: ...
    def GetN1(self) -> float: ...
    def GetN2(self) -> float: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetXRadius(self) -> float: ...
    def GetYRadius(self) -> float: ...
    def GetZRadius(self) -> float: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkParametricSuperEllipsoid: ...

    @staticmethod
    def SafeDownCast(
        o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkParametricSuperEllipsoid: ...

    def SetN1(self, _arg: float) -> None: ...
    def SetN2(self, _arg: float) -> None: ...
    def SetXRadius(self, _arg: float) -> None: ...
    def SetYRadius(self, _arg: float) -> None: ...
    def SetZRadius(self, _arg: float) -> None: ...


class vtkParametricSuperToroid(vtkParametricFunction):
    def Evaluate(self, uvw: MutableSequence[float],
                 Pt: MutableSequence[float], Duvw: MutableSequence[float]) -> None: ...
    def EvaluateScalar(
        self, uvw: MutableSequence[float], Pt: MutableSequence[float], Duvw: MutableSequence[float]) -> float: ...

    def GetCrossSectionRadius(self) -> float: ...
    def GetDimension(self) -> int: ...
    def GetN1(self) -> float: ...
    def GetN2(self) -> float: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetRingRadius(self) -> float: ...
    def GetXRadius(self) -> float: ...
    def GetYRadius(self) -> float: ...
    def GetZRadius(self) -> float: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkParametricSuperToroid: ...

    @staticmethod
    def SafeDownCast(
        o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkParametricSuperToroid: ...

    def SetCrossSectionRadius(self, _arg: float) -> None: ...
    def SetN1(self, _arg: float) -> None: ...
    def SetN2(self, _arg: float) -> None: ...
    def SetRingRadius(self, _arg: float) -> None: ...
    def SetXRadius(self, _arg: float) -> None: ...
    def SetYRadius(self, _arg: float) -> None: ...
    def SetZRadius(self, _arg: float) -> None: ...


class vtkParametricTorus(vtkParametricFunction):
    def Evaluate(self, uvw: MutableSequence[float],
                 Pt: MutableSequence[float], Duvw: MutableSequence[float]) -> None: ...
    def EvaluateScalar(
        self, uvw: MutableSequence[float], Pt: MutableSequence[float], Duvw: MutableSequence[float]) -> float: ...

    def GetCrossSectionRadius(self) -> float: ...
    def GetDimension(self) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetRingRadius(self) -> float: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkParametricTorus: ...

    @staticmethod
    def SafeDownCast(
        o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkParametricTorus: ...

    def SetCrossSectionRadius(self, _arg: float) -> None: ...
    def SetRingRadius(self, _arg: float) -> None: ...
