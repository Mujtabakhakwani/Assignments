def sumDigits(s):
    try:
        total = 0
        for char in s:
            if char.isdigit():  
                total += int(char)  
        return total
    except Exception as e:
        print(f"An error occurred: {e}")
        return None  

print(sumDigits('a2b3c'))  
print(sumDigits('abc123def456'))  
