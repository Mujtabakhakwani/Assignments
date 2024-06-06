x=int(input("enter height of pyramid" ))
for i in range(x):
        for j in range(i + 1):
            print("* ", end=" ")
        print()
for i in range(x):
        for j in range(x - i+1):
            print("* ", end=" ")
        print()