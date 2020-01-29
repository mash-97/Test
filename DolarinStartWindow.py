from signupWidget import *
from loginWidget import *
from addServiceWidget import *

class DolarinStartWindow(Widget):
	
	def __init__(self, parent=None):
		super().__init__(parent)
		
		self.__defineWidgets__()
		self.__setStackedLayout__()
		self.__setSignalsAndSlots__()
		
		self.setWindowTitle("Dolarin")
		self.resize(self.stack_layout.currentWidget().sizeHint())
		self.setStyleSheet("background-color: #000000;")
		self.setFixedSize(self.stack_layout.currentWidget().sizeHint())
		self.move(400, 150)
	
				
	def __defineWidgets__(self):
		self.login_widget = LoginWidget(self)
		self.signup_widget = SignupWidget(self)
	
	def __update__(self):
		self._login_page()
		self.show()
		
	def __setStackedLayout__(self):
		self.stack_layout = QStackedLayout()
		self.stack_layout.setCurrentIndex(0)
		self.stack_layout.addWidget(self.login_widget)
		self.stack_layout.addWidget(self.signup_widget)
	
	def __setSignalsAndSlots__(self):
		self.login_widget.getSignupPage.connect(self._signup_page)
		self.login_widget.getAuthorizedLogin[User].connect(self._next_page)
		
		self.signup_widget.getSigninPage.connect(self._login_page)
		self.signup_widget.getAuthorizedSignup.connect(self._next_page)
		
	def _signup_page(self):
		self.signup_widget.__update__()
		self.stack_layout.setCurrentIndex(1)
		self.resize(self.stack_layout.currentWidget().sizeHint())
		self.setFixedSize(self.stack_layout.currentWidget().sizeHint())
		
	def _login_page(self):
		self.login_widget.__update__()
		self.stack_layout.setCurrentIndex(0)
		self.resize(self.stack_layout.currentWidget().sizeHint())
		self.setFixedSize(self.stack_layout.currentWidget().sizeHint())
	
	def _next_page(self, user):
		print("In Development: \n")
		for service in Service.fetchAllServices(user.DatabasePath):
			print("Id: {0}, Date: {1}, CustomerName: {2}\n".format((service['Id'], type(service['Id'])), (service['Date'], type(service['Date'])), (service['CustomerName'], type(service['CustomerName']))))
			
		
		self.close()
		self.adsw =  AddServiceWidget(user)
		self.adsw.show()
		self.adsw.destroyed.connect(lambda: self.__update__())
	
		
		

if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = DolarinStartWindow()
	window.show()
	window.setContentsMargins(1,1,1,5)
	sys.exit(app.exec_())
