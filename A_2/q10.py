def perfect():
    for num in range(1, 1001):
        sums = 0
        for i in range(1, num):
            if num % i == 0:
                sums += i
        if sums == num:
            print(num)

perfect()