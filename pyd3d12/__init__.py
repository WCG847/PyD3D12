from .D3D12 import *
from .D3D12_2 import *
from .dll import *
from .d3d12sdklayers import *
from .d3d12sdklayers_2 import *
from .d3d12compatibility import *
import platform
import sys

if not sys.platform.startswith("win"):
    raise RuntimeError("PyD3D12 is a Direct3D 12 binding and only works on Windows.")

if platform.system() != "Windows":
    raise RuntimeError("PyD3D12 is a Direct3D 12 binding and only works on Windows.")

# check architecture
if platform.architecture()[0] != "64bit":
	raise RuntimeError("PyD3D12 requires a 64-bit Python interpreter.")