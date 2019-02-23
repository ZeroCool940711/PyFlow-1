"""
@package Core

Core functionality of the PyFlow.
"""
import sys

PYTHON_VERSION = sys.version_info

if PYTHON_VERSION < (3,0,0):
    from Pin import PinWidgetBase
    from Edge import Edge
    from Node import Node
    from Node import NodeName
    from GetVarNode import GetVarNode
    from SetVarNode import SetVarNode
    import FunctionLibrary
    import Variable
    import VariablesWidget
else:
    from .Pin import PinWidgetBase
    from .Edge import Edge
    from .Node import Node
    from .Node import NodeName
    from .GetVarNode import GetVarNode
    from .SetVarNode import SetVarNode
    from . import FunctionLibrary
    from . import Variable
    from . import VariablesWidget
    
