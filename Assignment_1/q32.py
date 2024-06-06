x = int(input("enter the height of triangle "))


def a():
    print("patteren A")
    for i in range(x):
        for j in range(i + 1):
            print("* ", end=" ")
        print()


def b():
    print("patteren B")
    for i in range(x):
        for j in range(x - i):
            print("* ", end=" ")
        print()


def c():
    print("patteren C")
    for i in range(x, 0, -1):
        for j in range(x - i):
            print(" ", end=" ")
        for k in range(i):
            print("*", end=" ")
        print()


def d():
    print("patteren D")
    for i in range(x+1):
        for j in range(x - i):
            print(" ", end="")
        for k in range(i):
            print("*", end=" ")
        print()


a()
b()
c()
d()
