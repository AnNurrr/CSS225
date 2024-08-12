# Ainur
# 11/29/2023
# Generates a list of numbers that are multiple of 10
# and appends qualifying numbers to the list

count = 0
tens = []
while count<50:
    if count%10==0:
        tens.append(count)
    count+=1



print("List of numbers that are divisible by tenL ", tens)


