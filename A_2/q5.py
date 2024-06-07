def range(start, stop, step=1):
    range_list = []
    
    if step == 0:
        raise ValueError("step must not be zero")
    
    if step > 0:
        while start < stop:
            range_list.append(start)
            start += step
    else:
        while start > stop:
            range_list.append(start)
            start += step
    
    return range_list

print(range(1, 10, 2)) 
print(range(10, 1, -2))  
print(range(5, 15, 3))
print(range(0, -10, -2))  
