from ..Core.Pin import PinWidgetBase
from ..Core.AGraphCommon import *

from shotgun_api3 import Shotgun


class SgPin(PinWidgetBase):
    """doc string for SgPin"""
    def __init__(self, name, parent, dataType, direction, **kwargs):
        super(SgPin, self).__init__(name, parent, dataType, direction, **kwargs)
        self.setDefaultValue(None)

    def supportedDataTypes(self):
        return (DataTypes.Sg,)

    @staticmethod
    def color():
        return Colors.Yellow

    @staticmethod
    def pinDataTypeHint():
        return DataTypes.Sg, ''

    # ISerializable interface
    def serialize(self):
        data = super(SgPin, self).serialize()
        data["value"] = None
        return data
    @staticmethod
    def processData( data):
        try:
            if isinstance(data,Shotgun):
                return data
            else:
                return  None
        except:
            return  None      
    def setData(self, data):
        self._data = self.processData(data)
        PinWidgetBase.setData(self, self._data)

