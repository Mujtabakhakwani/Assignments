def count_digit_one(n):
    count = 0
    i = 1
    while i <= n:
        high = n // (i * 10)
        current = (n // i) % 10
        low = n % i
        
        if current == 0:
            count += high * i
        elif current == 1:
            count += high * i + low + 1
        else:
            count += (high + 1) * i
        
        i *= 10
    
    return count

n = int(input("enter the value of n "))
print(count_digit_one(n)) 
