import sys
import os
import pathlib
import sql_helper
import helper

from pathlib import Path
from sql_helper import *
from helper import *

DOLARIND = Path.cwd()/'.'
BFP = {
					"directories": 
						{
							"dolarin": DOLARIND,
							"program_data": DOLARIND/'program_data', 
							"program_terminal_outputs": DOLARIND/'program_data'/'program_terminal_outputs',
							"users_data": DOLARIND/'users_data',
						},
						
					"files":
						{
							"program_logs": DOLARIND/'program_data'/'logs.txt'
						},
					
					"databases":
						{
							"dolarin_db": DOLARIND/'Dolarin.db'
						}
				}

Author_Data = {
			"author":
				{
					"name": "Mashiur Rahman",
					"email": "mahimnhd97@gmail.com"
				}
		}

TH = helper.Th()


T = None

def initializeTerminal(show_on_terminal=False):
	# generate terminal file name with the timestamps
	timestamps=BFP['directories']['program_terminal_outputs']/(helper.currentTime().replace(' ', '').replace('::', ''))
	file_path = helper.extentifyWith(timestamps, "ops")
	helper.createFile(file_path)
	
	# initializing global T with Terminal
	global T
	T = helper.Terminal(terminal_file_name = file_path, show_on_terminal=show_on_terminal)
	return T


def torchDES(dir_path, des_dict={}):
	dir_path = str(dir_path)
	
	if(not os.path.isdir(dir_path)):
		pass
	entries = os.listdir(dir_path)
	for e in entries:
		epath = os.path.join(dir_path, e)
		if os.path.isfile(epath):
			des_dict[e] = epath
		elif os.path.isdir(epath):
			des_dict[e] = torchDES(epath, {"path": epath})
			
	return des_dict

def initializeDFD():
	global BFP
	BFP['DFD'] = torchDES(DOLARIND)
	

def getDSFor(string="", data={}, tabs=""):
	if(type(data)==type({})):
		for key in data:
			string+= tabs+key+":\n"
			string = getDSFor(string, data[key], tabs+"\t")
	elif(type(data)==type([])):
		for i in data:
			string = getDSFor(string, i, tabs+"\t")
	else:
		string += tabs+str(data)+"\n"
	return string


def insertADummyUser():
	r = sql_helper.getResult(str(BFP['databases']['dolarin_db']), "SELECT id FROM USER WHERE id=1")
	if(r==None):
		db_name = str(BFP['databases']['dolarin_db'])
		statement = "INSERT INTO USER VALUES(1, ?, ?, ?);"
		tuple_value = ("mash97", "yossup", str(BFP['directories']['users_data']/("mash97_1.db")))
		r = sql_helper.executeDML(db_name, statement, tuple_value)
		
		TH.pts("--> Dummy USER inserted")
		# ~ print(r)
	
	
def confirmUsersTableInDolarin_DB():
	connection = sqlite3.connect(str(BFP['databases']['dolarin_db']))
	if(sql_helper.isTableExistsInDB(str(BFP['databases']['dolarin_db']), 'USER')):
		print("--> USER table exists in the dolarin_db")
	
	else:
		try:
			created = sql_helper.createTableInDb(User.DATABASE_NAME, User.TABLE_NAME, User.SCHEMA_DICT)
			if not created:
				print("###--> Failed to create %s table in the %s"%(User.TABLE_NAME, User.DATABASE_NAME))
			else:
				print("---> %s table is created in the %s"%(User.TABLE_NAME, User.DATABASE_NAME))
		
		except Exception as e:
			print("###--> Failed to create the",User.TABLE_NAME,"table in the dolarin_db:", e)
	
	connection.commit()
	connection.close()
	insertADummyUser()

def standBFS():
	message=("Making Stand of The BFS")
	TH.pts(cf=cf(), string=message, 
		mode=TH.MODE_ASSERTION)
		
	# Confirming Directories
	message="Checking %s in %s\n"%("directories", os.path.abspath(BFP['directories']['dolarin']))
	TH.pts(cf=cf(), string=message, 
		mode=TH.MODE_ASSERTION)
	
	for directory in BFP['directories']:
		dir_name = BFP['directories'][directory].name
		if BFP['directories'][directory].is_dir():
			print("OK:: directory: %s" % dir_name)
		else:
			print("W:: directory: %s" % dir_name)
			os.mkdir(str(BFP['directories'][directory]))
			if(BFP['directories'][directory].is_dir()):
				print("OK:: directory: %s" % dir_name)
	
	# Confirming Files
	message="Checking %s in %s\n"%("files", os.path.abspath(BFP['directories']['dolarin'].__str__()))
	TH.pts(cf=cf(), string=message, 
		mode=TH.MODE_ASSERTION)
		
	for file in BFP['files']:
		file_name = BFP['files'][file].name
		if BFP['files'][file].is_file():
			print("OK:: file: %s" % file_name)
		else:
			print("W:: file: %s" % file_name)
			open(str(BFP['files'][file]), "w")
			if(BFP['files'][file].is_file()):
				print("OK:: file: %s" % file_name)
	
	# Confirming Databases
	message="Checking %s in %s\n"%("databases", os.path.abspath(BFP['directories']['dolarin'].__str__()))
	TH.pts(cf=cf(), string=message, 
		mode=TH.MODE_ASSERTION)
		
	for db in BFP['databases']:
		db_name = BFP['databases'][db].name
		if BFP['databases'][db].is_file():
			print("OK:: database: %s" % db_name)
		else:
			print("W:: database: %s" % db_name)
			open(str(BFP['databases'][db]), "w")
			if(BFP['databases'][db].is_file()):
				print("OK:: database: %s" % db_name)
	
