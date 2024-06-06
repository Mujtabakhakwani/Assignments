positive = 0
negative = 0
zero =0
while True:
        
    num = input("Enter a number (or 'stop' to quit): ")
    if num.lower() == 'stop':
         break
    
    try:
        number = float(num)
        if number > 0 :
          positive += 1
        elif number < 0 :
          negative += 1
        else :
          zero += 1

    except ValueError:
        print("Invalid input. Please enter a number.")
print(f"Positive numbers: {positive}")
print(f"Negative numbers: {negative}")
print(f"Zero numbers: {zero}")

