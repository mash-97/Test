import sys
import helper
import os
from PyQt5.Qt import *
from widgetsHelper import *
from styleSheets import *
from initializor_granular import BFP

class AddServiceWidget(Widget):
	def __init__(self, user, parent=None):
		super().__init__(parent)
		self.__defineWidgets__()
		self.__setLayouts__()
		size = self.sizeHint()
		self.setFixedSize(QSize(size.width()-100, size.height()))
		# ~ self.setFixedSize(QSize(size.width(), size.height()))
		self.user = user
	
	
		
	def ___provide_completer_to_service_types___(self, model):
		completer = QCompleter(model)
		self.service_types_lineEdit.setCompleter(completer)
		
	def __defineWidgets__(self):
		self.customer_name_lineEdit = QLineEdit(self)
		
		self.service_types_lineEdit = QLineEdit(self)
		self.service_types_lineEdit.setPlaceholderText("e.g photocopy")
		
		
		self.cost_lineEdit = QLineEdit(self)
		self.description_lineEdit = QPlainTextEdit(self)
		self.description_lineEdit.setMaximumHeight(70)
		
		self.add_button = Button("Add", self)
		
	def __setLayouts__(self):
		
		vl = QVBoxLayout(self)
		
		form_layout = QFormLayout()
		form_layout.setSpacing(50)
		
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
		
		form_layout.addRow(name_label, self.customer_name_lineEdit)
		form_layout.addRow(service_types_label, self.service_types_comboBox)
		form_layout.addRow(cost_label, self.cost_lineEdit)
		form_layout.addRow(description_label, self.description_lineEdit)
		form_layout.addRow(button_layout)
		
		groupbox = QGroupBox("")
		
		v = QVBoxLayout(groupbox)
		
		vl.addWidget(head_label)
		v.addLayout(form_layout)
		
		vl.addWidget(groupbox)
		

if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = AddServiceWidget(user=None)
	window.setWindowTitle("Add Service")
	window.show()
	sys.exit(app.exec_())

	
