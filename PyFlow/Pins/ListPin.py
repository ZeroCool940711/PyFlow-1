from ..Core.Pin import PinWidgetBase
from ..Core.AGraphCommon import *


class ListPin(PinWidgetBase):
    """doc string for ListPin"""
    def __init__(self, name, parent, dataType, direction, **kwargs):
        super(ListPin, self).__init__(name, parent, dataType, direction, **kwargs)
        self.setDefaultValue([])

    def serialize(self):
        dt = super(PinWidgetBase, self).serialize()
        if isinstance(self._data, list):
            datas = []
            for i in self._data:
                datas.append(str(i))
            dt['value']=datas                         
        return dt

    def supportedDataTypes(self):
        return (DataTypes.Array,)

    @staticmethod
    def color():
        return Colors.Array

    @staticmethod
    def pinDataTypeHint():
        return DataTypes.Array, []
    @staticmethod
    def processData( data):
        if isinstance(data, list):
            return data
        else:
            return []
    def setData(self, data):
        self._data = self.processData(data)
        PinWidgetBase.setData(self, self._data)
