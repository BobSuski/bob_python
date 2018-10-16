import CEPIK_types, os, importlib


#to verify if key exists
def get_key():
    while True:
        key = input("Key to search ({}):\n".format(str(CEPIK_types.entry).replace(",","/").replace("'","").replace(":","").replace("{","").replace("}","")))
        if key in CEPIK_types.entry.keys():
            return key
        else:
            print("Key does not exist")

# #to verify if key exists
# def get_keys():
#     while True:
#         key = input("Key to search:\n")
#         if key in CEPIK_types.entry.keys():
#             return key
#         else:
#             print("Key does not exist")

#list whole database
def list_database():
    with open("src/db.dat","+r", encoding="utf-8") as file:
        for f in file.readlines():
            print(f)

#get by value
def get_database_entry(mode):
    found=False
    key = get_key()
    value = input("Value to search:\n")
    with open("src/db.dat","+r", encoding="utf-8") as file:
        #try as database is more like document style not relational database
        for f in file.readlines():
            try:
                dbname=eval(f)[key]
                if mode == "i":
                    if dbname.upper() == value.upper():
                        print(f)
                        found=True
                else:
                    if dbname == value:
                        print(f)
                        found=True
            except Exception:
                pass
    if not found:
        print("No data found")

#add database entry
def add_database_entry():
    for key in CEPIK_types.entry.keys():
        CEPIK_types.entry[key] = input("Set "  + key+"=\n ")
    with open("src/db.dat","+a", encoding="utf-8") as file:
        file.write(str(CEPIK_types.entry)+"\n")
    print("Entry {} has been added".format(CEPIK_types.entry))

#file refresh utility
def replace_files(file, new_file):
    try:
        os.remove(file+".old")
    except OSError:
        pass
    os.rename(file,file+".old")
    os.rename(new_file,file)

#drop by value
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

    replace_files("src/db.dat","src/newdb.dat")

#list number of entries by value
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

#clear whole database
def clear_database():
    with open("src/db.dat","+w", encoding="utf-8") as file:
        pass

#add new field
def add_field():
    new_col = input("New field")
    db={}
    with open("CEPIK_types.py","+r", encoding="utf-8") as file:
        while True:
            f=file.readline()
            if f[:5]== 'entry':
                db=(eval(f[6:]))
                db[new_col]=""
                break

    with open("new_CEPIK_types.py","+w", encoding="utf-8") as file:
        file.write("entry="+str(db))

    replace_files("CEPIK_types.py","new_CEPIK_types.py")
    importlib.reload(CEPIK_types)

#del field
def del_field():
    del_col = input("Field to delete {}".format(str(CEPIK_types.entry)))
    db={}
    with open("CEPIK_types.py","+r", encoding="utf-8") as file:
        while True:
            try:
                f=file.readline()
                if f[:5]== 'entry':
                    db=(eval(f[6:]))
                    del db[del_col]
                    break
            except Exception:
                print("Error deleting "+del_col)
                break

    with open("new_CEPIK_types.py","+w", encoding="utf-8") as file:
        file.write("entry="+str(db))

    replace_files("CEPIK_types.py","new_CEPIK_types.py")
    importlib.reload(CEPIK_types)