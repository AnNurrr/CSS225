# Ainur
# 11/13/23
# Takes a list of numbers and returns a new list with unique elements

def uniqueElements(inputList):
    uniqueList = []
    for num in inputList:
        if num not in uniqueList:
            uniqueList.append(num)
    return uniqueList

#Example
myList = [1, 3, 3, 3, 6, 2, 3, 5]
result = uniqueElements(myList)
print("The list with unique elements from " + str(myList) + " is " + str(result))