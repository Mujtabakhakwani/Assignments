height = float(input("enter the height of person in meters "))
weight = float(input("enter the mass of person in kilograms"))
bmi = weight / (height ** 2)
if bmi <18.5:
    print("underweight")
elif bmi>18.5 and bmi<24.5:
 print("normal weight")
elif bmi>25 and bmi<29.9:
 print("overweight")
else: 
 print("obese")