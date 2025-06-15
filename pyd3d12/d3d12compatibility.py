# -*- coding: mbcs -*-

from ctypes import *
import OLE
from comtypes import COMMETHOD, GUID, IUnknown
from ctypes import HRESULT
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from comtypes import hints


_lcid = 0  # change this if required
typelib_path = None
WSTRING = c_wchar_p

# values for enumeration 'D3D12_RESOURCE_DIMENSION'
D3D12_RESOURCE_DIMENSION_UNKNOWN = 0
D3D12_RESOURCE_DIMENSION_BUFFER = 1
D3D12_RESOURCE_DIMENSION_TEXTURE1D = 2
D3D12_RESOURCE_DIMENSION_TEXTURE2D = 3
D3D12_RESOURCE_DIMENSION_TEXTURE3D = 4
D3D12_RESOURCE_DIMENSION = c_int  # enum

# values for enumeration 'DXGI_FORMAT'
DXGI_FORMAT_UNKNOWN = 0
DXGI_FORMAT_R32G32B32A32_TYPELESS = 1
DXGI_FORMAT_R32G32B32A32_FLOAT = 2
DXGI_FORMAT_R32G32B32A32_UINT = 3
DXGI_FORMAT_R32G32B32A32_SINT = 4
DXGI_FORMAT_R32G32B32_TYPELESS = 5
DXGI_FORMAT_R32G32B32_FLOAT = 6
DXGI_FORMAT_R32G32B32_UINT = 7
DXGI_FORMAT_R32G32B32_SINT = 8
DXGI_FORMAT_R16G16B16A16_TYPELESS = 9
DXGI_FORMAT_R16G16B16A16_FLOAT = 10
DXGI_FORMAT_R16G16B16A16_UNORM = 11
DXGI_FORMAT_R16G16B16A16_UINT = 12
DXGI_FORMAT_R16G16B16A16_SNORM = 13
DXGI_FORMAT_R16G16B16A16_SINT = 14
DXGI_FORMAT_R32G32_TYPELESS = 15
DXGI_FORMAT_R32G32_FLOAT = 16
DXGI_FORMAT_R32G32_UINT = 17
DXGI_FORMAT_R32G32_SINT = 18
DXGI_FORMAT_R32G8X24_TYPELESS = 19
DXGI_FORMAT_D32_FLOAT_S8X24_UINT = 20
DXGI_FORMAT_R32_FLOAT_X8X24_TYPELESS = 21
DXGI_FORMAT_X32_TYPELESS_G8X24_UINT = 22
DXGI_FORMAT_R10G10B10A2_TYPELESS = 23
DXGI_FORMAT_R10G10B10A2_UNORM = 24
DXGI_FORMAT_R10G10B10A2_UINT = 25
DXGI_FORMAT_R11G11B10_FLOAT = 26
DXGI_FORMAT_R8G8B8A8_TYPELESS = 27
DXGI_FORMAT_R8G8B8A8_UNORM = 28
DXGI_FORMAT_R8G8B8A8_UNORM_SRGB = 29
DXGI_FORMAT_R8G8B8A8_UINT = 30
DXGI_FORMAT_R8G8B8A8_SNORM = 31
DXGI_FORMAT_R8G8B8A8_SINT = 32
DXGI_FORMAT_R16G16_TYPELESS = 33
DXGI_FORMAT_R16G16_FLOAT = 34
DXGI_FORMAT_R16G16_UNORM = 35
DXGI_FORMAT_R16G16_UINT = 36
DXGI_FORMAT_R16G16_SNORM = 37
DXGI_FORMAT_R16G16_SINT = 38
DXGI_FORMAT_R32_TYPELESS = 39
DXGI_FORMAT_D32_FLOAT = 40
DXGI_FORMAT_R32_FLOAT = 41
DXGI_FORMAT_R32_UINT = 42
DXGI_FORMAT_R32_SINT = 43
DXGI_FORMAT_R24G8_TYPELESS = 44
DXGI_FORMAT_D24_UNORM_S8_UINT = 45
DXGI_FORMAT_R24_UNORM_X8_TYPELESS = 46
DXGI_FORMAT_X24_TYPELESS_G8_UINT = 47
DXGI_FORMAT_R8G8_TYPELESS = 48
DXGI_FORMAT_R8G8_UNORM = 49
DXGI_FORMAT_R8G8_UINT = 50
DXGI_FORMAT_R8G8_SNORM = 51
DXGI_FORMAT_R8G8_SINT = 52
DXGI_FORMAT_R16_TYPELESS = 53
DXGI_FORMAT_R16_FLOAT = 54
DXGI_FORMAT_D16_UNORM = 55
DXGI_FORMAT_R16_UNORM = 56
DXGI_FORMAT_R16_UINT = 57
DXGI_FORMAT_R16_SNORM = 58
DXGI_FORMAT_R16_SINT = 59
DXGI_FORMAT_R8_TYPELESS = 60
DXGI_FORMAT_R8_UNORM = 61
DXGI_FORMAT_R8_UINT = 62
DXGI_FORMAT_R8_SNORM = 63
DXGI_FORMAT_R8_SINT = 64
DXGI_FORMAT_A8_UNORM = 65
DXGI_FORMAT_R1_UNORM = 66
DXGI_FORMAT_R9G9B9E5_SHAREDEXP = 67
DXGI_FORMAT_R8G8_B8G8_UNORM = 68
DXGI_FORMAT_G8R8_G8B8_UNORM = 69
DXGI_FORMAT_BC1_TYPELESS = 70
DXGI_FORMAT_BC1_UNORM = 71
DXGI_FORMAT_BC1_UNORM_SRGB = 72
DXGI_FORMAT_BC2_TYPELESS = 73
DXGI_FORMAT_BC2_UNORM = 74
DXGI_FORMAT_BC2_UNORM_SRGB = 75
DXGI_FORMAT_BC3_TYPELESS = 76
DXGI_FORMAT_BC3_UNORM = 77
DXGI_FORMAT_BC3_UNORM_SRGB = 78
DXGI_FORMAT_BC4_TYPELESS = 79
DXGI_FORMAT_BC4_UNORM = 80
DXGI_FORMAT_BC4_SNORM = 81
DXGI_FORMAT_BC5_TYPELESS = 82
DXGI_FORMAT_BC5_UNORM = 83
DXGI_FORMAT_BC5_SNORM = 84
DXGI_FORMAT_B5G6R5_UNORM = 85
DXGI_FORMAT_B5G5R5A1_UNORM = 86
DXGI_FORMAT_B8G8R8A8_UNORM = 87
DXGI_FORMAT_B8G8R8X8_UNORM = 88
DXGI_FORMAT_R10G10B10_XR_BIAS_A2_UNORM = 89
DXGI_FORMAT_B8G8R8A8_TYPELESS = 90
DXGI_FORMAT_B8G8R8A8_UNORM_SRGB = 91
DXGI_FORMAT_B8G8R8X8_TYPELESS = 92
DXGI_FORMAT_B8G8R8X8_UNORM_SRGB = 93
DXGI_FORMAT_BC6H_TYPELESS = 94
DXGI_FORMAT_BC6H_UF16 = 95
DXGI_FORMAT_BC6H_SF16 = 96
DXGI_FORMAT_BC7_TYPELESS = 97
DXGI_FORMAT_BC7_UNORM = 98
DXGI_FORMAT_BC7_UNORM_SRGB = 99
DXGI_FORMAT_AYUV = 100
DXGI_FORMAT_Y410 = 101
DXGI_FORMAT_Y416 = 102
DXGI_FORMAT_NV12 = 103
DXGI_FORMAT_P010 = 104
DXGI_FORMAT_P016 = 105
DXGI_FORMAT_420_OPAQUE = 106
DXGI_FORMAT_YUY2 = 107
DXGI_FORMAT_Y210 = 108
DXGI_FORMAT_Y216 = 109
DXGI_FORMAT_NV11 = 110
DXGI_FORMAT_AI44 = 111
DXGI_FORMAT_IA44 = 112
DXGI_FORMAT_P8 = 113
DXGI_FORMAT_A8P8 = 114
DXGI_FORMAT_B4G4R4A4_UNORM = 115
DXGI_FORMAT_P208 = 130
DXGI_FORMAT_V208 = 131
DXGI_FORMAT_V408 = 132
DXGI_FORMAT_SAMPLER_FEEDBACK_MIN_MIP_OPAQUE = 189
DXGI_FORMAT_SAMPLER_FEEDBACK_MIP_REGION_USED_OPAQUE = 190
DXGI_FORMAT_FORCE_UINT = -1
DXGI_FORMAT = c_int  # enum

