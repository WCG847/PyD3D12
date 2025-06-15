import ctypes
from ctypes import POINTER, byref, c_void_p, c_uint
from comtypes import GUID, cast
from .D3D12 import D3D_FEATURE_LEVEL_12_0, ID3D12Device, ID3D12Debug

# Load d3d12.dll
d3d12 = ctypes.windll.d3d12

# === GUIDs ===
IID_ID3D12Device = GUID("{189819f1-1db6-4b57-be54-1821339b85f7}")
IID_ID3D12Debug = GUID("{344488b7-6846-474b-b989-f027448245e0}")

# === Function Prototypes ===

# HRESULT D3D12CreateDevice(IUnknown* pAdapter, D3D_FEATURE_LEVEL MinimumFeatureLevel, REFIID riid, void** ppDevice)
D3D12CreateDevice = d3d12.D3D12CreateDevice
D3D12CreateDevice.argtypes = [c_void_p, c_uint, POINTER(GUID), POINTER(c_void_p)]
D3D12CreateDevice.restype = ctypes.c_int

# HRESULT D3D12GetDebugInterface(REFIID riid, void** ppvDebug)
D3D12GetDebugInterface = d3d12.D3D12GetDebugInterface
D3D12GetDebugInterface.argtypes = [POINTER(GUID), POINTER(c_void_p)]
D3D12GetDebugInterface.restype = ctypes.c_int

# HRESULT D3D12EnableExperimentalFeatures(UINT NumFeatures, const IID* pIIDs, void* pConfiguration, UINT* pConfigurationSize)
D3D12EnableExperimentalFeatures = d3d12.D3D12EnableExperimentalFeatures
D3D12EnableExperimentalFeatures.argtypes = [
    c_uint,
    POINTER(GUID),
    c_void_p,
    POINTER(c_uint),
]
D3D12EnableExperimentalFeatures.restype = ctypes.c_int

# HRESULT D3D12GetInterface(REFIID riid, void** ppvObject)
D3D12GetInterface = d3d12.D3D12GetInterface
D3D12GetInterface.argtypes = [POINTER(GUID), POINTER(c_void_p)]
D3D12GetInterface.restype = ctypes.c_int

# === Helpers ===


def CreateDevice(adapter=None, feature_level=D3D_FEATURE_LEVEL_12_0, debug=False):
    """
    Create a D3D12 device.
    :param adapter: Optional adapter to use, defaults to None (default adapter).
    :param feature_level: Desired feature level, defaults to D3D_FEATURE_LEVEL_12_0.
    :param debug: If True, enables the debug layer.
    :return: A pointer to the ID3D12Device interface or None on failure.
    """
    device = c_void_p()
    adapter = adapter or c_void_p(0)

    result = D3D12CreateDevice(
        adapter, feature_level, byref(IID_ID3D12Device), byref(device)
    )
    if result < 0:
        return None

    if debug:
        debug_interface = c_void_p()
        result = D3D12GetDebugInterface(byref(IID_ID3D12Debug), byref(debug_interface))
        if result >= 0:
            debug_obj = cast(debug_interface, POINTER(ID3D12Debug))
            debug_obj.EnableDebugLayer()

    return cast(device, POINTER(ID3D12Device))


def EnableExperimentalFeatures(features):
    """
    Enable experimental features in D3D12.
    :param features: A list of GUIDs representing the features to enable.
    :return: True if successful, False otherwise.
    """
    if not features:
        return True

    num_features = len(features)
    guid_array = (GUID * num_features)(*features)
    config_size = c_uint(0)

    result = D3D12EnableExperimentalFeatures(
        num_features, guid_array, None, byref(config_size)
    )
    return result >= 0


def GetInterface(riid):
    """
    Get a D3D12 interface by its GUID.
    :param riid: The GUID of the interface to retrieve.
    :return: A pointer to the requested interface or None on failure.
    """
    interface = c_void_p()
    result = D3D12GetInterface(byref(riid), byref(interface))
    if result < 0:
        return None
    return interface


def GetDebugInterface():
    """
    Get the D3D12 debug interface.
    :return: A pointer to the ID3D12Debug interface or None on failure.
    """
    debug_interface = c_void_p()
    result = D3D12GetDebugInterface(byref(IID_ID3D12Debug), byref(debug_interface))
    if result < 0:
        return None
    return cast(debug_interface, POINTER(ID3D12Debug))


def GetDevice(device_pointer):
    """
    Get a D3D12 device from a pointer.
    :param device_pointer: Pointer to the device.
    :return: A pointer to the ID3D12Device interface.
    """
    return cast(c_void_p(device_pointer), POINTER(ID3D12Device))


def GetDebugLayer():
    """
    Get the D3D12 debug layer interface.
    :return: A pointer to the ID3D12Debug interface or None if debug layer is not available.
    """
    return GetDebugInterface()
