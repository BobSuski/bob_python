import os;

entry = {
    "name":"",
    "veh_id":""
}

def list_database():
    with open("src/db.dat","+r", encoding="utf-8") as file:
        for f in file.readlines():
                print(f)

def get_user_database_by_name(mode):
    found=False
    name=input("Give name:\n ")
    with open("src/db.dat","+r", encoding="utf-8") as file:
        for f in file.readlines():
            if mode == "i":
                dbname=eval(f)["name"]
                if dbname.upper() == name.upper():
                    print(f)
                    found=True
            else:
                if eval(f)["name"] == name:
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
    name=input("Give name:\n ")
    newdb= open("src/newdb.dat","+w", encoding="utf-8");
    with open("src/db.dat","+r", encoding="utf-8") as file:
        for f in file.readlines():
            if mode == "i":
                dbname=eval(f)["name"]
                if dbname.upper() != name.upper():
                    newdb.write(f)
            else:
                if eval(f)["name"] != name:
                    newdb.write(f)
    newdb.close();
    try:
        os.remove("src/db.old")
    except OSError:
        pass
    os.rename("src/db.dat","src/db.old")
    os.rename("src/newdb.dat","src/db.dat")


def clear_database():
    with open("src/db.dat","+w", encoding="utf-8") as file:
        pass


while True:
    print("-"*30)
    operation=input("Choose option:\n"
                    "l  - list database\n"
                    "a  - add entry\n"
                    "sn(i) - search by name, case insensitive when i provided\n"
                    "c  - clear database\n"
                    "rn(i)  - remove entry by name, case insensitive when i provided\n"
                    "q  - exit\n ")

    if operation == "l":
        list_database()
    elif operation == "a":
        add_database_entry()
    elif operation == "sn":
        get_user_database_by_name("s")
    elif operation == "sni":
        get_user_database_by_name("i")
    elif operation == "rn":
        remove_database_entry_by_name("s")
    elif operation == "rni":
        remove_database_entry_by_name("i")
    elif operation == "c":
        clear_database()
    elif operation =="q":
        print("Exiting")
        break
    else:
        print("Unsupported option")



