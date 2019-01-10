from PyFlow.App import PyFlow
from Qt import QtCore
from Qt.QtWidgets import QMainWindow


from shiboken2 import wrapInstance
from maya import OpenMayaUI as OpenMayaUI
from maya.app.general.mayaMixin import MayaQWidgetDockableMixin
from maya.OpenMayaUI import MQtUtil
import maya.cmds as cmds

class MyWindow(MayaQWidgetDockableMixin, PyFlow):
    toolName = 'myToolWidget'

    def __init__(self, parent = None):
        # Delete any previous instances that is detected. Do this before parenting self to main window!
        self.deleteInstances()
        super(self.__class__, self).__init__(parent = parent)
        mayaMainWindowPtr = OpenMayaUI.MQtUtil.mainWindow() 
        self.mayaMainWindow = wrapInstance(long(mayaMainWindowPtr), QMainWindow)
        self.setObjectName(self.__class__.toolName) # Make this unique enough if using it to clear previous instance!

        # Setup window's properties
        self.setWindowFlags(QtCore.Qt.Window)
        self.setWindowTitle('My tool')
        self.resize(200, 200)
        # Create a button and stuff it in a layout

    # If it's floating or docked, this will run and delete it self when it closes.
    # You can choose not to delete it here so that you can still re-open it through the right-click menu, but do disable any callbacks/timers that will eat memory
    #def dockCloseEventTriggered(self):
    #    self.deleteInstances()

    # Delete any instances of this class
    def deleteInstances(self):
        #mayaMainWindowPtr = MQtUtil.mainWindow() 
        #mayaMainWindow = wrapInstance(long(mayaMainWindowPtr), QMainWindow) # Important that it's QMainWindow, and not QWidget/QDialog
        if cmds.workspaceControl(self.__class__.toolName+"WorkspaceControl", q=True, exists=True):
            cmds.workspaceControl(self.__class__.toolName+"WorkspaceControl", e=True, close=True)
            cmds.deleteUI(self.__class__.toolName+"WorkspaceControl", control=True)       
    def keyPressEvent(self, event):
    	pass
    # Show window with docking ability
    def run(self):
        self.show(dockable = True)

myWin = MyWindow()
myWin.run()