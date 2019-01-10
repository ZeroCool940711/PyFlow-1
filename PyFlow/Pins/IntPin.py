from ..Core.Pin import PinWidgetBase
from ..Core.AGraphCommon import *


class IntPin(PinWidgetBase):
    """doc string for IntPin"""
    def __init__(self, name, parent, dataType, direction, **kwargs):
        super(IntPin, self).__init__(name, parent, dataType, direction, **kwargs)
        self.setDefaultValue(0)

    @staticmethod
    def color():
        return Colors.Int

    @staticmethod
    def pinDataTypeHint():
        return DataTypes.Int, 0
    @staticmethod
    def processData( data):
        try:
            return int(data)
        except:
            return 0
    def supportedDataTypes(self):
        return (DataTypes.Int, DataTypes.Float)

    def setData(self, data):
        self._data = self.processData(data)
        PinWidgetBase.setData(self, self._data)