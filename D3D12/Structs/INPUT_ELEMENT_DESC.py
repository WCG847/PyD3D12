from ctypes import Structure as struct, c_uint as ENUM
from ctypes.wintypes import LPCSTR, UINT
from DXGI.Enums.FORMAT import DXGI_FORMAT
from D3D12.Enums.INPUT_CLASSIFICATION import D3D12_INPUT_CLASSIFICATION


class D3D12_INPUT_ELEMENT_DESC(struct):
    _fields_ = [
        ('SemanticName', LPCSTR),
        ('SemanticIndex', UINT),
        ('Format', ENUM),
        ('InputSlot', UINT),
        ('AlignedByteOffset', UINT),
        ('InputSlotClass', ENUM),
        ('InstanceDataStepRate', UINT),
    ]

    @property
    def format_enum(self):
        return DXGI_FORMAT(self.Format)

    @format_enum.setter
    def format_enum(self, val):
        self.Format = int(val)

    @property
    def input_slot_class_enum(self):
        return D3D12_INPUT_CLASSIFICATION(self.InputSlotClass)

    @input_slot_class_enum.setter
    def input_slot_class_enum(self, val):
        self.InputSlotClass = int(val)

