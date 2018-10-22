import sys, pickle
sys.path.insert(0, '../../src')

from  properties import properties
from helper.connection_manager import ConnectionManager
from helper import commons
from dao.personDAO import PersonDAO
from dao.daoFactory import DaoFactory
from entity.person import Person


while True:
    print("-"*30)
    input_operation=input("Choose option:\n"
                    "l [=database name] - list available databases, or show all data from specific database if name provided\n"
                    "a=database  - add entry\n"
                    "c=database  - clear database or create if not exists\n"
                    "s(i)=dabatase - search, case insensitive when i provided\n"
                    "r(i)=database  - remove entry by name, case insensitive when i provided\n"
                    "fc(i)=database  - count function\n"
                    "af  - add field\n"
                    "df  - delete field\n"
                    "q  - exit\n ")

    operation = None
    database = None

    try:
        operation=input_operation.split("=")[0]
    except:
        print("Operation attribute failure")


    try:
        database=input_operation.split("=")[1]
    except:
        pass

    if not( database is None ) and database not in properties.databases.keys():
        print("Not existing database!")
        continue

    if operation == "l":
        if database is None:
            commons.list_all_databases(properties.databases)
        else:
            all_data=[]
            all_data= DaoFactory().get_instance(database).get_all_data().copy()
            for p in all_data:
                try:
                    print(p)
                except Exception as e:
                    print(e.__str__())

    elif operation == "a":
        row={}
        if database is None:
            print("Provide database name")
        else:
            for i in properties.database_structure['person']:
                row[i] = input(f'{i}: ')
            DaoFactory().get_instance(database).add(row)

    elif operation == "c":
        if database is None:
            print("Provide database name")
        else:
            database = ConnectionManager().open_database_w(properties.databases[database])
            ConnectionManager().close_database(database)

    elif operation == "s" or operation == "si":
        if database is None:
            print("Provide database name")
        else:
            if operation == "si":
                mode = 'i'
            else:
                mode = 's'
            field=commons.get_valid_field(properties.database_structure[database])
            value = input('Search value: ')
            DaoFactory().get_instance(database).search(mode, field.strip(),value.strip())
            pass

    elif operation == "r" or operation == "ri":
        if database is None:
            print("Provide database name")
        else:
            if operation == "ri":
                mode = 'i'
            else:
                mode = 's'
            field=commons.get_valid_field(properties.database_structure[database])
            value = input('Delete by value: ')

            DaoFactory().get_instance(database).delete(mode, field,value)

    elif operation == "fci" or operation == "fc":
        if database is None:
            print("Provide database name")
        else:
            if operation == "fci":
                mode = 'i'
            else:
                mode = 's'
            field=commons.get_valid_field(properties.database_structure[database])
            value = input('Count by value: ')

            DaoFactory().get_instance(database).count(properties.databases[database],mode, field,value)


    # elif operation == "s":
    #     commons.get_database_entry("s")
    # elif operation == "si":
    #     commons.get_database_entry("i")
    # elif operation == "r":
    #     commons.remove_database_entry_by_name("s")
    # elif operation == "ri":
    #     commons.remove_database_entry_by_name("i")
    # elif operation == "c":
    #     commons.count_entries("s")
    # elif operation == "ci":
    #     commons.count_entries("i")
    # elif operation == "d":
    #     commons.clear_database()
    # elif operation == "af":
    #     commons.add_field()
    # elif operation == "df":
    #     commons.del_field()
    elif operation =="q":
        print("Exiting")
        break
    else:
        print("Unsupported option")

