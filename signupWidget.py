import sys
from PyQt5.Qt import *
from styleSheets import *
from widgetsHelper import *
from user import *

class SignupWidget(Widget):
	getSigninPage = pyqtSignal()
	getAuthorizedSignup = pyqtSignal()
	
	def __init__(self, parent=None):
		super().__init__(parent)
		self.__defineWidgets__()
		self.__setLayouts__()
		self.__setSignalsAndSlots__()
		self.setFixedSize(self.sizeHint())
	
	def __update__(self):
		self.username_lineEdit.clear()
		self.password_lineEdit.clear()
		self.confirm_password_lineEdit.clear()
		self.status_label.clear()
		
	def __defineWidgets__(self):
		# Username LineEdit
		self.username_lineEdit = QLineEdit()
		self.username_lineEdit.setPlaceholderText("e.g mash")
		self.username_lineEdit.setStyleSheet(S_FIELD_LINEEDIT)
		self.username_lineEdit.setFocus(True)
		
		# Password LineEdit
		self.password_lineEdit = QLineEdit()
		self.password_lineEdit.setEchoMode(QLineEdit.Password)
		self.password_lineEdit.setStyleSheet(S_FIELD_LINEEDIT)
		self.password_lineEdit.setPlaceholderText("****")
		
		# Confirm Password LineEdit
		self.confirm_password_lineEdit = QLineEdit()
		self.confirm_password_lineEdit.setEchoMode(QLineEdit.Password)
		self.confirm_password_lineEdit.setStyleSheet(S_FIELD_LINEEDIT)
		self.confirm_password_lineEdit.setPlaceholderText("****")
		
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
		
		login_head_label = QLabel("Sign Up")
		login_head_label.setAlignment(Qt.AlignCenter | Qt.AlignTop)
		login_head_label.setStyleSheet(S_HEAD_LABEL)
		
		form_layout = QFormLayout()	
		form_layout.setSpacing(50)	
		
		username_label = QLabel("Username: ")
		username_label.setStyleSheet(S_FIELD_LABEL)
		
		
		password_label = QLabel("Password: ")
		password_label.setStyleSheet(S_FIELD_LABEL)
		
		
		confirm_password_label = QLabel("Confirm Password: ")
		confirm_password_label.setStyleSheet(S_FIELD_LABEL)
		
		
		signup_button_layout = QHBoxLayout()
		signup_button_layout.addStretch(1)
		signup_button_layout.addWidget(self.signup_button)
		signup_button_layout.addStretch(1)
		
		
		login_button_layout = QHBoxLayout()
		login_button_layout.addStretch(1)
		login_button_layout.addWidget(self.login_button)
		login_button_layout.addStretch(1)
		
		form_layout.addRow(username_label, self.username_lineEdit)
		form_layout.addRow(password_label, self.password_lineEdit)
		form_layout.addRow(confirm_password_label, self.confirm_password_lineEdit)
		form_layout.addRow(self.status_label)
		form_layout.addRow(signup_button_layout)
		form_layout.addRow(login_button_layout)
		
		
		layout.addWidget(login_head_label)
		layout.addSpacing(15)
		layout.addLayout(form_layout)
		layout.setAlignment(Qt.AlignCenter)
		
		self.setLayout(layout)
		
	def __setSignalsAndSlots__(self):
		self.username_lineEdit.textChanged.connect(self._clear_status_label)
		self.username_lineEdit.returnPressed.connect(self._username_edited)
		
		self.password_lineEdit.returnPressed.connect(lambda: self.confirm_password_lineEdit.setFocus(True))
		self.password_lineEdit.textChanged.connect(self._clear_status_label)
		
		self.confirm_password_lineEdit.returnPressed.connect(self._confirmed_password)
		self.confirm_password_lineEdit.textChanged.connect(self._clear_status_label)
		
		self.signup_button.clicked.connect(self._signup_button_clicked)
		self.signup_button.returnKeyPressed.connect(self._signup_button_clicked)
		
		self.login_button.clicked.connect(lambda: self.getSigninPage.emit())
		self.login_button.returnKeyPressed.connect(lambda: self.getSigninPage.emit())
	
	def _username_edited(self):
		user = User(self.username_lineEdit.text(), self.password_lineEdit.text())
		if not User.checkAuthorizedUserNameExistency(user):
			self.status_label.setText(S_GREEN_LABEL%("Username Checked"))
			self.password_lineEdit.setFocus(True)
		else:
			self.status_label.setText(S_RED_LABEL%("Username Used"))
			self.username_lineEdit.setFocus(True)
	
	def _confirmed_password(self):
		if(self.password_lineEdit.text()!=self.confirm_password_lineEdit.text()):
			self.status_label.setText(S_RED_LABEL%("Passwords Don't Match"))
		else:
			print("Get Authorized Signup")
			self.getAuthorizedSignup.emit()
	
	def _signup_button_clicked(self):
		pass
		
	def _clear_status_label(self):
		self.status_label.setText("")


if __name__ == '__main__':
	app = QApplication(sys.argv)
	
	s = SignupWidget()
	s.show()
	
	sys.exit(app.exec_())


