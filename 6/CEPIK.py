import os;

entry = {
    "name":"",
    "veh_id":""
}

def get_key():
    while True:
        key = input("Key to search:\n")
        if key in entry.keys():
            return key
        else:
            print("Key does not exist")

def list_database():
    with open("src/db.dat","+r", encoding="utf-8") as file:
        for f in file.readlines():
                print(f)

def get_database_entry(mode):
    found=False
    key = get_key()
    value = input("Value to search:\n")
    with open("src/db.dat","+r", encoding="utf-8") as file:
        for f in file.readlines():
            dbname=eval(f)[key]
            if mode == "i":
                if dbname.upper() == value.upper():
                    print(f)
                    found=True
            else:
                if dbname == value:
                    print(f)
                    found=True
    if not found:
        print("No data found")

def add_database_entry():
    entry["name"] = input("Give name:\n ")
    entry["veh_id"] = input("Give veh id:\n ")
    with open("src/db.dat","+a", encoding="utf-8") as file:
        file.write(str(entry)+"\n")
    print("Entry {} has been added".format(entry))

def remove_database_entry_by_name(mode):
    key = get_key()
    value = input("Value to search:\n")
    newdb= open("src/newdb.dat","+w", encoding="utf-8");
    with open("src/db.dat","+r", encoding="utf-8") as file:
        for f in file.readlines():
            dbname=eval(f)[key]
            if mode == "i":
                if dbname.upper() != value.upper():
                    newdb.write(f)
            else:
                if dbname != value:
                    newdb.write(f)
    newdb.close();
    try:
        os.remove("src/db.old")
    except OSError:
        pass
    os.rename("src/db.dat","src/db.old")
    os.rename("src/newdb.dat","src/db.dat")

def count_entries(mode):
    key = get_key()
    value = input("Value to search:\n")
    count=0
    with open("src/db.dat","+r", encoding="utf-8") as file:
        for f in file.readlines():
            dbname=eval(f)[key]
            if mode == "i":
                if dbname.upper() == value.upper():
                    count=count+1
            else:
                if dbname == value:
                    count=count+1
    print("Number of entries({}): ({}={}) is {}".format("insensitive search" if mode == "i" else "sensitive search", key, value, count))


def clear_database():
    with open("src/db.dat","+w", encoding="utf-8") as file:
        pass


while True:
    print("-"*30)
    operation=input("Choose option:\n"
                    "l  - list database\n"
                    "a  - add entry\n"
                    "s(i) - search, case insensitive when i provided\n"
                    "r(i)  - remove entry by name, case insensitive when i provided\n"
                    "c(i)  - count by key and value, case insensitive when i provided\n"
                    "d  - clear database\n"
                    "q  - exit\n ")

    if operation == "l":
        list_database()
    elif operation == "a":
        add_database_entry()
    elif operation == "s":
        get_database_entry("s")
    elif operation == "si":
        get_database_entry("i")
    elif operation == "r":
        remove_database_entry_by_name("s")
    elif operation == "ri":
        remove_database_entry_by_name("i")
    elif operation == "c":
        count_entries("s")
    elif operation == "ci":
        count_entries("i")
    elif operation == "d":
        clear_database()
    elif operation =="q":
        print("Exiting")
        break
    else:
        print("Unsupported option")



