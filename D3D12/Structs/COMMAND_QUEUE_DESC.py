from ctypes import Structure as struct
from ctypes.wintypes import UINT, INT
from Enums.COMMAND_LIST import D3D12_COMMAND_LIST_TYPE
from Enums.COMMAD_QUEUE_FLAGS import D3D12_COMMAND_QUEUE_FLAGS

class D3D12_COMMAND_QUEUE_DESC(struct):
    _fields_ = [
        ("Type", UINT),
        ("Priority", INT),
        ("Flags", UINT),
        ("NodeMask", UINT),
    ]

    @property
    def type(self):
        return D3D12_COMMAND_LIST_TYPE(self.Type)

    @type.setter
    def type(self, val):
        self.Type = int(val)

    @property
    def flags(self):
        return D3D12_COMMAND_QUEUE_FLAGS(self.Flags)

    @flags.setter
    def flags(self, val):
        self.Flags = int(val)
