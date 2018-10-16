db={}
with open("CEPIK_types.py","+r", encoding="utf-8") as file:
    while True:
        f=file.readline()
        if f[:5]== 'entry':
            db=(eval(f[6:]))
            db["nazwisko"]=""
            break

with open("newtypes.py","+w", encoding="utf-8") as file:
    file.write("entry="+str(db))