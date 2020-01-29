import sys
from PyQt5.Qt import *
from dolarin import *
from styleSheets import *
from widgetsHelper import *

class LoginWidget(Widget):
	getSignupPage = pyqtSignal()
	getAuthorizedLogin = pyqtSignal([User])
	
	def __init__(self, parent=None):
		super().__init__(parent)
		self.__defineWidgets__()
		self.__setLayouts__()
		self.__setSignalsAndSlots__()
		self.setFixedSize(self.sizeHint())
	
	def __update__(self):
		self.username_lineEdit.clear()
		self.username_lineEdit.setFocus(True)
		self.password_lineEdit.clear()
		self.status_label.clear()
		
	def __defineWidgets__(self):
		# Username LineEdit
		self.username_lineEdit = QLineEdit(self)
		self.username_lineEdit.setPlaceholderText("e.g mash")
		self.username_lineEdit.setStyleSheet(S_FIELD_LINEEDIT)
		self.username_lineEdit.setFocus(True)
		
		# Password LineEdit
		self.password_lineEdit = QLineEdit(self)
		self.password_lineEdit.setEchoMode(QLineEdit.Password)
		self.password_lineEdit.setStyleSheet(S_FIELD_LINEEDIT)
		self.password_lineEdit.setPlaceholderText("****")
		
		# Status Label
		self.status_label = QLabel("")
		
		# Login Button
		self.login_button = Button("Login")
		self.login_button.setStyleSheet(S_FIELD_BUTTON)
		self.login_button.setFixedSize(100, 30)
		
		# Signup Button 
		self.signup_button = Button("Sign Up")
		self.signup_button.setStyleSheet(S_FIELD_BUTTON)
		self.signup_button.setFixedSize(100, 30)
	
	def __setLayouts__(self):
		layout = QVBoxLayout()
		
		login_head_label = QLabel("Login")
		login_head_label.setAlignment(Qt.AlignCenter)
		login_head_label.setStyleSheet(S_HEAD_LABEL)
		
		form_layout = QFormLayout()	
		form_layout.setSpacing(40)	
		
		username_label = QLabel("Username: ")
		username_label.setStyleSheet(S_FIELD_LABEL)
		
		password_label = QLabel("Password: ")
		password_label.setStyleSheet(S_FIELD_LABEL)
		
		login_button_layout = QHBoxLayout()
		login_button_layout.addStretch(1)
		
		login_button_layout.addWidget(self.login_button)
		login_button_layout.addStretch(1)
		
		signup_button_layout = QHBoxLayout()
		signup_button_layout.addStretch(1)
		
		signup_button_layout.addWidget(self.signup_button)
		signup_button_layout.addStretch(1)
		
		form_layout.addRow(username_label, self.username_lineEdit)
		form_layout.addRow(password_label, self.password_lineEdit)
		form_layout.addRow(self.status_label)
		form_layout.addRow(login_button_layout)
		form_layout.addRow(signup_button_layout)
		form_layout.setHorizontalSpacing(10)
		form_layout.setVerticalSpacing(20)
		l = QHBoxLayout()
		l.addStretch(1)
		form_layout.addRow(l)
		
		layout.addWidget(login_head_label, 1, Qt.AlignTop)
		layout.addSpacing(15)
		layout.addLayout(form_layout)
		layout.setAlignment(Qt.AlignCenter)		
		self.setLayout(layout)
		
	def __setSignalsAndSlots__(self):
		# signals and slots connections
		self.username_lineEdit.textChanged.connect(self._clear_status_label)
		self.username_lineEdit.returnPressed.connect(lambda: self.password_lineEdit.setFocus(True))
		self.password_lineEdit.returnPressed.connect(self._login_button_clicked)
		self.password_lineEdit.textChanged.connect(self._clear_status_label)
		self.login_button.clicked.connect(self._login_button_clicked)
		self.login_button.returnKeyPressed.connect(self._login_button_clicked)
		self.signup_button.clicked.connect(lambda: self.getSignupPage.emit())
		self.signup_button.returnKeyPressed.connect(lambda: self.getSignupPage.emit())
		
	def _clear_status_label(self):
		self.status_label.setText("")
	
	def _login_button_clicked(self):
		if not helper.isValidUsername(self.username_lineEdit.text()):
			self.status_label.setText(S_RED_LABEL%("Username is not valid"))
			return None
					
		user = User(self.username_lineEdit.text(), self.password_lineEdit.text())
		user.authorize()
		if not user.authorized:
			self.status_label.setText(S_RED_LABEL%("User Unauthorized"))
		else:
			self.status_label.setText(S_GREEN_LABEL%("User Authorized"))
			self.getAuthorizedLogin.emit(user)





if __name__ == '__main__':
	app = QApplication(sys.argv)
	
	l = LoginWidget()
	l.show()
	
	sys.exit(app.exec_())

