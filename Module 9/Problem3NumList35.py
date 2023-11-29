# Ainur
# 11/28/2023
# asks the user a number and adds up each value until the sum is greater than 100



sumofnumbers = 0
numbers = []

while sumofnumbers<=100:
    user_value = float(input("Enter a number: "))
    numbers.append(user_value)
    sumofnumbers = sum(numbers)

print("Sum is greater than 100, Final sum is: ", sumofnumbers)
