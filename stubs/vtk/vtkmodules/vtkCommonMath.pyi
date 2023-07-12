from typing import Callable, MutableSequence, Sequence, Tuple, TypeVar, Union, overload

import vtkmodules.vtkCommonCore

Callback = Union[Callable[..., None], None]
Buffer = TypeVar("Buffer")
Pointer = TypeVar("Pointer")
Template = TypeVar("Template")

vtkQuaternion: Template
vtkTuple: Template


class vtkAmoebaMinimizer(vtkmodules.vtkCommonCore.vtkObject):
    def EvaluateFunction(self) -> None: ...
    def GetContractionRatio(self) -> float: ...
    def GetContractionRatioMaxValue(self) -> float: ...
    def GetContractionRatioMinValue(self) -> float: ...
    def GetExpansionRatio(self) -> float: ...
    def GetExpansionRatioMaxValue(self) -> float: ...
    def GetExpansionRatioMinValue(self) -> float: ...
    def GetFunctionEvaluations(self) -> int: ...
    def GetFunctionValue(self) -> float: ...
    def GetIterations(self) -> int: ...
    def GetMaxIterations(self) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetNumberOfParameters(self) -> int: ...
    def GetParameterName(self, i: int) -> str: ...
    @overload
    def GetParameterScale(self, name: str) -> float: ...
    @overload
    def GetParameterScale(self, i: int) -> float: ...
    def GetParameterTolerance(self) -> float: ...
    @overload
    def GetParameterValue(self, name: str) -> float: ...
    @overload
    def GetParameterValue(self, i: int) -> float: ...
    def GetTolerance(self) -> float: ...
    def Initialize(self) -> None: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def Iterate(self) -> int: ...
    def Minimize(self) -> None: ...
    def NewInstance(self) -> vtkAmoebaMinimizer: ...

    @staticmethod
    def SafeDownCast(
        o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkAmoebaMinimizer: ...

    def SetContractionRatio(self, _arg: float) -> None: ...
    def SetExpansionRatio(self, _arg: float) -> None: ...
    def SetFunction(self, f: Callback) -> None: ...
    def SetFunctionValue(self, _arg: float) -> None: ...
    def SetMaxIterations(self, _arg: int) -> None: ...
    @overload
    def SetParameterScale(self, name: str, scale: float) -> None: ...
    @overload
    def SetParameterScale(self, i: int, scale: float) -> None: ...
    def SetParameterTolerance(self, _arg: float) -> None: ...
    @overload
    def SetParameterValue(self, name: str, value: float) -> None: ...
    @overload
    def SetParameterValue(self, i: int, value: float) -> None: ...
    def SetTolerance(self, _arg: float) -> None: ...


class vtkFFT(vtkmodules.vtkCommonCore.vtkObject):
    @staticmethod
    def BartlettGenerator(x: int, size: int) -> float: ...
    @staticmethod
    def BlackmanGenerator(x: int, size: int) -> float: ...

    @staticmethod
    def FftFreq(windowLength: int,
                sampleSpacing: float) -> Tuple[float, float]: ...

    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    @staticmethod
    def HanningGenerator(x: int, size: int) -> float: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkFFT: ...

    @staticmethod
    def RFftFreq(windowLength: int,
                 sampleSpacing: float) -> Tuple[float, float]: ...

    @staticmethod
    def RectangularGenerator(x: int, size: int) -> float: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkFFT: ...
    @staticmethod
    def SineGenerator(x: int, size: int) -> float: ...


class vtkFunctionSet(vtkmodules.vtkCommonCore.vtkObject):
    @overload
    def FunctionValues(
        self, x: MutableSequence[float], f: MutableSequence[float]) -> int: ...

    @overload
    def FunctionValues(
        self, x: MutableSequence[float], f: MutableSequence[float], userData: Pointer) -> int: ...

    def GetNumberOfFunctions(self) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetNumberOfIndependentVariables(self) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkFunctionSet: ...

    @staticmethod
    def SafeDownCast(
        o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkFunctionSet: ...


class vtkInitialValueProblemSolver(vtkmodules.vtkCommonCore.vtkObject):
    class ErrorCodes(int):
        ...
    NOT_INITIALIZED: ErrorCodes
    OUT_OF_DOMAIN: ErrorCodes
    UNEXPECTED_VALUE: ErrorCodes

    @overload
    def ComputeNextStep(
        self, xprev: MutableSequence[float], xnext: MutableSequence[float], t: float, delT: float, maxError: float, error: float
    ) -> int: ...

    @overload
    def ComputeNextStep(
        self,
        xprev: MutableSequence[float],
        xnext: MutableSequence[float],
        t: float,
        delT: float,
        maxError: float,
        error: float,
        userData: Pointer,
    ) -> int: ...

    @overload
    def ComputeNextStep(
        self,
        xprev: MutableSequence[float],
        dxprev: MutableSequence[float],
        xnext: MutableSequence[float],
        t: float,
        delT: float,
        maxError: float,
        error: float,
    ) -> int: ...

    @overload
    def ComputeNextStep(
        self,
        xprev: MutableSequence[float],
        dxprev: MutableSequence[float],
        xnext: MutableSequence[float],
        t: float,
        delT: float,
        maxError: float,
        error: float,
        userData: Pointer,
    ) -> int: ...

    @overload
    def ComputeNextStep(
        self,
        xprev: MutableSequence[float],
        xnext: MutableSequence[float],
        t: float,
        delT: float,
        delTActual: float,
        minStep: float,
        maxStep: float,
        maxError: float,
        error: float,
    ) -> int: ...

    @overload
    def ComputeNextStep(
        self,
        xprev: MutableSequence[float],
        xnext: MutableSequence[float],
        t: float,
        delT: float,
        delTActual: float,
        minStep: float,
        maxStep: float,
        maxError: float,
        error: float,
        userData: Pointer,
    ) -> int: ...
    def GetFunctionSet(self) -> vtkFunctionSet: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    def IsAdaptive(self) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkInitialValueProblemSolver: ...

    @staticmethod
    def SafeDownCast(
        o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkInitialValueProblemSolver: ...

    def SetFunctionSet(self, fset: vtkFunctionSet) -> None: ...


class vtkMatrix3x3(vtkmodules.vtkCommonCore.vtkObject):
    @overload
    def Adjoint(self, in_: vtkMatrix3x3, out: vtkMatrix3x3) -> None: ...

    @overload
    @staticmethod
    def Adjoint(inElements: Sequence[float],
                outElements: MutableSequence[float]) -> None: ...

    @overload
    def DeepCopy(self, source: vtkMatrix3x3) -> None: ...

    @overload
    @staticmethod
    def DeepCopy(
        elements: MutableSequence[float], source: vtkMatrix3x3) -> None: ...

    @overload
    @staticmethod
    def DeepCopy(
        elements: MutableSequence[float], newElements: Sequence[float]) -> None: ...

    @overload
    def DeepCopy(self, elements: Sequence[float]) -> None: ...
    @overload
    def Determinant(self) -> float: ...
    @overload
    @staticmethod
    def Determinant(elements: Sequence[float]) -> float: ...
    def GetData(self) -> Tuple[float, float, float,
                               float, float, float, float, float, float]: ...

    def GetElement(self, i: int, j: int) -> float: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    @overload
    def Identity(self) -> None: ...
    @overload
    @staticmethod
    def Identity(elements: MutableSequence[float]) -> None: ...
    @overload
    @staticmethod
    def Invert(in_: vtkMatrix3x3, out: vtkMatrix3x3) -> None: ...
    @overload
    def Invert(self) -> None: ...

    @overload
    @staticmethod
    def Invert(inElements: Sequence[float],
               outElements: MutableSequence[float]) -> None: ...

    def IsA(self, type: str) -> int: ...
    def IsIdentity(self) -> bool: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...

    @overload
    @staticmethod
    def Multiply3x3(a: vtkMatrix3x3, b: vtkMatrix3x3,
                    c: vtkMatrix3x3) -> None: ...

    @overload
    @staticmethod
    def Multiply3x3(a: Sequence[float], b: Sequence[float],
                    c: MutableSequence[float]) -> None: ...

    @overload
    def MultiplyPoint(
        self, in_: Sequence[float], out: MutableSequence[float]) -> None: ...

    @overload
    @staticmethod
    def MultiplyPoint(
        elements: Sequence[float], in_: Sequence[float], out: MutableSequence[float]) -> None: ...

    def NewInstance(self) -> vtkMatrix3x3: ...

    @staticmethod
    def SafeDownCast(
        o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkMatrix3x3: ...

    def SetElement(self, i: int, j: int, value: float) -> None: ...
    @overload
    @staticmethod
    def Transpose(in_: vtkMatrix3x3, out: vtkMatrix3x3) -> None: ...
    @overload
    def Transpose(self) -> None: ...

    @overload
    @staticmethod
    def Transpose(
        inElements: Sequence[float], outElements: MutableSequence[float]) -> None: ...

    @overload
    def Zero(self) -> None: ...
    @overload
    @staticmethod
    def Zero(elements: MutableSequence[float]) -> None: ...


class vtkMatrix4x4(vtkmodules.vtkCommonCore.vtkObject):
    @overload
    def Adjoint(self, in_: vtkMatrix4x4, out: vtkMatrix4x4) -> None: ...

    @overload
    @staticmethod
    def Adjoint(inElements: Sequence[float],
                outElements: MutableSequence[float]) -> None: ...

    @overload
    def DeepCopy(self, source: vtkMatrix4x4) -> None: ...

    @overload
    @staticmethod
    def DeepCopy(
        destination: MutableSequence[float], source: vtkMatrix4x4) -> None: ...

    @overload
    @staticmethod
    def DeepCopy(
        destination: MutableSequence[float], source: Sequence[float]) -> None: ...

    @overload
    def DeepCopy(self, elements: Sequence[float]) -> None: ...
    @overload
    def Determinant(self) -> float: ...
    @overload
    @staticmethod
    def Determinant(elements: Sequence[float]) -> float: ...
    def GetData(self) -> Pointer: ...
    def GetElement(self, i: int, j: int) -> float: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    @overload
    def Identity(self) -> None: ...
    @overload
    @staticmethod
    def Identity(elements: MutableSequence[float]) -> None: ...
    @overload
    @staticmethod
    def Invert(in_: vtkMatrix4x4, out: vtkMatrix4x4) -> None: ...
    @overload
    def Invert(self) -> None: ...

    @overload
    @staticmethod
    def Invert(inElements: Sequence[float],
               outElements: MutableSequence[float]) -> None: ...

    def IsA(self, type: str) -> int: ...
    def IsIdentity(self) -> bool: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...

    @overload
    @staticmethod
    def MatrixFromRotation(angle: float, x: float, y: float,
                           z: float, result: vtkMatrix4x4) -> None: ...

    @overload
    @staticmethod
    def MatrixFromRotation(angle: float, x: float, y: float,
                           z: float, matrix: MutableSequence[float]) -> None: ...

    @overload
    @staticmethod
    def Multiply4x4(a: vtkMatrix4x4, b: vtkMatrix4x4,
                    c: vtkMatrix4x4) -> None: ...

    @overload
    @staticmethod
    def Multiply4x4(a: Sequence[float], b: Sequence[float],
                    c: MutableSequence[float]) -> None: ...

    @staticmethod
    def MultiplyAndTranspose4x4(
        a: Sequence[float], b: Sequence[float], c: MutableSequence[float]) -> None: ...

    def MultiplyDoublePoint(
        self, in_: Sequence[float]) -> Tuple[float, float, float, float]: ...

    def MultiplyFloatPoint(
        self, in_: Sequence[float]) -> Tuple[float, float, float, float]: ...

    @overload
    def MultiplyPoint(
        self, in_: Sequence[float], out: MutableSequence[float]) -> None: ...

    @overload
    @staticmethod
    def MultiplyPoint(
        elements: Sequence[float], in_: Sequence[float], out: MutableSequence[float]) -> None: ...

    @overload
    def MultiplyPoint(self, in_: Sequence[float]) -> Tuple[float,
                                                           float, float, float]: ...

    def NewInstance(self) -> vtkMatrix4x4: ...

    @staticmethod
    def PoseToMatrix(
        pos: MutableSequence[float], ori: MutableSequence[float], mat: vtkMatrix4x4) -> None: ...

    @staticmethod
    def SafeDownCast(
        o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkMatrix4x4: ...

    def SetElement(self, i: int, j: int, value: float) -> None: ...
    @overload
    @staticmethod
    def Transpose(in_: vtkMatrix4x4, out: vtkMatrix4x4) -> None: ...
    @overload
    def Transpose(self) -> None: ...

    @overload
    @staticmethod
    def Transpose(
        inElements: Sequence[float], outElements: MutableSequence[float]) -> None: ...

    @overload
    def Zero(self) -> None: ...
    @overload
    @staticmethod
    def Zero(elements: MutableSequence[float]) -> None: ...


class vtkPolynomialSolversUnivariate(vtkmodules.vtkCommonCore.vtkObject):
    @staticmethod
    def FerrariSolve(c: MutableSequence[float], r: MutableSequence[float],
                     m: MutableSequence[int], tol: float) -> int: ...

    @staticmethod
    def FilterRoots(
        P: MutableSequence[float], d: int, upperBnds: MutableSequence[float], rootcount: int, diameter: float
    ) -> int: ...
    @staticmethod
    def GetDivisionTolerance() -> float: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...

    @overload
    @staticmethod
    def HabichtBisectionSolve(
        P: MutableSequence[float], d: int, a: MutableSequence[float], upperBnds: MutableSequence[float], tol: float
    ) -> int: ...

    @overload
    @staticmethod
    def HabichtBisectionSolve(
        P: MutableSequence[float],
        d: int,
        a: MutableSequence[float],
        upperBnds: MutableSequence[float],
        tol: float,
        intervalType: int,
    ) -> int: ...

    @overload
    @staticmethod
    def HabichtBisectionSolve(
        P: MutableSequence[float],
        d: int,
        a: MutableSequence[float],
        upperBnds: MutableSequence[float],
        tol: float,
        intervalType: int,
        divideGCD: bool,
    ) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...

    @staticmethod
    def LinBairstowSolve(
        c: MutableSequence[float], d: int, r: MutableSequence[float], tolerance: float) -> int: ...

    def NewInstance(self) -> vtkPolynomialSolversUnivariate: ...

    @staticmethod
    def SafeDownCast(
        o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkPolynomialSolversUnivariate: ...

    @staticmethod
    def SetDivisionTolerance(tol: float) -> None: ...
    @overload
    @staticmethod
    def SolveCubic(c0: float, c1: float, c2: float, c3: float) -> Pointer: ...

    @overload
    @staticmethod
    def SolveCubic(
        c0: float,
        c1: float,
        c2: float,
        c3: float,
        r1: MutableSequence[float],
        r2: MutableSequence[float],
        r3: MutableSequence[float],
        num_roots: MutableSequence[int],
    ) -> int: ...
    @overload
    @staticmethod
    def SolveLinear(c0: float, c1: float) -> Pointer: ...

    @overload
    @staticmethod
    def SolveLinear(c0: float, c1: float,
                    r1: MutableSequence[float], num_roots: MutableSequence[int]) -> int: ...

    @overload
    @staticmethod
    def SolveQuadratic(c0: float, c1: float, c2: float) -> Pointer: ...

    @overload
    @staticmethod
    def SolveQuadratic(
        c0: float, c1: float, c2: float, r1: MutableSequence[float], r2: MutableSequence[float], num_roots: MutableSequence[int]
    ) -> int: ...

    @overload
    @staticmethod
    def SolveQuadratic(
        c: MutableSequence[float], r: MutableSequence[float], m: MutableSequence[int]) -> int: ...

    @overload
    @staticmethod
    def SturmBisectionSolve(
        P: MutableSequence[float], d: int, a: MutableSequence[float], upperBnds: MutableSequence[float], tol: float
    ) -> int: ...

    @overload
    @staticmethod
    def SturmBisectionSolve(
        P: MutableSequence[float],
        d: int,
        a: MutableSequence[float],
        upperBnds: MutableSequence[float],
        tol: float,
        intervalType: int,
    ) -> int: ...

    @overload
    @staticmethod
    def SturmBisectionSolve(
        P: MutableSequence[float],
        d: int,
        a: MutableSequence[float],
        upperBnds: MutableSequence[float],
        tol: float,
        intervalType: int,
        divideGCD: bool,
    ) -> int: ...

    @staticmethod
    def TartagliaCardanSolve(
        c: MutableSequence[float], r: MutableSequence[float], m: MutableSequence[int], tol: float
    ) -> int: ...


class vtkQuaternionInterpolator(vtkmodules.vtkCommonCore.vtkObject):
    class vtkQuaternionInterpolationSearchMethod(int):
        ...
    BinarySearch: vtkQuaternionInterpolationSearchMethod
    INTERPOLATION_TYPE_LINEAR: int
    INTERPOLATION_TYPE_SPLINE: int
    LinearSearch: vtkQuaternionInterpolationSearchMethod
    MaxEnum: vtkQuaternionInterpolationSearchMethod
    @overload
    def AddQuaternion(self, t: float, q: vtkQuaterniond) -> None: ...
    @overload
    def AddQuaternion(self, t: float, q: MutableSequence[float]) -> None: ...
    def GetInterpolationType(self) -> int: ...
    def GetInterpolationTypeMaxValue(self) -> int: ...
    def GetInterpolationTypeMinValue(self) -> int: ...
    def GetMaximumT(self) -> float: ...
    def GetMinimumT(self) -> float: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetNumberOfQuaternions(self) -> int: ...
    def GetSearchMethod(self) -> int: ...
    def Initialize(self) -> None: ...
    @overload
    def InterpolateQuaternion(self, t: float, q: vtkQuaterniond) -> None: ...

    @overload
    def InterpolateQuaternion(
        self, t: float, q: MutableSequence[float]) -> None: ...

    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkQuaternionInterpolator: ...
    def RemoveQuaternion(self, t: float) -> None: ...

    @staticmethod
    def SafeDownCast(
        o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkQuaternionInterpolator: ...

    def SetInterpolationType(self, _arg: int) -> None: ...
    def SetInterpolationTypeToLinear(self) -> None: ...
    def SetInterpolationTypeToSpline(self) -> None: ...
    def SetSearchMethod(self, type: int) -> None: ...


class vtkTuple_IdLi4EE:
    def Compare(self, other: vtkTuple_IdLi4EE, tol: float) -> bool: ...
    def GetData(self) -> Pointer: ...
    def GetSize(self) -> int: ...


class vtkQuaternion_IdE(vtkTuple_IdLi4EE):
    def Conjugate(self) -> None: ...
    def Conjugated(self) -> vtkQuaternion_IdE: ...
    def FromMatrix3x3(self, A: Sequence[Sequence[float]]) -> None: ...
    def Get(self, quat: MutableSequence[float]) -> None: ...
    def GetRotationAngleAndAxis(
        self, axis: MutableSequence[float]) -> float: ...

    def GetW(self) -> float: ...
    def GetX(self) -> float: ...
    def GetY(self) -> float: ...
    def GetZ(self) -> float: ...
    @staticmethod
    def Identity() -> vtkQuaternion_IdE: ...
    def InnerPoint(self, q1: vtkQuaternion_IdE,
                   q2: vtkQuaternion_IdE) -> vtkQuaternion_IdE: ...

    def Inverse(self) -> vtkQuaternion_IdE: ...
    def Invert(self) -> None: ...
    def Norm(self) -> float: ...
    def Normalize(self) -> float: ...
    def NormalizeWithAngleInDegrees(self) -> None: ...
    def Normalized(self) -> vtkQuaternion_IdE: ...
    def NormalizedWithAngleInDegrees(self) -> vtkQuaternion_IdE: ...
    @overload
    def Set(self, w: float, x: float, y: float, z: float) -> None: ...
    @overload
    def Set(self, quat: MutableSequence[float]) -> None: ...

    @overload
    def SetRotationAngleAndAxis(
        self, angle: float, axis: MutableSequence[float]) -> None: ...

    @overload
    def SetRotationAngleAndAxis(
        self, angle: float, x: float, y: float, z: float) -> None: ...

    def SetW(self, w: float) -> None: ...
    def SetX(self, x: float) -> None: ...
    def SetY(self, y: float) -> None: ...
    def SetZ(self, z: float) -> None: ...
    def Slerp(self, t: float, q: vtkQuaternion_IdE) -> vtkQuaternion_IdE: ...
    def SquaredNorm(self) -> float: ...
    def ToIdentity(self) -> None: ...
    def ToMatrix3x3(
        self, A: MutableSequence[MutableSequence[float]]) -> None: ...

    def ToUnitExp(self) -> None: ...
    def ToUnitLog(self) -> None: ...
    def UnitExp(self) -> vtkQuaternion_IdE: ...
    def UnitLog(self) -> vtkQuaternion_IdE: ...


class vtkTuple_IfLi4EE:
    def Compare(self, other: vtkTuple_IfLi4EE, tol: float) -> bool: ...
    def GetData(self) -> Pointer: ...
    def GetSize(self) -> int: ...


class vtkQuaternion_IfE(vtkTuple_IfLi4EE):
    def Conjugate(self) -> None: ...
    def Conjugated(self) -> vtkQuaternion_IfE: ...
    def FromMatrix3x3(self, A: Sequence[Sequence[float]]) -> None: ...
    def Get(self, quat: MutableSequence[float]) -> None: ...
    def GetRotationAngleAndAxis(
        self, axis: MutableSequence[float]) -> float: ...

    def GetW(self) -> float: ...
    def GetX(self) -> float: ...
    def GetY(self) -> float: ...
    def GetZ(self) -> float: ...
    @staticmethod
    def Identity() -> vtkQuaternion_IfE: ...
    def InnerPoint(self, q1: vtkQuaternion_IfE,
                   q2: vtkQuaternion_IfE) -> vtkQuaternion_IfE: ...

    def Inverse(self) -> vtkQuaternion_IfE: ...
    def Invert(self) -> None: ...
    def Norm(self) -> float: ...
    def Normalize(self) -> float: ...
    def NormalizeWithAngleInDegrees(self) -> None: ...
    def Normalized(self) -> vtkQuaternion_IfE: ...
    def NormalizedWithAngleInDegrees(self) -> vtkQuaternion_IfE: ...
    @overload
    def Set(self, w: float, x: float, y: float, z: float) -> None: ...
    @overload
    def Set(self, quat: MutableSequence[float]) -> None: ...

    @overload
    def SetRotationAngleAndAxis(
        self, angle: float, axis: MutableSequence[float]) -> None: ...

    @overload
    def SetRotationAngleAndAxis(
        self, angle: float, x: float, y: float, z: float) -> None: ...

    def SetW(self, w: float) -> None: ...
    def SetX(self, x: float) -> None: ...
    def SetY(self, y: float) -> None: ...
    def SetZ(self, z: float) -> None: ...
    def Slerp(self, t: float, q: vtkQuaternion_IfE) -> vtkQuaternion_IfE: ...
    def SquaredNorm(self) -> float: ...
    def ToIdentity(self) -> None: ...
    def ToMatrix3x3(
        self, A: MutableSequence[MutableSequence[float]]) -> None: ...

    def ToUnitExp(self) -> None: ...
    def ToUnitLog(self) -> None: ...
    def UnitExp(self) -> vtkQuaternion_IfE: ...
    def UnitLog(self) -> vtkQuaternion_IfE: ...


class vtkQuaterniond(vtkQuaternion_IdE):
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, w: float, x: float, y: float, z: float) -> None: ...
    @overload
    def __init__(self, scalar: float) -> None: ...
    @overload
    def __init__(self, init: Sequence[float]) -> None: ...
    @overload
    def __init__(self, __a: vtkQuaterniond) -> None: ...
    def Conjugated(self) -> vtkQuaterniond: ...
    def Identity(self) -> vtkQuaterniond: ...
    def InnerPoint(self, q1: vtkQuaterniond,
                   q2: vtkQuaterniond) -> vtkQuaterniond: ...

    def Inverse(self) -> vtkQuaterniond: ...
    def Normalized(self) -> vtkQuaterniond: ...
    def NormalizedWithAngleInDegrees(self) -> vtkQuaterniond: ...
    def Slerp(self, t: float, q: vtkQuaterniond) -> vtkQuaterniond: ...
    def UnitExp(self) -> vtkQuaterniond: ...
    def UnitLog(self) -> vtkQuaterniond: ...


class vtkQuaternionf(vtkQuaternion_IfE):
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, w: float, x: float, y: float, z: float) -> None: ...
    @overload
    def __init__(self, scalar: float) -> None: ...
    @overload
    def __init__(self, init: Sequence[float]) -> None: ...
    @overload
    def __init__(self, __a: vtkQuaternionf) -> None: ...
    def Conjugated(self) -> vtkQuaternionf: ...
    def Identity(self) -> vtkQuaternionf: ...
    def InnerPoint(self, q1: vtkQuaternionf,
                   q2: vtkQuaternionf) -> vtkQuaternionf: ...

    def Inverse(self) -> vtkQuaternionf: ...
    def Normalized(self) -> vtkQuaternionf: ...
    def NormalizedWithAngleInDegrees(self) -> vtkQuaternionf: ...
    def Slerp(self, t: float, q: vtkQuaternionf) -> vtkQuaternionf: ...
    def UnitExp(self) -> vtkQuaternionf: ...
    def UnitLog(self) -> vtkQuaternionf: ...


class vtkRungeKutta2(vtkInitialValueProblemSolver):
    @overload
    def ComputeNextStep(
        self,
        xprev: MutableSequence[float],
        xnext: MutableSequence[float],
        t: float,
        delT: float,
        maxError: float,
        error: float,
        userData: Pointer,
    ) -> int: ...

    @overload
    def ComputeNextStep(
        self,
        xprev: MutableSequence[float],
        dxprev: MutableSequence[float],
        xnext: MutableSequence[float],
        t: float,
        delT: float,
        maxError: float,
        error: float,
        userData: Pointer,
    ) -> int: ...

    @overload
    def ComputeNextStep(
        self,
        xprev: MutableSequence[float],
        xnext: MutableSequence[float],
        t: float,
        delT: float,
        delTActual: float,
        minStep: float,
        maxStep: float,
        maxError: float,
        error: float,
        userData: Pointer,
    ) -> int: ...

    @overload
    def ComputeNextStep(
        self,
        xprev: MutableSequence[float],
        dxprev: MutableSequence[float],
        xnext: MutableSequence[float],
        t: float,
        delT: float,
        delTActual: float,
        minStep: float,
        maxStep: float,
        maxError: float,
        error: float,
        userData: Pointer,
    ) -> int: ...

    @overload
    def ComputeNextStep(
        self, xprev: MutableSequence[float], xnext: MutableSequence[float], t: float, delT: float, maxError: float, error: float
    ) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkRungeKutta2: ...

    @staticmethod
    def SafeDownCast(
        o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkRungeKutta2: ...


class vtkRungeKutta4(vtkInitialValueProblemSolver):
    @overload
    def ComputeNextStep(
        self,
        xprev: MutableSequence[float],
        xnext: MutableSequence[float],
        t: float,
        delT: float,
        maxError: float,
        error: float,
        userData: Pointer,
    ) -> int: ...

    @overload
    def ComputeNextStep(
        self,
        xprev: MutableSequence[float],
        dxprev: MutableSequence[float],
        xnext: MutableSequence[float],
        t: float,
        delT: float,
        maxError: float,
        error: float,
        userData: Pointer,
    ) -> int: ...

    @overload
    def ComputeNextStep(
        self,
        xprev: MutableSequence[float],
        xnext: MutableSequence[float],
        t: float,
        delT: float,
        delTActual: float,
        minStep: float,
        maxStep: float,
        maxError: float,
        error: float,
        userData: Pointer,
    ) -> int: ...

    @overload
    def ComputeNextStep(
        self,
        xprev: MutableSequence[float],
        dxprev: MutableSequence[float],
        xnext: MutableSequence[float],
        t: float,
        delT: float,
        delTActual: float,
        minStep: float,
        maxStep: float,
        maxError: float,
        error: float,
        userData: Pointer,
    ) -> int: ...

    @overload
    def ComputeNextStep(
        self, xprev: MutableSequence[float], xnext: MutableSequence[float], t: float, delT: float, maxError: float, error: float
    ) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkRungeKutta4: ...

    @staticmethod
    def SafeDownCast(
        o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkRungeKutta4: ...


class vtkRungeKutta45(vtkInitialValueProblemSolver):
    @overload
    def ComputeNextStep(
        self,
        xprev: MutableSequence[float],
        xnext: MutableSequence[float],
        t: float,
        delT: float,
        maxError: float,
        error: float,
        userData: Pointer,
    ) -> int: ...

    @overload
    def ComputeNextStep(
        self,
        xprev: MutableSequence[float],
        dxprev: MutableSequence[float],
        xnext: MutableSequence[float],
        t: float,
        delT: float,
        maxError: float,
        error: float,
        userData: Pointer,
    ) -> int: ...

    @overload
    def ComputeNextStep(
        self,
        xprev: MutableSequence[float],
        xnext: MutableSequence[float],
        t: float,
        delT: float,
        delTActual: float,
        minStep: float,
        maxStep: float,
        maxError: float,
        error: float,
        userData: Pointer,
    ) -> int: ...

    @overload
    def ComputeNextStep(
        self,
        xprev: MutableSequence[float],
        dxprev: MutableSequence[float],
        xnext: MutableSequence[float],
        t: float,
        delT: float,
        delTActual: float,
        minStep: float,
        maxStep: float,
        maxError: float,
        estErr: float,
        userData: Pointer,
    ) -> int: ...

    @overload
    def ComputeNextStep(
        self, xprev: MutableSequence[float], xnext: MutableSequence[float], t: float, delT: float, maxError: float, error: float
    ) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkRungeKutta45: ...

    @staticmethod
    def SafeDownCast(
        o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkRungeKutta45: ...


class vtkTuple_IdLi2EE:
    def Compare(self, other: vtkTuple_IdLi2EE, tol: float) -> bool: ...
    def GetData(self) -> Pointer: ...
    def GetSize(self) -> int: ...


class vtkTuple_IdLi3EE:
    def Compare(self, other: vtkTuple_IdLi3EE, tol: float) -> bool: ...
    def GetData(self) -> Pointer: ...
    def GetSize(self) -> int: ...


class vtkTuple_IfLi2EE:
    def Compare(self, other: vtkTuple_IfLi2EE, tol: float) -> bool: ...
    def GetData(self) -> Pointer: ...
    def GetSize(self) -> int: ...


class vtkTuple_IfLi3EE:
    def Compare(self, other: vtkTuple_IfLi3EE, tol: float) -> bool: ...
    def GetData(self) -> Pointer: ...
    def GetSize(self) -> int: ...


class vtkTuple_IhLi2EE:
    def Compare(self, other: vtkTuple_IhLi2EE, tol: int) -> bool: ...
    def GetData(self) -> Pointer: ...
    def GetSize(self) -> int: ...


class vtkTuple_IhLi3EE:
    def Compare(self, other: vtkTuple_IhLi3EE, tol: int) -> bool: ...
    def GetData(self) -> Pointer: ...
    def GetSize(self) -> int: ...


class vtkTuple_IhLi4EE:
    def Compare(self, other: vtkTuple_IhLi4EE, tol: int) -> bool: ...
    def GetData(self) -> Pointer: ...
    def GetSize(self) -> int: ...


class vtkTuple_IiLi2EE:
    def Compare(self, other: vtkTuple_IiLi2EE, tol: int) -> bool: ...
    def GetData(self) -> Pointer: ...
    def GetSize(self) -> int: ...


class vtkTuple_IiLi3EE:
    def Compare(self, other: vtkTuple_IiLi3EE, tol: int) -> bool: ...
    def GetData(self) -> Pointer: ...
    def GetSize(self) -> int: ...


class vtkTuple_IiLi4EE:
    def Compare(self, other: vtkTuple_IiLi4EE, tol: int) -> bool: ...
    def GetData(self) -> Pointer: ...
    def GetSize(self) -> int: ...
