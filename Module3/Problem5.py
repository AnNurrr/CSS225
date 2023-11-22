# Ainur
# 10/15/2023
# Computer the MPG for a car
miles_driven = float(input("Please enter the driven mile: "))
gallons_used = float(input("Please enter the number of gallons used: "))
MPG = float(miles_driven / gallons_used)
print(" The fuel efficiency of your vehicle is " + str(round(MPG, 2)))