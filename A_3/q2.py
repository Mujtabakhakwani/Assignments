n = int(input("enter an integer: "))

square_dict = {}
for i in range(1, n + 1):
    square_dict[i] = i * i
print(square_dict)
