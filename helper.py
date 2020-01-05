import os
import time
import hashlib
import inspect
import re

from inspect import currentframe as cf, getframeinfo as gfi
from pathlib import Path

class Time:
	week_days_names = ['', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
	
	def now(get_sec=False):
		now = time.localtime()
		date = "/".join([str(now.tm_mday), str(now.tm_mon), str(now.tm_year)])
		clock_time = [str(12 if now.tm_hour==24  or now.tm_hour%12==0 else now.tm_hour % 12), str(now.tm_min)]
		if get_sec:
			clock_time.append(str(now.tm_sec))
		clock_time = ":".join(clock_time)
		ampm = 'PM' if now.tm_hour//12==1 else 'AM'
		
		return ' :: '.join([Time.week_days_names[now.tm_wday+1], date, clock_time, ampm])

class Password:
	SALT = b'\x08z'
	VAL = 10
	def encode(password):
		return str(hashlib.pbkdf2_hmac('sha256', password.encode(), Password.SALT, Password.VAL))
	
	def compareWithHashedPassword(string_password, hashed_password):
		return Password.encode(string_password)==hashed_password

class Terminal:
	def __init__(self, terminal_file_name, show_on_terminal=False):
		self.tfn = terminal_file_name
		self.sot = show_on_terminal
		
	def puts(self, string=""):
		string += '\n'
		f = open(self.tfn, 'a+')
		f.write(string)
		f.close()
		if(self.sot):
			print(string)


		


def createFile(path):
	path = str(path)
	try:
		if os.path.exists(path):
			return True
		else:
			open(path._str, "w")
		return True
	except:
		pass
	return False

		
def extentifyWith(path, ext):
	path = str(path)
	ext = str(ext)
	return path+"."+ext

def currentTime(get_sec = False):
	return Time.now(get_sec)

def current_line_no():
	return gfi(cf().f_back).lineno

def current_function_name(cur_frame):
	return gfi(cf().cur_frame).function

def current_file_name():
	return gfi(cf().f_back).filename

def cpi(cur_frame):
	s = Path(gfi(cur_frame).filename).stem+"/ "
	f = gfi(cur_frame).function
	if(f!="<module>"):
		s += f+"/ "
	s+=str(gfi(cur_frame).lineno)+"::: "
	return s





































class Th:
	MODE_WARNING_1 = "#-->"
	MODE_WARNING_2 = "##->"
	MODE_WARNING_3 = "###>"
	MODE_WRONG = "W###>"
	MODE_OK = "OK::"
	MODE_ASSERTION = "-->"
	MODE_TRUE = "-->TRUE::"
	MODE_FALSE = "F###>"
	MODE_PROCCESSING = "...>"
	MODE_EXCEPTION = "EXCEPTION>"
	MODE_INABILITY = "I###>"
	MODE_TRYING = "T...>"

	def __init__(self, show=True):
		self.show = show
		self.__import_vars__()
	
	def __import_vars__(self):
		for d in dir(Th):
			if re.match(r'^MODE_', d):
				value = str(eval("Th.%s"%(d)))
				exec("self.%s = '%s';"%(d, value))
				
	def pts(self, cf=None, string="", mode = MODE_ASSERTION, exception=None):
		cp = cpi(cf)
		if self.show==True:
			print("\n")
			if mode==Th.MODE_EXCEPTION and exception!=None:
				print(mode+" "+str(type(exception))+": "+string+" "+str(exception))
			else:
				print(mode+" "+cp+string)
