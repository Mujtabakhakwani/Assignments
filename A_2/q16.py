def check():
    names = ['Ahmad', "Zainab","Hina","Ali"]
    name = str(input("login: "))
    if name in names:
        print("you are in! ")
    else:
        print("invalid user ")
    print ("done")
check()