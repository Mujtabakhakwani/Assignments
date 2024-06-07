def solid():
    x = int(input("enter the side of square "))
    y = str(input("enter the character "))
    for i in range(x):
       for j in range(x):
        print(y, end=" ")
       print()
solid()