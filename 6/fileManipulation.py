if False:
    import os
    file_r = open("src/file1")
    print("1*"*30)
    print(file_r.read())
    file_r.seek(0)
    print("2*"*30)
    for i in file_r.readlines():
        print(i)
        print(f"position {format(file_r.tell())}")


if False:
    print("3*"*30)
    file_w=os.fdopen(file_r.fileno(),"a+")
    file_w.write("line 3\n")
    file_r.close()


if False:
    with open("src/file1","+r", encoding="utf-8") as file:
        print(file.read(1))
        print(file.readlines())

if False:
    with open("src/file2","w", encoding="utf-8") as file:
        print(file.write("1\n"))
        print(file.write("2\n"))
        file.seek(0);
        print(file.write("0\n"))

if False:
    baza = [
        "Paris,Lyon,2",
        "London,Manchester,Leeds,3",
        "Warsaw,Cracow,Gdansk,Wroclaw,4"
    ]

    with open('src/baza.csv','w',encoding="utf-8") as file:
        file.writelines("\n".join(baza))
    file.close()


if False:
    with open('src/baza.csv','r',encoding="utf-8") as file:
        [print(f.strip().split(",")) for f in file.readlines()]


if False:
    def convert(value):
        for i in range(len(value)):
            try:
                value[i]=int(value[i])
            except:
                pass
        print(value)

    with open('src/baza.csv','r',encoding="utf-8") as file:
        #[convert(f.strip().split(",")) for f in file.readlines()]
        [convert(f.split(",")) for f in file.readlines()] #numbers at last position in file so 2\n maps to 2


if False:
    [print(f.strip().split(",")) for f in open('src/baza.csv','r',encoding="utf-8").readlines()]

