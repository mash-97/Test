import helper
import sql_helper
import initializor
import user
import service

from user import *
from helper import *
from sql_helper import *
from service import *
from initializor import *

initializor.initializeTerminal(True)
initializor.standBFS()
initializor.confirmUsersTableInDolarin_DB()
initializor.insertADummyUser()
