from ctypes.wintypes import UINT, LPCSTR, BYTE
from ctypes import Structure as struct

class D3D12_SO_DECLARATION_ENTRY(struct):
	_fields_ = [
		('Stream', UINT),
		('SemanticName', LPCSTR),
		('SemanticIndex', UINT),
		('StartComponent', BYTE),
		('ComponentCount', BYTE),
		('OutputSlot', UINT)
		]