# Ainur
# 11/13/23
# Calculates the area of a circle

import math

def areaOfCircle(r):
    area = math.pi*r**2
    return area

# Example
radius = 5
result = areaOfCircle(radius)
print("The area of circle with radius " + str(radius) + " is " + str(result))
