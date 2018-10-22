import sys, pickle
sys.path.insert(0, '../../src')

from  properties import properties
from helper.connection_manager import ConnectionManager
from entity.vehicle import Vehicle
from helper.commons import rename_file
from dao.daoInterface import DAOInterface

class VehicleDAO(DAOInterface):

    data=[]

    def get_all_data(self):
        database_path=properties.databases['vehicle']
        database = ConnectionManager().open_database_r(database_path)
        self.data=[]
        while True:
            try:
                self.data.append( pickle.load(database))
            except Exception as e:
                break
        ConnectionManager().close_database(database)
        return self.data

    def __str__(self):
        for i in self.data:
            print(i)

    def print(self, data):
        for i in data:
            print(i)

    def search(self,  mode, field, value):
        entries=[]
        entries = self.get_all_data()

        for i in entries:
            if (getattr(i,field) == value and mode != 'i')  or (getattr(i,field).upper().strip() == value.upper().strip() and mode == 'i'):
                print(i)

    def delete(self,  mode, field, value):
        database_path=properties.databases['vehicle']
        entries=[]
        entries = self.get_all_data()
        rename_file(database_path,database_path+".old")
        print("Entries survived in database:")
        for i in entries:
            if not ((getattr(i,field) == value and mode != 'i')  or (getattr(i,field).upper() == value.upper() and mode == 'i')):
                self.add({'vin':i.vin, 'model':i.model})

    def count(self, mode, field, value):
        entries=[]
        entries = self.get_all_data()
        seq=0
        for i in entries:
            if (getattr(i,field) == value and mode != 'i')  or (getattr(i,field).upper() == value.upper() and mode == 'i'):
                seq+=1
        print(f'count({vin}) = {seq}')

    def add(self,  row):
        vehicle = Vehicle(row['vin'],row['model'])
        database_path =  properties.databases['vehicle']
        database = ConnectionManager().open_database_a(database_path)
        print(f'adding {vehicle}')
        pickle.dump(vehicle,database)
        ConnectionManager().close_database(database)

    def update(self, mode, search_field, search_value, change_field, change_val):
        database_path=properties.databases['person']
        entries=[]
        entries = self.get_all_data()
        rename_file(database_path,database_path+".old")
        for i in entries:
            vehicle=i;
            if (getattr(i,search_field) == search_value and mode != 'i')  or (getattr(i,search_field).upper().strip() == search_value.upper().strip() and mode == 'i'):
                setattr(vehicle,change_field,change_val)
            self.add({'vin':vehicle.vin, 'model':vehicle.model})
