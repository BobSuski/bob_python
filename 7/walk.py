import os
if False:
    path= r'C:\\'

    for current_folder, subfolders, files in os.walk(path):
        print(f'Folder: {current_folder}')

        for folder in subfolders:
            print(f'Subfolder: {folder}')

        for file in files:
            print(f'File: {file}')


if False:
    files=os.listdir(os.getcwd())
    print('Files: ')
    print(files)

    for file in files:
        print(os.path.join(os.getcwd(),file))

if True:
    try:
        zm=1/0
    except ZeroDivisionError as e:
        print(e.__str__())
    finally:
        print("End")