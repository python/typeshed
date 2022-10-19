from cv2.cv2 import _Boolean, ocl_Device

DEVICE_EXEC_KERNEL: int
DEVICE_EXEC_NATIVE_KERNEL: int
DEVICE_FP_CORRECTLY_ROUNDED_DIVIDE_SQRT: int
DEVICE_FP_DENORM: int
DEVICE_FP_FMA: int
DEVICE_FP_INF_NAN: int
DEVICE_FP_ROUND_TO_INF: int
DEVICE_FP_ROUND_TO_NEAREST: int
DEVICE_FP_ROUND_TO_ZERO: int
DEVICE_FP_SOFT_FLOAT: int
DEVICE_LOCAL_IS_GLOBAL: int
DEVICE_LOCAL_IS_LOCAL: int
DEVICE_NO_CACHE: int
DEVICE_NO_LOCAL_MEM: int
DEVICE_READ_ONLY_CACHE: int
DEVICE_READ_WRITE_CACHE: int
DEVICE_TYPE_ACCELERATOR: int
DEVICE_TYPE_ALL: int
DEVICE_TYPE_CPU: int
DEVICE_TYPE_DEFAULT: int
DEVICE_TYPE_DGPU: int
DEVICE_TYPE_GPU: int
DEVICE_TYPE_IGPU: int
DEVICE_UNKNOWN_VENDOR: int
DEVICE_VENDOR_AMD: int
DEVICE_VENDOR_INTEL: int
DEVICE_VENDOR_NVIDIA: int
Device_EXEC_KERNEL: int
Device_EXEC_NATIVE_KERNEL: int
Device_FP_CORRECTLY_ROUNDED_DIVIDE_SQRT: int
Device_FP_DENORM: int
Device_FP_FMA: int
Device_FP_INF_NAN: int
Device_FP_ROUND_TO_INF: int
Device_FP_ROUND_TO_NEAREST: int
Device_FP_ROUND_TO_ZERO: int
Device_FP_SOFT_FLOAT: int
Device_LOCAL_IS_GLOBAL: int
Device_LOCAL_IS_LOCAL: int
Device_NO_CACHE: int
Device_NO_LOCAL_MEM: int
Device_READ_ONLY_CACHE: int
Device_READ_WRITE_CACHE: int
Device_TYPE_ACCELERATOR: int
Device_TYPE_ALL: int
Device_TYPE_CPU: int
Device_TYPE_DEFAULT: int
Device_TYPE_DGPU: int
Device_TYPE_GPU: int
Device_TYPE_IGPU: int
Device_UNKNOWN_VENDOR: int
Device_VENDOR_AMD: int
Device_VENDOR_INTEL: int
Device_VENDOR_NVIDIA: int
KERNEL_ARG_CONSTANT: int
KERNEL_ARG_LOCAL: int
KERNEL_ARG_NO_SIZE: int
KERNEL_ARG_PTR_ONLY: int
KERNEL_ARG_READ_ONLY: int
KERNEL_ARG_READ_WRITE: int
KERNEL_ARG_WRITE_ONLY: int
KernelArg_CONSTANT: int
KernelArg_LOCAL: int
KernelArg_NO_SIZE: int
KernelArg_PTR_ONLY: int
KernelArg_READ_ONLY: int
KernelArg_READ_WRITE: int
KernelArg_WRITE_ONLY: int
OCL_VECTOR_DEFAULT: int
OCL_VECTOR_MAX: int
OCL_VECTOR_OWN: int

def Device_getDefault() -> ocl_Device: ...
def finish() -> None: ...
def haveAmdBlas() -> bool: ...
def haveAmdFft() -> bool: ...
def haveOpenCL() -> bool: ...
def setUseOpenCL(flag: _Boolean) -> None: ...
def useOpenCL() -> bool: ...
