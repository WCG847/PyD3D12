from ctypes import c_int, c_uint, Structure as struct
from Enums.COMMAND_LIST import D3D12_COMMAND_LIST_TYPE
from Enums.COMMAD_QUEUE_FLAGS import D3D12_COMMAND_QUEUE_FLAGS

class D3D12_COMMAND_QUEUE_DESC(struct):
    _fields_ = [
        ("Type", c_uint),
        ("Priority", c_int),
        ("Flags", c_uint),
        ("NodeMask", c_uint),
    ]

    @property
    def TYPE(self):
        return D3D12_COMMAND_LIST_TYPE(self.Type)

    @TYPE.setter
    def TYPE(self, val):
        self.Type = int(val)

    @property
    def FLAGS(self):
        return D3D12_COMMAND_QUEUE_FLAGS(self.Flags)

    @FLAGS.setter
    def FLAGS(self, val):
        self.Flags = int(val)
