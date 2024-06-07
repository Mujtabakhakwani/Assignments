matrix = []
print("enter 9 elements for matrix ")

for i in range(3):
    row = []
    for j in range(3):
        numbers = int(input("enter elements of matrix "))
        row.append(numbers)
    matrix.append(row)


print("the entered matrix is ")
for row in matrix:
    for number in row:
        print(number, end=" ")
    print()

matrix2 = []
print("enter 9 elements for matrix2 ")

for i in range(3):
    row = []
    for j in range(3):
        numbers = int(input("enter elements of matrix2 "))
        row.append(numbers)
    matrix2.append(row)

print("the entered matrix2 is ")
for row in matrix2:
    for number in row:
        print(number, end=" ")
    print()

result =  [[0,0,0],
          [0,0,0],
          [0,0,0]]

for i in range (3):
    for j in range (3):
        for k in range (3):
            result[i][j] += matrix[i][k] * matrix2[k][j]

for i in result:
    print(i)
