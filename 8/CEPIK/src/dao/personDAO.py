import sys, pickle
sys.path.insert(0, '../../src')

from helper.connection_manager import ConnectionManager
from entity.person import Person
from helper.commons import replace_files


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

    def delete(self, database_path, mode, field, value):
        entries=[]
        new_entries=[]
        entries = self.get_all_data(database_path)
        if field == 'name':
            new_entries = self.delete_by_name(database_path, mode, entries,value)

        if field == 'surname':
            new_entries = self.delete_by_surname(database_path, mode, entries,value)

        replace_files(database_path+"_new.dat",database_path)

    def count(self,database_path, mode, field, value):
        entries=[]
        entries = self.get_all_data(database_path)
        if field == 'name':
            self.count_by_name(mode, entries, value)

        if field == 'surname':
            self.count_by_surname(mode, entries, value)


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

    def delete_by_name(self, database_path, mode, entries, name):
        print("Entries survived in database:")
        for i in entries:
            if not ((i.name == name and mode != 'i')  or (i.name.upper() == name.upper() and mode == 'i')):
                self.add(database_path+"_new.dat",{'name':i.name, 'surname':i.surname})

    def delete_by_surname(self, database_path, mode, entries, surname):
        print("Entries survived in database:")
        for i in entries:
            if not ((i.surname == surname and mode != 'i')  or (i.surname.upper() == surname.upper() and mode == 'i')):
                self.add(database_path+"_new.dat",{'name':i.name, 'surname':i.surname})

    def count_by_name(self, mode, entries, name):
        seq=0
        for i in entries:
            if (i.name == name and mode != 'i')  or (i.name.upper() == name.upper() and mode == 'i'):
                seq+=1
        print(f'count({name}) = {seq}')

    def count_by_surname(self, mode, entries, surname):
        seq=0
        for i in entries:
            if (i.surname == surname and mode != 'i')  or (i.surname.upper() == surname.upper() and mode == 'i'):
                seq+=1
        print(f'count({surname}) = {seq}')
