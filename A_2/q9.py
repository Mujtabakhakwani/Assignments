
def celsius(x):
    return (x - 32) * 5.0/9.0

def fahrenheit(y):
    return (y * 9.0/5.0) + 32

for x in range(32, 212):
    print(f"{x} fahrenheit is equal to {celsius(x)} celsius")

for y in range(0, 100):
    print(f"{y} celsius is equal to {fahrenheit(y)} fahrenheit")