# values for enumeration 'D3D12_TEXTURE_LAYOUT'
D3D12_TEXTURE_LAYOUT_UNKNOWN = 0
D3D12_TEXTURE_LAYOUT_ROW_MAJOR = 1
D3D12_TEXTURE_LAYOUT_64KB_UNDEFINED_SWIZZLE = 2
D3D12_TEXTURE_LAYOUT_64KB_STANDARD_SWIZZLE = 3
D3D12_TEXTURE_LAYOUT = c_int  # enum

# values for enumeration 'D3D12_RESOURCE_FLAGS'
D3D12_RESOURCE_FLAG_NONE = 0
D3D12_RESOURCE_FLAG_ALLOW_RENDER_TARGET = 1
D3D12_RESOURCE_FLAG_ALLOW_DEPTH_STENCIL = 2
D3D12_RESOURCE_FLAG_ALLOW_UNORDERED_ACCESS = 4
D3D12_RESOURCE_FLAG_DENY_SHADER_RESOURCE = 8
D3D12_RESOURCE_FLAG_ALLOW_CROSS_ADAPTER = 16
D3D12_RESOURCE_FLAG_ALLOW_SIMULTANEOUS_ACCESS = 32
D3D12_RESOURCE_FLAG_VIDEO_DECODE_REFERENCE_ONLY = 64
D3D12_RESOURCE_FLAG_VIDEO_ENCODE_REFERENCE_ONLY = 128
D3D12_RESOURCE_FLAG_RAYTRACING_ACCELERATION_STRUCTURE = 256
D3D12_RESOURCE_FLAGS = c_int  # enum

# values for enumeration 'D3D12_RESOURCE_STATES'
D3D12_RESOURCE_STATE_COMMON = 0
D3D12_RESOURCE_STATE_VERTEX_AND_CONSTANT_BUFFER = 1
D3D12_RESOURCE_STATE_INDEX_BUFFER = 2
D3D12_RESOURCE_STATE_RENDER_TARGET = 4
D3D12_RESOURCE_STATE_UNORDERED_ACCESS = 8
D3D12_RESOURCE_STATE_DEPTH_WRITE = 16
D3D12_RESOURCE_STATE_DEPTH_READ = 32
D3D12_RESOURCE_STATE_NON_PIXEL_SHADER_RESOURCE = 64
D3D12_RESOURCE_STATE_PIXEL_SHADER_RESOURCE = 128
D3D12_RESOURCE_STATE_STREAM_OUT = 256
D3D12_RESOURCE_STATE_INDIRECT_ARGUMENT = 512
D3D12_RESOURCE_STATE_COPY_DEST = 1024
D3D12_RESOURCE_STATE_COPY_SOURCE = 2048
D3D12_RESOURCE_STATE_RESOLVE_DEST = 4096
D3D12_RESOURCE_STATE_RESOLVE_SOURCE = 8192
D3D12_RESOURCE_STATE_RAYTRACING_ACCELERATION_STRUCTURE = 4194304
D3D12_RESOURCE_STATE_SHADING_RATE_SOURCE = 16777216
D3D12_RESOURCE_STATE_GENERIC_READ = 2755
D3D12_RESOURCE_STATE_ALL_SHADER_RESOURCE = 192
D3D12_RESOURCE_STATE_PRESENT = 0
D3D12_RESOURCE_STATE_PREDICATION = 512
D3D12_RESOURCE_STATE_VIDEO_DECODE_READ = 65536
D3D12_RESOURCE_STATE_VIDEO_DECODE_WRITE = 131072
D3D12_RESOURCE_STATE_VIDEO_PROCESS_READ = 262144
D3D12_RESOURCE_STATE_VIDEO_PROCESS_WRITE = 524288
D3D12_RESOURCE_STATE_VIDEO_ENCODE_READ = 2097152
D3D12_RESOURCE_STATE_VIDEO_ENCODE_WRITE = 8388608
D3D12_RESOURCE_STATES = c_int  # enum

