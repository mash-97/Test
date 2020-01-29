import helper

from PyQt5.Qt import *
from widgetsHelper import *

class ServiceRowButton(Button):
	def __init__(self, user=None, service=None, parent=None):
		super().__init__(parent)
		
		self.user = user
		self.service = service
		self.parent = parent
		
		self.__initButton__()
		
		#label_ss = "border: 1px solid; width: 20px; height: 40px"
		#self.setStyleSheet(label_ss)
		self.clicked.connect(self._crow_b)
		self.setMinimumSize(QSize(450, 40))
		
	def __initButton__(self):
		self.id_label = QLabel(str(self.service['Id']))
		# ~ self.id_label.setStyleSheet("border: 1px solid; height: 25;")
		
		self.date_label = QLabel(str(self.service['Date']))
		# ~ self.date_label.setStyleSheet("border: 1px solid; height: 25;")
		
		self.cname_label = QLabel("   "+str(self.service['CustomerName']))
		# ~ self.cname_label.setStyleSheet("border: 1px solid; height: 25;")
		
		layout = QHBoxLayout()
		layout.addWidget(self.id_label)
		layout.addWidget(self.date_label)
		layout.addWidget(self.cname_label)
		
		self.setLayout(layout)
	
	def _crow_b(self):
		print("clicked")


class ServiceRowHL(QLabel):
	def __init__(self, parent=None):
		super().__init__(parent)
		
		self.__initButton__()
		
		self.setMinimumSize(QSize(450, 40))
		
	def __initButton__(self):
		self.id_label = QLabel("ID")
		# ~ self.id_label.setStyleSheet("border: 1px solid; height: 25;")
		
		self.date_label = QLabel("Date")
		# ~ self.date_label.setStyleSheet("border: 1px solid; height: 25;")
		
		self.cname_label = QLabel("Customer Name")
		# ~ self.cname_label.setStyleSheet("border: 1px solid; height: 25;")
		
		layout = QHBoxLayout()
		layout.addWidget(self.id_label)
		layout.addWidget(self.date_label)
		layout.addWidget(self.cname_label)
		
		self.setLayout(layout)
	

if __name__=='__main__':
	a = QApplication([])
	w = ServiceRowButton(user=None, service={'Id': 2, 'Date': helper.currentTime(), 'CustomerName': "Mashiur Rahman"})
	w.show()
	l = ServiceRowHL()
	l.show()
	sys.exit(a.exec_())

