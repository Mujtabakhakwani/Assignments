a = int(input("enter the marks of A "))
b = int(input("enter the marks of B "))

if a>=55 and b>45:
    print("pass")
elif a>45 and a<55 and b> 55:
    print("pass")
elif a<45 and b> 65 :
    print("reappear")
else:
    print("fail")