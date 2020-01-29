import sqlite3
import pathlib
import helper

from pathlib import Path
from helper import *
from initializor import *

def touchTheDatabase(db_path):
	return helper.confirmFile(str(db_path))



def getResult(db_path, statement, tuple_value=()):
	result = None
	db_path = str(db_path)
	try:
		connection = sqlite3.connect(str(db_path))
		cursor = connection.execute(statement, tuple_value)
		result = cursor.fetchone()
	except Exception as e:
		TH.pts(cf=cf(), mode=TH.MODE_EXCEPTION, exception=e)
		
	connection.close()
	return result 

def getRowResult(db_path, statement, tuple_value=()):
	result = None
	db_path = str(db_path)
	try:
		connection = sqlite3.connect(db_path)
		connection.row_factory = sqlite3.Row
		cursor = connection.execute(statement, tuple_value)
		result = cursor.fetchone()
	except Exception as e:
		TH.pts(cf=cf(), mode=TH.MODE_EXCEPTION, exception=e)
	
	connection.close()
	return result 


def getResults(db_path, statement, tuple_value=()):
	result = None
	db_path = str(db_path)
	try:
		connection = sqlite3.connect(str(db_path))
		cursor = connection.execute(statement, tuple_value)
		result = cursor.fetchall()
	
	except Exception as e:
		TH.pts(cf=cf(), mode=TH.MODE_EXCEPTION, exception=e)
	
	connection.close()
	return result 

def getRowResults(db_path, statement, tuple_value=()):
	result = None
	db_path = str(db_path)
	try:
		connection = sqlite3.connect(str(db_path))
		connection.row_factory = sqlite3.Row
		cursor = connection.execute(statement, tuple_value)
		result = cursor.fetchall()
	except Exception as e:
		TH.pts(cf=cf(), mode=TH.MODE_EXCEPTION, exception=e)
	
	connection.close()
	return result 

def executeDML(db_path, statement, tuple_value=()):
	result = None
	db_path = str(db_path)
	
	try:
		connection = sqlite3.connect(str(db_path))
		cursor = connection.execute(statement, tuple_value)
		connection.commit()
		connection.close()
		return True
	
	except Exception as e:
		TH.pts(cf=cf(), mode=TH.MODE_EXCEPTION, exception=e)
	
	return False

def latestValue(db_path, table_name, autoincrement_column_name):
	connection = sqlite3.connect(str(db_path))
	cursor = connection.execute("SELECT max(%s) FROM %s;"%(autoincrement_column_name, table_name))
	result = cursor.fetchone()
	connection.close()
	
	if(result!=None and len(result)!=0):
		return result[0]
	return 0


def buildCreateTableSchema(table_name, schema_dict):
	schema = """CREATE TABLE %s("""%(table_name)
	length = len(schema_dict)
	count = 0
	for key in schema_dict:
		count+=1
		schema += str(key) +" "+schema_dict[key]
		if(count<length):
			schema += ", "
	
	schema += ");"
	return schema


def createTableInDb(db_path, table_name, table_schema_dict):
	if isTableExistsInDB(db_path, table_name):
		return False
	statement = buildCreateTableSchema(table_name, table_schema_dict)
	executeDML(db_path, statement)
	return True
	
def isTableExistsInDB(db_path, table_name):
	statement = "SELECT * FROM sqlite_master WHERE type=? AND tbl_name=?;"
	tuple_value = ("table", table_name)
	result = getResult(db_path, statement, tuple_value)
	if(result != None and len(result)!=0):
		return True
	return False

def insertTableDataInDb(db_path, table_name, table_schema_dict, statement, tuple_value):
	
	touched = touchTheDatabase(db_path)
	if(not touched):
		TH.pts(cf=cf(), string=("The %s database couldn't be touched"%(str(db_path))),
			mode=TH.MODE_INABILITY)
		return False
	
	if(not isTableExistsInDB(str(db_path), table_name)):
		string = "The %s database doesn't contain the table named %s"%(str(db_path), table_name)
		TH.pts(cf=cf(), string=string, mode=TH.MODE_WARNING_2)
		
		created = createTableInDb(db_path, table_name, table_schema_dict)
		if not created:
			string = "Couldn't create the table named %s in the database named %s"%(table_name, str(db_path))
			TH.pts(cf=cf(),	string=string, mode=Terminal_Helper.MODE_WARNING_3)
			return False
	
	if executeDML(db_path, statement, tuple_value):
		return True
	
	return False
