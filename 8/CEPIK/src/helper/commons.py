import os

def list_all_databases(databases):
    print("Available databases: ")
    for k in databases.keys():
        print("\t"+k)

def replace_files(from_file, to_file):
    try:
        os.remove(to_file+".old")
    except OSError:
        pass
    os.rename(to_file,to_file+".old")
    os.rename(from_file,to_file)

def rename_file(from_file, to_file):
    try:
        os.remove(to_file)
    except OSError:
        pass
    os.rename(from_file,to_file)

def get_valid_field(valid_fields):
    while True:
        field = input('By field: ')
        if field in valid_fields:
            break
        else:
            print(f'Wrong field. Allowed fields {valid_fields}')
    return field