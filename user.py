import sys
import os
import sqlite3
import initializor
import service

from initializor import *
from helper import *
from service import *


class User():
	TABLE_NAME = "USER"
	SCHEMA_DICT = {
					'Id': "INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE",
					'UserName':  "VARCHAR(32) UNIQUE NOT NULL",
					'Password':  "TEXT NOT NULL",
					'DatabasePath': "TEXT NOT NULL",
				}
	
	SCHEMA = sql_helper.buildCreateTableSchema(TABLE_NAME, SCHEMA_DICT)
	
	DATABASE_NAME = BFP['databases']['dolarin_db']
	
				
	__USER_EXISTS__ = "User Exists"
	__USER_DOESNT_EXIST__ = "User Doesn't Exists"
	__USER_ALREADY_AUTHORIZED__ = "User Already Authorized"
	__USER_NAME_USED__  = "User Name Used"
	
	def __init__(self, UserName, Password):
		
		self.Id = None
		self.UserName = UserName 
		self.Password = helper.Password.encode(Password)
		self.authorized = False
	
	
	def authorize(self):
		fetched_user_data = User.fetchUser(self.UserName)
		if(fetched_user_data):
			self.Id = fetched_user_data['Id']
			self.DatabasePath = fetched_user_data['DatabasePath']
			if(self.Password==fetched_user_data['Password']):
				self.authorized = True
		if self.authorized:
			return True
		return False
	
	
	def summerizeUserDependencies(user):
		TH.pts(cf=cf(), string=("Summerizing dependencies for user: ", user.UserName), mode=TH.MODE_ASSERTION)
		# Check user's authorized existency.
		if not user.authorized:
			TH.pts(cf=cf(), string="User isn't authorized. So no further inquiries.", mode=TH.MODE_FALSE)
			return False
		else:
			TH.pts(cf=cf(), string="User is authorized", mode=TH.MODE_TRUE)
		
		# Check User's database file and it's dependencies
	def authorizeNewUser(user):
		TH.pts(cf=cf(), string=("Authorizing new User: UserName: %s\n"%(user.UserName)), mode=TH.MODE_ASSERTION)
		try:
			# Check Username
			if User.checkAuthorizedUserNameExistency(user):
				TH.pts(cf=cf(), string=("Username with %s already exists\n"%(user.UserName)), mode=TH.MODE_FALSE)
				return User.__USER_NAME_USED__
			
			# Insert the user in the Dolarin.db
			user.DatabasePath = User.futorUserDBPathFor(user)
			
			statement = "INSERT INTO USER VALUES(NULL, ?, ?, ?);"
			tuple_value = (user.UserName, user.Password, str(user.DatabasePath))
			try:
				sql_helper.executeDML(User.DATABASE_NAME, statement, tuple_value)
			except Exception as e:
				TH.pts(cf=cf(), mode=TH.MODE_EXCEPTION, exception=e)
				return False
			
			# Create user.DatabasePath file
			created = helper.createFile(user.DatabasePath)
			if not created:
				TH.pts(cf=cf(), string=("Couldn't create the file: %s"%(str(user.DatabasePath))),
					mode=TH.MODE_INABILITY)
				return False
			
			# Create SERVICE TABLE in user.DatabasePath database
			created = sql_helper.createTableInDb(str(user.DatabasePath), Service.TABLE_NAME, Service.SCHEMA_DICT)
			if not created:
				string = "Couldn't create %s table in the %s database."%(Service.TABLE_NAME, str(user.DatabasePath))
				TH.pts(cf=cf(), string=string, mode=TH.MODE_WARNING_3)
			
			user.authorized = True
			TH.pts(cf=cf(), string=("User authorized. UserName: "+user.UserName), mode=TH.MODE_OK)
			
			return True
		except Exception as e:
			TH.pts(cf=cf(), string=("Exception: "+str(e)), mode=TH.MODE_EXCEPTION, exception=e)
		return False
	
	
	def futorUserDBPathFor(user):
		result = latestValue(User.DATABASE_NAME, "USER", "Id")
		path = BFP['directories']['users_data']/(str(user.UserName)+"_"+str(result+1)+".db")
		return path
	
	
	def checkAuthorizedUserNameExistency(user):
		statement = "SELECT * FROM USER WHERE UserName=?"
		tuple_value = ([user.UserName])
		result = sql_helper.getResult(User.DATABASE_NAME, statement, tuple_value)
		
		if(not result):
			TH.pts(cf=cf(), string=("%s doesn't exist in the db."%(user.UserName)), mode=TH.MODE_FALSE)
			return False
			
		TH.pts(cf=cf(), string=("%s exists in the db."%(user.UserName)), mode=TH.MODE_ASSERTION)
		return True
	
	
	def fetchUser(user_name):
		statement = "SELECT * FROM USER WHERE UserName=?;"
		tuple_value = ([user_name])
		result = sql_helper.getRowResult(User.DATABASE_NAME, statement, tuple_value)
		
		if(not result):
			return False
		
		return result
	
	
	def touchInterfaceYAML(user):
		if not user.authorized:
			return False
		path = helper.extentifyWith(user.DatabasePath, 'yml')
		return helper.createFile(path)
	
