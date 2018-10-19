import sys, pickle
sys.path.insert(0, '../../src')

from helper.connection_manager import ConnectionManager
from entity.vehicle import Vehicle
from helper.commons import replace_files


class VehicleDAO(object):

    data=[]

    def get_all_data(self, database_path):
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

    def search(self, database_path, mode, field, value):
        entries=[]
        entries = self.get_all_data(database_path)
        if field == 'model':
            self.get_vehicle_by_model(mode, entries,value)

        if field == 'vin':
            self.get_vehicle_by_vin(mode, entries,value)


    def delete(self, database_path, mode, field, value):
        entries=[]
        new_entries=[]
        entries = self.get_all_data(database_path)
        if field == 'model':
            new_entries = self.delete_by_model(database_path, mode, entries,value)

        if field == 'vin':
            new_entries = self.delete_by_vin(database_path, mode, entries,value)

        replace_files(database_path+"_new.dat",database_path)

    def get_vehicle_by_model(self, mode, entries,model):
        for i in entries:
            if (i.model == model and mode != 'i')  or (i.model.upper() == model.upper() and mode == 'i'):
                print(i)

    def get_vehicle_by_vin(self,mode, entries,vin):
        for i in entries:
            if (i.vin == vin and mode != 'i')  or (i.vin.upper() == vin.upper() and mode == 'i'):
                print(i)

    def add(self, database_path, row):
        vehicle = Vehicle(row['vin'],row['model'])
        database = ConnectionManager().open_database_a(database_path)
        print(f'adding {vehicle}')
        pickle.dump(vehicle,database)
        ConnectionManager().close_database(database)

    def delete_by_model(self, database_path, mode, entries, model):
        for i in entries:
            if not ((i.model == model and mode != 'i')  or (i.model.upper() == model.upper() and mode == 'i')):
                self.add(database_path+"_new.dat",{'vin':i.vin, 'model':i.model})




    def delete_by_vin(self, database_path, mode, entries, vin):
        for i in entries:
            if not ((i.vin == vin and mode != 'i')  or (i.vin.upper() == vin.upper() and mode == 'i')):
                self.add(database_path+"_new.dat",{'vin':i.vin, 'model':i.model})