# values for enumeration 'D3D12_CPU_PAGE_PROPERTY'
D3D12_CPU_PAGE_PROPERTY_UNKNOWN = 0
D3D12_CPU_PAGE_PROPERTY_NOT_AVAILABLE = 1
D3D12_CPU_PAGE_PROPERTY_WRITE_COMBINE = 2
D3D12_CPU_PAGE_PROPERTY_WRITE_BACK = 3
D3D12_CPU_PAGE_PROPERTY = c_int  # enum

# values for enumeration 'D3D12_HEAP_TYPE'
D3D12_HEAP_TYPE_DEFAULT = 1
D3D12_HEAP_TYPE_UPLOAD = 2
D3D12_HEAP_TYPE_READBACK = 3
D3D12_HEAP_TYPE_CUSTOM = 4
D3D12_HEAP_TYPE = c_int  # enum

# values for enumeration 'D3D12_MEMORY_POOL'
D3D12_MEMORY_POOL_UNKNOWN = 0
D3D12_MEMORY_POOL_L0 = 1
D3D12_MEMORY_POOL_L1 = 2
D3D12_MEMORY_POOL = c_int  # enum

# values for enumeration 'D3D12_HEAP_FLAGS'
D3D12_HEAP_FLAG_NONE = 0
D3D12_HEAP_FLAG_SHARED = 1
D3D12_HEAP_FLAG_DENY_BUFFERS = 4
D3D12_HEAP_FLAG_ALLOW_DISPLAY = 8
D3D12_HEAP_FLAG_SHARED_CROSS_ADAPTER = 32
D3D12_HEAP_FLAG_DENY_RT_DS_TEXTURES = 64
D3D12_HEAP_FLAG_DENY_NON_RT_DS_TEXTURES = 128
D3D12_HEAP_FLAG_HARDWARE_PROTECTED = 256
D3D12_HEAP_FLAG_ALLOW_WRITE_WATCH = 512
D3D12_HEAP_FLAG_ALLOW_SHADER_ATOMICS = 1024
D3D12_HEAP_FLAG_CREATE_NOT_RESIDENT = 2048
D3D12_HEAP_FLAG_CREATE_NOT_ZEROED = 4096
D3D12_HEAP_FLAG_ALLOW_ALL_BUFFERS_AND_TEXTURES = 0
D3D12_HEAP_FLAG_ALLOW_ONLY_BUFFERS = 192
D3D12_HEAP_FLAG_ALLOW_ONLY_NON_RT_DS_TEXTURES = 68
D3D12_HEAP_FLAG_ALLOW_ONLY_RT_DS_TEXTURES = 132
D3D12_HEAP_FLAGS = c_int  # enum

# values for enumeration 'D3D12_REFLECT_SHARED_PROPERTY'
D3D12_REFLECT_SHARED_PROPERTY_D3D11_RESOURCE_FLAGS = 0
D3D12_REFELCT_SHARED_PROPERTY_COMPATIBILITY_SHARED_FLAGS = 1
D3D12_REFLECT_SHARED_PROPERTY_NON_NT_SHARED_HANDLE = 2
D3D12_REFLECT_SHARED_PROPERTY = c_int  # enum

# values for enumeration 'D3D12_COMPATIBILITY_SHARED_FLAGS'
D3D12_COMPATIBILITY_SHARED_FLAG_NONE = 0
D3D12_COMPATIBILITY_SHARED_FLAG_NON_NT_HANDLE = 1
D3D12_COMPATIBILITY_SHARED_FLAG_KEYED_MUTEX = 2
D3D12_COMPATIBILITY_SHARED_FLAG_9_ON_12 = 4
D3D12_COMPATIBILITY_SHARED_FLAGS = c_int  # enum



class __LUID(Structure):
    pass


__LUID._fields_ = [
    ('LowPart', c_ulong),
    ('HighPart', c_int),
]

# The size provided by the typelib is incorrect.
# The size and alignment check for __LUID is skipped.


