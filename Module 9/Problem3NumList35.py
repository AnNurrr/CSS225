# Ainur
# 11/28/2023
# asks the user a number and adds up each value until the sum is greater than 100



sum = 0


while sum<=100:
    user_value = int(input("Enter a number: "))
    sum+=user_value

print("Sum is greater than 100, Final sum is: ", sum)
