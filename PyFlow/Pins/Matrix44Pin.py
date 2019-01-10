from ..Core.Pin import PinWidgetBase
from ..Core.AGraphCommon import *
from pyrr import Matrix44


class Matrix44Pin(PinWidgetBase):
    """doc string for Matrix44Pin"""
    def __init__(self, name, parent, dataType, direction, **kwargs):
        super(Matrix44Pin, self).__init__(name, parent, dataType, direction, **kwargs)
        self.setDefaultValue(Matrix44())

    def supportedDataTypes(self):
        return (DataTypes.Matrix44,)

    @staticmethod
    def color():
        return Colors.Matrix44

    @staticmethod
    def pinDataTypeHint():
        return DataTypes.Matrix44, Matrix44()

    def serialize(self):
        data = PinWidgetBase.serialize(self)
        m = self.currentData()
        data['value'] = [m.c1.tolist(), m.c2.tolist(), m.c3.tolist(), m.c4.tolist()]
        return data
    @staticmethod
    def processData( data):
        if isinstance(data, Matrix44):
            return data
        elif isinstance(data, list) and len(data) == 3:
            return Matrix44([data[0], data[1], data[2], data[3]])
        else:
            return Matrix44()
    def setData(self, data):
        self._data = self.processData(data)
        PinWidgetBase.setData(self, self._data)
