def print_table():
    print("number\tsquare\tcube")
    
    for i in range(6):
        square = i ** 2
        cube = i ** 3
        print(f"{i}\t{square}\t{cube}")

print_table()
