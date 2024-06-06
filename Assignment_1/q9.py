married = bool(input("is the driver married "))
male =bool(input("is the driver male "))
above25 = bool(input("is the driver above 25 "))
above30 =bool(input("is the driver above 30 "))

if married :
    print("insured")
elif male and above30 and not married :
    print("insured")
elif above25 and not married and not male :
    print("insured")
else:
    print("not insured")
    
