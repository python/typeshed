from typing import Callable, MutableSequence, Sequence, Tuple, TypeVar, Union, overload

import vtkmodules.vtkCommonCore
import vtkmodules.vtkCommonMath

Callback = Union[Callable[..., None], None]
Buffer = TypeVar("Buffer")
Pointer = TypeVar("Pointer")
Template = TypeVar("Template")



VTK_LANDMARK_AFFINE: int
VTK_LANDMARK_RIGIDBODY: int
VTK_LANDMARK_SIMILARITY: int
VTK_RBF_CUSTOM: int
VTK_RBF_R: int
VTK_RBF_R2LOGR: int


class vtkAbstractTransform(vtkmodules.vtkCommonCore.vtkObject):
    def CircuitCheck(self, transform: vtkAbstractTransform) -> int: ...
    def DeepCopy(self, __a: vtkAbstractTransform) -> None: ...
    def GetInverse(self) -> vtkAbstractTransform: ...
    def GetMTime(self) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...

    def InternalTransformDerivative(
        self, in_: Sequence[float], out: MutableSequence[float], derivative: MutableSequence[MutableSequence[float]]
    ) -> None: ...
    def InternalTransformPoint(
        self, in_: Sequence[float], out: MutableSequence[float]) -> None: ...

    def Inverse(self) -> None: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def MakeTransform(self) -> vtkAbstractTransform: ...
    def NewInstance(self) -> vtkAbstractTransform: ...

    @staticmethod
    def SafeDownCast(
        o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkAbstractTransform: ...

    def SetInverse(self, transform: vtkAbstractTransform) -> None: ...

    def TransformDoubleNormalAtPoint(
        self, point: Sequence[float], normal: Sequence[float]) -> Tuple[float, float, float]: ...

    @overload
    def TransformDoublePoint(self, x: float, y: float,
                             z: float) -> Tuple[float, float, float]: ...

    @overload
    def TransformDoublePoint(
        self, point: Sequence[float]) -> Tuple[float, float, float]: ...

    def TransformDoubleVectorAtPoint(
        self, point: Sequence[float], vector: Sequence[float]) -> Tuple[float, float, float]: ...

    def TransformFloatNormalAtPoint(
        self, point: Sequence[float], normal: Sequence[float]) -> Tuple[float, float, float]: ...

    @overload
    def TransformFloatPoint(self, x: float, y: float,
                            z: float) -> Tuple[float, float, float]: ...

    @overload
    def TransformFloatPoint(
        self, point: Sequence[float]) -> Tuple[float, float, float]: ...

    def TransformFloatVectorAtPoint(
        self, point: Sequence[float], vector: Sequence[float]) -> Tuple[float, float, float]: ...

    @overload
    def TransformNormalAtPoint(
        self, point: Sequence[float], in_: Sequence[float], out: MutableSequence[float]) -> None: ...

    @overload
    def TransformNormalAtPoint(
        self, point: Sequence[float], normal: Sequence[float]) -> Tuple[float, float, float]: ...

    @overload
    def TransformPoint(
        self, in_: Sequence[float], out: MutableSequence[float]) -> None: ...

    @overload
    def TransformPoint(self, x: float, y: float,
                       z: float) -> Tuple[float, float, float]: ...

    @overload
    def TransformPoint(
        self, point: Sequence[float]) -> Tuple[float, float, float]: ...

    def TransformPoints(self, inPts: vtkmodules.vtkCommonCore.vtkPoints,
                        outPts: vtkmodules.vtkCommonCore.vtkPoints) -> None: ...

    @overload
    def TransformVectorAtPoint(
        self, point: Sequence[float], in_: Sequence[float], out: MutableSequence[float]) -> None: ...

    @overload
    def TransformVectorAtPoint(
        self, point: Sequence[float], vector: Sequence[float]) -> Tuple[float, float, float]: ...

    def Update(self) -> None: ...


class vtkWarpTransform(vtkAbstractTransform):
    def GetInverseFlag(self) -> int: ...
    def GetInverseIterations(self) -> int: ...
    def GetInverseTolerance(self) -> float: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...

    def InternalTransformDerivative(
        self, in_: Sequence[float], out: MutableSequence[float], derivative: MutableSequence[MutableSequence[float]]
    ) -> None: ...
    def InternalTransformPoint(
        self, in_: Sequence[float], out: MutableSequence[float]) -> None: ...

    def Inverse(self) -> None: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkWarpTransform: ...

    @staticmethod
    def SafeDownCast(
        o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkWarpTransform: ...

    def SetInverseIterations(self, _arg: int) -> None: ...
    def SetInverseTolerance(self, _arg: float) -> None: ...

    @overload
    def TemplateTransformInverse(
        self, in_: Sequence[float], out: MutableSequence[float]) -> None: ...

    @overload
    def TemplateTransformInverse(
        self, in_: Sequence[float], out: MutableSequence[float], derivative: MutableSequence[MutableSequence[float]]
    ) -> None: ...

    @overload
    def TemplateTransformPoint(
        self, in_: Sequence[float], out: MutableSequence[float]) -> None: ...

    @overload
    def TemplateTransformPoint(
        self, in_: Sequence[float], out: MutableSequence[float], derivative: MutableSequence[MutableSequence[float]]
    ) -> None: ...


class vtkCylindricalTransform(vtkWarpTransform):
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def MakeTransform(self) -> vtkAbstractTransform: ...
    def NewInstance(self) -> vtkCylindricalTransform: ...

    @staticmethod
    def SafeDownCast(
        o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkCylindricalTransform: ...


class vtkGeneralTransform(vtkAbstractTransform):
    def CircuitCheck(self, transform: vtkAbstractTransform) -> int: ...

    @overload
    def Concatenate(
        self, matrix: vtkmodules.vtkCommonMath.vtkMatrix4x4) -> None: ...

    @overload
    def Concatenate(self, elements: Sequence[float]) -> None: ...
    @overload
    def Concatenate(self, transform: vtkAbstractTransform) -> None: ...
    def GetConcatenatedTransform(self, i: int) -> vtkAbstractTransform: ...
    def GetInput(self) -> vtkAbstractTransform: ...
    def GetInverseFlag(self) -> int: ...
    def GetMTime(self) -> int: ...
    def GetNumberOfConcatenatedTransforms(self) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def Identity(self) -> None: ...

    def InternalTransformDerivative(
        self, in_: Sequence[float], out: MutableSequence[float], derivative: MutableSequence[MutableSequence[float]]
    ) -> None: ...
    def InternalTransformPoint(
        self, in_: Sequence[float], out: MutableSequence[float]) -> None: ...

    def Inverse(self) -> None: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def MakeTransform(self) -> vtkAbstractTransform: ...
    def NewInstance(self) -> vtkGeneralTransform: ...
    def Pop(self) -> None: ...
    def PostMultiply(self) -> None: ...
    def PreMultiply(self) -> None: ...
    def Push(self) -> None: ...

    @overload
    def RotateWXYZ(self, angle: float, x: float,
                   y: float, z: float) -> None: ...

    @overload
    def RotateWXYZ(self, angle: float, axis: Sequence[float]) -> None: ...
    def RotateX(self, angle: float) -> None: ...
    def RotateY(self, angle: float) -> None: ...
    def RotateZ(self, angle: float) -> None: ...

    @staticmethod
    def SafeDownCast(
        o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkGeneralTransform: ...

    @overload
    def Scale(self, x: float, y: float, z: float) -> None: ...
    @overload
    def Scale(self, s: Sequence[float]) -> None: ...
    def SetInput(self, input: vtkAbstractTransform) -> None: ...
    @overload
    def Translate(self, x: float, y: float, z: float) -> None: ...
    @overload
    def Translate(self, x: Sequence[float]) -> None: ...


class vtkHomogeneousTransform(vtkAbstractTransform):
    def GetHomogeneousInverse(self) -> vtkHomogeneousTransform: ...
    @overload
    def GetMatrix(self, m: vtkmodules.vtkCommonMath.vtkMatrix4x4) -> None: ...
    @overload
    def GetMatrix(self) -> vtkmodules.vtkCommonMath.vtkMatrix4x4: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...

    def InternalTransformDerivative(
        self, in_: Sequence[float], out: MutableSequence[float], derivative: MutableSequence[MutableSequence[float]]
    ) -> None: ...
    def InternalTransformPoint(
        self, in_: Sequence[float], out: MutableSequence[float]) -> None: ...

    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkHomogeneousTransform: ...

    @staticmethod
    def SafeDownCast(
        o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkHomogeneousTransform: ...
    def TransformPoints(self, inPts: vtkmodules.vtkCommonCore.vtkPoints,
                        outPts: vtkmodules.vtkCommonCore.vtkPoints) -> None: ...


class vtkLinearTransform(vtkHomogeneousTransform):
    def GetLinearInverse(self) -> vtkLinearTransform: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...

    def InternalTransformDerivative(
        self, in_: Sequence[float], out: MutableSequence[float], derivative: MutableSequence[MutableSequence[float]]
    ) -> None: ...

    def InternalTransformNormal(
        self, in_: Sequence[float], out: MutableSequence[float]) -> None: ...

    def InternalTransformPoint(
        self, in_: Sequence[float], out: MutableSequence[float]) -> None: ...
    def InternalTransformVector(
        self, in_: Sequence[float], out: MutableSequence[float]) -> None: ...

    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkLinearTransform: ...

    @staticmethod
    def SafeDownCast(
        o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkLinearTransform: ...

    @overload
    def TransformDoubleNormal(self, x: float, y: float,
                              z: float) -> Tuple[float, float, float]: ...

    @overload
    def TransformDoubleNormal(
        self, normal: Sequence[float]) -> Tuple[float, float, float]: ...

    @overload
    def TransformDoubleVector(self, x: float, y: float,
                              z: float) -> Tuple[float, float, float]: ...

    @overload
    def TransformDoubleVector(
        self, vec: Sequence[float]) -> Tuple[float, float, float]: ...

    @overload
    def TransformFloatNormal(self, x: float, y: float,
                             z: float) -> Tuple[float, float, float]: ...

    @overload
    def TransformFloatNormal(
        self, normal: Sequence[float]) -> Tuple[float, float, float]: ...

    @overload
    def TransformFloatVector(self, x: float, y: float,
                             z: float) -> Tuple[float, float, float]: ...

    @overload
    def TransformFloatVector(
        self, vec: Sequence[float]) -> Tuple[float, float, float]: ...

    @overload
    def TransformNormal(
        self, in_: Sequence[float], out: MutableSequence[float]) -> None: ...

    @overload
    def TransformNormal(self, x: float, y: float,
                        z: float) -> Tuple[float, float, float]: ...

    @overload
    def TransformNormal(
        self, normal: Sequence[float]) -> Tuple[float, float, float]: ...

    def TransformNormals(
        self, inNms: vtkmodules.vtkCommonCore.vtkDataArray, outNms: vtkmodules.vtkCommonCore.vtkDataArray
    ) -> None: ...

    def TransformPoints(self, inPts: vtkmodules.vtkCommonCore.vtkPoints,
                        outPts: vtkmodules.vtkCommonCore.vtkPoints) -> None: ...

    @overload
    def TransformVector(self, x: float, y: float,
                        z: float) -> Tuple[float, float, float]: ...

    @overload
    def TransformVector(
        self, normal: Sequence[float]) -> Tuple[float, float, float]: ...

    @overload
    def TransformVector(
        self, in_: Sequence[float], out: MutableSequence[float]) -> None: ...

    def TransformVectors(
        self, inVrs: vtkmodules.vtkCommonCore.vtkDataArray, outVrs: vtkmodules.vtkCommonCore.vtkDataArray
    ) -> None: ...


class vtkIdentityTransform(vtkLinearTransform):
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...

    def InternalTransformDerivative(
        self, in_: Sequence[float], out: MutableSequence[float], derivative: MutableSequence[MutableSequence[float]]
    ) -> None: ...

    def InternalTransformNormal(
        self, in_: Sequence[float], out: MutableSequence[float]) -> None: ...

    def InternalTransformPoint(
        self, in_: Sequence[float], out: MutableSequence[float]) -> None: ...
    def InternalTransformVector(
        self, in_: Sequence[float], out: MutableSequence[float]) -> None: ...

    def Inverse(self) -> None: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def MakeTransform(self) -> vtkAbstractTransform: ...
    def NewInstance(self) -> vtkIdentityTransform: ...

    @staticmethod
    def SafeDownCast(
        o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkIdentityTransform: ...

    def TransformNormals(
        self, inNms: vtkmodules.vtkCommonCore.vtkDataArray, outNms: vtkmodules.vtkCommonCore.vtkDataArray
    ) -> None: ...

    def TransformPoints(self, inPts: vtkmodules.vtkCommonCore.vtkPoints,
                        outPts: vtkmodules.vtkCommonCore.vtkPoints) -> None: ...

    def TransformVectors(
        self, inVrs: vtkmodules.vtkCommonCore.vtkDataArray, outVrs: vtkmodules.vtkCommonCore.vtkDataArray
    ) -> None: ...


class vtkLandmarkTransform(vtkLinearTransform):
    def GetMTime(self) -> int: ...
    def GetMode(self) -> int: ...
    def GetModeAsString(self) -> str: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetSourceLandmarks(self) -> vtkmodules.vtkCommonCore.vtkPoints: ...
    def GetTargetLandmarks(self) -> vtkmodules.vtkCommonCore.vtkPoints: ...
    def Inverse(self) -> None: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def MakeTransform(self) -> vtkAbstractTransform: ...
    def NewInstance(self) -> vtkLandmarkTransform: ...

    @staticmethod
    def SafeDownCast(
        o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkLandmarkTransform: ...

    def SetMode(self, _arg: int) -> None: ...
    def SetModeToAffine(self) -> None: ...
    def SetModeToRigidBody(self) -> None: ...
    def SetModeToSimilarity(self) -> None: ...

    def SetSourceLandmarks(
        self, source: vtkmodules.vtkCommonCore.vtkPoints) -> None: ...
    def SetTargetLandmarks(
        self, target: vtkmodules.vtkCommonCore.vtkPoints) -> None: ...


class vtkMatrixToHomogeneousTransform(vtkHomogeneousTransform):
    def GetInput(self) -> vtkmodules.vtkCommonMath.vtkMatrix4x4: ...
    def GetMTime(self) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def Inverse(self) -> None: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def MakeTransform(self) -> vtkAbstractTransform: ...
    def NewInstance(self) -> vtkMatrixToHomogeneousTransform: ...

    @staticmethod
    def SafeDownCast(
        o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkMatrixToHomogeneousTransform: ...

    def SetInput(self, __a: vtkmodules.vtkCommonMath.vtkMatrix4x4) -> None: ...


class vtkMatrixToLinearTransform(vtkLinearTransform):
    def GetInput(self) -> vtkmodules.vtkCommonMath.vtkMatrix4x4: ...
    def GetMTime(self) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def Inverse(self) -> None: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def MakeTransform(self) -> vtkAbstractTransform: ...
    def NewInstance(self) -> vtkMatrixToLinearTransform: ...

    @staticmethod
    def SafeDownCast(
        o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkMatrixToLinearTransform: ...

    def SetInput(self, __a: vtkmodules.vtkCommonMath.vtkMatrix4x4) -> None: ...


class vtkPerspectiveTransform(vtkHomogeneousTransform):
    def AdjustViewport(
        self,
        oldXMin: float,
        oldXMax: float,
        oldYMin: float,
        oldYMax: float,
        newXMin: float,
        newXMax: float,
        newYMin: float,
        newYMax: float,
    ) -> None: ...
    def AdjustZBuffer(self, oldNearZ: float, oldFarZ: float,
                      newNearZ: float, newFarZ: float) -> None: ...

    def CircuitCheck(self, transform: vtkAbstractTransform) -> int: ...

    @overload
    def Concatenate(
        self, matrix: vtkmodules.vtkCommonMath.vtkMatrix4x4) -> None: ...

    @overload
    def Concatenate(self, elements: Sequence[float]) -> None: ...
    @overload
    def Concatenate(self, transform: vtkHomogeneousTransform) -> None: ...
    def Frustum(self, xmin: float, xmax: float, ymin: float,
                ymax: float, znear: float, zfar: float) -> None: ...

    def GetConcatenatedTransform(self, i: int) -> vtkHomogeneousTransform: ...
    def GetInput(self) -> vtkHomogeneousTransform: ...
    def GetInverseFlag(self) -> int: ...
    def GetMTime(self) -> int: ...
    def GetNumberOfConcatenatedTransforms(self) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def Identity(self) -> None: ...
    def Inverse(self) -> None: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def MakeTransform(self) -> vtkAbstractTransform: ...
    def NewInstance(self) -> vtkPerspectiveTransform: ...

    def Ortho(self, xmin: float, xmax: float, ymin: float,
              ymax: float, znear: float, zfar: float) -> None: ...
    def Perspective(self, angle: float, aspect: float,
                    znear: float, zfar: float) -> None: ...

    def Pop(self) -> None: ...
    def PostMultiply(self) -> None: ...
    def PreMultiply(self) -> None: ...
    def Push(self) -> None: ...

    @overload
    def RotateWXYZ(self, angle: float, x: float,
                   y: float, z: float) -> None: ...

    @overload
    def RotateWXYZ(self, angle: float, axis: Sequence[float]) -> None: ...
    def RotateX(self, angle: float) -> None: ...
    def RotateY(self, angle: float) -> None: ...
    def RotateZ(self, angle: float) -> None: ...

    @staticmethod
    def SafeDownCast(
        o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkPerspectiveTransform: ...

    @overload
    def Scale(self, x: float, y: float, z: float) -> None: ...
    @overload
    def Scale(self, s: Sequence[float]) -> None: ...
    def SetInput(self, input: vtkHomogeneousTransform) -> None: ...

    @overload
    def SetMatrix(
        self, matrix: vtkmodules.vtkCommonMath.vtkMatrix4x4) -> None: ...

    @overload
    def SetMatrix(self, elements: Sequence[float]) -> None: ...

    @overload
    def SetupCamera(
        self, position: Sequence[float], focalpoint: Sequence[float], viewup: Sequence[float]) -> None: ...

    @overload
    def SetupCamera(
        self, p0: float, p1: float, p2: float, fp0: float, fp1: float, fp2: float, vup0: float, vup1: float, vup2: float
    ) -> None: ...
    def Shear(self, dxdz: float, dydz: float, zplane: float) -> None: ...
    def Stereo(self, angle: float, focaldistance: float) -> None: ...
    @overload
    def Translate(self, x: float, y: float, z: float) -> None: ...
    @overload
    def Translate(self, x: Sequence[float]) -> None: ...


class vtkSphericalTransform(vtkWarpTransform):
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def MakeTransform(self) -> vtkAbstractTransform: ...
    def NewInstance(self) -> vtkSphericalTransform: ...

    @staticmethod
    def SafeDownCast(
        o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkSphericalTransform: ...


class vtkThinPlateSplineTransform(vtkWarpTransform):
    def GetBasis(self) -> int: ...
    def GetBasisAsString(self) -> str: ...
    def GetMTime(self) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetRegularizeBulkTransform(self) -> bool: ...
    def GetSigma(self) -> float: ...
    def GetSourceLandmarks(self) -> vtkmodules.vtkCommonCore.vtkPoints: ...
    def GetTargetLandmarks(self) -> vtkmodules.vtkCommonCore.vtkPoints: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def MakeTransform(self) -> vtkAbstractTransform: ...
    def NewInstance(self) -> vtkThinPlateSplineTransform: ...
    def RegularizeBulkTransformOff(self) -> None: ...
    def RegularizeBulkTransformOn(self) -> None: ...

    @staticmethod
    def SafeDownCast(
        o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkThinPlateSplineTransform: ...

    def SetBasis(self, basis: int) -> None: ...
    def SetBasisToR(self) -> None: ...
    def SetBasisToR2LogR(self) -> None: ...
    def SetRegularizeBulkTransform(self, _arg: bool) -> None: ...
    def SetSigma(self, _arg: float) -> None: ...

    def SetSourceLandmarks(
        self, source: vtkmodules.vtkCommonCore.vtkPoints) -> None: ...
    def SetTargetLandmarks(
        self, target: vtkmodules.vtkCommonCore.vtkPoints) -> None: ...


class vtkTransform(vtkLinearTransform):
    def CircuitCheck(self, transform: vtkAbstractTransform) -> int: ...

    @overload
    def Concatenate(
        self, matrix: vtkmodules.vtkCommonMath.vtkMatrix4x4) -> None: ...

    @overload
    def Concatenate(self, elements: Sequence[float]) -> None: ...
    @overload
    def Concatenate(self, transform: vtkLinearTransform) -> None: ...
    def GetConcatenatedTransform(self, i: int) -> vtkLinearTransform: ...
    def GetInput(self) -> vtkLinearTransform: ...

    @overload
    def GetInverse(
        self, inverse: vtkmodules.vtkCommonMath.vtkMatrix4x4) -> None: ...

    @overload
    def GetInverse(self) -> vtkAbstractTransform: ...
    def GetInverseFlag(self) -> int: ...
    def GetMTime(self) -> int: ...
    def GetNumberOfConcatenatedTransforms(self) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    @overload
    def GetOrientation(self, orient: MutableSequence[float]) -> None: ...
    @overload
    def GetOrientation(self) -> Tuple[float, float, float]: ...

    @overload
    @staticmethod
    def GetOrientation(
        orient: MutableSequence[float], matrix: vtkmodules.vtkCommonMath.vtkMatrix4x4) -> None: ...

    @overload
    def GetOrientationWXYZ(self, wxyz: MutableSequence[float]) -> None: ...
    @overload
    def GetOrientationWXYZ(self) -> Tuple[float, float, float, float]: ...
    @overload
    def GetPosition(self, pos: MutableSequence[float]) -> None: ...
    @overload
    def GetPosition(self) -> Tuple[float, float, float]: ...
    @overload
    def GetScale(self, scale: MutableSequence[float]) -> None: ...
    @overload
    def GetScale(self) -> Tuple[float, float, float]: ...
    def GetTranspose(
        self, transpose: vtkmodules.vtkCommonMath.vtkMatrix4x4) -> None: ...

    def Identity(self) -> None: ...
    def Inverse(self) -> None: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def MakeTransform(self) -> vtkAbstractTransform: ...
    def MultiplyPoint(
        self, in_: Sequence[float], out: MutableSequence[float]) -> None: ...

    def NewInstance(self) -> vtkTransform: ...
    def Pop(self) -> None: ...
    def PostMultiply(self) -> None: ...
    def PreMultiply(self) -> None: ...
    def Push(self) -> None: ...

    @overload
    def RotateWXYZ(self, angle: float, x: float,
                   y: float, z: float) -> None: ...

    @overload
    def RotateWXYZ(self, angle: float, axis: Sequence[float]) -> None: ...
    def RotateX(self, angle: float) -> None: ...
    def RotateY(self, angle: float) -> None: ...
    def RotateZ(self, angle: float) -> None: ...

    @staticmethod
    def SafeDownCast(
        o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkTransform: ...

    @overload
    def Scale(self, x: float, y: float, z: float) -> None: ...
    @overload
    def Scale(self, s: Sequence[float]) -> None: ...
    def SetInput(self, input: vtkLinearTransform) -> None: ...

    @overload
    def SetMatrix(
        self, matrix: vtkmodules.vtkCommonMath.vtkMatrix4x4) -> None: ...

    @overload
    def SetMatrix(self, elements: Sequence[float]) -> None: ...
    @overload
    def Translate(self, x: float, y: float, z: float) -> None: ...
    @overload
    def Translate(self, x: Sequence[float]) -> None: ...


class vtkTransform2D(vtkmodules.vtkCommonCore.vtkObject):
    def GetInverse(
        self, inverse: vtkmodules.vtkCommonMath.vtkMatrix3x3) -> None: ...

    def GetMTime(self) -> int: ...
    @overload
    def GetMatrix(self) -> vtkmodules.vtkCommonMath.vtkMatrix3x3: ...

    @overload
    def GetMatrix(
        self, matrix: vtkmodules.vtkCommonMath.vtkMatrix3x3) -> None: ...

    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetPosition(self, pos: MutableSequence[float]) -> None: ...
    def GetScale(self, scale: MutableSequence[float]) -> None: ...
    def GetTranspose(
        self, transpose: vtkmodules.vtkCommonMath.vtkMatrix3x3) -> None: ...

    def Identity(self) -> None: ...
    def Inverse(self) -> None: ...

    @overload
    def InverseTransformPoints(
        self, inPts: Sequence[float], outPts: MutableSequence[float], n: int) -> None: ...

    @overload
    def InverseTransformPoints(
        self, inPts: vtkmodules.vtkCommonCore.vtkPoints2D, outPts: vtkmodules.vtkCommonCore.vtkPoints2D
    ) -> None: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def MultiplyPoint(
        self, in_: Sequence[float], out: MutableSequence[float]) -> None: ...

    def NewInstance(self) -> vtkTransform2D: ...
    def Rotate(self, angle: float) -> None: ...

    @staticmethod
    def SafeDownCast(
        o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkTransform2D: ...

    @overload
    def Scale(self, x: float, y: float) -> None: ...
    @overload
    def Scale(self, s: Sequence[float]) -> None: ...

    @overload
    def SetMatrix(
        self, matrix: vtkmodules.vtkCommonMath.vtkMatrix3x3) -> None: ...

    @overload
    def SetMatrix(self, elements: Sequence[float]) -> None: ...

    @overload
    def TransformPoints(
        self, inPts: Sequence[float], outPts: MutableSequence[float], n: int) -> None: ...

    @overload
    def TransformPoints(
        self, inPts: vtkmodules.vtkCommonCore.vtkPoints2D, outPts: vtkmodules.vtkCommonCore.vtkPoints2D
    ) -> None: ...
    @overload
    def Translate(self, x: float, y: float) -> None: ...
    @overload
    def Translate(self, x: Sequence[float]) -> None: ...


class vtkTransformCollection(vtkmodules.vtkCommonCore.vtkCollection):
    def AddItem(self, __a: vtkTransform) -> None: ...
    def GetNextItem(self) -> vtkTransform: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkTransformCollection: ...

    @staticmethod
    def SafeDownCast(
        o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkTransformCollection: ...


class vtkTransformConcatenation:
    @overload
    def Concatenate(self, transform: vtkAbstractTransform) -> None: ...
    @overload
    def Concatenate(self, elements: Sequence[float]) -> None: ...
    def GetInverseFlag(self) -> int: ...
    def GetMaxMTime(self) -> int: ...
    def GetNumberOfPostTransforms(self) -> int: ...
    def GetNumberOfPreTransforms(self) -> int: ...
    def GetNumberOfTransforms(self) -> int: ...
    def GetPreMultiplyFlag(self) -> int: ...
    def GetTransform(self, i: int) -> vtkAbstractTransform: ...
    def Identity(self) -> None: ...
    def Inverse(self) -> None: ...
    def Rotate(self, angle: float, x: float, y: float, z: float) -> None: ...
    def Scale(self, x: float, y: float, z: float) -> None: ...
    def SetPreMultiplyFlag(self, flag: int) -> None: ...
    def Translate(self, x: float, y: float, z: float) -> None: ...


class vtkTransformConcatenationStack:
    ...


class vtkTransformPair:
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, __a: vtkTransformPair) -> None: ...
    def SwapForwardInverse(self) -> None: ...
