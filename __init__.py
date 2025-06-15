from .d3d12lib.D3D12 import *  
from .d3d12lib.D3D12_2 import *  
import sys  
import platform  

if platform.system() != "Windows":  
   raise RuntimeError("PyD3D12 only supports Windows.")  

if platform.architecture()[0] != "64bit":  
   raise RuntimeError("PyD3D12 requires a 64-bit Python interpreter.")  
