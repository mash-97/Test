import sys
import os
import helper
import initializor
import user
import service
import PyQt5
import widgetsHelper

from user import *
from service import *
from PyQt5.Qt import *
from widgetsHelper import *

class DisplayServiceWidget(Widget):
	def __init__(self, user=None, service=None, parent=None
