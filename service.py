import sys
import sql_helper
import initializor
from initializor import *

class Customer:
	def __init__(self, CustomerName, CustomerNumber, CustomerAddress):
		self.CustomerName = CustomerName
		self.CustomerNumber = CustomerNumber
		self.CustomerAddress = CustomerAddress

class Service:
	TABLE_NAME = "SERVICE"
	
	SCHEMA_DICT = {
					'Id': "INTEGER  PRIMARY KEY AUTOINCREMENT UNIQUE",
					'Date': "VARCHAR(100) NOT NULL",
					'ServiceTypes': "VARCHAR(500) NOT NULL",
					'CustomerName': "VARCHAR(100) NOT NULL",
					'CustomerNumber': "VARCHAR(20) NULL",
					'CustomerAddress': "VARCHAR(100) NULL",
					'Description': "VARCHAR(1001) NULL", 
					'Cost': "REAL NOT NULL"
				}
	
	__SERVICE_EXISTS__ = "Service Exists"
	__SERVICE_DOESNT_EXIST__ = "Service Doesn't Exists"
	
	def __init__(self, date, service_types, customer, description, cost):
		if(type(service_types)==type([])):
			', '.join(service_types)
		
		self.Date = date
		self.ServiceTypes =  service_types
		self.CustomerName = customer.CustomerName
		self.CustomerNumber = customer.CustomerNumber
		self.CustomerAddress = customer.CustomerAddress
		self.Description = description
		self.Cost = cost
	
	def addServiceToDB(db_path, service):
		try:
			statement = """INSERT INTO %s VALUES(NULL, ?, ?, ?, ?, ?, ?, ?);"""%(Service.TABLE_NAME)
			tuple_value = (service.Date, service.ServiceTypes, 
							service.CustomerName, service.CustomerNumber, service.CustomerAddress, service.Description,
							service.Cost)
			sql_helper.executeDML(str(db_path), statement, tuple_value)
			
		except Exception as e:
			TH.pts(cf=cf(), string=("Exception: "+str(e)),	
								mode=TH.MODE_EXCEPTION, exception=e)
			return False
		return True
	
	def fetchAllServices(db_path):
		serivces = None
		try:
			statement = """SELECT * FROM %s;"""%(Service.TABLE_NAME)
			services = sql_helper.getRowResults(db_path, statement, ())
		except Exception as e:
			TH.pts(cf=cf(), mode=TH.MODE_EXCEPTION, exception=e)
			return None
		return services
	
	def fetchServicesByColumnName(db_path, ColumnName, ColumnValue):
		services = None
		try:
			statement = """SELECT * FROM %s WHERE %s=?;"""%(Service.TABLE_NAME, ColumnName)
			tuple_value = ([ColumnValue])
			services = sql_helper.getRowResults(db_path, statement, tuple_value)
		except Exception as e:
			TH.pts(cf(), string="", mode=TH.MODE_EXCEPTION, exception=e)
			return None
		return services
	
	def fetchServicesByColumnNames(db_path, column_dict):
		temps = []
		for columnName in column_dict.keys():
			temps.append(str(columnName)+"=="+("'%s'"%str(column_dict[columnName])))
		
		statement = """SELECT * FROM %s WHERE %s;"""%(Service.TABLE_NAME, " AND ".join(temps))
		
		try:
			temps = sql_helper.getRowResults(db_path, statement, ())
			return temps
		except Exception as e:
			TH.pts((cpi(cf())), mode=TH.MODE_EXCEPTION, exception=e)
		
		return None

	
	
