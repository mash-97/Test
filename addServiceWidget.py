import sys
import helper
import os

from PyQt5.Qt import *
from widgetsHelper import *
from styleSheets import *
from initializor import BFP
from user import *

class AddServiceWidget(Widget):
	def __init__(self, user, parent=None):
		super().__init__(parent)
		self.__defineWidgets__()
		self.__signalsAndSlots__()
		self.__setLayouts__()
		size = self.sizeHint()
		self.setFixedSize(QSize(size.width()-100, size.height()))
		# ~ self.setFixedSize(QSize(size.width(), size.height()))
		self.user = user
	
	
		
	def ___provide_completer_to_service_types___(self, model):
		completer = QCompleter(model)
		self.service_types_lineEdit.setCompleter(completer)
	
	def __clear_lineEdit_texts__(self):
		self.customer_name_lineEdit.setText("")
		self.service_types_lineEdit.setText("")
		self.cost_lineEdit.setText("")
		self.description_lineEdit.setPlainText("")
		
	def __defineWidgets__(self):
		self.customer_name_lineEdit = QLineEdit(self)
		self.customer_name_lineEdit.setPlaceholderText("e.g mash")
		
		self.service_types_lineEdit = QLineEdit(self)
		self.service_types_lineEdit.setPlaceholderText("e.g photocopy")
		
		self.cost_lineEdit = QLineEdit(self)
		self.cost_lineEdit.setPlaceholderText("Tk")
		
		self.description_lineEdit = QPlainTextEdit(self)
		self.description_lineEdit.setPlaceholderText("e.g phone, address")
		self.description_lineEdit.setMaximumHeight(70)
		
		self.status_label = QLabel("")
		
		self.add_button = Button("Add", self)
		
		self.form_layout = QFormLayout()
		self.form_layout.setSpacing(50)
		
	def __setLayouts__(self):
		
		vl = QVBoxLayout(self)
		
		# Labels
		head_label = QLabel("Add Service", self)
		head_label.setStyleSheet(S_SUBHEAD_LABEL)
		head_label.setAlignment(Qt.AlignCenter | Qt.AlignTop)
		
		name_label = QLabel("Name: ", self)
		service_types_label = QLabel("Service Types: ", self)
		cost_label = QLabel("Cost: ", self)
		description_label = QLabel("Description: ", self)
		
		button_layout = QHBoxLayout()
		button_layout.addStretch(1)
		button_layout.addWidget(self.add_button)
		button_layout.addStretch(1)
		
		self.form_layout.addRow(name_label, self.customer_name_lineEdit)
		self.form_layout.addRow(service_types_label, self.service_types_lineEdit)
		self.form_layout.addRow(cost_label, self.cost_lineEdit)
		self.form_layout.addRow(description_label, self.description_lineEdit)
		self.form_layout.addRow(button_layout)
		self.form_layout.addRow(self.status_label)
		self.form_layout.setHorizontalSpacing(10)
		self.form_layout.setVerticalSpacing(20)
		groupbox = QGroupBox("")
		
		v = QVBoxLayout(groupbox)
		
		vl.addWidget(head_label)
		v.addLayout(self.form_layout)
		
		vl.addWidget(groupbox)
		
	def __signalsAndSlots__(self):
		self.customer_name_lineEdit.textChanged.connect(lambda: self._csl() if len(self.customer_name_lineEdit.text()) == 1 else None)
		self.customer_name_lineEdit.returnPressed.connect(lambda: self.service_types_lineEdit.setFocus(True))
		
		self.service_types_lineEdit.textChanged.connect(lambda: self._csl() if len(self.service_types_lineEdit.text()) == 1 else None)
		self.service_types_lineEdit.returnPressed.connect(lambda: self.cost_lineEdit.setFocus(True))
		
		self.cost_lineEdit.textChanged.connect(lambda: self._csl() if len(self.cost_lineEdit.text()) == 1 else None)
		self.cost_lineEdit.returnPressed.connect(lambda: self.add_button.setFocus(True))
		
		self.description_lineEdit.textChanged.connect(lambda: self._csl() if len(self.description_lineEdit.toPlainText()) == 1 else None)
		# ~ self.description_lineEdit.returnPressed.connect(lambda: self.add_button.setFocus(True))
		
		self.add_button.clicked.connect(self._add_service)
		self.add_button.returnKeyPressed.connect(self._add_service)
	
	def _csl(self):
		self.status_label.setText("")
	
	
	def _add_service(self):
		if self.__is_validate_data__():
			d = helper.currentTime()
			st = self.service_types_lineEdit.text()
			c = Customer(self.customer_name_lineEdit.text(), None, None)
			des = str(self.description_lineEdit.toPlainText())
			ct = self.cost_lineEdit.text()
			
			service = Service(d, st, c, des, ct)
			added = Service.addServiceToDB(self.user.DatabasePath, service)
			if added:
				TH.pts(cf = cf(), string="Service Added.\n\tId No: "+str(added))
				self.status_label.setText(S_GREEN_LABEL%"New service is added with ID: "+str(added))
				self.__clear_lineEdit_texts__()
			else:
				TH.pts(cf=cf(), string="Couldn't add the service", mode=TH.MODE_INABILITY)
				self.status_label.setText(S_RED_LABEL%"Couldn't add the service")
		else:
			self.status_label.setText(S_RED_LABEL%"Invalid Data")
		self.form_layout.update()
		self.customer_name_lineEdit.setFocus(True)
		
			
			
	def __is_validate_data__(self):
		if len(self.customer_name_lineEdit.text()) < 2:
			return False
		if str(self.cost_lineEdit.text()).isalpha():
			return False
		if len(self.cost_lineEdit.text()) < 1:
			return False
		return True
	
	

if __name__ == '__main__':
	app = QApplication(sys.argv)
	u = User("tash", "dash")
	u.authorize()
	window = AddServiceWidget(user=u)
	window.setWindowTitle("Add Service")
	window.show()
	sys.exit(app.exec_())

	
