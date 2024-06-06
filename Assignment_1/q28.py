x = int(input("enter the number to calculate factorial "))
result =1 
if x == 0 or x == 1:
    fact = 1
else:
    for i in range(1, x+1):
        result =result * i
print(result)