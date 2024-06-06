x = int(input("enter the number of days book returned late "))
fine = 0
if x < 5 :
    fine = 50
    print(fine)

elif x>5 and x<=10:
    fine = 1
    print(fine)
elif x>10 and x<29 :
    fine =5
    print(fine)
else:
    print ("membership cancelled")
