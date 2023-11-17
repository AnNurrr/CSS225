# Ainur
# 11/13/23
# Multiplies all the numbers in a list

def multiplyList(numbers):
    result =1
    for num in numbers:
        result = result*num
    return result

#Example
myList = [5, 2, 7, -1]
result = multiplyList(myList)
print("The result of multiplying all numbers in the list " + str(myList) + " is " + str(result))