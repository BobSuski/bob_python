import sys, pickle
sys.path.insert(0, '../../src')

from  properties import properties
from helper.connection_manager import ConnectionManager
from entity.person import Person
from helper.commons import rename_file


class PersonDAO(object):

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
        if field == 'name':
            self.get_person_by_name(mode, entries, value)

        if field == 'surname':
            self.get_person_by_surname(mode, entries, value)

        if field == 'pesel':
            self.get_person_by_pesel(mode, entries,value)

    def delete(self, mode, field, value):
        database_path=properties.databases['person']
        entries=[]
        new_entries=[]
        entries = self.get_all_data()
        if field == 'name':
            new_entries = self.delete_by_name(database_path,mode, entries,value)

        if field == 'surname':
            new_entries = self.delete_by_surname(database_path, mode, entries,value)




    def count(self,database_path, mode, field, value):
        entries=[]
        entries = self.get_all_data()
        if field == 'name':
            self.count_by_name(mode, entries, value)

        if field == 'surname':
            self.count_by_surname(mode, entries, value)

        if field == 'pesel':
            self.count_by_pesel(mode, entries, value)

    def get_person_by_name(self,mode, entries,name):
        for i in entries:
            if (i.name == name and mode != 'i')  or (i.name.upper().strip() == name.upper().strip() and mode == 'i'):
                print(i)

    def get_person_by_surname(self,mode, entries,surname):
        for i in entries:
            if (i.surname == surname and mode != 'i')  or (i.surname.upper().strip() == surname.upper().strip() and mode == 'i'):
                print(i)

    def get_person_by_pesel(self,mode, entries,pesel):
        for i in entries:
            if (i.pesel == pesel and mode != 'i')  or (i.pesel.upper().strip() == pesel.upper().strip() and mode == 'i'):
                print(i)


    def add(self, row):
        person=Person(row['pesel'], row['name'],row['surname'])
        database_path =  properties.databases['person']
        database = ConnectionManager().open_database_a(database_path)
        print(f'adding {person}')
        pickle.dump(person,database)
        ConnectionManager().close_database(database)

    def delete_by_name(self, database_path, mode, entries, name):
        rename_file(database_path,database_path+".old")
        print("Entries survived in database:")
        for i in entries:
            if not ((i.name == name and mode != 'i')  or (i.name.upper().strip == name.upper().strip() and mode == 'i')):
                self.add({'pesel':i.pesel, 'name':i.name, 'surname':i.surname})

    def delete_by_surname(self, database_path, mode, entries, surname):
        rename_file(database_path,database_path+".old")
        print("Entries survived in database:")
        for i in entries:
            if not ((i.surname == surname and mode != 'i')  or (i.surname.upper().strip() == surname.upper().strip() and mode == 'i')):
                self.add({'pesel':i.pesel, 'name':i.name, 'surname':i.surname})


    def delete_by_pesel(self, database_path, mode, entries, pesel):
        rename_file(database_path,database_path+".old")
        print("Entries survived in database:")
        for i in entries:
            if not ((i.pesel == pesel and mode != 'i')  or (i.pesel.upper().strip() == pesel.upper().strip() and mode == 'i')):
                self.add({'pesel':i.pesel, 'name':i.name, 'surname':i.surname})

    def count_by_name(self, mode, entries, name):
        seq=0
        for i in entries:
            if (i.name == name and mode != 'i')  or (i.name.upper().strip() == name.upper().strip() and mode == 'i'):
                seq+=1
        print(f'count({name}) = {seq}')

    def count_by_surname(self, mode, entries, surname):
        seq=0
        for i in entries:
            if (i.surname == surname and mode != 'i')  or (i.surname.upper().strip() == surname.upper().strip() and mode == 'i'):
                seq+=1
        print(f'count({surname}) = {seq}')

    def count_by_pesel(self, mode, entries, pesel):
        seq=0
        for i in entries:
            if (i.pesel == pesel and mode != 'i')  or (i.pesel.upper().strip() == pesel.upper().strip() and mode == 'i'):
                seq+=1
        print(f'count({pesel}) = {seq}')