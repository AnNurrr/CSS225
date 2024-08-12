# Ainur
# 11/13/23
# Checks if the number is in range

def checkInRange():
    myRange = range(1, 11)


    number = int(input("Please enter a number: "))

    if number in myRange:
        print(str(number) + " is in the range.")
    else:
        print(str(number) + " is not in range. ")


checkInRange()

