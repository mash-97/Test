import sys
from PyQt5.Qt import *
import PyQt5

class Button(QPushButton):
	returnKeyPressed = PyQt5.Qt.pyqtSignal()
	
	def __init__(self, text=None, parent=None):
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
	cursorOverTheWidget = PyQt5.Qt.pyqtSignal()
	
	def __init__(self, parent=None):
		super().__init__(parent)
		self.setMouseTracking(True)
		
		
	def mouseMoveEvent(self, event):
		self.cursorOverTheWidget.emit()
		self.update()
	
	def closeEvent(self, event):
		self.destroyed.emit()
			
		

class Seque():
	def __init__(self, max_size=500):
		self.list = []
		self.max_size = max_size
		self.size = 0
	
	def free(self):
		self.list.remove(self.list[0])
		self.size -= 1
		
	def en(self, item):
		if(Seque.isSequable(item)):
			return None
		if(self.size < self.max_size):
			self.list.append(item)
		else:
			self.free()
			self.list.append(item)
		self.size += 1
	
	def isSequable(string):
		return "^[[" in string 
		
	def indexify(self, string):
		index = self.size-1
		for i in string.split("^[["):
			if('A' in i):
				if(index>0):
					index -= 1
			elif('B' in i):
				if(index < self.size-1):
					index += 1
		return index
		
		
	def get(self, string):
		if(not Seque.isSequable(string)):
			return string
		
		result = self.list[self.indexify(string)]
		self.en(result)
		print(result)
		return result

		
class Eval():
	
	def __init__(self):
		import inspect
		self.count = 0
		self.seque = Seque(max_size=2)
		
	def run(self):
		i = ''
		print(dir(i))
		while(True):
			self.count+=1
			try:
				i = input("eval[%d]: "%(self.count)).strip()
			except EOFError:
				break
				
			if(i==''):
				pass
			elif(i!='END'):
				try:
					print(eval(self.seque.get(i)))
					self.seque.en(i)
				except Exception as e:
					print(e)


if __name__=='__main__':
	import inspect
	app = QApplication(sys.argv)
	w = Widget()
	w.show()
	
	Eval().run()
	
	sys.exit(app.exec_())
