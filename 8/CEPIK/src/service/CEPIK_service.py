import sys, pickle
sys.path.insert(0, '../../src')

from  properties import properties
from helper.connection_manager import ConnectionManager
from helper import commons
from dao.personDAO import PersonDAO
from dao.daoFacade import DaoFacade

from entity.person import Person


while True:
    print("-"*30)
    input_operation=input("Choose option:\n"
                    "l [=database name] - list available databases, or show all from specific database if name provided\n"
                    "a  - add entry\n"
                    "c  - clear database or create if not exists\n"
                    "s(i)=field=value - search, case insensitive when i provided\n"
                    "r(i)  - remove entry by name, case insensitive when i provided\n"
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


    if operation == "l":
        if database is None:
            commons.list_all_databases(properties.databases)
        else:
            all_data=[]
            all_data= DaoFacade().get_instance(database).get_all_data(properties.databases[database]).copy()
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
            for i in properties.database_structure[database]:
                row[i] = input(f'{i}: ')
            DaoFacade().get_instance(database).add(properties.databases[database],row)

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
            field = input('Search field: ')
            value = input('Search value: ')

            DaoFacade().get_instance(database).search(properties.databases[database],mode, field,value)
            pass

    elif operation == "r" or operation == "ri":
        if database is None:
            print("Provide database name")
        else:
            if operation == "ri":
                mode = 'i'
            else:
                mode = 's'
            field = input('Delete by field: ')
            value = input('Delete by value: ')

            DaoFacade().get_instance(database).delete(properties.databases[database],mode, field,value)


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

