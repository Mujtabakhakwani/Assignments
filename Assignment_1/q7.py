x = int(input("enter five digit number "))
a = x%10
b = (x//10)%10
c = (x//100)%10
d = (x//1000)%10
e = x//10000
print("the sum is ",a+b+c+d+e)