def find_minimum(numbers):
    if len(numbers) != 10:
        raise ValueError("The input tuple must contain exactly 10 numbers.")
    return min(numbers)

numbers_tuple = tuple(int(input(f"Enter number {i+1}: ")) for i in range(10))
minimum_number = find_minimum(numbers_tuple)
print("The minimum number in the tuple is:", minimum_number)