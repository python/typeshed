from _typeshed import Incomplete
from ctypes import HRESULT, _CArgObject, Structure, c_int32, c_uint, c_void_p, wintypes
from typing_extensions import TypeAlias
from collections.abc import Callable

from d3dshot.dll.dxgi import IDXGIAdapter

# TODO: Complete types once we can import non-types dependencies
# See: https://github.com/python/typeshed/issues/5768
# import comtypes
_IUnknown: TypeAlias = Incomplete

class DXGI_SAMPLE_DESC(Structure):
    Count: wintypes.UINT
    Quality: wintypes.UINT

class D3D11_BOX(Structure):
    left: wintypes.UINT
    top: wintypes.UINT
    front: wintypes.UINT
    right: wintypes.UINT
    bottom: wintypes.UINT
    back: wintypes.UINT

class D3D11_TEXTURE2D_DESC(Structure):
    Width: wintypes.UINT
    Height: wintypes.UINT
    MipLevels: wintypes.UINT
    ArraySize: wintypes.UINT
    Format: wintypes.UINT
    SampleDesc: DXGI_SAMPLE_DESC
    Usage: wintypes.UINT
    BindFlags: wintypes.UINT
    CPUAccessFlags: wintypes.UINT
    MiscFlags: wintypes.UINT

class ID3D11DeviceChild(_IUnknown):
    GetDevice: Callable[[], None]
    GetPrivateData: Callable[[], HRESULT]
    SetPrivateData: Callable[[], HRESULT]
    SetPrivateDataInterface: Callable[[], HRESULT]

class ID3D11Resource(ID3D11DeviceChild):
    GetType: Callable[[], None]
    SetEvictionPriority: Callable[[], None]
    GetEvictionPriority: Callable[[], wintypes.UINT]

class ID3D11Texture2D(ID3D11Resource):
    GetDesc: Callable[[D3D11_TEXTURE2D_DESC], None]

class ID3D11DeviceContext(ID3D11DeviceChild):
    VSSetConstantBuffers: Callable[[], None]
    PSSetShaderResources: Callable[[], None]
    PSSetShader: Callable[[], None]
    PSSetSamplers: Callable[[], None]
    VSSetShader: Callable[[], None]
    DrawIndexed: Callable[[], None]
    Draw: Callable[[], None]
    Map: Callable[[], HRESULT]
    Unmap: Callable[[], None]
    PSSetConstantBuffers: Callable[[], None]
    IASetInputLayout: Callable[[], None]
    IASetVertexBuffers: Callable[[], None]
    IASetIndexBuffer: Callable[[], None]
    DrawIndexedInstanced: Callable[[], None]
    DrawInstanced: Callable[[], None]
    GSSetConstantBuffers: Callable[[], None]
    GSSetShader: Callable[[], None]
    IASetPrimitiveTopology: Callable[[], None]
    VSSetShaderResources: Callable[[], None]
    VSSetSamplers: Callable[[], None]
    Begin: Callable[[], None]
    End: Callable[[], None]
    GetData: Callable[[], HRESULT]
    SetPredication: Callable[[], None]
    GSSetShaderResources: Callable[[], None]
    GSSetSamplers: Callable[[], None]
    OMSetRenderTargets: Callable[[], None]
    OMSetRenderTargetsAndUnorderedAccessViews: Callable[[], None]
    OMSetBlendState: Callable[[], None]
    OMSetDepthStencilState: Callable[[], None]
    SOSetTargets: Callable[[], None]
    DrawAuto: Callable[[], None]
    DrawIndexedInstancedIndirect: Callable[[], None]
    DrawInstancedIndirect: Callable[[], None]
    Dispatch: Callable[[], None]
    DispatchIndirect: Callable[[], None]
    RSSetState: Callable[[], None]
    RSSetViewports: Callable[[], None]
    RSSetScissorRects: Callable[[], None]
    CopySubresourceRegion: Callable[
        [ID3D11Resource, wintypes.UINT, wintypes.UINT, wintypes.UINT, wintypes.UINT, ID3D11Resource, wintypes.UINT, D3D11_BOX],
        None,
    ]
    CopyResource: Callable[[ID3D11Resource, ID3D11Resource], None]
    UpdateSubresource: Callable[[], None]
    CopyStructureCount: Callable[[], None]
    ClearRenderTargetView: Callable[[], None]
    ClearUnorderedAccessViewUint: Callable[[], None]
    ClearUnorderedAccessViewFloat: Callable[[], None]
    ClearDepthStencilView: Callable[[], None]
    GenerateMips: Callable[[], None]
    SetResourceMinLOD: Callable[[], None]
    GetResourceMinLOD: Callable[[], wintypes.FLOAT]
    ResolveSubresource: Callable[[], None]
    ExecuteCommandList: Callable[[], None]
    HSSetShaderResources: Callable[[], None]
    HSSetShader: Callable[[], None]
    HSSetSamplers: Callable[[], None]
    HSSetConstantBuffers: Callable[[], None]
    DSSetShaderResources: Callable[[], None]
    DSSetShader: Callable[[], None]
    DSSetSamplers: Callable[[], None]
    DSSetConstantBuffers: Callable[[], None]
    CSSetShaderResources: Callable[[], None]
    CSSetUnorderedAccessViews: Callable[[], None]
    CSSetShader: Callable[[], None]
    CSSetSamplers: Callable[[], None]
    CSSetConstantBuffers: Callable[[], None]
    VSGetConstantBuffers: Callable[[], None]
    PSGetShaderResources: Callable[[], None]
    PSGetShader: Callable[[], None]
    PSGetSamplers: Callable[[], None]
    VSGetShader: Callable[[], None]
    PSGetConstantBuffers: Callable[[], None]
    IAGetInputLayout: Callable[[], None]
    IAGetVertexBuffers: Callable[[], None]
    IAGetIndexBuffer: Callable[[], None]
    GSGetConstantBuffers: Callable[[], None]
    GSGetShader: Callable[[], None]
    IAGetPrimitiveTopology: Callable[[], None]
    VSGetShaderResources: Callable[[], None]
    VSGetSamplers: Callable[[], None]
    GetPredication: Callable[[], None]
    GSGetShaderResources: Callable[[], None]
    GSGetSamplers: Callable[[], None]
    OMGetRenderTargets: Callable[[], None]
    OMGetRenderTargetsAndUnorderedAccessViews: Callable[[], None]
    OMGetBlendState: Callable[[], None]
    OMGetDepthStencilState: Callable[[], None]
    SOGetTargets: Callable[[], None]
    RSGetState: Callable[[], None]
    RSGetViewports: Callable[[], None]
    RSGetScissorRects: Callable[[], None]
    HSGetShaderResources: Callable[[], None]
    HSGetShader: Callable[[], None]
    HSGetSamplers: Callable[[], None]
    HSGetConstantBuffers: Callable[[], None]
    DSGetShaderResources: Callable[[], None]
    DSGetShader: Callable[[], None]
    DSGetSamplers: Callable[[], None]
    DSGetConstantBuffers: Callable[[], None]
    CSGetShaderResources: Callable[[], None]
    CSGetUnorderedAccessViews: Callable[[], None]
    CSGetShader: Callable[[], None]
    CSGetSamplers: Callable[[], None]
    CSGetConstantBuffers: Callable[[], None]
    ClearState: Callable[[], None]
    Flush: Callable[[], None]
    GetType: Callable[[], None]
    GetContextFlags: Callable[[], wintypes.UINT]
    FinishCommandList: Callable[[], HRESULT]

