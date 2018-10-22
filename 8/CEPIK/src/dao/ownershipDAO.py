import sys, pickle
sys.path.insert(0, '../../src')

from  properties import properties
from helper.connection_manager import ConnectionManager
from entity.person import Person
from helper.commons import rename_file
from dao.daoInterface import DAOInterface

class OwnershipDAO(DAOInterface):
    pass