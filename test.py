

# ~ import sqlite3
# ~ import sys
# ~ import os
# ~ import re

# ~ from helper import *
# ~ from initializor_granular import *



# ~ def regexp(pattern, input):
	# ~ return bool(re.match(pattern, input))

# ~ data = """
# ~ ----------
# ~ 1
# ~ 2
# ~ 3
# ~ 4
# ~ 5
# ~ 6
# ~ 7
# ~ ----------
# ~ Paul
# ~ Allen
# ~ Teddy
# ~ Mark
# ~ David
# ~ Kim
# ~ James

# ~ ----------
# ~ 32
# ~ 25
# ~ 23
# ~ 25
# ~ 27
# ~ 22
# ~ 24

# ~ ----------
# ~ California
# ~ Texas
# ~ Norway
# ~ Rich-Mond
# ~ Texas
# ~ South-Hall
# ~ Houston

# ~ ----------
# ~ 20000.0
# ~ 15000.0
# ~ 20000.0
# ~ 65000.0
# ~ 85000.0
# ~ 45000.0
# ~ 10000.0
# ~ """

# ~ data = data.split("----------")
# ~ segments = []
# ~ for segment in data:
	# ~ templ = segment.split("\n")
	# ~ while(True):
		# ~ try:
			# ~ templ.remove('')
		# ~ except ValueError:
			# ~ break
	# ~ if(templ.__len__()!=0):
		# ~ segments.append(tuple(templ))

# ~ data = []
# ~ for index1 in range(0, len(segments[0])):
	# ~ temp = []
	# ~ for index in range(0, len(segments)):
		# ~ temp.append(segments[index][index1])
	# ~ data.append(tuple(temp))

# ~ for d in data:
	# ~ print(d)


# ~ connection = sqlite3.connect("./Dolarin.db")
# ~ connection.row_factory = sqlite3.Row
# ~ connection.create_function('regexp', 2, regexp)

# ~ while True:
	# ~ s = input("\nsqlite3>> ")
	# ~ if(s==".q" or re.match('[.]quit', s)):
		# ~ break
	# ~ try:
		# ~ cursor = connection.execute(s)
		# ~ result = cursor.fetchall()
		# ~ result.sort(key=lambda x: x[1])
		# ~ for r in result:
			# ~ print("Id: {:2d} {:>10s}: {:s} {:>10s}: {:d}".format(r['Id'], "Name", r['Name'], "Age", r['Age']))
	# ~ except Exception as e:
		# ~ print("Exception: {}\n".format(e))
		# ~ pass

# ~ connection.close()

# ~ print(isTheTableExistsInTheDB("./Dolarin.db", "Users"))

# ~ def a(*ar):
	# ~ print("ar: {0}, type: {1}".format(ar, type(ar)))
	# ~ print(type(*ar))
	# ~ print("*ar: ", *ar, "*type: ", type(*ar))

# ~ a(1,2,3)

def pa(l, tabs):
	print("{0}{1}".format(tabs, id(l)))
	if(type(l)==type([]) or type(l)==type({}) or type(l)==type(())):
		tabs += "\t"
		for i in l:
		  pa(i, tabs)
		
		
# ~ l = [[1,2], 3, [343,33], "dkjf"]
# ~ print("l ids")
# ~ pa(l, "")
# ~ print("")


# ~ c = l.copy()
# ~ print("c ids")
# ~ pa(c, "")
# ~ print("")

# ~ import copy
# ~ d = copy.deepcopy(l)
# ~ print("d ids")
# ~ pa(d, "")
# ~ print("")


# ~ from PyQt5.QtWidgets import(QWidget, QFrame, QHBoxLayout, QSplitter, QStyleFactory, QApplication)
# ~ from PyQt5.QtCore import Qt
# ~ import sys

# ~ class Example(QWidget):
	# ~ def __init__(self, parent=None):
		# ~ super().__init__(parent)
		# ~ self.initUi()
	
	# ~ def initUi(self):
		# ~ hbox = QHBoxLayout(self)
		
		# ~ topleft = QFrame(self)
		# ~ topleft.setFrameShape(QFrame.StyledPanel)
		
		# ~ topright = QFrame(self)
		# ~ topright.setFrameShape(QFrame.StyledPanel)
		
		# ~ bottom = QFrame(self)
		# ~ bottom.setFrameShape(QFrame.StyledPanel)
		
		# ~ splitter1 = QSplitter(Qt.Horizontal)
		# ~ splitter1.addWidget(topleft)
		# ~ splitter1.addWidget(topright)
		
		# ~ splitter2 = QSplitter(Qt.Vertical)
		# ~ splitter2.addWidget(splitter1)
		# ~ splitter2.addWidget(bottom)
		
		# ~ hbox.addWidget(splitter2)
		# ~ self.setLayout(hbox)
		
		# ~ self.setGeometry(300, 300, 300, 200)
		# ~ self.setWindowTitle('QSplitter')
		# ~ self.show()


# ~ app = QApplication(sys.argv)
# ~ ex = Example()
# ~ sys.exit(app.exec_())

# ~ import copy
# ~ d = {'a': 1, 'b': 2, 'c': 3, 'd': {1: 'a', 2: 'b', 3: 'c', 4: {'a': {1: 'a'}, 'b': 2}}}
# ~ print("d:  ", d)

# ~ e = copy.deepcopy(d)
# ~ print("e: ", e)

# ~ e['d'][4]['a'][1]='b'
# ~ print(d['d'][4]['a'][1])


# ~ ddf=1

# ~ def ad(v):
	# ~ print(ddf)
	# ~ ddf+=v

# ~ ad(5)
# ~ print(ddf)

# ~ b = {'a': 1}
# ~ c = 1
# ~ def t():
	# ~ global c
	# ~ print(b)
	# ~ print(c)
	# ~ b['b'] = 2
	# ~ c+=1
# ~ t()
# ~ print(b)
# ~ print(c)
# ~ def count():
	# ~ t = 0
	# ~ def inc():
		# ~ nonlocal t
		# ~ t += 1
		# ~ return t
	# ~ return (inc, t)

# ~ c = count()
# ~ print(c[0](), c[1])
# ~ print(c[0](), c[1])

# ~ d = count()
# ~ print(d[0](), d[1])
# ~ print(d[0](), d[1])

import os
df = {}
def dir_glob(dir_path, tabs):
	global df
	if(not os.path.isdir(dir_path)):
		pass
	print(tabs+os.path.basename(dir_path)+":")
	entries = os.listdir(dir_path)
	df[os.path.basename(dir_path)]  = {}
	df[os.path.basename(dir_path)]['directories'] = []
	df[os.path.basename(dir_path)]['files'] = []
	
	for e in entries:
		epath = os.path.join(dir_path, e)
		if(os.path.isfile(epath)):
			print(tabs+"\t"+e)
			df[os.path.basename(dir_path)]['files'].append(e)
		elif(os.path.isdir(epath)):
			df[os.path.basename(dir_path)]['directories'].append(e)
			dir_glob(epath, tabs+"\t")
		

dir_glob(".dolarin", "")
print(df)
	


		
