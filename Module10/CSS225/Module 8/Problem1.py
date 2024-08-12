# Ainur
# 11/18/20233
# Takes two inputs from a user and prints whether they are equal or not

def compare_inputs():

    # Takes two input from user
    input1 = input("Please enter the first number: ")
    input2 = input("Please enter the second number: ")

    # Checks whether they are equal or not
    if input1 == input2:
        print("The inputs are equal.")
    else:
        print("The inputs are not equal.")

 # Calls the function to test
compare_inputs()
