x = int(input("enter number of hours worker worked "))
rate = float(input("enter hourly rate of worker "))
if x > 40 :
    overtime = x - 40
    overtime_pay = overtime * 1.5 * rate + (x*rate)
    print("salary is ", overtime_pay)
elif x < 40 :
    print("salary is ", x * rate)