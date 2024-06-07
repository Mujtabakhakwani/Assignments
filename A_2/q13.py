import random

random_int = [random.randint(0, 100) for _ in range(20)]
print("Original list:", random_int)

random_int = list(dict.fromkeys(random_int))
print("List with duplicates removed:", random_int)

# list(dict.fromkeys(random_int)) remember this