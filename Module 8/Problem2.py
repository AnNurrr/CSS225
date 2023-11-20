# Ainur
# 11/18/2023
# Takes two inputs from user and prints whether the sum
# is greater than 10, less than 10, or equal to 10 with python.

def compare_sum_to_10():
    # Get input from user
    number1 = float(input("Please enter the first number: "))
    number2 = float(input("Please enter the second number: "))

    # Calculate the sum
    sum_result = number1 + number2

    # Compare the sum with 10
    if sum_result > 10:
        print("The sum is greater than 10.")
    elif sum_result < 10:
        print("The sum is less than 10.")
    else:
        print("The sum is equal to 10.")

# Call the function to test
compare_sum_to_10()
