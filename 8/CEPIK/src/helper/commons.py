import os

def list_all_databases(databases):
    print("Available databases: ")
    for k in databases.keys():
        print("\t"+k)

def replace_files(fromfile, to_file):
    try:
        os.remove(to_file+".old")
    except OSError:
        pass
    os.rename(to_file,to_file+".old")
    os.rename(fromfile,to_file)
