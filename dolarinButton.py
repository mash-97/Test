from PyQt5.Qt import *

class Button(QPushButton):
	returnKeyPressed = pyqtSignal()
	
	def __init__(self, text):
		super().__init__(text)
	
	def keyPressEvent(self, event):
		print("A key is pressed on the keyboard")
		if event.key() == Qt.Key_Enter or event.key() == Qt.Key_Return:
			print("Qt.Key_Enter")
			self.returnKeyPressed.emit()

