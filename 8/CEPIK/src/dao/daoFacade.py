import sys, pickle
sys.path.insert(0, '../../src')

from  properties import properties
from dao.personDAO import PersonDAO
from dao.vehicleDAO import VehicleDAO


class DaoFacade():

    def get_instance(self,database):
        if database == 'person':
            return PersonDAO()

        if database == 'vehicle':
            return VehicleDAO()
