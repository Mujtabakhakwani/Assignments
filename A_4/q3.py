def r_array(arr, k):
    n = len(arr)
    k = k % n  
    rotated = arr[-k:] + arr[:-k]
    return rotated

def f_min(arr):
    min = 0
    min_value = arr[0]
    for i in range(1, len(arr)):
        if arr[i] < min_value:
            min_value = arr[i]
            min = i
    return min

arr = [1, 2, 3, 4, 5, 6, 7]
k = 3
rotated = r_array(arr, k)
min = f_min(rotated)

print("rotated array ", rotated)
print("Index of minimum value ", min)