class ID3D11Device(_IUnknown):
    CreateBuffer: Callable[[], HRESULT]
    CreateTexture1D: Callable[[], HRESULT]
    CreateTexture2D: Callable[[D3D11_TEXTURE2D_DESC, c_void_p, _CArgObject], HRESULT]
    CreateTexture3D: Callable[[], HRESULT]
    CreateShaderResourceView: Callable[[], HRESULT]
    CreateUnorderedAccessView: Callable[[], HRESULT]
    CreateRenderTargetView: Callable[[], HRESULT]
    CreateDepthStencilView: Callable[[], HRESULT]
    CreateInputLayout: Callable[[], HRESULT]
    CreateVertexShader: Callable[[], HRESULT]
    CreateGeometryShader: Callable[[], HRESULT]
    CreateGeometryShaderWithStreamOutput: Callable[[], HRESULT]
    CreatePixelShader: Callable[[], HRESULT]
    CreateHullShader: Callable[[], HRESULT]
    CreateDomainShader: Callable[[], HRESULT]
    CreateComputeShader: Callable[[], HRESULT]
    CreateClassLinkage: Callable[[], HRESULT]
    CreateBlendState: Callable[[], HRESULT]
    CreateDepthStencilState: Callable[[], HRESULT]
    CreateRasterizerState: Callable[[], HRESULT]
    CreateSamplerState: Callable[[], HRESULT]
    CreateQuery: Callable[[], HRESULT]
    CreatePredicate: Callable[[], HRESULT]
    CreateCounter: Callable[[], HRESULT]
    CreateDeferredContext: Callable[[], HRESULT]
    OpenSharedResource: Callable[[], HRESULT]
    CheckFormatSupport: Callable[[], HRESULT]
    CheckMultisampleQualityLevels: Callable[[], HRESULT]
    CheckCounterInfo: Callable[[], HRESULT]
    CheckCounter: Callable[[], HRESULT]
    CheckFeatureSupport: Callable[[], HRESULT]
    GetPrivateData: Callable[[], HRESULT]
    SetPrivateData: Callable[[], HRESULT]
    SetPrivateDataInterface: Callable[[], HRESULT]
    GetFeatureLevel: Callable[[], c_int32]
    GetCreationFlags: Callable[[], c_uint]
    GetDeviceRemovedReason: Callable[[], HRESULT]
    GetImmediateContext: Callable[[_CArgObject], None]
    SetExceptionMode: Callable[[], HRESULT]
    GetExceptionMode: Callable[[], c_uint]

def initialize_d3d_device(dxgi_adapter: IDXGIAdapter) -> tuple[ID3D11Device, ID3D11DeviceContext]: ...
def describe_d3d11_texture_2d(d3d11_texture_2d: ID3D11Texture2D) -> D3D11_TEXTURE2D_DESC: ...
def prepare_d3d11_texture_2d_for_cpu(d3d11_texture_2d: ID3D11Texture2D, d3d_device: ID3D11Device) -> ID3D11Texture2D: ...
