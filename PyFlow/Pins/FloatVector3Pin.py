from ..Core.Pin import PinWidgetBase
from ..Core.AGraphCommon import *
from pyrr import Vector3


class FloatVector3Pin(PinWidgetBase):
    """doc string for FloatVector3Pin"""
    def __init__(self, name, parent, dataType, direction, **kwargs):
        super(FloatVector3Pin, self).__init__(name, parent, dataType, direction, **kwargs)
        self.setDefaultValue(Vector3())

    def supportedDataTypes(self):
        return (DataTypes.FloatVector3,)

    @staticmethod
    def color():
        return Colors.FloatVector3

    @staticmethod
    def pinDataTypeHint():
        return DataTypes.FloatVector3, Vector3()
    @staticmethod
    def processData( data):
        if isinstance(data, Vector3):
            return data
        elif isinstance(data, list) and len(data) == 3:
            return Vector3(data)
        else:
            return Vector3()
    def serialize(self):
        data = PinWidgetBase.serialize(self)
        data['value'] = self.currentData().xyz.tolist()
        return data

    def setData(self, data):
        self._data = self.processData(data)
        PinWidgetBase.setData(self, self._data)
