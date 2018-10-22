import sys, pickle
sys.path.insert(0, '../../src')

from  properties import properties
from helper.connection_manager import ConnectionManager
from entity.person import Person
from helper.commons import rename_file
from dao.daoInterface import DAOInterface

class PersonDAO(DAOInterface):

    data=[]

    def get_all_data(self,):
        database_path=properties.databases['person']
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

    def search(self,mode, field, value ):
        database_path=properties.databases['person']
        entries=[]
        entries = self.get_all_data()

        for i in entries:
            if (getattr(i,field) == value and mode != 'i')  or (getattr(i,field).upper().strip() == value.upper().strip() and mode == 'i'):
                print(i)

    def delete(self, mode, field, value):
        database_path=properties.databases['person']
        entries=[]
        new_entries=[]
        entries = self.get_all_data()

        rename_file(database_path,database_path+".old")
        print("Entries survived in database:")
        for i in entries:
            if not ((getattr(i,field) == value and mode != 'i')  or (getattr(i,field).upper().strip() == value.upper().strip() and mode == 'i')):
                self.add({'pesel':i.pesel, 'name':i.name, 'surname':i.surname})

    def count(self, mode, field, value):
        entries=[]
        entries = self.get_all_data()

        seq=0
        for i in entries:
            if (getattr(i,field) == value and mode != 'i')  or (getattr(i,field).upper().strip() == value.upper().strip() and mode == 'i'):
                seq+=1
        print(f'count({name}) = {seq}')

    def add(self, row):
        person=Person(row['pesel'], row['name'],row['surname'])
        database_path =  properties.databases['person']
        database = ConnectionManager().open_database_a(database_path)
        print(f'adding {person}')
        pickle.dump(person,database)
        ConnectionManager().close_database(database)

    def update(self, mode, search_field, search_value, change_field, change_val):
        database_path=properties.databases['person']
        entries=[]
        entries = self.get_all_data()
        rename_file(database_path,database_path+".old")
        for i in entries:
            person=i;
            if (getattr(i,search_field) == search_value and mode != 'i')  or (getattr(i,search_field).upper().strip() == search_value.upper().strip() and mode == 'i'):
                setattr(person,change_field,change_val)
            self.add({'pesel':person.pesel, 'name':person.name, 'surname':person.surname})

