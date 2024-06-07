import random 
import statistics

random_int = [random.randint(1,100) for _ in range(10)]
print("random numbers are ", random_int)
mean = statistics.mean(random_int)
print("mean is ", mean)
median = statistics.median(random_int)
print("median is ", median)

try:
    mode =statistics.mode(random_int)
    print("mode is ", mode)
except statistics.StatisticsError:
    print("no unique mode found")
