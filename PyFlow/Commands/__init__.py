import os, sys

for n in os.listdir(os.path.dirname(__file__)):
    if n.endswith(".py") and "__init__" not in n:
        commandName = n.split(".")[0]
        PYTHON_VERSION = sys.version_info
        
        if PYTHON_VERSION < (3,0,0):        
            exec("from {0} import *".format(commandName))
        else:
            exec("from .{0} import *".format(commandName))
