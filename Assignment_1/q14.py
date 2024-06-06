x =int(input("enter first number "))
y = int(input("enter second number "))
z = int(input("enter third number "))
list=[x,y,z]
a=x+y+z
b=a/3
c = x*y*z
largest_num = max(list)
smallest_num = min(list)
print("sum of numbers is ",a)
print("average of numbers is ",b)
print("product of numbers is ",c)
print("smallest number is ",smallest_num)
print("largest number is ",largest_num)
