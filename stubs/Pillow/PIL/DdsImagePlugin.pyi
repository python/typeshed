from typing import ClassVar, Final, Literal

from .ImageFile import ImageFile

DDS_MAGIC: Final = 0x20534444

DDSD_CAPS: Final = 0x1
DDSD_HEIGHT: Final = 0x2
DDSD_WIDTH: Final = 0x4
DDSD_PITCH: Final = 0x8
DDSD_PIXELFORMAT: Final = 0x1000
DDSD_MIPMAPCOUNT: Final = 0x20000
DDSD_LINEARSIZE: Final = 0x80000
DDSD_DEPTH: Final = 0x800000

DDSCAPS_COMPLEX: Final = 0x8
DDSCAPS_TEXTURE: Final = 0x1000
DDSCAPS_MIPMAP: Final = 0x400000

DDSCAPS2_CUBEMAP: Final = 0x200
DDSCAPS2_CUBEMAP_POSITIVEX: Final = 0x400
DDSCAPS2_CUBEMAP_NEGATIVEX: Final = 0x800
DDSCAPS2_CUBEMAP_POSITIVEY: Final = 0x1000
DDSCAPS2_CUBEMAP_NEGATIVEY: Final = 0x2000
DDSCAPS2_CUBEMAP_POSITIVEZ: Final = 0x4000
DDSCAPS2_CUBEMAP_NEGATIVEZ: Final = 0x8000
DDSCAPS2_VOLUME: Final = 0x200000

DDPF_ALPHAPIXELS: Final = 0x1
DDPF_ALPHA: Final = 0x2
DDPF_FOURCC: Final = 0x4
DDPF_PALETTEINDEXED8: Final = 0x20
DDPF_RGB: Final = 0x40
DDPF_LUMINANCE: Final = 0x20000

DDS_FOURCC: Final = 0x4
DDS_RGB: Final = 0x40
DDS_RGBA: Final = 0x41
DDS_LUMINANCE: Final = 0x20000
DDS_LUMINANCEA: Final = 0x20001
DDS_ALPHA: Final = 0x2
DDS_PAL8: Final = 0x20

DDS_HEADER_FLAGS_TEXTURE: int
DDS_HEADER_FLAGS_MIPMAP: int
DDS_HEADER_FLAGS_VOLUME: int
DDS_HEADER_FLAGS_PITCH: int
DDS_HEADER_FLAGS_LINEARSIZE: int
DDS_HEIGHT: int
DDS_WIDTH: int
DDS_SURFACE_FLAGS_TEXTURE: int
DDS_SURFACE_FLAGS_MIPMAP: int
DDS_SURFACE_FLAGS_CUBEMAP: int
DDS_CUBEMAP_POSITIVEX: int
DDS_CUBEMAP_NEGATIVEX: int
DDS_CUBEMAP_POSITIVEY: int
DDS_CUBEMAP_NEGATIVEY: int
DDS_CUBEMAP_POSITIVEZ: int
DDS_CUBEMAP_NEGATIVEZ: int

DXT1_FOURCC: Final = 0x31545844
DXT3_FOURCC: Final = 0x33545844
DXT5_FOURCC: Final = 0x35545844

DXGI_FORMAT_R8G8B8A8_TYPELESS: Final = 27
DXGI_FORMAT_R8G8B8A8_UNORM: Final = 28
DXGI_FORMAT_R8G8B8A8_UNORM_SRGB: Final = 29
DXGI_FORMAT_BC5_TYPELESS: Final = 82
DXGI_FORMAT_BC5_UNORM: Final = 83
DXGI_FORMAT_BC5_SNORM: Final = 84
DXGI_FORMAT_BC6H_UF16: Final = 95
DXGI_FORMAT_BC6H_SF16: Final = 96
DXGI_FORMAT_BC7_TYPELESS: Final = 97
DXGI_FORMAT_BC7_UNORM: Final = 98
DXGI_FORMAT_BC7_UNORM_SRGB: Final = 99

class DdsImageFile(ImageFile):
    format: ClassVar[Literal["DDS"]]
    format_description: ClassVar[str]
    def load_seek(self, pos) -> None: ...
