import sys
from PyQt5.Qt import *

class Button(QPushButton):
	returnKeyPressed = pyqtSignal()
	
	def __init__(self, text, parent=None):
		super().__init__(text, parent)
		self.setMouseTracking(True)
		
	def keyPressEvent(self, event):
		if event.key() == Qt.Key_Enter or event.key() == Qt.Key_Return:
			self.returnKeyPressed.emit()
		self.update()
		
	def mouseMoveEvent(self, event):
		self.update()

class Label(QLabel):
	def __init__(self, text, parent=None):
		super().__init__(text, parent)
	
	
class Widget(QWidget):
	cursorOverTheWidget = pyqtSignal()
	
	def __init__(self, parent=None):
		super().__init__(parent)
		self.setMouseTracking(True)
		
		
	def mouseMoveEvent(self, event):
		self.cursorOverTheWidget.emit()
		self.update()
	

if __name__=='__main__':
	app = QApplication(sys.argv)
	w = Widget()
	w.show()
	sys.exit(app.exec_())
