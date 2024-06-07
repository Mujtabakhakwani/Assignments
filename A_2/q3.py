x = int(input("enter the number to check armstrong or not "))

n = x
sum = 0
while n != 0 :
    digit = n % 10
    sum = sum + digit ** 3
    n = n // 10
if sum == x :
        print("the number is armstrong")
else :
     print("the number is not armstrong")
