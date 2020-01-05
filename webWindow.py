import webview
from PyQt5.Qt import *
from PyQt5.QtWebEngineWidgets import *

class WebWidget(QWebEngineView):
	def __init__(self, parent=None):
		super().__init__(parent)
		self.setPage(self._s(parent))
	
	def _s(self, parent):
		s = QWebEnginePage(parent)
		s.setUrl(QUrl("/home/mash/Progus/Exturbus/HTML/testo1.htm"))
		s.view()
		return s


a = QApplication([])
w = WebWidget()
w.show()
a.exec_()
