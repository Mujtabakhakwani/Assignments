def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def prime_factors(x):
    factors = []
    x = int(input("enter number you want to find prime factors of: "))
    for i in range(2, x + 1):
        while x % i == 0:
            if is_prime(i):
                factors.append(i)
                print("prime factor:", i)
            x = x // i

    if not factors:
        print("no prime factors found.")
    return factors


prime_factors("x")
