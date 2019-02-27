from ..Core.AbstractGraph import *
from ..Core.Settings import *
from ..Core import Node

class SelectFile(Node):
	def __init__(self, name, graph):
		super(SelectFile, self).__init__(name, graph)
		self.Select_File = self.addInputPin("Select_File", DataTypes.Exec,self.compute,hideLabel=True)
		self.output = self.addOutputPin("output", DataTypes.String,hideLabel=False)

		for i in self.inputs.values():
			for o in self.outputs.values():
				pinAffects(i, o)        
	@staticmethod
	def pinTypeHints():
		'''
		    used by nodebox to suggest supported pins
		    when drop wire from pin into empty space
		'''
		return {'inputs': [DataTypes.Bool], 'outputs': [DataTypes.Bool]}

	@staticmethod
	def category():
		'''
		    used by nodebox to place in tree
		    to make nested one - use '|' like this ( 'CatName|SubCatName' )
		'''
		return 'Common'

	@staticmethod
	def keywords():
		'''
		    used by nodebox filter while typing
		'''
		return []

	@staticmethod
	def description():
		'''
		    used by property view and node box widgets
		'''
		return 'Open a Dialog to select a file from your computer. Returns the path to the file as a String.'
	def compute(self):
		# access pins like this
				# self.pinName.getData()
				# self.pinName.setData()
				# self.getData(name) to get data from input pin by name
				# self.setData(name, data) to set data to output pin by name
		import sys
		from PyQt4.QtGui import QApplication, QWidget, QFileDialog

		# Create an PyQT4 application object.
		a = QApplication(sys.argv)

		# The QWidget widget is the base class of all user interface objects in PyQt4.
		w = QWidget()
		# Get filename using QFileDialog
		filename = str(QFileDialog.getOpenFileName(w, 'Open File', '', '', None, QFileDialog.DontUseNativeDialog))
		if filename:
			print ('File Path: '+ filename)
		else:
			print ("Nothing was selected.")
		self.setData("output", filename)    
