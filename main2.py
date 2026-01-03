'''Write a program to calculate the electricity bill based on the number of units consumed by a user.

If the units consumed are less than 50, the cost per unit is ₹2.60 and the tax is ₹25.

If the units consumed are 50 or more but less than 100, the cost per unit is ₹3.25 and the tax is ₹35.

If the units consumed are 100 or more but less than 200, the cost per unit is ₹5.26 and the tax is ₹45.

If the units consumed are 200 or more, the cost per unit is ₹8.45 and the tax is ₹75.

The program should take the number of units as input and display the total electricity bill.'''
bill_unit=int(input("Enter your electricity bill units only: "))
if bill_unit<50:
    totalbill=(bill_unit*2.60)+25
    print("The money you have to pay is",totalbill)
elif bill_unit>=50 and bill_unit<100:
    totalbill=(bill_unit*3.25)+35
    print("The money you have to pay is",totalbill)
elif bill_unit>=100 and bill_unit<200:
    totalbill=(bill_unit*5.26)+45
    print("The money you have to pay is",totalbill)
elif bill_unit>=200:
    totalbill=(bill_unit*8.45)+75
    print("The money you have to pay is",totalbill)
else:
    print("invalid input")