def square ():
    n = int(input("enter number till you want to square "))
    for i in range(n):
        for j in range (n):
         if i==j:
          print(i**2)
    print()
square()