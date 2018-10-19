import sys, pickle
sys.path.insert(0, '../../src')

from helper.connection_manager import ConnectionManager
from entity.person import Person


class PersonDAO(object):

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

    def search(self,database_path, mode, field, value ):
        entries=[]
        entries = self.get_all_data(database_path)
        if field == 'name':
            self.get_person_by_name(mode, entries, value)

        if field == 'surname':
            self.get_person_by_surname(mode, entries, value)

    def get_person_by_name(self,mode, entries,name):
        for i in entries:
            if (i.name == name and mode != 'i')  or (i.name.upper() == name.upper() and mode == 'i'):
                print(i)

    def get_person_by_surname(self,mode, entries,surname):
        for i in entries:
            if (i.surname == surname and mode != 'i')  or (i.surname.upper() == surname.upper() and mode == 'i'):
                print(i)

    def add(self, database_path, row):
        person=Person(row['name'],row['surname'])
        database = ConnectionManager().open_database_a(database_path)
        print(f'adding {person}')
        pickle.dump(person,database)
        ConnectionManager().close_database(database)
        pass

    def delete_by_name(self, name):
        pass

    def delete_by_surname(self, surname):
        pass
