# Ainur
# 11/18/2023
# Takes a list and prints if the number 5 is in that list

def check_5(myList):
    if 5 in myList:
        print("The number 5 is in the list")
    else:
        print("The number 5 is not in the list")

userInput = input("Please enter a list of numbers separated by spaces: ")

userList = [int(item) for item in userInput.split()]

check_5(userList)