from ..Core.Pin import PinWidgetBase
from ..Core.AGraphCommon import *
from pyrr import Vector4


class FloatVector4Pin(PinWidgetBase):
    """doc string for FloatVector4Pin"""
    def __init__(self, name, parent, dataType, direction, **kwargs):
        super(FloatVector4Pin, self).__init__(name, parent, dataType, direction, **kwargs)
        self.setDefaultValue(Vector4())

    def supportedDataTypes(self):
        return (DataTypes.FloatVector4,)

    @staticmethod
    def pinDataTypeHint():
        return DataTypes.FloatVector4, Vector4()

    @staticmethod
    def color():
        return Colors.FloatVector4

    @staticmethod
    def processData( data):
        if isinstance(data, Vector4):
            return data
        elif isinstance(data, list) and len(data) == 4:
            return Vector4(data)
        else:
            return Vector4()  
           
    def serialize(self):
        data = PinWidgetBase.serialize(self)
        data['value'] = self.currentData().xyzw.tolist()
        return data

    def setData(self, data):
        self._data = self.processData(data)
        PinWidgetBase.setData(self, self._data)
