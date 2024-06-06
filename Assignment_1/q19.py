a = int(input("enter first angle of triangle "))
b = int(input("enter second angle of triangle "))
c = int(input("enter third angle of triangle "))


if a==b or a==c or b==c:
    print("it is an isosceles triangle")
elif a==b and a==c and b==c:
    print("it is an equilateral triangle")
elif a==90 or b==90 or c==90:
    print("it is a right angled triangle")
elif a!=b or a!=c or b!=c :
    print("it is a scalene triangle")
