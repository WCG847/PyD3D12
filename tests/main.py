import ctypes
from ctypes import POINTER, c_void_p, byref, c_uint
import comtypes
from comtypes import GUID
from d3d12lib.D3D12 import ID3D12Device
from comtypes import cast


# === Constants ===
D3D_FEATURE_LEVEL_11_0 = 0xB000

# === Load D3D12 DLL ===
d3d12 = ctypes.windll.d3d12

# === Declare D3D12CreateDevice prototype ===
D3D12CreateDevice = d3d12.D3D12CreateDevice
D3D12CreateDevice.restype = ctypes.c_long  # HRESULT
D3D12CreateDevice.argtypes = [
    c_void_p,            # IUnknown* pAdapter (can be None)
    c_uint,              # D3D_FEATURE_LEVEL
    POINTER(GUID),       # REFIID
    POINTER(c_void_p),   # void**
]

# === Initialize COM ===
comtypes.CoInitialize()

# === Prepare output interface pointer ===
device_ptr = c_void_p()
iid_ID3D12Device = ID3D12Device._iid_

# === Create the device ===
hr = D3D12CreateDevice(
    None,                     # Use default adapter
    D3D_FEATURE_LEVEL_11_0,
    byref(iid_ID3D12Device),
    byref(device_ptr)
)

if hr != 0 or not device_ptr.value:
    raise OSError(f"D3D12CreateDevice failed (HRESULT=0x{hr:08X})")

print(f"HRESULT: 0x{hr:08X}")
print("device_ptr:", device_ptr.value)


device = cast(device_ptr, POINTER(ID3D12Device))


print("✅ D3D12 Device created successfully!")
print("✅ D3D12 device interface is ready:", device)
print("Available methods:", dir(device))


# === Shutdown COM ===
comtypes.CoUninitialize()