class DirectMLPyTorchCreatorID(OLE.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{AF029192-FBA1-4B05-9116-235E06560354}')
    _idlflags_ = []


DirectMLPyTorchCreatorID._methods_ = [
]

################################################################
# code template for DirectMLPyTorchCreatorID implementation
# class DirectMLPyTorchCreatorID_Impl(object):


class D3D12_RESOURCE_DESC(Structure):
    pass


class DXGI_SAMPLE_DESC(Structure):
    pass


DXGI_SAMPLE_DESC._fields_ = [
    ('Count', c_uint),
    ('Quality', c_uint),
]

# The size provided by the typelib is incorrect.
# The size and alignment check for DXGI_SAMPLE_DESC is skipped.

D3D12_RESOURCE_DESC._fields_ = [
    ('Dimension', D3D12_RESOURCE_DIMENSION),
    ('Alignment', c_ulonglong),
    ('Width', c_ulonglong),
    ('Height', c_uint),
    ('DepthOrArraySize', c_ushort),
    ('MipLevels', c_ushort),
    ('Format', DXGI_FORMAT),
    ('SampleDesc', DXGI_SAMPLE_DESC),
    ('Layout', D3D12_TEXTURE_LAYOUT),
    ('Flags', D3D12_RESOURCE_FLAGS),
]

# The size provided by the typelib is incorrect.
# The size and alignment check for D3D12_RESOURCE_DESC is skipped.


class D3D9On12CreatorID(OLE.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{FFFCBB7F-15D3-42A2-841E-9D8D32F37DDD}')
    _idlflags_ = []


D3D9On12CreatorID._methods_ = [
]

################################################################
# code template for D3D9On12CreatorID implementation
# class D3D9On12CreatorID_Impl(object):


class __MIDL___MIDL_itf_d3d12compatibility_0002_0223_0001(Union):
    pass


class D3D12_DEPTH_STENCIL_VALUE(Structure):
    pass


D3D12_DEPTH_STENCIL_VALUE._fields_ = [
    ('Depth', c_float),
    ('Stencil', c_ubyte),
]

# The size provided by the typelib is incorrect.
# The size and alignment check for D3D12_DEPTH_STENCIL_VALUE is skipped.

__MIDL___MIDL_itf_d3d12compatibility_0002_0223_0001._fields_ = [
    ('Color', c_float * 4),
    ('DepthStencil', D3D12_DEPTH_STENCIL_VALUE),
]

# The size provided by the typelib is incorrect.
# The size and alignment check for __MIDL___MIDL_itf_d3d12compatibility_0002_0223_0001 is skipped.


class ID3D12Object(OLE.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{C4FEC28F-7966-4E95-9F94-F431CB56C3B8}')
    _idlflags_ = []

    if TYPE_CHECKING:  # commembers
        def GetPrivateData(self, guid: hints.Incomplete, pDataSize: hints.Incomplete, pData: hints.Incomplete) -> hints.Hresult: ...
        def SetPrivateData(self, guid: hints.Incomplete, DataSize: hints.Incomplete, pData: hints.Incomplete) -> hints.Hresult: ...
        def SetPrivateDataInterface(self, guid: hints.Incomplete, pData: hints.Incomplete) -> hints.Hresult: ...
        def SetName(self, Name: hints.Incomplete) -> hints.Hresult: ...


ID3D12Object._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'GetPrivateData',
        (
            [],
            POINTER(OLE.GUID),
            'guid',
        ),
        ([], POINTER(c_uint), 'pDataSize'),
        ([], c_void_p, 'pData')
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetPrivateData',
        (
            [],
            POINTER(OLE.GUID),
            'guid',
        ),
        ([], c_uint, 'DataSize'),
        ([], c_void_p, 'pData')
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetPrivateDataInterface',
        (
            [],
            POINTER(OLE.GUID),
            'guid',
        ),
        ([], POINTER(IUnknown), 'pData')
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetName',
        ([], WSTRING, 'Name')
    ),
]

################################################################
# code template for ID3D12Object implementation
# class ID3D12Object_Impl(object):
#     def GetPrivateData(self, guid, pDataSize, pData):
#         '-no docstring-'
#         #return 
#
#     def SetPrivateData(self, guid, DataSize, pData):
#         '-no docstring-'
#         #return 
#
#     def SetPrivateDataInterface(self, guid, pData):
#         '-no docstring-'
#         #return 
#
#     def SetName(self, Name):
#         '-no docstring-'
#         #return 
#


class ID3D12SwapChainAssistant(OLE.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{F1DF64B6-57FD-49CD-8807-C0EB88B45C8F}')
    _idlflags_ = []

    if TYPE_CHECKING:  # commembers
        def GetLUID(self) -> hints.Hresult: ...
        def GetSwapChainObject(self, riid: hints.Incomplete) -> hints.Incomplete: ...
        def GetCurrentResourceAndCommandQueue(self, riidResource: hints.Incomplete, riidQueue: hints.Incomplete) -> hints.Tuple[hints.Incomplete, hints.Incomplete]: ...
        def InsertImplicitSync(self) -> hints.Hresult: ...


ID3D12SwapChainAssistant._methods_ = [
    COMMETHOD([], __LUID, 'GetLUID'),
    COMMETHOD(
        [],
        HRESULT,
        'GetSwapChainObject',
        (
            [],
            POINTER(OLE.GUID),
            'riid',
        ),
        (['out'], POINTER(c_void_p), 'ppv')
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetCurrentResourceAndCommandQueue',
        (
            [],
            POINTER(OLE.GUID),
            'riidResource',
        ),
        (['out'], POINTER(c_void_p), 'ppvResource'),
        (
            [],
            POINTER(OLE.GUID),
            'riidQueue',
        ),
        (['out'], POINTER(c_void_p), 'ppvQueue')
    ),
    COMMETHOD([], HRESULT, 'InsertImplicitSync'),
]

################################################################
# code template for ID3D12SwapChainAssistant implementation
# class ID3D12SwapChainAssistant_Impl(object):
#     def GetLUID(self):
#         '-no docstring-'
#         #return 
#
#     def GetSwapChainObject(self, riid):
#         '-no docstring-'
#         #return ppv
#
#     def GetCurrentResourceAndCommandQueue(self, riidResource, riidQueue):
#         '-no docstring-'
#         #return ppvResource, ppvQueue
#
#     def InsertImplicitSync(self):
#         '-no docstring-'
#         #return 
#


class DirectMLTensorFlowCreatorID(OLE.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{CB7490AC-8A0F-44EC-9B7B-6F4CAFE8E9AB}')
    _idlflags_ = []


DirectMLTensorFlowCreatorID._methods_ = [
]

################################################################
# code template for DirectMLTensorFlowCreatorID implementation
# class DirectMLTensorFlowCreatorID_Impl(object):


class D3D11On12CreatorID(OLE.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{EDBF5678-2960-4E81-8429-99D4B2630C4E}')
    _idlflags_ = []


D3D11On12CreatorID._methods_ = [
]

################################################################
# code template for D3D11On12CreatorID implementation
# class D3D11On12CreatorID_Impl(object):


class ID3D12DeviceChild(ID3D12Object):
    _case_insensitive_ = True
    _iid_ = GUID('{905DB94B-A00C-4140-9DF5-2B64CA9EA357}')
    _idlflags_ = []

    if TYPE_CHECKING:  # commembers
        def GetDevice(self, riid: hints.Incomplete) -> hints.Incomplete: ...


ID3D12DeviceChild._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'GetDevice',
        (
            ['in'],
            POINTER(OLE.GUID),
            'riid',
        ),
        (['out'], POINTER(c_void_p), 'ppvDevice')
    ),
]

################################################################
# code template for ID3D12DeviceChild implementation
# class ID3D12DeviceChild_Impl(object):
#     def GetDevice(self, riid):
#         '-no docstring-'
#         #return ppvDevice
#


class D3D11_RESOURCE_FLAGS(Structure):
    pass


D3D11_RESOURCE_FLAGS._fields_ = [
    ('BindFlags', c_uint),
    ('MiscFlags', c_uint),
    ('CPUAccessFlags', c_uint),
    ('StructureByteStride', c_uint),
]

# The size provided by the typelib is incorrect.
# The size and alignment check for D3D11_RESOURCE_FLAGS is skipped.


class OpenGLOn12CreatorID(OLE.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{6BB3CD34-0D19-45AB-97ED-D720BA3DFC80}')
    _idlflags_ = []


OpenGLOn12CreatorID._methods_ = [
]

################################################################
# code template for OpenGLOn12CreatorID implementation
# class OpenGLOn12CreatorID_Impl(object):


class Library(object):
    name = 'D3D12Lib'
    _reg_typelib_ = ('{4173F496-5631-4986-8102-5D495D6A058B}', 1, 0)


class D3D12_CLEAR_VALUE(Structure):
    pass


D3D12_CLEAR_VALUE._fields_ = [
    ('Format', DXGI_FORMAT),
    ('__MIDL____MIDL_itf_d3d12compatibility_0002_02230000', __MIDL___MIDL_itf_d3d12compatibility_0002_0223_0001),
]

# The size provided by the typelib is incorrect.
# The size and alignment check for D3D12_CLEAR_VALUE is skipped.


class D3D12_HEAP_DESC(Structure):
    pass


class D3D12_HEAP_PROPERTIES(Structure):
    pass


D3D12_HEAP_PROPERTIES._fields_ = [
    ('Type', D3D12_HEAP_TYPE),
    ('CPUPageProperty', D3D12_CPU_PAGE_PROPERTY),
    ('MemoryPoolPreference', D3D12_MEMORY_POOL),
    ('CreationNodeMask', c_uint),
    ('VisibleNodeMask', c_uint),
]

# The size provided by the typelib is incorrect.
# The size and alignment check for D3D12_HEAP_PROPERTIES is skipped.

D3D12_HEAP_DESC._fields_ = [
    ('SizeInBytes', c_ulonglong),
    ('Properties', D3D12_HEAP_PROPERTIES),
    ('Alignment', c_ulonglong),
    ('Flags', D3D12_HEAP_FLAGS),
]

# The size provided by the typelib is incorrect.
# The size and alignment check for D3D12_HEAP_DESC is skipped.


class OpenCLOn12CreatorID(OLE.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{3F76BB74-91B5-4A88-B126-20CA0331CD60}')
    _idlflags_ = []


OpenCLOn12CreatorID._methods_ = [
]

################################################################
# code template for OpenCLOn12CreatorID implementation
# class OpenCLOn12CreatorID_Impl(object):


class ID3D12CompatibilityDevice(OLE.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{8F1C0E3C-FAE3-4A82-B098-BFE1708207FF}')
    _idlflags_ = []

    if TYPE_CHECKING:  # commembers
        def CreateSharedResource(self, pHeapProperties: hints.Incomplete, HeapFlags: hints.Incomplete, pDesc: hints.Incomplete, InitialResourceState: hints.Incomplete, pOptimizedClearValue: hints.Incomplete, pFlags11: hints.Incomplete, CompatibilityFlags: hints.Incomplete, pLifetimeTracker: hints.Incomplete, pOwningSwapchain: hints.Incomplete, riid: hints.Incomplete) -> hints.Incomplete: ...
        def CreateSharedHeap(self, pHeapDesc: hints.Incomplete, CompatibilityFlags: hints.Incomplete, riid: hints.Incomplete) -> hints.Incomplete: ...
        def ReflectSharedProperties(self, pHeapOrResource: hints.Incomplete, ReflectType: hints.Incomplete, pData: hints.Incomplete, DataSize: hints.Incomplete) -> hints.Hresult: ...


class ID3D12LifetimeTracker(ID3D12DeviceChild):
    _case_insensitive_ = True
    _iid_ = GUID('{3FD03D36-4EB1-424A-A582-494ECB8BA813}')
    _idlflags_ = []

    if TYPE_CHECKING:  # commembers
        def DestroyOwnedObject(self, pObject: hints.Incomplete) -> hints.Hresult: ...


ID3D12CompatibilityDevice._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'CreateSharedResource',
        ([], POINTER(D3D12_HEAP_PROPERTIES), 'pHeapProperties'),
        ([], D3D12_HEAP_FLAGS, 'HeapFlags'),
        ([], POINTER(D3D12_RESOURCE_DESC), 'pDesc'),
        ([], D3D12_RESOURCE_STATES, 'InitialResourceState'),
        ([], POINTER(D3D12_CLEAR_VALUE), 'pOptimizedClearValue'),
        ([], POINTER(D3D11_RESOURCE_FLAGS), 'pFlags11'),
        ([], D3D12_COMPATIBILITY_SHARED_FLAGS, 'CompatibilityFlags'),
        ([], POINTER(ID3D12LifetimeTracker), 'pLifetimeTracker'),
        ([], POINTER(ID3D12SwapChainAssistant), 'pOwningSwapchain'),
        (
            [],
            POINTER(OLE.GUID),
            'riid',
        ),
        (['out'], POINTER(c_void_p), 'ppResource')
    ),
    COMMETHOD(
        [],
        HRESULT,
        'CreateSharedHeap',
        ([], POINTER(D3D12_HEAP_DESC), 'pHeapDesc'),
        ([], D3D12_COMPATIBILITY_SHARED_FLAGS, 'CompatibilityFlags'),
        (
            [],
            POINTER(OLE.GUID),
            'riid',
        ),
        (['out'], POINTER(c_void_p), 'ppHeap')
    ),
    COMMETHOD(
        [],
        HRESULT,
        'ReflectSharedProperties',
        ([], POINTER(ID3D12Object), 'pHeapOrResource'),
        ([], D3D12_REFLECT_SHARED_PROPERTY, 'ReflectType'),
        ([], c_void_p, 'pData'),
        ([], c_uint, 'DataSize')
    ),
]

################################################################
# code template for ID3D12CompatibilityDevice implementation
# class ID3D12CompatibilityDevice_Impl(object):
#     def CreateSharedResource(self, pHeapProperties, HeapFlags, pDesc, InitialResourceState, pOptimizedClearValue, pFlags11, CompatibilityFlags, pLifetimeTracker, pOwningSwapchain, riid):
#         '-no docstring-'
#         #return ppResource
#
#     def CreateSharedHeap(self, pHeapDesc, CompatibilityFlags, riid):
#         '-no docstring-'
#         #return ppHeap
#
#     def ReflectSharedProperties(self, pHeapOrResource, ReflectType, pData, DataSize):
#         '-no docstring-'
#         #return 
#

ID3D12LifetimeTracker._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'DestroyOwnedObject',
        ([], POINTER(ID3D12DeviceChild), 'pObject')
    ),
]

################################################################
# code template for ID3D12LifetimeTracker implementation
# class ID3D12LifetimeTracker_Impl(object):
#     def DestroyOwnedObject(self, pObject):
#         '-no docstring-'
#         #return 
#

__all__ = [
    'DXGI_FORMAT_R8_SNORM', 'D3D12_TEXTURE_LAYOUT',
    'D3D12_COMPATIBILITY_SHARED_FLAG_KEYED_MUTEX',
    'DXGI_FORMAT_R8_UINT', 'DXGI_FORMAT_B8G8R8X8_TYPELESS',
    'D3D12_RESOURCE_STATE_ALL_SHADER_RESOURCE', 'DXGI_FORMAT',
    'DXGI_FORMAT_R16_UNORM',
    'D3D12_RESOURCE_STATE_VERTEX_AND_CONSTANT_BUFFER',
    'D3D12_HEAP_FLAG_ALLOW_ONLY_NON_RT_DS_TEXTURES',
    'DXGI_FORMAT_R32G32B32A32_SINT', 'DXGI_FORMAT_R8G8_UINT',
    'DXGI_FORMAT_BC3_UNORM_SRGB', 'D3D12_RESOURCE_DIMENSION_BUFFER',
    'DXGI_FORMAT_Y216', 'DXGI_FORMAT_R8G8B8A8_SNORM',
    'DXGI_FORMAT_P016', 'D3D12_HEAP_FLAG_ALLOW_ONLY_BUFFERS',
    'D3D12_RESOURCE_STATE_VIDEO_ENCODE_WRITE',
    'DXGI_FORMAT_BC4_UNORM', 'OpenGLOn12CreatorID',
    'DXGI_FORMAT_B8G8R8A8_TYPELESS', 'DXGI_FORMAT_G8R8_G8B8_UNORM',
    'D3D12_RESOURCE_STATE_NON_PIXEL_SHADER_RESOURCE',
    'D3D12_RESOURCE_STATE_VIDEO_PROCESS_WRITE',
    'DXGI_FORMAT_R16_SNORM', 'DXGI_FORMAT_BC6H_UF16',
    'DXGI_FORMAT_R32G32B32_UINT', 'DXGI_FORMAT_NV11',
    'DXGI_FORMAT_BC7_UNORM_SRGB', 'D3D12_HEAP_FLAG_CREATE_NOT_ZEROED',
    'D3D12_HEAP_FLAGS', 'DXGI_FORMAT_Y210',
    'D3D12_REFLECT_SHARED_PROPERTY_NON_NT_SHARED_HANDLE',
    'DXGI_FORMAT_D16_UNORM', 'D3D12_HEAP_FLAG_HARDWARE_PROTECTED',
    'DXGI_FORMAT_R10G10B10A2_TYPELESS', 'DXGI_FORMAT_P010',
    'DXGI_FORMAT_X24_TYPELESS_G8_UINT',
    'D3D12_TEXTURE_LAYOUT_64KB_STANDARD_SWIZZLE',
    'DXGI_FORMAT_R32G32_UINT', 'ID3D12LifetimeTracker', 'Library',
    'D3D12_HEAP_TYPE_UPLOAD',
    'D3D12_COMPATIBILITY_SHARED_FLAG_NON_NT_HANDLE',
    'DXGI_FORMAT_R16G16B16A16_SINT',
    'DXGI_FORMAT_R24_UNORM_X8_TYPELESS',
    'D3D12_RESOURCE_STATE_RESOLVE_SOURCE', 'DXGI_FORMAT_BC3_TYPELESS',
    'D3D12_RESOURCE_STATE_RAYTRACING_ACCELERATION_STRUCTURE',
    'D3D12_RESOURCE_STATES', 'ID3D12CompatibilityDevice',
    'DXGI_FORMAT_BC7_TYPELESS', 'D3D12_HEAP_DESC',
    'DXGI_FORMAT_R1_UNORM', 'DXGI_FORMAT_R8G8B8A8_UNORM',
    'DXGI_FORMAT_R16_UINT', 'D3D12_RESOURCE_FLAG_ALLOW_RENDER_TARGET',
    'DXGI_FORMAT_R32G32B32_FLOAT', 'DXGI_FORMAT_BC1_TYPELESS',
    'DXGI_FORMAT_V408', 'DXGI_FORMAT_BC5_SNORM',
    'D3D12_RESOURCE_DIMENSION_UNKNOWN',
    'D3D12_TEXTURE_LAYOUT_UNKNOWN', 'DXGI_FORMAT_BC1_UNORM_SRGB',
    'DXGI_FORMAT_D32_FLOAT', 'DXGI_FORMAT_BC2_UNORM',
    'D3D12_REFLECT_SHARED_PROPERTY', 'DXGI_FORMAT_R32G32B32A32_FLOAT',
    'D3D12_RESOURCE_STATE_SHADING_RATE_SOURCE',
    'DXGI_FORMAT_R8G8_TYPELESS', 'D3D12_RESOURCE_STATE_PREDICATION',
    'D3D12_HEAP_FLAG_NONE', 'D3D12_RESOURCE_STATE_RESOLVE_DEST',
    'DXGI_FORMAT_R8G8B8A8_UNORM_SRGB', 'DXGI_FORMAT_R32_SINT',
    'DXGI_SAMPLE_DESC', 'D3D12_HEAP_FLAG_ALLOW_ONLY_RT_DS_TEXTURES',
    'DXGI_FORMAT_R8_TYPELESS', 'DXGI_FORMAT_BC7_UNORM',
    'DXGI_FORMAT_BC5_TYPELESS', 'DXGI_FORMAT_B5G6R5_UNORM',
    'D3D12_RESOURCE_STATE_INDIRECT_ARGUMENT',
    'D3D12_HEAP_TYPE_READBACK', 'DXGI_FORMAT_R16G16B16A16_FLOAT',
    'DXGI_FORMAT_BC6H_SF16', 'DXGI_FORMAT_FORCE_UINT',
    'D3D12_COMPATIBILITY_SHARED_FLAG_9_ON_12',
    'D3D12_REFELCT_SHARED_PROPERTY_COMPATIBILITY_SHARED_FLAGS',
    'DXGI_FORMAT_R32_TYPELESS', 'D3D12_RESOURCE_FLAGS',
    'DXGI_FORMAT_R16_TYPELESS', 'DXGI_FORMAT_R16G16_SNORM',
    'D3D12_HEAP_TYPE_DEFAULT', 'DXGI_FORMAT_R32G32B32A32_TYPELESS',
    'DXGI_FORMAT_R16G16_UNORM', 'DXGI_FORMAT_R32_FLOAT',
    'D3D12_RESOURCE_FLAG_VIDEO_ENCODE_REFERENCE_ONLY',
    'DXGI_FORMAT_BC4_TYPELESS',
    'D3D12_HEAP_FLAG_ALLOW_ALL_BUFFERS_AND_TEXTURES',
    'DXGI_FORMAT_R24G8_TYPELESS', 'DXGI_FORMAT_V208',
    'DXGI_FORMAT_R8_UNORM', 'D3D11_RESOURCE_FLAGS',
    'DXGI_FORMAT_P208', 'D3D12_RESOURCE_STATE_RENDER_TARGET',
    'D3D12_RESOURCE_FLAG_ALLOW_SIMULTANEOUS_ACCESS',
    'DXGI_FORMAT_R32G32_FLOAT',
    'D3D12_RESOURCE_FLAG_RAYTRACING_ACCELERATION_STRUCTURE',
    'D3D12_RESOURCE_STATE_STREAM_OUT',
    'DXGI_FORMAT_R10G10B10A2_UNORM', 'DXGI_FORMAT_R8G8_UNORM',
    'D3D12_RESOURCE_STATE_DEPTH_READ',
    'D3D12_RESOURCE_STATE_DEPTH_WRITE',
    'D3D12_RESOURCE_DIMENSION_TEXTURE1D',
    'DXGI_FORMAT_R32G32B32_SINT', 'DXGI_FORMAT_R32G32_SINT',
    'DXGI_FORMAT_D32_FLOAT_S8X24_UINT',
    'DXGI_FORMAT_R16G16B16A16_UNORM', 'DXGI_FORMAT_BC4_SNORM',
    'D3D12_HEAP_FLAG_DENY_RT_DS_TEXTURES',
    'D3D12_HEAP_FLAG_CREATE_NOT_RESIDENT',
    'DXGI_FORMAT_R32G32B32_TYPELESS', 'DirectMLPyTorchCreatorID',
    'DXGI_FORMAT_R8G8_SNORM', 'D3D12_DEPTH_STENCIL_VALUE',
    'ID3D12Object', 'D3D12_COMPATIBILITY_SHARED_FLAG_NONE',
    'D3D12_RESOURCE_FLAG_NONE', 'DXGI_FORMAT_NV12',
    'D3D12_CPU_PAGE_PROPERTY_WRITE_BACK', 'DXGI_FORMAT_P8',
    'D3D12_RESOURCE_FLAG_ALLOW_DEPTH_STENCIL',
    'D3D12_HEAP_FLAG_SHARED', 'D3D9On12CreatorID',
    'DXGI_FORMAT_BC5_UNORM', 'D3D12_HEAP_FLAG_ALLOW_WRITE_WATCH',
    'D3D12_RESOURCE_STATE_VIDEO_PROCESS_READ', 'DXGI_FORMAT_R16_SINT',
    'DXGI_FORMAT_B8G8R8X8_UNORM_SRGB', 'DXGI_FORMAT_R8G8_SINT',
    '__MIDL___MIDL_itf_d3d12compatibility_0002_0223_0001',
    'DXGI_FORMAT_R8G8_B8G8_UNORM',
    'DXGI_FORMAT_SAMPLER_FEEDBACK_MIP_REGION_USED_OPAQUE',
    'D3D12_RESOURCE_STATE_VIDEO_DECODE_READ',
    'DXGI_FORMAT_R16G16_FLOAT',
    'D3D12_RESOURCE_FLAG_ALLOW_CROSS_ADAPTER',
    'D3D12_HEAP_FLAG_DENY_BUFFERS',
    'D3D12_HEAP_FLAG_SHARED_CROSS_ADAPTER',
    'D3D12_RESOURCE_STATE_UNORDERED_ACCESS', 'D3D12_HEAP_TYPE_CUSTOM',
    'D3D12_RESOURCE_DIMENSION_TEXTURE3D',
    'D3D12_HEAP_FLAG_ALLOW_DISPLAY',
    'D3D12_COMPATIBILITY_SHARED_FLAGS',
    'DXGI_FORMAT_B8G8R8A8_UNORM_SRGB', 'DXGI_FORMAT_R8G8B8A8_SINT',
    'D3D12_RESOURCE_DIMENSION', 'DirectMLTensorFlowCreatorID',
    'DXGI_FORMAT_R10G10B10_XR_BIAS_A2_UNORM',
    'DXGI_FORMAT_R32G8X24_TYPELESS', 'DXGI_FORMAT_R16G16_TYPELESS',
    'DXGI_FORMAT_YUY2',
    'D3D12_REFLECT_SHARED_PROPERTY_D3D11_RESOURCE_FLAGS',
    'DXGI_FORMAT_R32G32_TYPELESS', 'DXGI_FORMAT_R16G16_UINT',
    'DXGI_FORMAT_R8G8B8A8_UINT', 'DXGI_FORMAT_BC2_UNORM_SRGB',
    'DXGI_FORMAT_Y410', 'DXGI_FORMAT_A8P8',
    'DXGI_FORMAT_B4G4R4A4_UNORM', 'D3D12_TEXTURE_LAYOUT_ROW_MAJOR',
    'D3D12_RESOURCE_FLAG_DENY_SHADER_RESOURCE', 'D3D12_MEMORY_POOL',
    'D3D12_HEAP_FLAG_DENY_NON_RT_DS_TEXTURES', 'D3D11On12CreatorID',
    'DXGI_FORMAT_R11G11B10_FLOAT', 'DXGI_FORMAT_Y416',
    'DXGI_FORMAT_BC3_UNORM', 'D3D12_RESOURCE_DIMENSION_TEXTURE2D',
    'DXGI_FORMAT_B5G5R5A1_UNORM', 'D3D12_RESOURCE_STATE_COMMON',
    'D3D12_MEMORY_POOL_L0', 'D3D12_CPU_PAGE_PROPERTY_UNKNOWN',
    'DXGI_FORMAT_X32_TYPELESS_G8X24_UINT',
    'D3D12_MEMORY_POOL_UNKNOWN', 'D3D12_RESOURCE_STATE_PRESENT',
    'D3D12_RESOURCE_DESC', '__LUID', 'DXGI_FORMAT_R16G16B16A16_SNORM',
    'D3D12_RESOURCE_FLAG_ALLOW_UNORDERED_ACCESS', 'ID3D12DeviceChild',
    'typelib_path', 'DXGI_FORMAT_R32_FLOAT_X8X24_TYPELESS',
    'D3D12_RESOURCE_STATE_COPY_DEST',
    'D3D12_RESOURCE_STATE_VIDEO_DECODE_WRITE',
    'D3D12_CPU_PAGE_PROPERTY_NOT_AVAILABLE',
    'D3D12_TEXTURE_LAYOUT_64KB_UNDEFINED_SWIZZLE', 'D3D12_HEAP_TYPE',
    'D3D12_RESOURCE_STATE_PIXEL_SHADER_RESOURCE',
    'DXGI_FORMAT_R9G9B9E5_SHAREDEXP',
    'DXGI_FORMAT_SAMPLER_FEEDBACK_MIN_MIP_OPAQUE',
    'D3D12_CPU_PAGE_PROPERTY_WRITE_COMBINE', 'DXGI_FORMAT_R8_SINT',
    'DXGI_FORMAT_R16G16B16A16_TYPELESS',
    'D3D12_RESOURCE_STATE_COPY_SOURCE',
    'D3D12_RESOURCE_STATE_VIDEO_ENCODE_READ',
    'DXGI_FORMAT_R16G16_SINT', 'DXGI_FORMAT_IA44',
    'D3D12_RESOURCE_STATE_INDEX_BUFFER', 'DXGI_FORMAT_R16_FLOAT',
    'DXGI_FORMAT_BC6H_TYPELESS', 'DXGI_FORMAT_B8G8R8A8_UNORM',
    'DXGI_FORMAT_R16G16B16A16_UINT', 'DXGI_FORMAT_R32G32B32A32_UINT',
    'D3D12_HEAP_PROPERTIES', 'DXGI_FORMAT_BC2_TYPELESS',
    'ID3D12SwapChainAssistant', 'D3D12_RESOURCE_STATE_GENERIC_READ',
    'DXGI_FORMAT_AYUV', 'DXGI_FORMAT_R8G8B8A8_TYPELESS',
    'D3D12_CPU_PAGE_PROPERTY', 'DXGI_FORMAT_A8_UNORM',
    'D3D12_HEAP_FLAG_ALLOW_SHADER_ATOMICS', 'DXGI_FORMAT_420_OPAQUE',
    'DXGI_FORMAT_R32_UINT', 'DXGI_FORMAT_D24_UNORM_S8_UINT',
    'D3D12_MEMORY_POOL_L1', 'DXGI_FORMAT_R10G10B10A2_UINT',
    'DXGI_FORMAT_BC1_UNORM', 'DXGI_FORMAT_B8G8R8X8_UNORM',
    'D3D12_RESOURCE_FLAG_VIDEO_DECODE_REFERENCE_ONLY',
    'OpenCLOn12CreatorID', 'DXGI_FORMAT_UNKNOWN', 'D3D12_CLEAR_VALUE',
    'DXGI_FORMAT_AI44'
]


